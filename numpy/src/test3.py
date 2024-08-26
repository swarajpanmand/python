from numpy import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.displot([0, 1, 2, 3, 4, 5])          # plot a histogram distplot is deprecated in favor of displot
plt.savefig('numpy/src/plot1.png')

print(random.normal(size=(2, 3)))        # return a 2x3 matrix with random values from a normal distribution with mean 0 and standard deviation 1
print(random.normal(loc=1, scale=2, size=(2, 3))) # return a 2x3 matrix with random values from a normal distribution with mean 1 and standard deviation 2
sns.displot(random.normal(size=100))
plt.savefig('numpy/src/plot2.png')

print(random.binomial(n=10, p=0.5, size=10)) # return a 1-D array with 10 elements, each element a random number between 0 and 10 where n is number of trials and p is probability of each trial
sns.displot(random.binomial(n=10, p=0.5, size=100))
plt.savefig('numpy/src/plot3.png')

sns.displot(random.normal(loc=50, scale=5, size=1000), kind='kde') # kde is kernel density estimation binomial is discrete distribution and normal is continuous distribution
plt.savefig('numpy/src/plot4.png')                                 

#poisson distribution is a distribution of the number of events that happened in a fixed interval of time
print(random.poisson(lam=2, size=10))       #lam is the rate of the poisson distribution and size is the number of random numbers to generate
sns.displot(random.poisson(lam=2, size=100))
plt.savefig('numpy/src/plot5.png')

#uniform distribution is a distribution where each value has an equal probability of occuring
print(random.uniform(size=10))              # return a 1-D array with 10 elements, each element a random number between 0 and 1
sns.displot(random.uniform(size=1000) , kind='kde')
plt.savefig('numpy/src/plot6.png')

#logistic distribution is a distribution that is used to describe growth
print(random.logistic(loc=1, scale=2, size=10)) # return a 1-D array with 10 elements, each element a random number from a logistic distribution with mean 1 and scale 2
sns.displot(random.logistic(loc=1, scale=2, size=1000), kind='kde') # kde is kernel density estimation means it will plot a smooth curve instead of bars in histogram(like a line graph)
plt.savefig('numpy/src/plot7.png')
# diff between logistic and normal distribution is that logistic distribution has more values around the mean and less values in the tails

#multinomial distribution is a generalization of binomial distribution where each trial can have more than 2 outcomes
print(random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])) # return a 1-D array with 6 elements, each element a random number from a multinomial distribution with 6 trials and 6 possible outcomes

#exponential distribution is a distribution that describes the time between events in a poisson process where events occur continuously and independently at a constant average rate
print(random.exponential(scale=2, size=10))
sns.displot(random.exponential(scale=2, size=1000), kind='kde')
plt.savefig('numpy/src/plot8.png')
#poisson distribution is the number of events in a fixed interval of time and exponential distribution is the time between events in a poisson process

#chisquare distribution is a distribution of the sum of squares of k independent standard normal random variables
print(random.chisquare(df=2, size=10)) # return a 1-D array with 10 elements, each element a random number from a chisquare distribution with 2 degrees of freedom (df means number of degrees of freedom   )
sns.displot(random.chisquare(df=2, size=1000), kind='kde')

#rayleigh distribution is a distribution of the distance from the origin to a point with normal distribution with mean 0 and standard deviaion 1
print(random.rayleigh(scale=2, size=10)) # return a 1-D array with 10 elements, each element a random number from a rayleigh distribution with scale 2
sns.displot(random.rayleigh(scale=2, size=1000), kind='kde')
plt.savefig('numpy/src/plot9.png')

#pareto distribution is a distribution of the probability of an event with a certain size or larger occuring in a given interval
print(random.pareto(a=2, size=10)) # return a 1-D array with 10 elements, each element a random number from a pareto distribution with shape 2
sns.displot(random.pareto(a=2, size=1000), kind='kde')
plt.savefig('numpy/src/plot10.png')

#zipf distribution is a distribution of the frequency of the nth most common value in a dataset
#zipf law states that the nth most common value in a dataset is 1/n times as common as the most common value
print(random.zipf(a=2, size=10)) # return a 1-D array with 10 elements, each element a random number from a zipf distribution with shape 2
x = random.zipf(a=2, size=1000)
sns.displot(x[x<10], kde=False) # plot only values less than 10
plt.savefig('numpy/src/plot11.png')