name = "Bethel melesse"

message1 = f"Hello {name}, would you like to learn some Python today?"
print(message1)

message2 = f"Hello {name.lower()}, would you like to learn some Python today?"
message3 = f"Hello {name.upper()}, would you like to learn some Python today?"
message4 = f"Hello {name.title()}, would you like to learn some Python today?"
print(message2)
print(message3)
print(message4)

qoute = '\tMiley Cyrus once said, "Life is a climb, \n\tbut the view is great"'
print(qoute)

famous_person = "miley cyrus"
qoute2 = f'\t{famous_person.title()} once said, "Life is a climb, \n\tbut the view is great"'
print(qoute2)
print()

famous_person2 = " miley cyrus "
qoute3 = f'\t{famous_person2.title().strip()} once said, "Life is a climb, \n\tbut the view is great"'
print(qoute3)
print()

qoute4 = f'\t{famous_person2.title().rstrip()} once said, "Life is a climb, \n\tbut the view is great"'
print(qoute4)
print()

qoute5 = f'\t{famous_person2.title().lstrip()} once said, "Life is a climb, \n\tbut the view is great"'
print(qoute5)
print()