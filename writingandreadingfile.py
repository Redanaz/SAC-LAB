f=open("quote.txt","w")
f.write("hi there")
f.close()

f=open("quote.txt","r")
print(f.read())
