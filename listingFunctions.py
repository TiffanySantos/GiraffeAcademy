lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby", "Karen"]

friends.extend(lucky_numbers) #add the two lists together
friends.append("Creed") #adds in an extra item AT THE END OF THE LIST
friends.insert(1, "Kelly") # inserts the item in that position
friends.remove("Jim") # removes item from list
 
 # friends.clear() # clears out the list

friends.pop() # removes last element from the list, in this case Creed which was added in earlier

print(friends.index("Kevin")) # gives you the index of Kevin, which in this case is 0
# print(friends.index("Anna")) # gives you an error "Anna is not in list"
print(friends.count("Karen")) # tells you how many of this item are in list, in this case 2
print(friends)

lucky_numbers.sort() #sorts list, numerically or alphabetically
print(lucky_numbers)
lucky_numbers.reverse() # reverses the above order
print(lucky_numbers)

friends2 = friends.copy() # makes a copy of the list
print(friends2) 


