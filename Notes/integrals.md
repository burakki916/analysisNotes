# The Riemann Integral 
## Paritions 
### Definition

Suppose we have an interval $I = [a,b]$ then a **partition** defined on $I$ is 
a set
$\mathcal{P}$ of *closed intervals* such that, 
$$
    \mathcal{P} = \{\mathcal{I}_1,\mathcal{I}_2, \dots, \mathcal{I}_n, \}
$$
Where
$$
    \bigcap \mathcal{P}_i = \empty \text{\ and \ } \bigcup \mathcal{P_i} = \mathcal{P}
$$
We can refer to every interval by 
$$
    I_i = [ x_{i-1} , x_i ].
$$ 
Where $a= x_0 < x_1 < \dots <  x_n = b$,  

We say a partition is *tagged* when for every $\mathcal{I}_i$ there exists unique
$t_i \in \mathcal{I}_i$, called *tags*. Then the **Tagged Partition** is 

$$
    \mathcal{P} = \{ 
        (\mathcal{P}_1, x_1) , (\mathcal{P}_2, x_2),  \dots 
        (\mathcal{P}_n, x_n) 
            \} 
$$

### Norm of a partition

We define the norm of  $\mathcal{P}$ as the length of the 
biggest partition, denoted 
$$
    ||\mathcal{P}|| :=  \max (\{ {x_{i+1} - x_i | i \in 1,...,n-1}  \}) 
$$
## Riemann sums
We define the **Riemann sum** of a function,
    $f : [a,b] \to \mathbb{R}$
with respect to a tagged 
partition $\dot{\mathcal{P}}$
as 

$$
    S(f;\dot{\mathcal{P}}) := \sum_{i = 1}^{n} f(t_i)(x_i - x_{i-1})
$$
We say a $f$ is 
***Riemann Integrable*** if there exists 
$L \in \mathbb{R}$
such that for all $\varepsilon > 0$ there exists $\delta_{\epsilon} >0$ such that $||\mathcal{P}|| < \delta_{\epsilon}$ then, 
$$ 
    | S(f, \dot{\mathcal{P}}) - L | < \epsilon
$$ 
Instead of writting $L$ we usually write 
$$ 
L = \int_a^b f(x)dx 
$$
###  Riemann Integral Properties

- *Property 1* (7.1.3)
    
    Let $f(x) = g(x)$ over $[a,b]/J$, where $J$ is of finite 
    carnality. Then 
    $$
    f(x) \in \mathcal{R}[a,b] \implies g(x) \in \mathcal{R}[a,b]
    $$
    And 
    $$
        \int_a ^b f = \int_a^b g
    $$
- *Property 2* (7.1.3) 
$$
    \int kf(x) = k \int f(x) 
$$
- *Property 3* (7.1.3)
$$
    \int_a^b (f + g) = \int_a^b f + \int_a^b g 
$$
- *Property 4* (7.1.5)
 
    $f(x) \leq g(x)$ for every $x \in [a,b]$, then 
    $$
        \int_a^b f  \leq \int_a^b g 
    $$
- *Property 5* (7.1.6)

    If $f \in \mathcal{R}[a,b],$ then $f$ is bounded on $[a,b]$

- *Property 6* (7.2.9)
    $$
        \int _a ^b f = \int _a ^ c f + \int _c ^ b f 
    $$
- *Property 7* (7.2.10) 
  
  If $f \in \mathcal{R}[a,b]$, and if $[c,d] \subseteq [a,b],$ then $f$ 
  restricted to $c,d$ is in $\mathcal{R}[c,d]$

- *Property 8 (7.2.12)*
    If $\alpha < \beta$, then 
    $$
        \int_\beta ^ \alpha f := -\int_\alpha ^\beta f 
    $$
    and 
    $$
        \int_\alpha ^\alpha = 0
    $$

## Classes of Riemann Integrable functions (7.2.4, 7.2.5, 7.2.7)
- Step functions are integrable (7.2.4)
- Step functions are integrable (7.2.5)
- Continuous implies integrable (7.2.7)
## Non Integrable Functions 
$$
1/x ; [-1,1]
$$
Need to state more. 
## State and apply the Squeeze Theorem 7.2.3

## State and apply the "Sequential Criterion:" for Riemann integral (Q 7.1.9)
$f$ is in $\mathcal{R}[a,b]$  if and only if $\forall \epsilon >0$ there is 
$\omega_\epsilon(x)$ and $\alpha_\epsilon(x)$, both in $\mathcal{R}[a,b]$ with  
$$
    \int \alpha_\epsilon - \omega_{\epsilon}  < \epsilon 
$$
## State and apply the Fundamental Theorem of Calculus (both forms)   
### FTC First Form KAGE NO JITSU 
Let $F(x) : [a,b] \to \mathbb{R}$ and let $f(x) = \frac{d}{dx} F(x)$, 
and F is continuous and $f\in \mathcal{R}$
then 
$$
\int_a^b f= F(b) - F(a)   
$$


### FTC Second Form KAGE NO JITSU 
$$
    \frac{d}{dx} \int_a^x f(t) dt = f(x) 
$$
## Cauchy Criterion  
A function $[a,b] \to \mathbb{R}$ belongs to $\mathcal{R}[a,b]$ if and only if  
for every $\epsilon > 0$ there is $\eta_\epsilon >0$ such that if 
$\dot{\mathcal{P}}$ and 
$\dot{\mathcal{Q}}$  are tagged partitions of $[a,b]$ with 
$||\dot{\mathcal{P}}||  < \eta_\epsilon$ and 
$||\dot{\mathcal{Q}}||  < \eta_\epsilon$, then 
$$
    | S(f;\dot{\mathcal{P}}) -  S(f;\dot{\mathcal{Q}})| < \epsilon 
$$