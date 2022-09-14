class Question:
    def __init__(
        self, 
        question_category, 
        question_type, 
        question_text, 
        question_answers,
        ):
        self.question_category=question_category
        self.question_type=question_type
        self.question_text=question_text
        self.question_answers=question_answers