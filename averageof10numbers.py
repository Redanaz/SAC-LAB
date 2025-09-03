count=0
total=0
while count<10:
    n=int(input(f"Enter number {count+1}:"))
    total+=n
    count+=1
avg=total/10
print(f"avg of 10 numbers is:{avg}")
