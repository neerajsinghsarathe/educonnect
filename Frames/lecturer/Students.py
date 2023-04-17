import tkinter as tk

from services.services import getStudents


class Students:

    def __init__(self, root, res):
        if res:
            print(res['message'])
            for name in res['message']:
                label = tk.Button(root, width=15, text=name['name'], font=('Arial', '15'))
                label.pack()
