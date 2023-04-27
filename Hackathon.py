'STOP IF YOU GET HERE' "woofjgnnins"
from breezypythongui import EasyFrame

class Rock_Paper_Scissors(EasyFrame):
    
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = 'Final Grades!')

        # Label and field for User play
        # TRANSIT TO TEXT FIELD WHEN
        self.addLabel(text = "Student Final Grade ",
                      row = 4, column = 0)
        self.playField = self.addIntegerField(value=0, row = 4, column = 1)
        
        self.addLabel(text = "Student Test Grade ",
                      row = 2, column = 0)
        self.playField = self.addIntegerField(value=0, row = 2, column = 1)
        
        self.addLabel(text = "Student Midterm Grade  ",
                      row = 3, column = 0)
        self.playField = self.addIntegerField(value=0, row = 3, column = 1)
        
        
        self.addLabel(text = "Student Quiz Grade",
                      row = 1, column = 0)
        self.playField = self.addIntegerField(value=0, row = 1, column = 1)



        self.addLabel(text = "Student Attendence",
                      row = 0, column = 0)
        self.playField = self.addIntegerField(value=0, row = 0, column = 1)

        # The Play button
        self.addButton(text = "Check", row = 2, column = 0,
                       columnspan = 2, command = self.rps_winner)

        # Label and field for the user's play
        self.addLabel(text = "Pass/Fail",
                      row = 5, column = 0)
        self.userField = self.addTextField(text = "", row = 5,
                                           column = 1,
                                           state = "readonly")

        
    


    
    # The event handler method for the button
    def rps_winner(self):
        """Obtains the data from the input field and uses
        that to choose the winner of the rock, paper, and
        scissors game."""
        user_play = self.playField.getNumber()             # user play
        comp_play = computer_choice()                      # computer play
        who_won = compare(user_play, comp_play)            # winner (int)
        the_winner = passFail(user_play, comp_play, who_won) # winner (string)
        self.userField.setText(num_to_word(user_play))     # display user play
        self.compField.setText(num_to_word(comp_play))     # display computer play
        self.winField.setText(the_winner)                  # display winner
           
# ------------------------------------
# Function to get computer's play
def computer_choice():
    from random import randint
    return randint (0,2)

# --------------------------------
# Function to compare choices
def compare(p1choice, p2choice):
    # Player 1 wins
    if (p1choice == 0 and p2choice == 2) \
    or (p1choice == 1 and p2choice == 0) \
    or (p1choice == 2 and p2choice == 1):
        return 

    # There is a tie
    elif p1choice == p2choice:
        return 0
    
    # Otherwise Player 2 wins
    else:
        return 2


# ------------------------------------
# Display the winner as a message
def passFail(p1c, p2c, who):
    p1c = num_to_word(p1c)
    p2c = num_to_word(p2c)
    
    if who >= 0:  # Player 1 won
        return 'Student is Passing!'
         
    elif who <= 59:
         return 'Student is Failing'
     
    elif who == 69:
        return 'Student is in Warning'
        
    else:
        return 'INVALID'

# ------------------------------------------------
# Convert numbers to words for player choices
def num_to_word(number):
    if number >= 70:
        return 'Passing'
    elif number >= 60:
        return 'Warning'
    elif number <= 59:
        return 'Failing'
    else:
        return 'Invalid input!'

# ------------------
# Main function
def main():
    Rock_Paper_Scissors().mainloop()
    
# ------------------------------------------------------------------------
# Driver section:  this is the part that is executed when code is run
if __name__ == "__main__":
    main()
    nw = EasyFrame()

