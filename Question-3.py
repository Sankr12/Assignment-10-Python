# Write a python script to print M multiples of N

N = int(input("Enter the number: "))

for i in range(0,int(input("Enter the multiples: ")),1):
    print((i+1)*N,end=' ')

print()