class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.question_count = 0

    def still_has_question(self):
        return self.question_number != len(self.question_list)

    def check_answers(self, user_ans, current_question):
        if user_ans.lower() == current_question.lower():
            print("yaay!, you got it right")
            self.score += 1
        else:
            print("sorry, you got it wrong")
        self.question_count += 1
        print(f"the current answer is : {current_question}")
        print(f"your current score is : {self.score}/{self.question_count}")
        print("\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_question.text} (True/False) ")
        self.check_answers(user_ans, current_question.answer)
