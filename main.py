from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  
  num1 = float(input("What's the first number: "))

  for key in operations:
    print(key)

  flag = True

  while flag:
    operation_symbol = input("Pick an operation symbol: ")
    num2 = float(input("What's the next number?: "))
    operation = operations[operation_symbol]
    answer = operation(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'no' to exit: ") == "y":
      num1 = answer
    else:
      flag = False
      calculator()

calculator()