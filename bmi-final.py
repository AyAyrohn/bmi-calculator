height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = (weight / height **2)

rbmi = round(bmi)

if rbmi < 18.5:
    print(f"Your BMI is {rbmi}, you are underweight.")
elif rbmi < 25:
    print(f"Your BMI is {rbmi}, you have a normal weight.")
elif rbmi < 30:
    print(f"Your BMI is {rbmi}, you are slightly overweight.")
elif rbmi < 35:
    print(f"Your BMI is {rbmi}, you are obese.")
else:
    print(f"Your BMI is {rbmi}, you are clinically obeset.")