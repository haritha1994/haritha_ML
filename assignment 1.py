#Task1.2
x=[]

y=2000

for i in range(3200-2000):
    
    if y%5!=0 and y%7==0:
        
       x.append(y)
   
    y=y+1

print(x)


#Task1.3
first=input("enter ur 1st name")


last=input("enter ur last name")

print(first[::-1]+" "+last[::-1])
https://github.com/haritha1994/haritha_ML/blob/master/As1_task1.3

#Task1.4
d=12

r=d/2


print("the volume of sphere is "+ str((4/3)*(22/7)*(r**3)))

#Task2.1
n=input("enter the number of numberswith comma separation")


print(n.split(","))


#TASk2.3
name=input("enter the name: ")

print(name[::-1])

#Task2.4
x= "WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens"


