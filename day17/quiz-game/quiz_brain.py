class Quiz_Brain:
    def __init__(self, question_list) -> None:
        self.question_no = 0
        self.question_list = question_list
        self.score = 0
        


    def still_has_questions(self):
        if self.question_no == len(self.question_list):
            return True
        else:
            return False
        

    def next_question(self):
        current_question = self.question_list[self.question_no].text
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}: {current_question}. (True/False)")
        correct_answer = self.question_list[self.question_no].answer
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct answer")
            self.score += 1
        else:
            print("Wrong answer")
            print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_no}")
