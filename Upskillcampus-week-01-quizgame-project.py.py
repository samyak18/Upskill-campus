#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run_quiz(self):
        self.score = 0  
        for question in self.questions:
            user_answer = input(question.prompt + "Your answer: ")
            if user_answer.lower() == question.answer.lower():
                self.score += 1
                print("Correct!")
            else:
                print("Incorrect!")
        print("You got", self.score, "out of", len(self.questions), "questions correct.")
question_prompts = [
    "What color is the sky?\n(a) Blue\n(b) Red\n(c) Yellow\n\n",
    "What is 2+2?\n(a) 3\n(b) 4\n(c) 5\n\n",
    "Who is the current president of the United States?\n(a) Barack Obama\n(b) Donald Trump\n(c) Joe Biden\n\n"
]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")
]
quiz = Quiz(questions)
while True:
    quiz.run_quiz()
    restart = input("Do you want to restart the quiz? (yes/no): ")
    if restart.lower() != "yes":
        break


# In[ ]:




