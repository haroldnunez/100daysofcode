from art import logo
# Add
def add(n1, n2):
  return n1 + n2
# Substract
def substract(n1, n2):
  return n1 - n2
# Multiply
def multiply(n1, n2):
  return n1 * n2
# Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  
  continue_operation = True
  while continue_operation:
    operation = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation]
    answer = calculation_function(num1,num2)
    print(f"{num1} {operation} {num2} = {answer}")  
    if input(
          f"Type 'y' to continue calculationg with {answer}, or type 'n' to exit: "
        ) == "y":    
      num1 = answer
    else:
      continue_operation = False
      calculator()
calculator()
