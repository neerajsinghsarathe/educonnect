import tkinter as tk


class Assignments:
    def __init__(self, root, res):
        if res:
            print(res['message'])
            for response in res['message']:
                frame = tk.Frame(root)
                frame.pack()
                label = tk.Label(frame, justify='left', text=f"Question : {response['question']}",
                                 font=('Arial', '15'))
                label.pack(expand=True)
                label = tk.Label(frame, justify='left', text=f"Data : {response['data']}",
                                 font=('Arial', '15'))
                label.pack(expand=True)
