import tkinter as tk
from PIL import ImageTk, Image

courses = [
    {"name": "Python Programming", "details": "Learn Python programming language"},
    {"name": "Web Development", "details": "Build web applications using HTML, CSS, and JavaScript"},
    {"name": "Data Science", "details": "Learn data analysis and machine learning using Python"},
    {"name": "Mobile App Development", "details": "Build mobile apps using Java or Kotlin"}
]


class Courses:

    def __init__(self, root):
        frame = tk.Frame(root)
        frame.pack()

        label = tk.Label(frame, text="Courses Page", font=('Arial', '20'))
        label.pack()

        root.geometry('500x300')

        for course in courses:
            course_widget = tk.Frame(frame)
            course_widget.pack(side=tk.TOP, padx=5, pady=5)

            name_label = tk.Label(course_widget, text=course["name"])
            name_label.pack(side=tk.LEFT)

            enrollButton = tk.Button(course_widget, width=10, text="Enroll",
                                     command=lambda name=course["name"]: enroll(name))
            enrollButton.pack(padx=10, pady=10, side=tk.LEFT)

            viewDetailsButton = tk.Button(course_widget, width=10, text="View Details",
                                          command=lambda details=course["details"]: view_details(details))
            viewDetailsButton.pack(padx=10, pady=10, side=tk.LEFT)

        def enroll(course_name):
            print(f"Enrolling in {course_name}...")

        def view_details(details):
            # Open a new window to show course details
            details_window = tk.Toplevel()
            details_window.title('Course Details')
            details_label = tk.Label(details_window, text=details)
            details_label.pack()

        # lecturerButton = Button(self.frame, text="Lecturer Login", font=('Helvetica', 18))
        # lecturerButton.pack(padx=10, pady=10)
