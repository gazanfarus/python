from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()
quiz.finale()
