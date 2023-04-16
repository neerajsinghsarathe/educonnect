import tkinter as tk

assignments = [
    {"assignment_no": "1", "question": "Python Programming"},
    {"assignment_no": "2", "question": "Web Development"},
    {"assignment_no": "3", "question": "Data Science"},
    {"assignment_no": "4", "question": "Mobile App Development"}
]


class Assignments:
    def __init__(self, root):
        frame = tk.Frame(root)
        frame.pack()

        label = tk.Label(frame, text="Courses Page", font=('Arial', '20'))
        label.pack()

        for assignment in assignments:
            course_widget = tk.Frame(frame)
            course_widget.pack(side=tk.TOP, padx=5, pady=5)

            name_label = tk.Label(course_widget, text=assignment["question"])
            name_label.pack(side=tk.LEFT)

            enrollButton = tk.Button(course_widget, width=10, text="Submit",
                                     command=lambda name=assignment["assignment_no"]: submit(name))
            enrollButton.pack(padx=10, pady=10, side=tk.LEFT)

        def submit(assignment_title):
            print(f"Submitting {assignment_title}...")
