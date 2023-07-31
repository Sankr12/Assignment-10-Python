# Write a python script to print all prime numbers within a range.
# Range
# Start = 15
# end = 45

print()
print("Prime numbers between 15 and 45: ")
for i in range(15,46):
    for a in range(2,i):
        if i%a==0:
            break
    else:
     	print(i,end=' ')            
print()
print()
