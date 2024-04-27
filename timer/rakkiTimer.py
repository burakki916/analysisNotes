import os
import datetime
import threading
import time
import pygame  # You may need to install this library: pip install pygame
def generateTodaysTasks(tasksDirectory): 
    tasks = [] 
    taskFiles = []
    taskFileCounter = 0 
    for file in os.listdir(tasksDirectory):
        if(file.endswith(".rakkiTask")):
            taskFileCounter += 1
            taskFiles.append(file)
            print(f"{taskFileCounter}: {file}")
    if taskFileCounter != 0:
        print("Would you like to load a task file? (y/n)")
        response = input()
        if response == "y":
            taskFile = int(input("Enter the number of the task file you would like to load: "))
            with open(f"{tasksDirectory}/{taskFiles[taskFile - 1]}", "r") as f:
                tasks = f.readlines()
            return tasks
    print("No task files found, please enter your tasks manually:")
    stringInput = " " 
    tasks.append("OFF TOPIC")
    while stringInput != "": 
        stringInput = input("Enter a task for today: ")
        if stringInput != "":
            tasks.append(stringInput) 
    response = input("Would you like to save these tasks for future use? (y/n)")
    if response == "y":
        taskFileName = input("Enter the name of the task file: ")
        with open(f"{tasksDirectory}/{taskFileName}.rakkiTask", "w") as f:
            for task in tasks:
                f.write(f"{task}\n")
    return tasks

def updateJournal(tasks, note_file): 
    response = (0,"away")
    poll_tasks_thread = threading.Thread(target=pollTasks, args=(tasks, response))
    poll_tasks_thread.start()
    poll_tasks_thread.join(timeout=5*60)  # Wait for 5 minutes
    taskNum, note = response  # Retrieve response
    writeNote(tasks[taskNum], datetime.datetime.now().strftime("%H:%M:%S"), note_file, note)
    
def pollTasks(tasks, response): 
    response = (0,"Away")
    for i, task in enumerate(tasks):
        print(i, task)
    taskNum = int(input("Enter The task you have worked on so far: "))
    note = input("Note: ")
    response = (taskNum, note)

def writeNote(task, time, noteDocument, comment=""): 
    print(f"Writing to {noteDocument}")
    output = f"[{time}] : {task} : {comment} \n"
    with open(noteDocument, "a") as f:
        print(f"Writing: {output}")
        f.write(f"{output}")

def play_song(file_path):
    print(f"Playing {file_path}")
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play() 
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()
    pygame.quit() 

def printProgressBar(startTime, endTime):
    currentTime = time.time()
    total = endTime - startTime
    elapsed = currentTime - startTime
    progress = elapsed / total
    progressBarWidth = 50  # Set the progress bar width in characters 
    filledChars = int(progress * progressBarWidth)
    print(f"[{'#' * filledChars}{'-' * (progressBarWidth - filledChars)}] [{progress * 100}%]")

def game(interval, sounds,note_folder="journal", task_folder="tasks"):
    i = 0
    # Set the note file to be a file with today's date in a notes folder
    note_date = datetime.date.today().strftime("%Y-%m-%d")
    note_file = f"{note_folder}/{note_date}.rakkiNote"

    # Check if the note file exists, if not create a new one
    if not os.path.exists(note_folder):
        os.makedirs(note_folder)
    if not os.path.exists(note_file):
        open(note_file, "w").close()

    if not os.path.exists(task_folder):
        os.makedirs(task_folder) 


    # Initialize the user to the program 
    print("Good Morning! Welcome to the rakki time management system")
    print("How many hours would you like to work today?")
    startTime = time.time()
    hours = int(input("Enter the number of hours: "))
    endTime = startTime + hours * 60 * 60
    print("Great! You will be working for", hours, "hours")

    print("This program will help you keep track of your time")
    print("Initialize Tasks...") 
    tasks = generateTodaysTasks(task_folder) 
    print("Great! Every 30 minutes I will check up on you") 
    print("Enter the number corresponding to the task you have been working on the majority of the time ")
    print("If you have been working on an off-topic task enter 0")
    print("Every 10 minutes there will be sound to remind you to take note of what you're you doing") 

    while True:
        printProgressBar(startTime, endTime)
        if i % 6 == 0:
            play_song(sounds[0])
            play_song(sounds[0])
            play_song(sounds[0])
            print("An Hour has gone by ")
        elif i % 3 == 0: 
            play_song(sounds[0])
            play_song(sounds[0])
            print("Half has gone by ")
        else:
            play_song(sounds[0])
            print("10 minutes has gone by ")
        if i % 3 == 0:  # Every 30 minutes try to poll the user for their tasks
            update_journal_thread = threading.Thread(target=updateJournal, args=(tasks, note_file))
            update_journal_thread.start()
        i += 1
        time.sleep(interval * 60)  # Convert minutes to seconds
if __name__ == "__main__":
    interval = 10  # Set the interval in minutes
    boom = "./boom.mp3" # Vine Boom Sound Effect
    game(interval, [boom])
