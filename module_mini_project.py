TooDooList = {
     "Garbage" : 'Low',
     "Dishes": "High"
}

def main():
    while True:
        # try:
            ans = input('''
Welcome to TooDoo, the next step in To-Do list Apps!
    What can I do for you today:

    1- Add TooDoo
    2- Remove TooDoo
    3- View & mark TooDoo complete
    4- Quit TooDoo
''')
            if ans == '1':
                add_toodoo()            # Add a TooDoo 
            elif ans == '2':
                remove_toodoo()           # Remove a TooDoo
            elif ans == '3':
                 view_check()            # View your TooDoos and Mark complete
            elif ans == '4':
                print("Finish those TooDoo's and I'll see you after completion!")     # Quiting the program   
                break
            elif ans > 4:
                print("Enter a valid input")        #  If they enter a number greater then 5 it wont work
                continue
        # except Exception as e:                      # Include Exceptions for invalid responses and allow for resubmittion 
        #     print("Invalid entry, try again")
        

def add_toodoo():
    while True:
        toodoo = input('''                        
Lets get started on your new TooDoo!
                       
What is the task you would like to complete:                
    ''')                        # First I am going to set my key by asking for the Task at hand
        priority = input('''
And and what priority would you like set you TooDoo at:
        LOW         or          HIGH                     
                                           
        ''')                        # Next I will set the value as the priority   
        print(f'\nTooDoo: {toodoo} \nPriority: {priority}')
        correct_info = input('Is everything looking correct? Yes or No\n')        # Make sure the informations is correct
        if correct_info == 'Yes' or 'yes' or 'YES':
            TooDooList.update({toodoo : priority})          # If correct, add to the dictionary of To Do's
            print(TooDooList)
            break
        else:                       # If any  other input, restart making the TooDoo
            continue

def remove_toodoo():
    while True:
        completion = input('''
Before deleting a TooDoo, we reccomend completing it first!
    Were you able to complete the task?

    Yes             or             No
''')
        if completion == 'Yes' or 'yes' or 'YES':
            print("Congrats! Lets get rid that task for you")
            keylist = list(TooDooList.keys())
            print(keylist)
            remove = input('Which TooDoo would you like to remove:\n')
            deleted =TooDooList.pop(remove, "Please check spelling and reenter TooDoo you would like to remove")
            print(deleted, "has been removed from your current TooDoo list")
            break            
        elif completion == 'no' or 'No' or 'NO':
            print("It's okay there is always next time! ")
            keylist = list(TooDooList.keys())
            print(keylist)
            remove = input('Which TooDoo would you like to remove:\n')
            deleted =TooDooList.pop(remove, "Please check spelling and reenter TooDoo you would like to remove")
            print(remove, "has been removed from your current TooDoo list")
        else:
            continue              
        
def view_check():
    while True:
        print("Your current TooDoo List with Priority")
        for keys,values in TooDooList.items():
                    print(keys, ':', values)
        X = print(input('''\n
Have you completed any tasks you want to check off the list!?
    Yes     or      No
'''))
        if X == 'Yes' or 'YES' or 'yes':
            keylist = list(TooDooList.keys())
            print(keylist)
            checked = input("\nAwesome! Which TooDoo would you like to check off")
            if checked in TooDooList.keys():
                adding_x = "X"  # Concat strings to add X
                Marked = adding_x + checked
                break

            ##### STILL FIGURING OUT THIS! A LITTLE STUCK
        else:
             return main()



        
                    
        



main()

