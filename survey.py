from random import randint
from answer_model import Answer

class Survey():
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_bank = question_bank
        self.asked_question_indeces = []

    def still_has_questions(self):
        return self.question_number < len(self.question_bank)

    def ask_question(self):
        """Retrieves question from the question_list and presents it to the user"""
        random_question_index = randint(0, len(self.question_bank) -1)
        if random_question_index not in self.asked_question_indeces:
            self.asked_question_indeces.append(random_question_index)
            current_question = self.question_bank[random_question_index]
            self.question_number += 1
            if current_question.question_type == "spinner":
                print(
                f"~~~{current_question.question_text}~~~")
                input("Press [ENTER] to continue")
                answer = current_question.question_answers
            elif current_question.question_type == "not asked":
                answer = current_question.question_answers
            elif current_question.question_type == "switch":
                question_prefixes = ["A) ", "B) ", "C) ", "D) "]
                options = list(current_question.question_answers.keys())
                
                print(f"Q. {current_question.question_text}")
                for (question_prefix, option) in zip(question_prefixes, options):
                    print(question_prefix, option)
                choice = input("Answer: ").lower()
                
                while len(choice) != 1:
                    print("Please enter either A, B, C, or D")
                    choice = input("Answer: ").lower()
                
                if choice == "a":
                    print(current_question.question_answers[options[0]])
                    answer = current_question.question_answers[options[0]]
                elif choice == "b":
                    answer = current_question.question_answers[options[1]]
                elif choice == "c":
                    answer = current_question.question_answers[options[2]]
                else:
                    answer = current_question.question_answers[options[3]]
            
            else:
                if current_question.question_type == "field":
                    print(
                        f"Q. {current_question.question_text}\n")
                    response = input("Answer: ")
                    answer = response + current_question.question_answers

            return Answer(current_question.question_category, answer)
        return
