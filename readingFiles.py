#employee_file = open("employees.txt", "w") #open file in write mode
#employee_file = open("employees.txt", "a") #open file in append mode, tag comething on the end


employee_file = open("employees.txt", "r") #open file in read mode
print(employee_file.readable()) # returns bool to check file readbility
print(employee_file.readline()) # prints a single line of file

for employee in employee_file.readlines(): # loops the above list
    print(employee) # prints all lines in file in an list
employee_file.close() # close file when done