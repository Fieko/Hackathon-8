import tkinter as tk
import tkinter.simpledialog
import tkinter.messagebox
from tkinter import ttk
from tkinter import *
import time
import re

LargeFont = ("Verdana", 12)


def options():
    print ('''\n**************************************************************
          Student Grade Tracker
**************************************************************''')

class PageContainer(tk.Tk):
    def __init__(self, *args, **kwargs):
        options()
        tk.Tk.__init__(self, *args, **kwargs)
		
        container = tk.Frame(self)  
        tk.Tk.geometry(self,'250x250')  
        container.pack(side='top', fill='both', expand = True )     
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frame = {}

        for F in (MainMenu, Student1, Student2, Student3, Student4, Student5):

            frame = F(container, self)

            self.frame[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew") 

        self.show_frame(MainMenu)
	
    def show_frame(self, cont):
        frame = self.frame[cont]    
        frame.tkraise()

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)   
        label = tk.Label(self, text="MAIN MENU", font = LargeFont)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text = "Student1", command = lambda: controller.show_frame(Student1), width = 20, height = 1)     
        button2 = tk.Button(self, text = "Student2", command = lambda: controller.show_frame(Student2), width = 20, height = 1)
        button3 = tk.Button(self, text = "Student3", command = lambda: controller.show_frame(Student3), width = 20, height = 1)
        button4 = tk.Button(self, text = "Student4", command = lambda: controller.show_frame(Student4), width = 20, height = 1)
        button5 = tk.Button(self, text = "Student5",command = lambda: controller.show_frame(Student5), width = 20, height = 1)
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()

class Student1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Student1", font = LargeFont)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text = "Input Email", command = input_email, width = 25, height = 1)
        button1.pack()
        button2 = tk.Button(self, text = "Input Student Grades", command = lambda: controller.show_frame(grade), width = 25, height = 1)
        button2.pack()
        button3 = tk.Button(self, text = "Student Weighted Grade", command = stud_grade, width = 25, height = 1)
        button3.pack()
        button4 = tk.Button(self, text = "Status", command = status, width = 25, height = 1)
        button4.pack()
        button5 = tk.Button(self, text = "Main Menu",command = lambda: controller.show_frame(MainMenu), width = 25, height = 1)
        button5.pack()

class Student2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Student2", font = LargeFont)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text = "Input Email", command = input_email, width = 25, height = 1)
        button1.pack()
        button2 = tk.Button(self, text = "Input Student Grades", command = lambda: controller.show_frame(grade), width = 25, height = 1)
        button2.pack()
        button3 = tk.Button(self, text = "Student Weighted Grade", command = stud_grade, width = 25, height = 1)
        button3.pack()
        button4 = tk.Button(self, text = "Status", command = status, width = 25, height = 1)
        button4.pack()
        button5 = tk.Button(self, text = "Main Menu",command = lambda: controller.show_frame(MainMenu), width = 25, height = 1)
        button5.pack()

class Student3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Student3", font = LargeFont)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text = "Input Email", command = input_email, width = 25, height = 1)
        button1.pack()
        button2 = tk.Button(self, text = "Input Student Grades", command = lambda: controller.show_frame(grade), width = 25, height = 1)
        button2.pack()
        button3 = tk.Button(self, text = "Student Weighted Grade", command = stud_grade, width = 25, height = 1)
        button3.pack()
        button4 = tk.Button(self, text = "Status", command = status, width = 25, height = 1)
        button4.pack()
        button5 = tk.Button(self, text = "Main Menu",command = lambda: controller.show_frame(MainMenu), width = 25, height = 1)
        button5.pack()

class Student4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Student4", font = LargeFont)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text = "Input Email", command = input_email, width = 25, height = 1)
        button1.pack()
        button2 = tk.Button(self, text = "Input Student Grades", command = lambda: controller.show_frame(grade), width = 25, height = 1)
        button2.pack()
        button3 = tk.Button(self, text = "Student Weighted Grade", command = stud_grade, width = 25, height = 1)
        button3.pack()
        button4 = tk.Button(self, text = "Status", command = status, width = 25, height = 1)
        button4.pack()
        button5 = tk.Button(self, text = "Main Menu",command = lambda: controller.show_frame(MainMenu), width = 25, height = 1)
        button5.pack()

class Student5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Student5", font = LargeFont)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text = "Input Email", command = input_email, width = 25, height = 1)
        button1.pack()
        button2 = tk.Button(self, text = "Input Student Grades", command = lambda: controller.show_frame(grade), width = 25, height = 1)
        button2.pack()
        button3 = tk.Button(self, text = "Student Weighted Grade", command = stud_grade, width = 25, height = 1)
        button3.pack()
        button4 = tk.Button(self, text = "Status", command = status, width = 25, height = 1)
        button4.pack()
        button5 = tk.Button(self, text = "Main Menu",command = lambda: controller.show_frame(MainMenu), width = 25, height = 1)
        button5.pack()
        
class grade(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter Grades", font = LargeFont)
        label.pack(pady=10,padx=10)

def input_email():
    email = tkinter.simpledialog.askstring(title= "email", prompt = "Please enter your email to receive alerts: ")
    print("Thank You", email)
    tkinter.messagebox.showinfo("Message", "Received email")
    check_email(email)

def check_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if (re.fullmatch(regex, email)):
        tkinter.messagebox.showinfo("Message", "Email Valid")
        print("Valid Email")
 
    else:
        tkinter.messagebox.showinfo("Message", "Email InValid")
        print("Invalid Email")

    
    

def stud_grade():
sumOfallGrades = grade1+grade2+grade3+grade4+grade5
average = sumOfallGrades/5


def status():	
if average >= 90:
        print(name + "is passing with an letter grade of A")
    elif average >= 80:
        print(name + "is passing with an letter grade of B")
    elif average >= 70:
        print("*CAUTION* " + name + "is passing with an letter grade of C")
    elif average >= 60:
        print("*CAUTION* " + name + "is passing with an letter grade of D, but will not recieve credit points from the University")
    else:
        print("*CAUTION* " + "The student " + name + " is failing the class, We are sending an email to Alert you now")
	email_sender = "codefriendlyvsu@gmail.com"
	email_password ="ydjhkctorziqkfnz"
	email_reciever = "darienwalker121@outlook.com"
	student1 = "Nichalos"
	
	subject = "STUDENT ACADEMIC WARNING"
	body = """
	NOTICE: Your Student """ + student1 """is currently in Academic Warning status Please email you student and schedule an appointment. 
	
	"""
	em = EmailMessage()
	em["From"] = email_sender 
	em['To'] = email_reciever
	em['Subject'] = subject 
	em.set_content(body)
	
	context = ssl.create_default_context()
	
	with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
		smtp.login(email_sender, email_password)
		smtp.sendmail(email_sender, email_reciever, em.as_string())


    
        
    
app = PageContainer()
app.mainloop() 


    
