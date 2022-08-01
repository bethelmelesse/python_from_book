guest = ['akhil', 'belle', 'sara']
print(guest)
print( )
print(f"Hi {guest[0].title()}, I am having dinner tonight. Come if you have time!")
print(f"Hi {guest[1].title()}, I am having dinner tonight. Come if you have time!")
print(f"Hi {guest[2].title()}, I am having dinner tonight. Come if you have time!")
print( )

not_coming = guest[2].title()
print(f"{not_coming} is not coming for dinner.")
guest[2] = 'phay'
print(guest)

print( )
print(f"Hi {guest[0].title()}, I am having dinner tonight. Come if you have time!")
print(f"Hi {guest[1].title()}, I am having dinner tonight. Come if you have time!")
print(f"Hi {guest[2].title()}, I am having dinner tonight. Come if you have time!")
print( )

print("we have got a bigger table. we have more space for more people now")
print( )

guest.insert(0, 'bizu')
print(guest)
guest.insert(3, 'natanim')
print(guest)
guest.append('abigail')
print(guest)

print( )
print(f"Hi {guest[0].title()}, I am having dinner tonight. Come if you have time!")
print(f"Hi {guest[1].title()}, I am having dinner tonight. Come if you have time!")
print(f"Hi {guest[2].title()}, I am having dinner tonight. Come if you have time!")
print(f"Hi {guest[3].title()}, I am having dinner tonight. Come if you have time!")
print(f"Hi {guest[4].title()}, I am having dinner tonight. Come if you have time!")
print(f"Hi {guest[5].title()}, I am having dinner tonight. Come if you have time!")
print( )

print("I am sorry. The big dinning table wont arrive in time for dinner so we have to limit the guest list to only two guests")
print( )

print(guest)
first_guest = guest.pop(0)
print(f"Hi {first_guest.title()}, I am sorry. I have to un-invite you")
second_guest = guest.pop(2)
print(f"Hi {second_guest.title()},  I am sorry. I have to un-invite you")
third_guest = guest.pop(2)
print(f"Hi {third_guest.title()},  I am sorry. I have to un-invite you")
fourth_guest = guest.pop(2)
print(f"Hi {fourth_guest.title()},  I am sorry. I have to un-invite you")
print( )
print(guest)
print(f"{guest[0].title()} you are still invited")
print(f"{guest[1].title()} you are still invited")
print(len(guest))
print( )

del guest[0]
del guest[0]
print(guest)
print(len(guest))