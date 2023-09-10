people = []

profile = {
    "name": "Kristaps", 
    "role": "Teacher", 
}

profile_anne = {
    "name": "Anna",
    "role": "substitue",
}

people.append(profile)
people.append(profile_anne)

print(people)

for profile in people:
    for attribute, value in profile.items():
        print(attribute, value)

for profile in people:
    print("""
    ---------profile----------
    --name: {}
    --role: {}
    """.format(profile['name'], profile["role"]))