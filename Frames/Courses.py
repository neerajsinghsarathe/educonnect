from tkinter import Frame, Label


class Courses:
    def __init__(self, root):

        self.frame = Frame(root)
        Label(self.frame, text="Courses Page").grid(row=0, column=0)

