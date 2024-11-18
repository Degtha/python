# Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"

def bmi(weight, height):
    x = weight / height**2
    if x <= 18.5 :
        return "Underweight"
    elif x <= 25.0 :
        return "Normal"
    elif x <= 30.0 :
        return "Overweight"
    else:
        return "Obese"
    
print(bmi(25,40))
    