
# Giraffe language translator swaps vowels for "g"
# for loops with if statements nested inside

def translate(phrase):
    translation = " "
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper ():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else: 
            translation = translation + letter
    return translation # see the return function is in line with the varaible directly under function

print(translate(input("Enter a phrase: "))) 