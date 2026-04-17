# quiz_kbc_mcq.py
# KBC Style Quiz Application with Multiple Choice

def run_quiz():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"],
            "answer": "A"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "B"
        },
        {
            "question": "Who developed the Python programming language?",
            "options": ["A. James Gosling", "B. Dennis Ritchie", "C. Guido van Rossum", "D. Bjarne Stroustrup"],
            "answer": "C"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
            "answer": "C"
        },
        {
            "question": "Which data structure uses FIFO principle?",
            "options": ["A. Stack", "B. Queue", "C. Tree", "D. Graph"],
            "answer": "B"
        },
        {
            "question": "What is 5 * 6?",
            "options": ["A. 25", "B. 30", "C. 35", "D. 40"],
            "answer": "B"
        },
        {
            "question": "Which gas do humans inhale for survival?",
            "options": ["A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"],
            "answer": "B"
        },
        {
            "question": "What is the national animal of India?",
            "options": ["A. Lion", "B. Tiger", "C. Elephant", "D. Peacock"],
            "answer": "B"
        },
        {
            "question": "Which HTML tag is used to create a hyperlink?",
            "options": ["A. <p>", "B. <a>", "C. <h1>", "D. <link>"],
            "answer": "B"
        },
        {
            "question": "What is the square root of 64?",
            "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
            "answer": "C"
        },
        {
            "question": "Which year did World War II end?",
            "options": ["A. 1939", "B. 1942", "C. 1945", "D. 1950"],
            "answer": "C"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A. func", "B. def", "C. function", "D. lambda"],
            "answer": "B"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A. H2O", "B. O2", "C. CO2", "D. HO"],
            "answer": "A"
        },
        {
            "question": "Which Indian city is called the 'Financial Capital'?",
            "options": ["A. Delhi", "B. Bengaluru", "C. Mumbai", "D. Hyderabad"],
            "answer": "C"
        },
        {
            "question": "What is the output of 10 % 3 in Python?",
            "options": ["A. 0", "B. 1", "C. 2", "D. 3"],
            "answer": "B"
        },
        {
            "question": "Which device is used to process data in a computer?",
            "options": ["A. GPU", "B. CPU", "C. RAM", "D. Hard Disk"],
            "answer": "B"
        }
    ]

    rewards = [
        "₹1,000", "₹2,000", "₹3,000", "₹5,000",
        "₹10,000", "₹20,000", "₹40,000", "₹80,000",
        "₹1,60,000", "₹3,20,000", "₹6,40,000", "₹12,50,000",
        "₹25,00,000", "₹50,00,000", "₹1 Crore", "₹7 Crore"
    ]

    print("🎉 Welcome to Python KBC Quiz! 🎉\n")
    print("Choose the correct option (A/B/C/D).\n")

    for i, q in enumerate(questions):
        print(f"Q{i+1}. {q['question']}")
        for option in q["options"]:
            print(option)
        user_answer = input("Your choice (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print(f"✅ Correct! You have won {rewards[i]}!\n")
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")
            print(f"You leave the game with {rewards[i-1] if i>0 else '₹0'}.\n")
            break
    else:
        print("🎉 Congratulations! You answered all questions correctly!")
        print(f"You are the winner of {rewards[-1]}!\n")

if __name__ == "__main__":
    run_quiz()
