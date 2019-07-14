for letter in "Giraffe Academy":  # define a variable, each loop changes the var, one by one going along
    print(letter) #prints each letter on a line as each loop funs on a new line

friends = ["Jim", "Karen", "Kevin"] # you can use an array
for friend in friends:
    print(friend)
for index in range(len(friends)): #tells you how many items are in the array
    print(friends[index]) # prints the result

for index in range(3, 10): # or a range of numbers 
    print(index) #prints UP TO but NOT INCLUDING last number

for index in range(5):
    if index == 1:
        print("Frist Iteration")
    else:
        print("Not first")

        