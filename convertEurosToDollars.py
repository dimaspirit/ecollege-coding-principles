def convertEurosToDollars(noOfEuros):
  # 1 Euro = 1.08 Dollars
  rate = 1.08
  dollars = noOfEuros * rate

  return dollars

print('5 Euros is', convertEurosToDollars(5), 'Dollars.')
print('8 Euros is', convertEurosToDollars(8), 'Dollars.')   
print('10 Euros is', convertEurosToDollars(10), 'Dollars.')

