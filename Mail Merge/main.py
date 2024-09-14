#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
with open("Input/Letters/starting_letter.txt") as template:
    contents = template.readlines()
    with open(file="Input/Names/invited_names.txt", mode="r") as file:
        names_list = file.readlines()
        for i in names_list:
            print(i)
            a= i.rstrip()
            with open(f"Output/ReadyToSend/{a}.txt", mode="w") as f:
                personalized = contents[:]
                personalized[0] = personalized[0].replace("[name]",f"{a}")
                f.writelines(personalized)
#
#
# with open(file="Input/Names/invited_names.txt", mode="r") as file:
#
#     for i in file:
#         a=i.rstrip()
#         print(a)

# try:
#     with open("Input/Letters/starting_letter.txt", mode="r") as file:
#         contents = file.readlines()  # Reading all lines into a list
#         if not contents:
#             print("The file is empty!")
#         else:
#             print(contents[0].replace("[name]", "Aang"))  # This will show the lines read from the file
#
# except FileNotFoundError:
#     print("File not found. Check the file path.")


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp