'''
mod2Lab.py
Proudly Engineered by Zachary Roberts 18 JAN 2026.

This program allows the user to input names and GPAs and returns if a student has achieved Honor Roll or Dean's list.
Specifications:

Write a Python app that will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll. Your app will:
ask for and accept a student's last name.
quit processing student records if the last name entered is 'ZZZ'.
ask for and accept a student's first name.
ask for and accept the student's GPA as a float.
test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
test if the student's GPA is 3.25 or greater and, if so, print a message saying that the student has made the Honor Roll.
Test your app using at least five students.
Your header comments need to contain
Your name
The file name for your app
A brief description of what your app will do
'''

''' Schema
# FIXME Determine path forward with this. I have written a similar program in SDEV-120 using lists, it turns into a mess. I'll try this as an OOP program first.  
'''
'''# create class studentRecord with string fname, lname, and float gpa. 
class studentRecord:
    instance_incrementor: int = 0

    def __int__(self):
        self.lname = str(input('Enter student first name: '))
        self.fname = str(input('Enter student first name: '))
        self.gpa = float(input('Enter student gpa: '))
        studentRecord.instance_incrementor += 1


last_name = str(input('Enter student first name: '))
first_name = str(input('Enter student first name: '))
usr_in_gpa = float(input('Enter student gpa: '))

lname = last_name
fname = first_name
gpa = usr_in_gpa


print(studentRecord.__dict__)'''

