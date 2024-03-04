class QuizBrain:

    def __init__(self,question_list):
        self.question_number=0
        self.score=0
        self.question_list=question_list

    def check_answer(self,user_answer,currect_answer):    
        if currect_answer.lower()==user_answer: #because question_number increased automatically
            self.score+=1
            print(f'You are great \nscore is {self.score}/{self.question_number+1}')
        else:
            print('Try again')

    def next_question(self):    
        answes=['true','false','exit']
        user_input='worng'

        current_question=self.question_list[self.question_number]
        while user_input not in answes:
            user_input = input(f'Q.{self.question_number+1}: {current_question.text} (True/False)?: ').lower()
            if user_input not in answes:
                print('Please enter True or False')
                continue 
            elif user_input=='exit':
                return user_input
            else:
                self.check_answer(user_input,current_question.answer)
                self.question_number+=1
                return user_input

    def still_has_question(self):            
        return self.question_number < len(self.question_list)

