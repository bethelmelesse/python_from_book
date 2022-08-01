favourite_languages = {'jen': 'python',
                       'sarah': 'c',
                       'edward': 'ruby',
                       'phil': 'python'
                       }

language = favourite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}.")
print(favourite_languages['sarah'])
print(" ")

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")

print(" ")

for name in favourite_languages.keys():
    print(name.title())

print(" ")

friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

print(" ")

if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")

print(" ")

for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print(" ")

print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

print(" ")

for language in set(favourite_languages.values()):
    print(language.title())

