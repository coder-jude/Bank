# run the code using an extenal python IDE eg.pydroid

import random
import time
import threading


def counter():
    myTimer = 5
    for x in range(5):
        myTimer -= 1
        time.sleep(1)


Timer = threading.Thread(target=counter)
Timer.start()

score = 0
questNum = 1
IsWrong = False
firstNum1 = 0
firstNum2 = 0
lastNum1 = 0
lastNum2 = 0
print("you get 5 chances,if you answer 4 questions correctly you get more chances!!!")
print(f"Your score is {score}")


def quest1():
    # vars
    global score
    global firstNum1
    global firstNum2
    global lastNum1
    global lastNum2
    global questNum
    global IsWrong
    global answer
    # vars

    # score
    try:
        if score <= 25:
            firstNum1 = 2
            lastNum1 = 10
            firstNum2 = 2
            lastNum2 = 10
        elif score > 25 and score <= 45:
            firstNum1 = 10
            lastNum1 = 26
            firstNum2 = 10
            lastNum2 = 26
        elif score > 45 and score <= 75:
            firstNum1 = 20
            lastNum1 = 50
            firstNum2 = 20
            lastNum2 = 50
        elif score > 75 and score <= 120:
            firstNum1 = 50
            lastNum1 = 100
            firstNum2 = 50
            lastNum2 = 100

        # score

        signs = ['*', '+', '-']
        sign = random.choice(signs)
        numb1 = random.randint(firstNum1, lastNum1)
        numb2 = random.randint(firstNum2, lastNum2)
        if numb1 == numb2:
            numb1 += 1
            numb2 += 1
        if sign == "-":
            if numb1 < numb2:
                numb1 = numb2
                numb1 += 2
        answer = eval(f"{numb1}  {sign}  {numb2}")
        print(answer)
        ques = int(input(f"{questNum}. {numb1} {sign} {numb2}: "))
        questNum += 1

        # check answer
        if ques == answer:
            score += 5
            print("Correct!!")
        elif ques != answer:
            print("Wrong!!")
            IsWrong = True
        if score >= 35:
            if IsWrong == True:
                score -= 5
        print(f"Your score is {score}\n")
    except (ValueError):
        if answer != "quit":
            print("Nums onmy")


chances = 5
while chances > 0:
    quest1()
    chances -= 1
    if score > 20:
        chances += 1
    if score == 120:
        print("Well done! you answered all the questions correctly!")
        break
