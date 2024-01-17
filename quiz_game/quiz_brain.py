class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = []
        self.question_list = q_list

    def still_have_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        current_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question} (True/False): ")
        self.check_answer(user_answer, current_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Well done!")
            self.score += 1
        else:
            print("Wrong answer...")
        print(f"The correct answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")

    def finale(self):
        print("This is the end of quiz")
        print(f"Your score is {self.score}/{self.question_number}")
