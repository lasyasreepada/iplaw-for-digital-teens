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
        ("Copyright protects both expression of an idea and the idea itself. \nTrue or False?", "f", "cp"),

        ("Clothing, such as Katy Perry’s “Left Shark” costume is a useful article and is therefore copyrightable. \nTrue or False?", "f", "cp"),

        ("One of the factors of evaluation for fair use is the effect of the use upon the potential market for the work in question. \nTrue or False?", "t", "cp"),

        ("In Cariou vs. Prince, the defendant was brought to court because he used images from Cariou’s 2000 book, Yes Rasta, to create a new exhibition of photos with some apparent modifications. This was not fair use because it did not comment on the original work about the nature of the photographs. \nTrue or False?", "t", "cp"),

        ("Copyright is an inevitable, “divine” grant entrusting total ownership rights to the creator of a work. \nTrue or False?", "f", "cp"),

        ("In Christian Louboutin vs. YSL, the defendant was brought to court for using a red outsole on women’s shoes that were also red in color. The court ruled that this was a trademark infringement. \nTrue or False? ", "f", "tm"),

        ("Descriptive names for a company or product (e.g. FishFri) are never trademarkable. \nTrue or False?", "f", "tm"),

        ("Companies such as Google can potentially lose their trademark protection because of genericide. \nTrue or False?", "t", "tm"),

        ("The same trademark (e.g. a word) can be registered by different parties, so long as the trademarks are in different classes. \nTrue or False?", "t", "tm"),

        ("Trademarked goods or services must be made available for commercial sale on a national level (beyond state boundaries). \nTrue or False?", "t", "tm"),

        ("A utility patent application consists of three parts: drawings, a written description, and claim statements. The drawings of the product are most important in determining what exactly gets patented. \nTrue or False?", "f", "pt"),

        ("Naturally occurring processes or products, such as human DNA, are not patentable. \nTrue or False?", "t", "pt"),

        ("The tests that the court used in Alice Corp v. CLS Bank Intl to determine whether the computer software was patent eligible were (1) whether the claims directed to an abstract idea and (2) whether the claims added something inventive. \nTrue or False?", "t", "pt"),

        ("The level of skill required to develop a product or process is not considered when determining whether it satisfies the non-obviousness requirement for patent eligibility. \nTrue or False?", "f", "pt"),

        ("There is a distinction between utility and design, therefore, it is possible for one product to have both a utility patent and a design patent. \nTrue or False?", "t", "pt")
    ]

    shuffle(questions)
    cp_correct = 0 
    tm_correct = 0 
    pt_correct = 0

    print("Welcome to Which IP Law Is for You!")
    time.sleep(2)
    print("We will ask you a series of true or false questions about various cases related with copyrights, trademarks, and patents.")
    time.sleep(5)
    print("When a question is displayed, you will be prompted for an answer. Please type t for true, and f for false.")
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
        if (cp_correct >= tm_correct and cp_correct >= pt_correct):
            print("You are Copyright Law!")
        elif (tm_correct >= cp_correct and tm_correct >= pt_correct):
            print("You are Trademark Law!")
        else:
            print("You are Patent Law!")

quiz()

