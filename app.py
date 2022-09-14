import json
import os
from mash_factory import MashFactory
from results import Results
from question_model import Question
from survey import Survey

question_bank = []
with open("mash.json", mode="r") as mash_data:
    data = json.load(mash_data)
    for question in data["questions"][:]:
        question_category = question["category"]
        question_type = question["type"]
        question_text = question["question"]
        question_answers = question["answers"]
        new_question = Question(
            question_category=question_category, 
            question_type=question_type, 
            question_text=question_text, 
            question_answers=question_answers
            )
        question_bank.append(new_question)

os.system("clear")
input("\nWelcome to the game of \n\n~~~~MASH~~~~ \n\npress [ENTER]")
os.system("clear")
print("\nThe same game you played as a wide-eyed optimistic child \nNow modernized and automated so your friend Jenny doesn't screw up counting again!")
print("\nAnswer a few simple questions and all your questions: \n...what do do with your life, \n...who is your eternal love, and \n...just how filthy rich you will be, \ncan be answered!")
input("Are you ready to make the uknown, known? \nPress [ENTER] to proceed\n")
os.system("clear")

survey = Survey(question_bank)
answer_bank = {}
while survey.still_has_questions():
    answer = survey.ask_question()
    # os.system("clear")
    if answer:
        if answer.question_category == "house" or answer.question_category == "kids" or answer.question_category == "salary":
            answer_bank[answer.question_category] = answer.answer
        else:
            if answer.question_category not in answer_bank.keys():
                answer_bank[answer.question_category] = []
            answer_bank[answer.question_category].append(answer.answer)
    os.system("clear")
mash_factory = MashFactory(answer_bank)
fortune = mash_factory.get_fortune()

results = Results(fortune)
