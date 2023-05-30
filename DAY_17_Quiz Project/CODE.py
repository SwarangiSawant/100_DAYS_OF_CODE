from ART import logo
from QUESTION_MODEL import Question
from DATA import question_data
from QUIZ_BRAIN import QuizBrain

print(logo)

question_bank=[]
for question in question_data:
   question_text=question['text']
   question_answer=question['answer']
   question_bank.append(Question(question_text,question_answer)) 

quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("YOU 'VE COMPLETED THE QUIZ! 🎉")
print(f"YOUR FINAL SCORE WAS: {quiz.score}/{quiz.question_number}\n")