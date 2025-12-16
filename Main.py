import random

def generate_question(level):
    if level == 1:
        a, b = random.randint(1, 10), random.randint(1, 10)
        return f"{a} + {b}", a + b

    if level == 2:
        a, b = random.randint(2, 10), random.randint(2, 10)
        return f"{a} * {b}", a * b

    if level >= 3:
        x = random.randint(1, 10)
        a = random.randint(1, 5)
        b = random.randint(1, 10)
        c = a * x + b
        return f"{a}x + {b} = {c}. What is x?", x


def main():
    print("=== MATH DUNGEON ===")
    room = 1
    lives = 3

    while lives > 0 and room <= 5:
        print(f"\nYou entered Room {room}")

        if room <= 2:
            level = 1
        elif room <= 4:
            level = 2
        else:
            level = 3

        question, correct_answer = generate_question(level)
        user_answer = input(f"Solve: {question} ")

        try:
            if int(user_answer) == correct_answer:
                print("Correct! You move to the next room.")
                room += 1
            else:
                print("Wrong answer!")
                lives -= 1
                print(f"Lives left: {lives}")
        except ValueError:
            print("Please enter a number.")
            lives -= 1

    if lives > 0:
        print("\n🏆 Congratulations! You escaped the dungeon.")
    else:
        print("\n💀 Game Over. Try again!")

if __name__ == "__main__":
    main()
