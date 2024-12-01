num1 =  int(input("enter first number:"))
num2 =  int(input("enter second number:"))

moqmedeba = input("enter matematikuri moqmedeba(-,+,,/,)")


if moqmedeba == "-":
    print(num1 - num2)

elif moqmedeba == "+":
    print(num1 + num2)

elif moqmedeba == "":
    print(num1 * num2)

elif moqmedeba == "/":
    print(num1 / num2)