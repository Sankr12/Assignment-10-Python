# Write a python script to print the first 10 multiples of N in reverse order

N = int(input("Enter a number: "))

for i in range(10,0,-1):
    print(i*N,end=' ')

print()