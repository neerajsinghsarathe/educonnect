import tkinter as tk
import subprocess as sb_p
from Login import Login


def navigateTo(current, userType):
    current.destroy()
    Login(userType).mainloop()


class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("400x400")
        self.title("EduConnect")
        label = tk.Label(self, text="Enter your Credentials", font=('Helvetica', 18))
        label.pack(padx=10, pady=20)

        studentLoginButton = tk.Button(self, width=20, text="Student Login", font=('Helvetica', 14),
                                       command=lambda: navigateTo(self, 'student'))
        studentLoginButton.pack(padx=10, pady=10)

        lecturerLoginButton = tk.Button(self, width=20, text="Lecturer Login", font=('Helvetica', 14),
                                        command=lambda: navigateTo(self, 'lecturer'))
        lecturerLoginButton.pack(padx=10, pady=10)

        newWindowButton = tk.Button(self, width=20, text="New Window", font=('Helvetica', 14),
                                    command=lambda: sb_p.call("start python main.py", shell=True))
        newWindowButton.pack(padx=10, pady=10)


if __name__ == "__main__":
    app = Main()
    app.mainloop()
