"""Bug Detective - a tiny Python quiz game for the terminal."""

QUESTIONS = [
    {
        "question": "What does print(type(3.0)) show?",
        "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>"],
        "answer": 2,
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["func", "define", "def"],
        "answer": 3,
    },
    {
        "question": "What is len([1, 2, 3])?",
        "options": ["3", "2", "6"],
        "answer": 1,
    },
]


def ask_choice():
    """Keep asking until the player types 1, 2, or 3."""
    while True:
        choice = input("Your answer (1-3): ").strip()
        if choice in ("1", "2", "3"):
            return int(choice)
        print("Please enter 1, 2, or 3.")


def main():
    print("Bug Detective - answer 3 Python questions.\n")
    score = 0

    for number, q in enumerate(QUESTIONS, start=1):
        print(f"Question {number}: {q['question']}")
        for i, option in enumerate(q["options"], start=1):
            print(f"  {i}. {option}")

        choice = ask_choice()
        correct_text = q["options"][q["answer"] - 1]
        if choice == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong - the answer was {q['answer']}. {correct_text}\n")

    print(f"Final score: {score}/{len(QUESTIONS)}")


if __name__ == "__main__":
    main()
