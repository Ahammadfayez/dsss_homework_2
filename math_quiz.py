import random


def generate_random_integer(min_value, max_value):
    """
    Generates a random integer between the given min and max values (inclusive)
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Generates a random mathematical operator: '+', '-', or '*'.
    """"
    return random.choice(['+', '-', '*'])


def calculate_result(num1, num2, operator):
    """
    Calculates the result of applying the given operator to the two numbers.
    """"
    
    if operator == '+':
        result = num1 + num2
    elif o == '-': 
        result = num1 - num2
    else: 
        result = num1 * num2
    return result

def math_quiz():
    """
    Conducts a math quiz and calculates the user's score.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5) 
        operator = generate_random_operator()

        problem, answer = calculate_result(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        try: 
            user_answer = int(input("Your answer: "))
        except ValueError:
            print ("Invalid input! Please enter a valid integer.")
            user_answer = 0 #Assign a default value in case of invalid input
        if user_answer == answer:
            print("Correct! You earned a point.

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
