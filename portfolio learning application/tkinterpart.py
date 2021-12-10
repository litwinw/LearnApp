import tkinter as tk
from tkinter import *
from QuestionClass import Question, ListOfQuestions
from UserAndQuestionsClass import User, ListOfUsers, listOfUsers

window = tk.Tk()

greeting = tk.Label(text = "Welcome in the learning application!\n Choose a language")
greeting.grid(row = 1, column = 2, padx = 5, pady = 5)

def clear():

    for label in window.grid_slaves():
        label.grid_forget()

def searchAUser(username):

    clear()
    
    listOfUsers.searchAUser(username)
    
    position = tk.Label(text= "This feature will be implemented in the next release")
    position.grid(row =3, column = 3, padx =5, pady = 5)
def displayResults(username):

    print(username.points)

def displayRanking(username):

    clear()
    
    RankingLabel= tk.Label(text = listOfUsers.sortRanking())
    RankingLabel.grid(rowspan = 1, columnspan = 4, padx = 5, pady =5)
    optionbutton = tk.Button(master = window, text="Search a user", width = 20, height = 2, bg="blue", command= lambda: searchAUser(username))
    optionbutton.grid(row = 2, column = 1, padx = 5, pady = 5)
def menu(username ):

    clear()

    menulabel = tk.Label(text= "Congratulations! You finished the exercise!\n What do you want to do now?")
    menulabel.grid(row = 1, columnspan = 3, padx = 5, pady = 5)

    option1 = tk.Button(master = window, text="Display results", width = 20, height = 2, bg="blue", command= lambda: displayResults(username))
    option1.grid(row = 2, column = 1, padx = 5, pady = 5)

    option2 = tk.Button(master = window, text="Display ranking", width = 20, height = 2, bg="blue", command= lambda: displayRanking(username))
    option2.grid(row = 2, column = 3, padx = 5, pady= 5)

def ask5Question(username):
     
    i = 4

    clear()

    var = StringVar(master = window)

    Question1 = tk.Label(text = username.enqueuedQuestions[i]['questionContent'])
    Question1.grid(row = 1, columnspan = 3, padx = 5, pady = 5)
    
    answerA = tk.Radiobutton(window, text = username.enqueuedQuestions[i]['ansA'], variable=var, value = "A", command =lambda: menu(username), width=20, height=5)
    answerB = tk.Radiobutton(window, text = username.enqueuedQuestions[i]['ansB'], variable=var, value = "B", command =lambda: menu(username), width=20, height=5)
    answerC = tk.Radiobutton(window, text = username.enqueuedQuestions[i]['ansC'], variable=var, value = "C", command =lambda: menu(username), width=20, height=5)
    answerD = tk.Radiobutton(window, text = username.enqueuedQuestions[i]['ansD'], variable=var, value = "D", command =lambda: menu(username), width=20, height=5)

    userAns = var.get()

    answerA.grid(row = 2, column = 1, padx = 5, pady = 5)
    answerB.grid(row = 2, column = 2, padx = 5, pady = 5)
    answerC.grid(row = 2, column = 3, padx = 5, pady = 5)
    answerD.grid(row = 2, column = 4, padx = 5, pady = 5)

    print(userAns)
    
    if userAns == username.enqueuedQuestions[i]['rightAnswer']:
        username.points += username.enqueuedQuestions[i]['pointsForAnswer']
    
    username.askQuestions() #This method will store all asked questions in the list in user object

