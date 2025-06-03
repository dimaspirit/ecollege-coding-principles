from math import pow

print("Welcome to the BMI (Body Mass Index) Calculator")
userWeight = float(input("Enter your weight in KG: "))
userHeight = float(input("Enter you height in meters: "))

bmiIndex = userWeight / pow(userHeight, 2)

print("Your BMI result is:", bmiIndex)

if(bmiIndex >= 30):
  print("Obese")
elif (bmiIndex >= 25 and bmiIndex <= 30):
  print("Overweight")
elif (bmiIndex >=18.5 and bmiIndex < 25):
  print("Healthy Weight")
else:
  print("Underweight")