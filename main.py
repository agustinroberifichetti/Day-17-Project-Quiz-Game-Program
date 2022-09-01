from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for n in range(len(question_data)):
    question = Question(question_data[n]["text"], question_data[n]["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed this challenge!\nYour final score is {quiz.score}/{quiz.question_number}.")
