class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        item_text = self.question_list[self.question_number].text
        item_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {item_text} (True/False)?: ")
        self.check_answer(user_answer, item_answer)

    def check_answer(self, user_answer, item_answer):
        if user_answer.lower() == item_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {item_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")
