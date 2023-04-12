from tkinter import Frame, Label


class Files:
    def __init__(self, root):
        self.frame = Frame(root)
        Label(self.frame, text="Files Page").grid(row=0, column=0)
