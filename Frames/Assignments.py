from tkinter import Frame, Label


class Assignments:
    def __init__(self, root):
        self.frame = Frame(root)
        Label(self.frame, text="Assignment Page").grid(row=0, column=0)

