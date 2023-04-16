import tkinter as tk

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest ocean in the world?",
        "options": ["Atlantic Ocean", "Arctic Ocean", "Indian Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Yen", "Dollar", "Euro", "Pound"],
        "answer": "Yen"
    }
]

user_answers = {}


def select_option(question_index, option):
    user_answers[question_index] = option


class Quizzes:
    def __init__(self, root):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Paris", "Berlin", "Madrid"],
                "answer": "Paris"
            },
            {
                "question": "What is the largest ocean in the world?",
                "options": ["Atlantic Ocean", "Arctic Ocean", "Indian Ocean", "Pacific Ocean"],
                "answer": "Pacific Ocean"
            },
            {
                "question": "What is the currency of Japan?",
                "options": ["Yen", "Dollar", "Euro", "Pound"],
                "answer": "Yen"
            }
        ]

        # Create a dictionary to store the user's answers
        self.user_answers = {}

        # Create a frame to display the questions
        self.questions_frame = tk.Frame(root)
        self.questions_frame.pack()

        # Add a label to display the title of the quiz
        self.title_label = tk.Label(self.questions_frame, text="Quiz")
        self.title_label.pack(side=tk.TOP, padx=5, pady=5)

        # Loop through each question and add it to the frame
        for i, question in enumerate(self.questions):
            # Add a label for the question
            question_label = tk.Label(self.questions_frame, text=f"{i + 1}. {question['question']}")
            question_label.pack(side=tk.TOP, padx=5, pady=5)

            # Loop through each option and add it to the frame as a radio button
            for option in question["options"]:
                option_button = tk.Radiobutton(self.questions_frame, text=option, variable=i, value=option,
                                               command=lambda i=i, option=option: self.select_option(i, option))
                option_button.pack(side=tk.TOP, padx=5, pady=2)

        # Add a button to submit the answers
        self.submit_button = tk.Button(self.questions_frame, text="Submit", command=self.submit_answers)
        self.submit_button.pack(side=tk.TOP, padx=5, pady=5)

        # Add a label to display the result of the quiz
        self.result_label = tk.Label(self.questions_frame, text="")
        self.result_label.pack(side=tk.TOP, padx=5, pady=5)

        # Function to handle submit button click

    def submit_answers(self):
        # Check if all questions have been answered
        if len(self.user_answers) != len(self.questions):
            self.result_label.config(text="Please answer all questions.")
            return

        # Check each answer and update the result label
        correct_answers = 0
        for i, question in enumerate(self.questions):
            if self.user_answers[i] == question["answer"]:
                correct_answers += 1
        self.result_label.config(text=f"You got {correct_answers} out of {len(self.questions)} questions correct.")

    def select_option(self, question_index, option):
        self.user_answers[question_index] = option
