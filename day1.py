for i in range(5):
    for i in range(5):
        print("*",end=" ");
    print()
print("---------------------------------------------");
print("\n\n")
for i in range(5):
    for j in range(5):
        if(i==j or i+j==4):
            print('*',end='')
        else:
            print('',end='  ')
    print()

a="ujwal"
for i in a:
    print(i)
print(len(a))
print("j"in a)
if "j" in a:
    print("j is present")


a="i am ujwal"
b="i am ujwal"
a.upper()
b.lower
print(a.upper(),b.lower())
print(a.strip())
a="i am,ujwal"
print(a.split(","))
a="my name is \"punith\"gowda"
print(a)


num1=int(input("enter the value of a"))
num2=int(input("enter the value of b"))
if num1>num2:
    print("num1 is greater")
else:
    print("num2 is greater")


name=['ram','sham']
print(name)
print(name[1])
print(name[0:1])


a=['mango',"apple"]
var = a.insert[3,"mang"]