class QuizBrain:

    def __init__(self, question_list):
        self.user_answer = ""
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} "
                            f"(True/False) --> ").title()
        self.check_answer(user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("Correct answer!!")
        else:
            print("Incorrect answer.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number + 1}.\n\n")
