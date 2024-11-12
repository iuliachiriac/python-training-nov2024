person = {'name': 'Jane', 'age': 20, 'height': 1.8}  # , 'weight': 70}

if "weight" in person and "height" in person:
    bmi = person["weight"] / person["height"] ** 2
else:
    bmi = 0

bmi_2 = person.get("weight", 0) / person.get("height", 0.5) ** 2

print(bmi, bmi_2)
