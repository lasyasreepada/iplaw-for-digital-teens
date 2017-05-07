"""Set of questions for the IP Law quiz

questions.py
Lasya Sreepada
Yale College '19

May 6, 2017
"""
from random import shuffle
import time

def quiz():

    questions = [
        ("cp1", "1", "cp"),
        ("cp2", "2", "cp"),
        ("cp3", "3", "cp"),
        ("cp4", "4", "cp"),
        ("tm1", "1", "tm"),
        ("tm2", "2", "tm"),
        ("tm3", "3", "tm"),
        ("tm4", "4", "tm"),
        ("pt1", "1", "pt"),
        ("pt2", "2", "pt"),
        ("pt3", "3", "pt"),
        ("pt4", "4", "pt")
    ]

    shuffle(questions)
    cp_correct = 0 
    tm_correct = 0 
    pt_correct = 0

    print("Welcome to Which IP Law Is for You!")
    time.sleep(2)
    print("We will ask you a series of true or false questions about various cases related with copyrights, trademarks, and patents.")
    time.sleep(5)
    print("When a question is displayed, you will be prompted for an answer. Please type a for true, and b for false.")
    time.sleep(5)
    print("At the end of the quiz, we will sort you into a branch of IP Law based on your quiz performance. Good Luck!")
    time.sleep(5)
    print()
    
    for question, correct_ans, typ in questions:
        print(question)
        answer = input()
        if answer == correct_ans:
            print("correct!")
            print()
            if typ == "cp":
                cp_correct += 1
            elif typ == "tm":
                tm_correct += 1
            else: pt_correct += 1
            time.sleep(1)
        else:
            print("incorrect")
            print()
            time.sleep(1)

    total_correct = cp_correct + tm_correct + pt_correct
    if total_correct == len(questions):
        print("Congratulations, you are the IP Law Supreme Overlord! You got all the questions right and would do well in any branch.")
    else:
        if (cp_correct > tm_correct and cp_correct > pt_correct):
            print("You are Copyright Law!")
        if (tm_correct >= cp_correct and tm_correct >= pt_correct):
            print("You are Trademark Law!")
        else:
            print("You are Patent Law!")

quiz()

