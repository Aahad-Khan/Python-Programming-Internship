#quiz_game 

def display_question(question, options, correct_answer):
    print("\n" + question)
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")
    while True:
        try:
            choice = int(input("Enter the number of your answer: "))
            if 1 <= choice <= len(options):
                return choice == correct_answer
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    # Define questions, options, and correct answers
    quiz = [
        {
            "question": "What is the capital of India?",
            "options": ["Mumbai", "New Delhi", "Bangalore", "Chennai"],
            "answer": 2 
        },
        {
            "question": "Who is known as the Father of India?",
            "options": ["Jawaharlal Nehru", "APJ Abdul Kalam", "Mahatma Gandhi", "Sardar Patel"],
            "answer": 3  
        },
        {
            "question": "Which river is the longest in India?",
            "options": ["Ganga", "Indus", "Brahmaputra", "Yamuna"],
            "answer": 1  
        },
        {
            "question": "What is the process by which plants convert sunlight into energy?",
            "options": ["Respiration", "Photosynthesis", "Fermentation", "Decomposition"],
            "answer": 1  
        },
        {
            "question": "What is the SI unit of electric current?",
            "options": ["Volt", "Ampere", "Ohm", "Watt"],
            "answer": 2  
        },
    ]

    print("Welcome to the Quiz Game!")
    

    score = 0
    question_number = 1
    for q in quiz:
        print(f"\nQuestion {question_number}:")
        if display_question(q["question"], q["options"], q["answer"]):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['options'][q['answer'] - 1]}")
        question_number += 1

    print("\nQuiz Complete!")
    print(f"Your final score is {score} out of {len(quiz)}.")

if __name__ == "__main__":
      main()
