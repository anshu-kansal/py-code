print('''
+ ADD
- SUBTRACT
* MULTIPLY
/ DIVIDE
'''
)

num1= int(input("Enter the number: "))
num2= int(input("Enter the number: "))
opr=input("Enter the function: ")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1 - num2 )
elif opr=="*" :
    print(num1*num2) 
elif opr=="/" :
    print(num1/num2)
else:
    print("Invalid")          
  