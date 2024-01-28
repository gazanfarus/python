# TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt", mode="r") as names:
    for name in names.readlines():
        name = name.strip()
        with open("./Input/Letters/starting_letter.txt", mode="r") as starting_letter:
            letter = starting_letter.read()
            letter = letter.replace("[name]", f"{name}")
            letter = letter.replace("Angela", "Gazanfar")
            with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as final_letters:
                final_letters.write(letter)
