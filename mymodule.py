
import calculator
print("select operation")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
choice = input("1/2/3/4:")
num1 = int(input("enter a 1st no:"))
num2 = int(input("enter a 2nd no:"))
if choice == '1':
    print("ans:",calculator.add(num1,num2))
elif choice == '2':
    print("ans:",calculator.sub(num1,num2))
elif choice == '3':    
    print("ans:",calculator.mul(num1,num2))
elif choice == '4':
    print("ans:",calculator.div(num1,num2))
