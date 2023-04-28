from tkinter import*

class Table:
    
    def __init__(self, root):
        for i in range(totalRow):
            for j in range(totalColumn):
                self.e = Entry(root, width=22, fg='blue', font=('Arial', '15', 'bold'))
                self.e.grid(row=i , column=j) 
                self.e.insert(END, listData[i][j])
                

listData = [
    ('Students: ', 'Jason', 'Laniya', 'Parker',),
    ('Classwork Grade : ', '89', '77', '82',),
    ('Quiz Grades : ', '90', '88', '70',),
    ('Test Grade : ', '76', '80', '77',)
    

]

totalRow = len(listData)
totalColumn = len(listData[0]) 


root = Tk()
t = Table(root)
root.mainloop()