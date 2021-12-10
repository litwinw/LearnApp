
from QuestionClass import *
import random

class User:

    def __init__(self, username):
        self.username = username
        self.questionsAsked = []
        self.points = 0
        self.enqueuedQuestions = []

    def createASetOfQuestions(self):

        listToDrawQuestions = []
        
        while len(listToDrawQuestions) < 5:
        
            j = random.randint(0,9)
        
            if j not in listToDrawQuestions:
                listToDrawQuestions.append(j)
       
        for i in range(len(listToDrawQuestions)):
        
            index = int(listToDrawQuestions[i])
            self.enqueuedQuestions.append(listOfQuestions.displayQuestions(index))
        
        return self.enqueuedQuestions
        
    def askQuestions(self):
        
        for i in range(len(self.enqueuedQuestions)):
        
            self.questionsAsked.append(self.enqueuedQuestions[0])
            self.enqueuedQuestions.remove(self.enqueuedQuestions[0])

user1 = User("user1")
user1.points = 2

user2 = User("user2")
user2.points = 1

exampleUser = User("ExampleUser")
exampleUser.points = 5

user9876 = User("user9876")
user9876.points = 4

userUser = User("userUser")
userUser.points= 0

class ListOfUsers:

    def __init__(self):

        self.listOfUsers = []

    def addUser(self, user):

        self.listOfUsers.append(user)
   
    def displayListOfUsers(self):

        for i in range(len(self.listOfUsers)):
            print(self.listOfUsers[i])
    def sortRanking(self):
        for i in range (1, len(self.listOfUsers)):
            key = self.listOfUsers[i]['points']
            j = i-1
            while j>= 0 and key < self.listOfUsers[j]['points'] :
                self.listOfUsers[j + 1]['points'] = self.listOfUsers[j]['points']
                j -= 1 
                self.listOfUsers[j+1]['points'] = key
        sorted = []
        for x in self.listOfUsers:
            x = [x['username'], x['points']]
            sorted.append(x)
        return sorted  
    def searchAUser(self, username):
        username = username.__dict__
        self.sortRanking()
        l = 0 
        r = len(self.listOfUsers)-1
        while l <= r:
            mid = (l + r)// 2
            if self.listOfUsers[mid]['points'] == username['points']:
                return mid
            elif self.listOfUsers[mid]['points'] < username['points']:
                l = mid + 1
            elif self.listOfUsers[mid]['points'] > username['points']:
                r = mid - 1
        if self.listOfUsers[mid]['username'] == username['username']:
            return mid
        else:
            return "User not found"
listOfUsers = ListOfUsers()

listOfUsers.addUser(user1.__dict__)
listOfUsers.addUser(user2.__dict__)
listOfUsers.addUser(exampleUser.__dict__)
listOfUsers.addUser(user9876.__dict__)  
listOfUsers.addUser(userUser.__dict__)


print(listOfUsers.sortRanking())

print(listOfUsers.searchAUser(userUser))
        