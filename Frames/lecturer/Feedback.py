import tkinter as tk


class Feedback:
    def __init__(self, root, res):
        if res:
            print(res['message'])
            for response in res['message']:
                frame = tk.Frame(root)
                frame.pack()
                label = tk.Label(frame, justify='left', text=f"{response['email']} : {response['feedback']}",
                                 font=('Arial', '10'))
                label.pack(expand=True)

