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
FIXME Determine path forward with this. I have written a similar program in SDEV-120 using lists, it turns into a mess. I'll try this as an OOP program first.
OOP proved to be too difficult at my current skill level, but I believe I was over-complicating the assignment initially anyway. A more direct approach was settled on.   
'''
last_name: str = ''
first_name: str = ''
gpa: float = 0 
on_the_dl: float = float(3.5)
on_the_hr: float = float(3.25)
dl_message: str = ("This student has made the Dean's List.\n")
hr_message: str =('This student is on the Honor Roll.\n')
no_easy_way: str = ('Student did not make any academic list.\n')

while True:

    last_name: str = input('Enter student last name: ')
 
    if last_name == 'ZZZ':
        break
    else:
         print(f'"{last_name}" accepted!\n')
                
    first_name: str = input('Enter student first name: ')
    print(f'"{first_name}" accepted!')
    while True:
        try:
            gpa: float = float(input('Enter student gpa: '))
            print('GPA accepted!')
            break
        except ValueError:
            print('Enter a float!\n')
    # process user inputs
    if gpa >= on_the_dl:
        print(dl_message)
    elif gpa >= on_the_hr and gpa <= on_the_dl:
        print(hr_message)
    else:
        print(no_easy_way)

print('end_program')   




