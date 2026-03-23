# Write a python function to print table of user input number
def table():
    num = int(input("Enter the value: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
table()

#Write a python program to calculate the average of 3 User inputs
 def avg():
     print("Enter all the Values")
     num1 = float(input("Enter the first value:"))
     num2 = float(input("Enter the second value:"))
     num3 = float(input("Enter the third value:"))

     total = num1 + num2 + num3
     avg =total/3
     print(avg)
         