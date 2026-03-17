# Write a python function to print table of user input number
def table():
    num = int(input("Enter the value: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
table()
