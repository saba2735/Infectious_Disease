# Infectious Disease Homework 3
The goal of the homework was to better understand SIR models for different groups. Different groups such as immuno-compromised people are more susceptible to getting infected than those who are not. Similariry, elderly people are also more susceptible to getting infected than those who are not. This will help us understand how the disease epidemic will end or die out.  

## Problem 2c 
The goal of this problem was to assume that 99.9% of people in each group are susceptible and the other 0.1% of people are infected.
We simulated the epidemic wave using delta t and maximum simulation time to capture the wave. The simulation was done for each group. The image below shouw the varying levels of saturation between the four groups. 

![image](https://github.com/saba2735/Infectious_Disease/assets/143537736/defa7623-d881-4c63-944c-fc184dceb4a9)


## Problem 2d 
Defining the average relative susceptibility among the susceptibles at any point in time p(t). The graphs below show the si(t) where i = 1,2,3,4 and the second graph shows the p(t). 

![image](https://github.com/saba2735/Infectious_Disease/assets/143537736/a8e017a9-a32c-4acd-8e4c-e8866064de57)


![image](https://github.com/saba2735/Infectious_Disease/assets/143537736/3061c1ae-43cd-4c8b-8879-e0ce0be1faeb)


## Problem 3a 
Code uses branching process that start from a single infecton and then draws G generations with each infection creating NB(R0,k) additional infections. The code estimates q (probability) that an epidemic with die out in a finite time. We assumed that R0 = 3 and used k = 0.1,0.5,1.0,5.0, and 10.0. 

![image](https://github.com/saba2735/Infectious_Disease/assets/143537736/8f97c1a2-9c5c-4a86-8015-8a434190a258)


## Problem 3 extra credit 
Plotted a histogram of 100,000 finite outbreaks modeling different k values and R0 = 3. The graphs for a few different k values are shown below. 

K = 0.5
![image](https://github.com/saba2735/Infectious_Disease/assets/143537736/74a6d8bf-0f89-489d-b1ac-f850a78184a0)

K = 1.0
![image](https://github.com/saba2735/Infectious_Disease/assets/143537736/6360354c-7f92-4d57-9763-bfde3055f1a9)


K = 5.0

![image](https://github.com/saba2735/Infectious_Disease/assets/143537736/e070bec7-cba4-480b-bea3-75e8d1338af4)


K = 10.0

![image](https://github.com/saba2735/Infectious_Disease/assets/143537736/17c1ae59-082f-4db1-a929-6cb9b681500a)

