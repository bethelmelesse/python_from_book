for number in range(1,21):
    print(number)

numbers = list(range(1,1000001))
print(numbers)

print( )

#for num in numbers:
 #   print(num)

print(min(numbers))
print(max(numbers))
print(sum(numbers))
print( )

numbers = list(range(1, 21, 2))
print(numbers)
for number in numbers:
    print(number)
print( )

multiple = []
for nums in range (1, 11):
    multi = nums * 3
    multiple.append(multi)
print(multiple)
print( )

cubes = []
for nums in range (1, 11):
    cube = nums ** 3
    cubes.append(cube)
print(cubes)
print( )

cubes = [num**3 for num in range (1,11)]
print(cubes)
