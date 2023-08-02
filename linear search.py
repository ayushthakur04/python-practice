#linear search
a={}
#n=int(input("enter the length of list : "))
for i in range(0,4):
    a[i]=eval(input("enter the value : "))

x=eval(input("enter the number to be search : "))
for i in range(0,4):
    if a[i]==x:
        Flag=1
        break
if Flag==1:
    print("the number in present in the list :) ")
else:
    print("not found :(")







enter the value : 1
enter the value : 2
enter the value : 3
enter the value : 2
enter the number to be search : 1
the number in present in the list :) 
