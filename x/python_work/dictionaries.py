# Dictionaries

# my_cat = {"name":"Salem","colour":"black","mood":"sassy"}

# --------------------------------------------

# Activity 1

# dict_of_dol = {
#     "Name": "Dolores",
#     "Type": "Orbital Frame",
#     "Colour": "Pink",
#     "Mood": "Wholesome",
#     "Weapons": "Burst Shot",
#     "Sub-Weapons": "Zero Shift",
#     "Battle Stress": False
# }

# print(dict_of_dol)

# dict_of_dol["Name"] = "Isis",
# dict_of_dol["Mood"] = "Angry",
# dict_of_dol["Weapons"] = "Arm Blade",
# dict_of_dol["Sub-Weapons"] = "Particle Canon",
# dict_of_dol["Battle Stress"] = True


# print(dict_of_dol)

# --------------------------------------------

# dict_of_dd = {
#     "Name": "D.D.",
#     "Type": "Dog?",
#     "Colour": "Gray",
#     "Occupation": "Attack Dog",
#     "Mood": "Wholesome",
#     "Weapons": "Combat Knife",
#     "Armour": "None",
#     "Recently told he is a good boy?": False
# }

# print(dict_of_dd)

# dict_of_dd["Type"] = "Wolf",
# dict_of_dd["Mood"] = "Alert",
# dict_of_dd["Weapons"] = "Tactical Fulton",
# dict_of_dd["Armour"] = "Battle Dress",
# dict_of_dd["Recently told he is a good boy?"] = True


# print(dict_of_dd)

# --------------------------------------------

# Activity 2

dict_of_act2 = {
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Spain": "Madrid",
    "Italy": "Rome",
}

print(dict_of_act2)

dict_of_act2.setdefault("Japan", "Tokyo")
dict_of_act2.setdefault("Egypt", "Cairo")

for i, value in dict_of_act2.items():
    print(i, ' : ', value)