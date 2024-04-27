---
title: Integrals
layout: default
---
```
    Section 7.1: 11, 12
    Section 7.2: 2, 10, 16
    Section 7.3: 11, 12, 13
```

# Practice Problems 
## 7.1 
### Problem 11 
#### Question
Suppose that $f$ is bounded on $[a,b]$ and that there exists two sequences 
of tagged parititons on $[a,b]$ such that $||\mathcal{P}_n|| \to 0$ and
$||\mathcal{Q}_n|| \to 0$, but such that $\lim_{n \to \infty} S(f;\mathcal{P}_n) \neq \lim_{n \to \infty} S(f;\mathcal{Q}_n)$. Show that $f$ is not Riemann integrable.
#### Solution 
Suppose for sake of contradiction that $f \in \mathcal{R}[a,b]$. Then, by the definition of Riemann integrability, there exists $L \in \mathbb{R}$ such that for all $\varepsilon > 0$ there exists $\delta_{\varepsilon} > 0$ such that if $||\mathcal{P}|| < \delta_{\varepsilon}$ and $||\mathcal{Q}|| < \delta_{\varepsilon}$ then 
$$
    |S(f;\mathcal{P}) - L| < \varepsilon/2 \quad \text{and} \quad |S(f;\mathcal{Q}) - L| < \varepsilon/2
$$
Then by the triangle inequality we see that,  
$$
    |S(f;\mathcal{P}) - S(f;\mathcal{Q})| \leq |S(f;\mathcal{P}) - L| + |S(f;\mathcal{Q}) - L| < \varepsilon
$$
Thus, we have that $S(f;\mathcal{P}) = S(f;\mathcal{Q})$ which is a contradiction. Thus, $f$ is not Riemann integrable.
### Problem 12 
#### Problem 
Let $f(x) =  x+ 1$ for $ x \in \mathbb{Q}$ and $f(x) = 0$ if $x \in \mathbb{R} \setminus \mathbb{Q}$. Show that $f$ is not Riemann integrable on $[0,1]$. 
#### Solution  
Let $\dot{\mathcal{P}}$ and $\dot{\mathcal{Q}}$ be tagged partitions, defined by  
$$
\dot{\mathcal{P}} = \set{(I_i , p_i)}
\\ 
\dot{\mathcal{Q}} = \set{(I_i , q_i)} 
$$
Where $i$ ranges are integers from $0,n$, and $I_i= [x_{i+1}, x_{i}]$
$$
x_i = i/n
$$
Which satisfies $x_0 = 0$ and $x_n = 1$
and we define the tags $p_i , q_i$ as 
$$
p_i = x \in I_i \setminus \mathbb{Q}  \
( p_i \text{ is irrational} ) 
\\
q_i = x \in I_i \cap \mathbb{Q}
\ 
( q_i \text{ is rational} ) 
$$
and we know $x$ exists for every $I_i$ by the density of the reals. 
Then notice that 
$$
\sum_{i=0}^{n-1} f(p_i) (x_{i+1} - x_{i}) =  0 
$$
as $f(p_i) = 0$ as $p_i$ is irrational. 
and 
$$
\sum_{i=0}^{n-1} f(q_i) (x_{i+1} - x_{i}) = x_n - x_0 =  1 . 
$$ 
Thus by *Problem 11* We have that $f$ is not Riemann Integrable. 
## 7.2
### Problem 2
#### Problem 

Let $f(x) = 1$  if $x \in \mathbb{Q}$ and $f(x) = 0$ if $x \in \mathbb{R} \setminus \mathbb{Q}$. Show that $f$ is not Riemann integrable on $[0,1]$. 
#### Solution 
Let $\dot{\mathcal{P}}$ and $\dot{\mathcal{Q}}$ be tagged partitions, defined by  
$$
\dot{\mathcal{P}} = \set{(I_i , p_i)}
\\ 
\dot{\mathcal{Q}} = \set{(I_i , q_i)} 
$$
Where $i$ ranges are integers from $0,n$, and $I_i= [x_{i+1}, x_{i}]$
$$
x_i = i/n
$$
Which satisfies $x_0 = 0$ and $x_n = 1$
and we define the tags $p_i , q_i$ as 
$$
p_i = x \in I_i \setminus \mathbb{Q}  \
( p_i \text{ is irrational} ) 
\\
q_i = x \in I_i \cap \mathbb{Q}
\ 
( q_i \text{ is rational} ) 
$$
and we know $x$ exists for every $I_i$ by the density of the reals. 
Then notice that 
$$
\sum_{i=0}^{n-1} f(p_i) (x_{i+1} - x_{i}) =  0 
$$
as $f(p_i) = 0$ as $p_i$ is irrational. 
and 
$$
\sum_{i=0}^{n-1} f(q_i) (x_{i+1} - x_{i}) = x_n - x_0 =  1 . 
$$ 
Thus by *Problem 11* We have that $f$ is not Riemann Integrable. 
### Problem 10
## 7.3 
### Problem 11  
### Problem 12
### Problem 13 