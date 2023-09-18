import random
import os

import art
import words

#Welcome
print(art.logo)
print("\n\033[35mWelcome in \033[31mhangman\033[35m game!")

#Randomly generate answer
full_answer = random.choice(words.word_list)
answer = full_answer.split()[0]
topic = full_answer.split()[1:]
print(f"\n\033[09mAnswer:\033[0m \033[09m{answer}\033[0m")

print("\n\033[35mHint:\033[0m", " ".join(topic))

#change answer to list that can be used in loops
answer_list = list(answer)
answer_list_len = len(answer_list)

#make display
display_list = []
for _ in range(answer_list_len):
    display_list += "_"

#Make loop
iteration_of_loop = 0
lives = 6

while display_list != answer_list:
    guess = input("\n\033[0mGuess a letter: ").lower()
    os.system("clear")

    i = 0
    for letter in display_list:
        if answer_list[i] == guess:
            display_list[i] = guess
        i += 1

    display = " ".join(display_list)
    iteration_of_loop += 1
    if guess not in display_list:
        lives -= 1

    if display_list == answer_list:
        print("\033[01m\033[32m" + art.stages[lives])
    else:
        print("\nHint:\033[0m", " ".join(topic))
        print(art.stages[lives])

    print(f"\033[0;0m{display}")

    if lives <= 0:
        break

if lives > 0:
    print("\n\033[32m\033[01mYou win!")
else:
    print("\n\033[31mYou loose!")
