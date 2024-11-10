import random

def function_1(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)

def function_2():
    return random.choice(['+', '-', '*'])

def function_3(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+':
        a = n1 + n2
    elif o == '-':
        a = n1 - n2
    else:
        a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    t_q = 3  # it was a float number, changed to integer

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = function_1(1, 10)
        n2 = function_1(1, 5)  # Changed 5.5 to 5 for integer range
        o = function_2()

        PROBLEM, ANSWER = function_3(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        
        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
