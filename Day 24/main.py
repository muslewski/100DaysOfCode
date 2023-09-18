# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
with open("Input/Names/invited_names.txt") as file:
    names = file.read()
name_list = [s.strip() for s in names.split('\n') if s]

# Replace the [name] placeholder with the actual name.
with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()

for name in name_list:
    new_letter = letter.replace("[name]", name)
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as file:
        file.write(new_letter)
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
