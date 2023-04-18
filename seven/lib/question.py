class Question:
    def __init__(self, question, choices, correct_answer):
        self.question = question
        self.choices = []
        for choice in choices:
            self.choices.append(AnswerChoice(choice))
        self.correct_answer = correct_answer
    
    def add_choice(self, choice):
        new_choice = AnswerChoice(choice)
        self.choices.append(new_choice)
        return True
    
    def remove_choice(self, choice):
        for c in self.choices:
            if c.choice_text == choice:
                self.choices.remove(c)
                return True
        return False
    
    def update_choice(self, choice, new_choice_text):
        for c in self.choices:
            if c.choice_text == choice:
                c.choice_text = new_choice_text
                return True
        return False
