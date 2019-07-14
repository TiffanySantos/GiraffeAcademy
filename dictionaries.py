monthConversions = { #to create a dictionary set a variable = {}, inside the {} place dictionary items
"Jan": "January", # Keys must be unique, seperated by : ending in a ,
"Feb": "February",
"Mar": "March",
"Apr": "April",
"May": "May",
"Jun": "June",
"Jul": "July",
"Aug": "August",
"Sep": "September",
"Oct": "October",
"Nov": "November",
"Dec": "December",
}

print(monthConversions["Nov"]) # can get value with [] like a list
print(monthConversions.get("Dec")) # can get with .get()
print(monthConversions.get("Luv", "Not a valid Key")) # can add message for invalid item, idefault prints "none"