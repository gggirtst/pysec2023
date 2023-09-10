profile = ("Girts", "Tutans", "Students", ["Pitons", "Matematika", "Politika"])

firstname, lastname, role, subjects = profile

print("name:", firstname)
print("lastname:", lastname)
print("subjects:", subjects)

profile_list = list(profile)
profile_list.insert(4, "10")

profile = tuple(profile_list)

firstname, lastname, role, subjects, grade = profile

print("name:", firstname)
print("lastname:", lastname)
print("subjects:", subjects)
print("grade:", grade)
