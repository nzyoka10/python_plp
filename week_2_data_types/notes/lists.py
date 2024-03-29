# List data type
# A list contains items separated by commas and enclosed within square brackets []
# python list take any/ all/ different data types
    # example below
# my_list = [1, 2, 'apple', True]

# make new list
shoppingList = ['Bread', 'Orange', 'Milk', 'Eggs']
print(type(shoppingList))
print("\n", shoppingList)
print(shoppingList[0])

# example 2
buildingList = [450, 'Cement', 'Paint', 5000, 'Wheelbarrows']
print("\n", buildingList)
print(buildingList[0])

# example 3
finalList = shoppingList + buildingList
print("\n", finalList)
print(finalList[-1])
print("\n", finalList * 1000)







'''
myList = [2024, 'Apple', 5+6j, 'False']
# print(myList) # prints the all list items
# print(type(2024))

list = ['abcd', 456, 3.89, 'Nzyoka', 70.5]
tinyList = [123, 'Nzyoka', 5+6j, 'False']
print("\n Original list:-> ", list)
print('\n Tiny list: ->', tinyList)
print('\n')

# accessing the list items
#print(list[0])   # accesses first item of the list (index starts from 0)
print(list[2:3]) 
# print(list + tinyList)
print(tinyList * 8)




# Nested list
# list with items of other lists
'''
'''
nestedList = [
    [2024, 'Apple', 5+6j],
    ['Orange', False, 3.14],
    9876543210
]
print(nestedList[:]) # prints all list items
print(nestedList[0]) # prints 
print(nestedList[1])
'''