# calculate and return the sum of first N natural numbers
# N is given by user as an input
# this script is an example of type casting

N = input("Please enter the value of N: \n")
N = int(N)
print(type(N))
# perform operation on N
result = (N*(N+1))/2
result = int(result)
print(result)
