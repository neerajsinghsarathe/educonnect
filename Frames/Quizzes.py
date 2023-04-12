from tkinter import Frame, Label


class Quizzes:
    def __init__(self, root):
        self.frame = Frame(root)
        Label(self.frame, text="Quizzes Page").grid(row=0, column=0)
