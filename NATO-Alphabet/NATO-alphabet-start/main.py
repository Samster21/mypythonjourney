import pandas

print("====================NATO ALPHABETS!- Find out the Nato Alphabets for any word==============")

nato_codes = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_codes.iterrows()}

output = [nato_dict[letter] for letter in input("Please enter you word: ").upper()]


print(output)
