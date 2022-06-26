#This is a Landing Menu program, designed to let you customize what
# webpages you want to load on startup. That way, you save time by
# having to open everything up manually. 
# It should be noted that to initiate the program I copied a version of it to this path location:
# C:\Users\admin1\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
#       Come to think of it, I'll have to circle back and include this in the code !
import webbrowser

#Create the menu, show it to user and call the function
def menu():
    print('[1] Open Google Docs')
    print('[2] Open UQAM email')
    print('[3] Open Moodle')
    print('[4] Launch Chamanism toolbox')
    print('[0] Exit program')    
menu()

#Create functions for each Option
def option1():
    webbrowser.open('https://docs.google.com/document/u/0/')
    
def option2():
    webbrowser.open('https://outlook.office.com/mail/')
    
def option3():
    webbrowser.open('https://moodle.uqam.ca/')
    
def option4():
   

#Take input from user to know which tools to load
option = int(input('Pick an option to load certain tools: '))

#Start the Landing Menu processes associated w/ user's choice
while option != 0:
    if option == 1:
        option1()
        option = option - 1
        
    elif option == 2:
        option2()
        option = option - 2
        
    elif option == 3:
        option3()
        option = option - 3
        
    elif option == 4:
        option4()
        option = option - 4
    else:
        print('Invalid option, please choose another: ')
        
    menu()
    option = int(input('Pick an option to load certain tools: '))

print('All tools have been loaded. Now, get to work')
