#reversing a number
a=int(input("Enter value to be reversed:"))
rev=0
while a>0:
    rem=a%10
    rev=rev*10+rem
    a=a//10
print(rev)
