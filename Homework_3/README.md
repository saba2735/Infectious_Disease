# Infectious Disease Homework 3
The goal of the homework was to better understand SIR models for different groups. Different groups such as immuno-compromised people are more susceptible to getting infected than those who are not. Similariry, elderly people are also more susceptible to getting infected than those who are not. This will help us understand how the disease epidemic will end or die out.  

## Problem 2c 
The goal of this problem was to assume that 99.9% of people in each group are susceptible and the other 0.1% of people are infected.
We simulated the epidemic wave using delta t and maximum simulation time to capture the wave. The simulation was done for each group. The image below shouw the varying levels of saturation between the four groups. 

![Alt text](image.png)

## Problem 2d 
Defining the average relative susceptibility among the susceptibles at any point in time p(t). The graphs below show the si(t) where i = 1,2,3,4 and the second graph shows the p(t). 

![Alt text](image-2.png)

![Alt text](image-3.png)

## Problem 3a 
Code uses branching process that start from a single infecton and then draws G generations with each infection creating NB(R0,k) additional infections. The code estimates q (probability) that an epidemic with die out in a finite time. We assumed that R0 = 3 and used k = 0.1,0.5,1.0,5.0, and 10.0. 

![Alt text](image-4.png)

## Problem 3 extra credit 
Plotted a histogram of 100,000 finite outbreaks modeling different k values and R0 = 3. The graphs for a few different k values are shown below. 

![Alt text](image-5.png)

![Alt text](image-6.png)

![Alt text](image-7.png)

![Alt text](image-8.png)
