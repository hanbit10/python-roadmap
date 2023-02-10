def start_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "answer": "Paris"
        },
        {
            "question": "What is the largest ocean in the world?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": "Pacific Ocean"
        },
        {
            "question": "Who was the first president of the United States?",
            "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John F. Kennedy"],
            "answer": "George Washington"
        },
        {
            "question": "What is the currency used in Japan?",
            "options": ["Yen", "Dollar", "Euro", "Pound"],
            "answer": "Yen"
        },
        {
            "question": "What is the highest mountain in the world?",
            "options": ["Mount Kilimanjaro", "Mount Everest", "Mount Denali", "Mount Aconcagua"],
            "answer": "Mount Everest"
        }
    ]
    score = 0
    for i, question in enumerate(questions):
        print(f"Question {i + 1}: {question['question']}")
        print("Options: ", question["options"])
        user_answer = input("Your answer: ")
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {question['answer']}.")
        print()
    print(f"You scored {score} out of {len(questions)}.")

if __name__ == "__main__":
    print("this starts the quiz")
    start_quiz()