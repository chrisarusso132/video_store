# **NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

from breezypythongui import EasyFrame
from tkinter.font import Font

class VideoStore(EasyFrame):

    def __init__(self):
        
        # Call to the Easy Frame class constructor
        EasyFrame.__init__(self, title="Video Rental", background="orange2", resizable=False)
        # Variable to store a Font design for multiple labels (Must come before needing to use the variable in your code)
        labelFont = Font(family="Arial", size=15)

        # Top panel with movie selection checkboxes
        topPanel = self.addPanel(row=0, column=0, columnspan=2, background="blue")
        topPanel.addLabel(text="BLOCKBOOSTER", row=0, column=0, sticky="NSEW", columnspan=2, background="blue", foreground="orange2", font=Font(family="Impact", size=22))
        
        # Label for new movie section and price
        topPanel.addLabel(text="New Selection = $3.50 Per Copy", row=1, column=0, columnspan=2, sticky="NSEW", background="orange2", foreground="black", font=labelFont)

        # Checkboxes for new movie selections
        self.opp = topPanel.addCheckbutton(text="Oppenheimer", row=2, column=0, sticky="W")
        self.barbie = topPanel.addCheckbutton(text="Barbie", row=2, column=1, sticky="W")
        self.spider = topPanel.addCheckbutton(text="Spiderman Across\nthe Spiderverse", row=3, column=0, sticky="W")
        self.creed = topPanel.addCheckbutton(text="Creed 3", row=3, column=1, sticky="W")
        self.tenet = topPanel.addCheckbutton(text="Tenet", row=4, column=0, sticky="W")
        self.avatar = topPanel.addCheckbutton(text="Avatar", row=4, column=1, sticky="W")
        self.top = topPanel.addCheckbutton(text="Top Gun: Maverick", row=5, column=0, sticky="W")
        self.godzilla = topPanel.addCheckbutton(text="Godzilla Minus One", row=5, column=1, sticky="W")
        self.everything = topPanel.addCheckbutton(text="Everything Everywhere\nAll at Once", row=6, column=0, sticky="W")
        self.past = topPanel.addCheckbutton(text="Past Lives", row=6, column=1, sticky="W")

        # Label for old movie section and price
        topPanel.addLabel(text="Old Selection = $2.00 Per Copy", row=7, column=0, columnspan=2, sticky="NSEW", background="orange2", foreground="black", font=labelFont)
        # Checkboxes for old movie selection
        self.shaw = topPanel.addCheckbutton(text="The Shawshank Redemtion", row=8, column=0, sticky="W")
        self.forrest = topPanel.addCheckbutton(text="Forrest Gump", row=8, column=1, sticky="W")
        self.raiders = topPanel.addCheckbutton(text="Raiders of the Lost Ark", row=9, column=0, sticky="W")
        self.matrix = topPanel.addCheckbutton(text="The Matrix", row=9, column=1, sticky="W")
        self.terminator = topPanel.addCheckbutton(text="The Terminator", row=10, column=0, sticky="W")
        self.die = topPanel.addCheckbutton(text="Die Hard", row=10, column=1, sticky="W")
        self.basterds = topPanel.addCheckbutton(text="Inglourious Basterds", row=11, column=0, sticky="W")
        self.gladiator = topPanel.addCheckbutton(text="Gladiator", row=11, column=1, sticky="W")

        # Styling for checkboxes
        for checkbox in [self.opp, self.barbie, self.spider, self.creed, self.forrest, self.shaw, self.raiders, self.matrix, self.tenet, self.avatar, self.top, self.godzilla, self.everything, self.past, self.terminator, self.die, self. basterds, self.gladiator]:
            checkbox["background"] = "blue"
            checkbox["foreground"] = "orange2"
            checkbox["font"] = labelFont

        # Calculate button
        self.calculate = self.addButton(text="CALCULATE", row=12, column=0, columnspan=2, command=self.calculate)

        # Bottom panel with output labels
        bottomPanel = self.addPanel(row=13, column=0, columnspan=2, background="blue4")
        self.outputSub = bottomPanel.addLabel(text="", row=0, column=0, columnspan=2, sticky="NSEW", background="blue4", foreground="white")
        self.outputTax = bottomPanel.addLabel(text="", row=1, column=0, columnspan=2, sticky="NSEW", background="blue4", foreground="white")
        self.outputTotal = bottomPanel.addLabel(text="", row=2, column=0, columnspan=2, sticky="NSEW", background="blue4", foreground="white")

        
    def calculate(self):
        # Sets new and old variable to a preset of 0
        new = 0
        old = 0

        # New movies, if checkbox is selected update "new" variable
        if self.opp.isChecked():
            new += 3.50
        if self.barbie.isChecked():
            new += 3.50
        if self.spider.isChecked():
            new += 3.50
        if self.creed.isChecked():
            new += 3.50
        if self.tenet.isChecked():
            new += 3.50
        if self.avatar.isChecked():
            new += 3.50
        if self.top.isChecked():
            new += 3.50
        if self.godzilla.isChecked():
            new += 3.50
        if self.everything.isChecked():
            new += 3.50
        if self.past.isChecked():
            new += 3.50

        # Old movies, if checkbox is selected update "old" variable
        if self.shaw.isChecked():
            old += 2
        if self.forrest.isChecked():
            old += 2
        if self.raiders.isChecked():
            old += 2
        if self.matrix.isChecked():
            old += 2
        if self.terminator.isChecked():
            old += 2
        if self.die.isChecked():
            old += 2
        if self.basterds.isChecked():
            old += 2
        if self.gladiator.isChecked():
            old += 2

        # Calculate subtotal and output it
        subtotal = new + old
        self.outputSub["text"] = "Subtotal: $%0.2f" % subtotal

        # Calculate tax and total. Output to proper areas
        self.outputTax["text"] = "Tax: 8.79%"
        tax = subtotal * 0.0879
        total = subtotal + tax
        self.outputTotal["text"] = "Total: $%0.2f" % total

def main():
    # Instantiate an object from the class into mainloop()
    VideoStore().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
    main()
