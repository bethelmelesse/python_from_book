message1 = "This is a string."
message2 = 'This is also a string'
message3 = 'I told my friend, "Python is my favourite language!"'
message4 = "The language 'Python' is named after Monty Python, not the snake."
message5 = "One of Python's strength is its divese and supportive community."

print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print("")

name = "ada lovelace"
print(name)
print(name.title())
print(name)
print(name.upper())
print(name.lower())
print("")

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print("")

print(f"hello, {full_name.title()}!")
print("")

message6 = f"hello, {full_name.title()}!"
print(message6)
print("")

print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
print("")

favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language)

favorite_language = favorite_language.rstrip()
print(favorite_language)

favprote_language = " python "
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())