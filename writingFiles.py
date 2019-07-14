employee_file  = open("emplyees.txt", "a") 
employee_file.write("\nEmilie - Teacher") #appends entry on to a new line
employee_file.close()

employee_file  = open("emplyees.txt", "w") # OVER-WRITE the existing file
employee_file.write("\nEmilie - Teacher")
employee_file.close()

employee_file  = open("index.html", "w") # write a new file
employee_file.write("<p>This is a HTML paragraph. <p>") 
employee_file.close()