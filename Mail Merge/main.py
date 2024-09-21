#Prepares a ready-made template letter by substituting the names.
with open("Input/Letters/starting_letter.txt") as template:
    contents = template.readlines()
    with open(file="Input/Names/invited_names.txt", mode="r") as file:
        names_list = file.readlines()
        for i in names_list:
            a = i.rstrip()
            with open(f"Output/ReadyToSend/{a}.txt", mode="w") as f:
                personalized = contents[:]
                personalized[0] = personalized[0].replace("[name]", f"{a}")
                f.writelines(personalized)
