def compareTwoNumbers(num1, num2):
  result = 'equal to'

  if(num1 > num2):
    result = 'greater than'
  if(num1 < num2):
    result = 'less than'

  print('num1', num1, 'is', result, 'num2', num2)


compareTwoNumbers(100,12)
compareTwoNumbers(1,10)
compareTwoNumbers(7,7)
