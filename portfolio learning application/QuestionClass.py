import json

class Question:

    def __init__(self, questionContent, ansA, ansB, ansC, ansD, rightAnswer, pointsForAnswer):
    
        self.questionContent = questionContent
        self.ansA = ansA
        self.ansB = ansB
        self.ansC = ansC
        self.ansD = ansD
        self.rightAnswer = rightAnswer 
        self.pointsForAnswer = int(pointsForAnswer)
    
    def displayQuestion(self):
    
        return self.questionContent, self.ansA, self.ansB, self.ansC, self.ansD
    
class ListOfQuestions:
    
    def __init__(self):
    
        self.listOfQuestions = []
    
    def addQuestion(self,question):#This function is used to manually append questions 
    
        self.listOfQuestions.append(question.__dict__)
    
    def importQuestions():
        pass#This function will be used to import questions to the listOfQuestion in the further development of the application
    
    def displayQuestions(self,n):
    
        return self.listOfQuestions[n]


listOfQuestions = ListOfQuestions()

question1 = Question("I'm _________computer now", "A. play", "B.plays", "C. playing", "D. played", "A", 1) 

question2 = Question(" If you hadn't been late, we ________the bus.", "A. will not miss", "B. wouldn't have missed", "C. wouldn't miss", "D. could not miss", "B", 3) 

question3 = Question("She will stay in London if she ____ a job.", "A. gets", "B. would get", "C. will get", "D.got", "A", 1)

question4 = Question("Lucy is arriving ___February.", "A. in", "B. at", "C. by", "D. on", "D", 1) 

question5 = Question("The train leaves _____tomorrow morning _____8:00 am.", "A. on/at", "B. at/on", "C. -/at", "D. -/on", "C", 2) 

question6 = Question("The journey was ________! Twelve hours by bus!", "A. exhausted", "B. exhausting", "C. exhaustive", "D. exhaustting", "B", 2) 

question7 = Question(" We're meeting _______lunchtime _______next Tuesday.", "A. at/-", "B. at/on", "C. on/-", "D. in/on", "A", 2) 

question8 = Question(" I don't know what we'll do at the weekend. It depends _________________the weather.", "A. at", "B. on", "C. by", "D. from", "B", 1) 

question9 = Question("I _______ in a cafe when you ________.", "A. was sittting/ were calling", "B. sat/called", "C. was sitting/called", "D. sat/ were calling", "C", 2) 

question10 = Question("Susie _______ a film when she _______ the noise.", "A. was watching/was hearing", "B. watched/ heard", "C. watched/was hearing", "D. was watching/heard", "D", 2)

listOfQuestions.addQuestion(question1)

listOfQuestions.addQuestion(question2)

listOfQuestions.addQuestion(question3)

listOfQuestions.addQuestion(question4)

listOfQuestions.addQuestion(question5)

listOfQuestions.addQuestion(question6)

listOfQuestions.addQuestion(question7)

listOfQuestions.addQuestion(question8)

listOfQuestions.addQuestion(question9)

listOfQuestions.addQuestion(question10)



