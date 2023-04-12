from tkinter import Frame, Label


class DiscussionForum:
    def __init__(self, root):
        self.frame = Frame(root)
        Label(self.frame, text="Discussion Forum Page").grid(row=0, column=0)

