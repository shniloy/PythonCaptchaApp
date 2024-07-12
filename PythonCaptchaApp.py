import random

a = random.randint(1, 10)
b = random.randint(1, 10)

print("Pythn Captcha App")

print(f"{a}+{b}")

ans = input("Enter Ans:")

if int(ans) == (a+b):
    print("Good job, your answer is correct")
else:
    print("Sorry, your answer is incorrect")
