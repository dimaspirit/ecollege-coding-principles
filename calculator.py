def calculator(operand1, operand2, operator):
  if(operator == '+'):
    return operand1 + operand2
  elif(operator == '-'):
    return operand1 - operand2
  elif(operator == '*'):
    return operand1 * operand2
  elif(operator == '/'):
    return operand1 / operand2
  elif(operator == '%'):
    return operand1 % operand2

num1 = input('Enter number 1: ')
num2 = input('Enter number 2: ')
operator = input('Enter operator. Either + - * / %: ')

print('Result:', calculator(int(num1), int(num2), operator))