def ask4Question(username):
     
    i = 3
   
    clear()
   
    var = StringVar(master = window)
   
    Question1 = tk.Label(text = username.enqueuedQuestions[i]['questionContent'])
    Question1.grid(row = 1, columnspan = 3, padx = 5, pady = 5)
     
    answerA = tk.Radiobutton(window, text = username.enqueuedQuestions[i]['ansA'], variable=var, value = "A", command =lambda:ask5Question(username) , width=20, height=5)
    answerB = tk.Radiobutton(window, text = username.enqueuedQuestions[i]['ansB'], variable=var, value = "B", command =lambda:ask5Question(username) , width=20, height=5)
    answerC = tk.Radiobutton(window, text = username.enqueuedQuestions[i]['ansC'], variable=var, value = "C", command = lambda:ask5Question(username), width=20, height=5)
    answerD = tk.Radiobutton(window, text = username.enqueuedQuestions[i]['ansD'], variable=var, value = "D", command = lambda:ask5Question(username), width=20, height=5)
    
    userAns = var.get()
    
    answerA.grid(row = 2, column = 1, padx = 5, pady = 5)
    answerB.grid(row = 2, column = 2, padx = 5, pady = 5)
    answerC.grid(row = 2, column = 3, padx = 5, pady = 5)
    answerD.grid(row = 2, column = 4, padx = 5, pady = 5)

    userAns.upper()
    print(userAns)
    
    if userAns == username.enqueuedQuestions[i]['rightAnswer']:
        username.points += username.enqueuedQuestions[i]['pointsForAnswer']

def ask3Question(username):
 
    i = 2

    clear()

    var = StringVar(master = window)

    Question1 = tk.Label(text = username.enqueuedQuestions[i]['questionContent'])
    Question1.grid(row = 1, columnspan = 3, padx = 5, pady = 5)
    
    answerA = tk.Radiobutton(window, text = username.enqueuedQuestions[i]['ansA'], variable=var, value = "A", command =lambda:ask4Question(username) , width=20, height=5)
    answerB = tk.Radiobutton(window, text = username.enqueuedQuestions[i]['ansB'], variable=var, value = "B", command =lambda: ask4Question(username) , width=20, height=5)
    answerC = tk.Radiobutton(window, text = username.enqueuedQuestions[i]['ansC'], variable=var, value = "C", command =lambda:ask4Question(username), width=20, height=5)
    answerD = tk.Radiobutton(window, text = username.enqueuedQuestions[i]['ansD'], variable=var, value = "D", command =lambda: ask4Question(username), width=20, height=5)
    userAns = var.get()

    answerA.grid(row = 2, column = 1, padx = 5, pady = 5)
    answerB.grid(row = 2, column = 2, padx = 5, pady = 5)
    answerC.grid(row = 2, column = 3, padx = 5, pady = 5)
    answerD.grid(row = 2, column = 4, padx = 5, pady = 5)
    print(userAns)
    userAns.upper()

    if userAns == username.enqueuedQuestions[i]['rightAnswer']:
        username.points += username.enqueuedQuestions[i]['pointsForAnswer']

def ask2Question(username,userAns):
    userAns.upper()
    print(userAns)
    if userAns == username.enqueuedQuestions[0]['rightAnswer']:
        username.points += username.enqueuedQuestions[0]['pointsForAnswer']
    i = 1
    print(username.enqueuedQuestions[i])
    clear()

    var = StringVar(master = window)

    Question1 = tk.Label(text = username.enqueuedQuestions[i]['questionContent'])
    Question1.grid(row = 1, columnspan = 3, padx = 5, pady = 5)
        
    answerA = tk.Radiobutton(window, text = username.enqueuedQuestions[i]['ansA'], variable=var, value = 'A', command =ask3Question(username) , width=20, height=5)
    answerB = tk.Radiobutton(window, text = username.enqueuedQuestions[i]['ansB'], variable=var, value = 'B', command =ask3Question(username) , width=20, height=5)
    answerC = tk.Radiobutton(window, text = username.enqueuedQuestions[i]['ansC'], variable=var, value = 'C', command = ask3Question(username), width=20, height=5)
    answerD = tk.Radiobutton(window, text = username.enqueuedQuestions[i]['ansD'], variable=var, value = 'D', command = ask3Question(username), width=20, height=5)
    
    userAns = var.get()
    
    answerA.grid(row = 2, column = 1, padx = 5, pady = 5)
    answerB.grid(row = 2, column = 2, padx = 5, pady = 5)
    answerC.grid(row = 2, column = 3, padx = 5, pady = 5)
    answerD.grid(row = 2, column = 4, padx = 5, pady = 5)
    print(userAns)
    userAns.upper()
    right=username.enqueuedQuestions[i]['rightAnswer']
    if userAns == right:
        username.points += username.enqueuedQuestions[i]['pointsForAnswer']

