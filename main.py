from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_txt = question["question"]
    question_ans = question["correct_answer"]
    new_question = Question(question_txt, question_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()
while quiz.still_has_question():
    quiz.next_question()

print("you have completed the quiz!")
print(f"your final score is : {quiz.score}/{quiz.question_count}")
