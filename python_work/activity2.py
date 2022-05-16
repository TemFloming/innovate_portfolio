# Activity 2

import random

print("This is a small repository program for Blade Runner (1982). You can pull a random quote from the film, or input an actors name to view their role.")

input01 = input("\n1. Pull a random Blade Runner quote?\n" "\n2. Input an actors name to view their role?\n")


while input01 !="1" and input01 != "2":
    print("\nAcceptable inputs are 1 or 2.\n")
    input01 = input("\n1. Pull a random Blade Runner quote?\n" "\n2. Input an actors name to view their role?\n")
    if input01=="1":
        def random_quote():
            quotes = [
            "Replicants are like any other machine, are either a benefit or a hazard. If they're a benefit it's not my problem. - Rick Deckard",
            "All those moments will be lost in time, like tears in rain. Time to die. - Roy Batty",
            "Is this testing whether I'm a replicant or a lesbian, Mr. Deckard? - Rachael",
            "Its too bad she wont live, but then again who does? - Gaff",
            "I need ya, Decks. This is a bad one, the worst yet. I need the old blade runner, I need your magic. - Bryant",
            "I think, Sebastian, therefore I am. - Pris",
            "There's a part of me in you... - J.F. Sebastian",
            "Let me tell you about my mother. - Leon Kowalski",
            "The light that burns twice as bright burns half as long, and you have burned so very very brightly, Roy. - Dr. Eldon Tyrell",
            "Of course it's not real. You think I would be working in a place like this if I could afford a real snake? - Zhora"
            ]
            print(random.choice(quotes))

# list_of_cast = [
#     "Harrison Ford - Rick Deckard",
#     "Rutger Hauer - Roy Batty",
#     "Sean Young - Rachael",
#     "Edward James Olmos - Gaff",
#     "M. Emmet Walsh - Bryant",
#     "Daryl Hannah - Pris",
#     "William Sanderson - J.F. Sebastian",
#     "Brion James - Leon Kowalski",
#     "Joe Turkel - Dr. Eldon Tyrell",
#     "Joanna Cassidy - Zhora"
# ]

# input02 = input("Harrison Ford",
#     "Rutger Hauer",
#     "Sean Young",
#     "Edward James Olmos",
#     "M. Emmet Walsh",
#     "Daryl Hannah",
#     "William Sanderson",
#     "Brion James",
#     "Joe Turkel",
#     "Joanna Cassidy")

# list_of_quotes = [
#     "Replicants are like any other machine, are either a benefit or a hazard. If they're a benefit it's not my problem. - Rick Deckard",
#     "All those moments will be lost in time, like tears in rain. Time to die. - Roy Batty",
#     "Is this testing whether I'm a replicant or a lesbian, Mr. Deckard? - Rachael",
#     "Its too bad she wont live, but then again who does? - Gaff",
#     "I need ya, Decks. This is a bad one, the worst yet. I need the old blade runner, I need your magic. - Bryant",
#     "I think, Sebastian, therefore I am. - Pris",
#     "There's a part of me in you... - J.F. Sebastian",
#     "Let me tell you about my mother. - Leon Kowalski",
#     "The light that burns twice as bright burns half as long, and you have burned so very very brightly, Roy. - Dr. Eldon Tyrell",
#     "Of course it's not real. You think I would be working in a place like this if I could afford a real snake? - Zhora"
# ]

# answer = input("Pull a random Blade Runner quote?\n")
# if answer = ("yes"):
#     print(list_of_quotes)
# if answer = ("no"):
#     print("k bye")
#     else:
#         print("Please enter ""yes"" or ""no"".")

# input01 = input("\n1. Pull a random Blade Runner quote?\n" "\n2. Input an actors name to view their role?\n")
#     while input01 !="1" and input01 != "2":
#         print("\nAcceptable inputs are 1 or 2.\n")
#         input01 = input("\n1. Pull a random Blade Runner quote?\n" "\n2. Input an actors name to view their role?\n")