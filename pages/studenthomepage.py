import tkinter as tk
from tkinter import *

from Frames.Assignments import Assignments
from Frames.Courses import Courses
from Frames.DiscussionForum import DiscussionForum
from Frames.Files import Files
from Frames.Quizzes import Quizzes


def destroyAllFrames(root):
    for frame in root.winfo_children():
        frame.pack_forget()
        for widget in frame.winfo_children():
            widget.destroy()


def goTo(self, frameName):
    destroyAllFrames(self)
    match frameName:
        case 'Courses':
            Courses(self).frame.pack()
        case 'Assignments':
            Assignments(self).frame.pack()
        case 'Quizzes':
            Quizzes(self).frame.pack()
        case 'Files':
            Files(self).frame.pack()
        case 'Discussion Forum':
            DiscussionForum(self).frame.pack()
        case 'exit':
            self.destroy()


class StudentHomePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('HomePage')
        self.geometry('500x300')

        # Creating Menubar
        menubar = Menu(self)
        self.config(menu=menubar)

        # Adding Menus
        menubar.add_command(label='Courses', command=lambda: goTo(self, 'Courses'))
        menubar.add_command(label='Assignments', command=lambda: goTo(self, 'Assignments'))
        menubar.add_command(label='Quizzes', command=lambda: goTo(self, 'Quizzes'))
        menubar.add_command(label='Files', command=lambda: goTo(self, 'Files'))
        menubar.add_command(label='Discussion Forum', command=lambda: goTo(self, 'Discussion Forum'))
        menubar.add_command(label='Exit', command=lambda: goTo(self, 'exit'))

# if __name__ == "__main__":
#     app = HomePage()
#     app.mainloop()
