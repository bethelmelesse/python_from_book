my_pizza = ['cheese pizza', 'hot chicken pizza', 'mushroom pizza']
friend_pizza = my_pizza[:]
print(my_pizza)
print(friend_pizza)
print( )

my_pizza.append('potato pizza')
friend_pizza.append('pineapple pizza')
print(my_pizza)
print(friend_pizza)
print( )

print("my favourite pizzas are:")
for pizza in my_pizza:
    print(pizza)


print("\nmy friends favourite pizzas are:")
for pizza in friend_pizza:
    print(pizza)
