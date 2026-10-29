
import random
import time

suspects = {
    "Ali": "His hands smell like biryani.",
    "Rahul": "He says he is dieting but looks suspicious.",
    "Muneeb": "He was missing when the biryani disappeared.",
    "Ahmed": "He has a spoon hidden in his pocket.",
    "Danish": "He keeps saying 'I know nothing' while chewing."
}

print("=" * 45)
print("       THE GREAT BIRYANI MYSTERY")
print("=" * 45)
print("\nSomeone has stolen the biryani! 😱")
print("You are the detective. Find the culprit!")
print("\nSuspects:")

names = list(suspects.keys())

for i, name in enumerate(names, 1):
    print(f"{i}. {name}")

culprit = random.choice(names)
attempts = 3

print("\nYou have 3 chances to catch the thief!")

while attempts > 0:
    print(f"\nChances left: {attempts}")

    choice = input("Who stole the biryani? Enter a name: ").strip().title()

    if choice not in suspects:
        print("That person isn't even a suspect! 😂")
        continue

    if choice == culprit:
        print("\n🎉 CASE SOLVED!")
        print(f"{culprit} stole the biryani!")
        print("Justice has been served. 🍗")
        break

    attempts -= 1

    if attempts > 0:
        print("Wrong suspect! 😂")
        print("CLUE:", suspects[culprit])
    else:
        print("\n🚨 CASE CLOSED!")
        print(f"The real thief was {culprit}!")
        print("Your detective career is finished. 💀")

print("\n" + "=" * 45)
print("GAME OVER — Thanks for playing!")
print("=" * 45)
