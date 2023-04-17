from tkinter import Frame, Label


class Files:
    def __init__(self, root):
        self.frame = Frame(root)
        Label(self.frame, text="Files Page",font=("Arial",20)).grid(row=0, column=0)
        Label(self.frame, text="No Files Available").grid(row=1, column=0)