def ask1Question(username):

    i = 0

    clear()

    var = StringVar(window)
    Question1 = tk.Label(text = username.enqueuedQuestions[i]['questionContent'])
    Question1.grid(row = 1, columnspan = 3, padx = 5, pady = 5)
    
    answerA = tk.Radiobutton(window, text = username.enqueuedQuestions[i]['ansA'], variable=var, value = 'A', command =lambda: ask2Question(username,userAns) , width=20, height=5)
    answerB = tk.Radiobutton(window, text = username.enqueuedQuestions[i]['ansB'], variable=var, value = 'B', command =lambda: ask2Question(username,userAns) , width=20, height=5)
    answerC = tk.Radiobutton(window, text = username.enqueuedQuestions[i]['ansC'], variable=var, value = 'C', command =lambda: ask2Question(username,userAns), width=20, height=5)
    answerD = tk.Radiobutton(window, text = username.enqueuedQuestions[i]['ansD'], variable=var, value = 'D', command =lambda: ask2Question(username,userAns), width=20, height=5)
    
    answerA.grid(row = 2, column = 1, padx = 5, pady = 5)
    answerB.grid(row = 2, column = 2, padx = 5, pady = 5)
    answerC.grid(row = 2, column = 3, padx = 5, pady = 5)
    answerD.grid(row = 2, column = 4, padx = 5, pady = 5)

    userAns = var.get()


        
def afterCreate(entry):

    username = entry.get()
    username = User(username)

    listOfUsers.addUser(username.__dict__)

    message2= tk.Label(text = "Thank you! You will be asked some questions marked with 0-3 points.\nEach question contains 4 possible answers. Choose the right one.\n Good luck!\n ")
    message2.grid(row = 3, column = 1, padx = 5, pady = 5)

    listOfUsers.displayListOfUsers()

    username.createASetOfQuestions()
    
    button=tk.Button(master=window, width = 10, height = 5, text = "Start", command =lambda:  ask1Question(username))
    button.grid(row = 3, column = 2, padx = 5, pady = 5)
    
def Englishbutton():

    clear()

    message1 = tk.Label(width = 50, height = 10, bg= "white", text = "We need your username to compare your results with other users.\n Please enter a username: ")
    message1.grid(row = 1, column = 1, padx = 5, pady = 5)

    entry= tk.Entry (window)
    entry.grid(row = 2, column = 1, padx = 5, pady = 5)

    createButton = tk.Button(master=window, width = 20, height = 5, text = "Create", command =lambda: afterCreate(entry))
    createButton.grid(row = 2, column = 2, padx = 5, pady = 5)
    
def Spanishbutton():

    message = tk.Label(width = 20, height = 5, text = "This part of application will be developed later")
    message.grid(rowspan =3 , column = 2, padx = 5, pady = 5)

def Germanbutton():

    message = tk.Label(text = "This part of application will be developed later")
    message.grid(row = 3, column = 3, padx = 5, pady = 5)

button1 = tk.Button(master = window, text="English", width = 10, height = 2, bg="blue", command=Englishbutton)

button2 = tk.Button(master=window, text="Spanish", width = 10, height = 2, bg="blue", command=Spanishbutton)

button3 = tk.Button(master=window, text="German", width = 10, height = 2, bg="blue", command=Germanbutton)

button1.grid(row = 2, column = 1, padx = 5, pady = 5)

button2.grid(row = 2, column = 2, padx = 5, pady = 5)

button3.grid(row = 2, column = 3, padx = 5, pady = 5)

window.mainloop()