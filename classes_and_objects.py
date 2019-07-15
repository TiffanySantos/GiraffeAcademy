#an object is an isntance of a class
# aka a class is the template, an object is a filled in template

from student import student

student1 = student("Jim", "Business", 3.1, False)
student2 = student("Bob", "Art", 3.5, True)
print(student1.name)
print(student2.gpa)

