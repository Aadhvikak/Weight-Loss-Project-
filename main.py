from easygui import *
import easygui as g
import easygui as eg

title = "Weight Loss"

msg = "Choose one. Are you a ... "
choices = ["Male","Female","Other"]
reply = choicebox(msg, choices = choices)
print("You selected : ", end = "")
print(reply)

choices = ["adult (age 18+)", "child", "senior (age 60+)"]
msg = "Choose one. Are you a(n) ... "
reply2 = choicebox(msg, choices = choices)
print("You selected : ", end = "")
print(reply2)


msg = "What is your weight? (pounds)"
weight = float(g.enterbox(msg, title))
print("Your weight is: ", end = "")
print(weight)        
msg = "What is your desired weight goal? (pounds)"
reply4 = float(g.enterbox(msg, title))
print("Your desired weight goal is: ", end = "")
print(reply4)  
msg = "What is your height? (put in inches)"
height = float(g.enterbox(msg, title))
print("Your height, in inches, is: ", end = "")
print(height)
bm = weight/(height**2)*703
bmi = float(format(bm, ".2f"))

if bmi < 18.5:
  score = str("You are underweight")
elif 18.5 < bmi < 24.9:
  score = str("You are a healthy weight")
elif 25 < bmi < 29.9:
  score = str("You are overweight")
elif bmi > 30:
  score = str("You are obese")

eg.msgbox(msg='Your BMI score is '+ str(bmi) + " " + score)
