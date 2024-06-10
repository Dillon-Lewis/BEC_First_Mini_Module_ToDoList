TooDooList = {}

def main():
    while True:
            ans = input('''
Welcome to TooDoo, the next step in To-Do list Apps!
    What can I do for you today:

    1- Add TooDoo
    2- Remove TooDoo
    3- View & mark TooDoo complete
    4- Quit TooDoo
''')
            if ans == '1':
                add_toodoo()                                                                # Add a TooDoo 
            elif ans == '2':
                remove_toodoo()                                                         # Remove a TooDoo
            elif ans == '3':
                 view_check()                                                           # View your TooDoos and Mark complete
            elif ans == '4':
                print("\nFinish those TooDoo's and I'll see you after completion!")       # Quiting the program   
                break
            else:
                 print('\nEnter a valid number')
                 continue
        

def add_toodoo():
    while True:
        toodoo = input('''                        
Lets get started on your new TooDoo!
                       
What is the task you would like to complete:                
    ''').upper()                                                                            # First I am going to set my key by asking for the Task at hand
        priority = input('''
And and what priority would you like set you TooDoo at:
        Low         or          High                     
                                           
        ''').title()                                                                                # Next I will set the value as the priority   
        print(f'\nTooDoo: {toodoo} \nPriority: {priority}')
        correct_info = input('Is everything looking correct? Yes or No\n').upper()          # Make sure the informations is correct
        if correct_info == 'YES':
            TooDooList.update({toodoo : priority})                                          # If correct, add to the dictionary of To Do's
            print(TooDooList)
            break
        elif correct_info == "NO":                                                          # If any  other input, restart making the TooDoo
            print("Lets get it fixed up then!\n")
            return add_toodoo()

def remove_toodoo():
    while True:                                                                            # Create a while true statment to test all possible answers
        completion = input('''
Before deleting a TooDoo, we reccomend completing it first!
    Were you able to complete the task?

    Yes             or             No
''').upper()                                                                                # Ask if task is complete and provide yes and no answers
        if completion == 'YES':
            print("Congrats! Lets get rid that task for you")
            keylist = list(TooDooList.keys())
            print(keylist)
            remove = input('Which TooDoo would you like to remove:\n').title()              # Using .Upper(), I can avoid some errors
            if remove in TooDooList.keys(): 
                TooDooList.pop(remove, " Please check spelling and reenter TooDoo you would like to remove")
                print(remove + ' has been removed from your TooDoo List!')
                break
            else:
                 print('Please enter a current task!')                                      # If not a valid task in list, reset the loop                          
        elif completion == 'NO':
            print("It's okay there is always next time! Don't give up!\n ")                 # Encourage the user not to give up but still allow options to get out
            keylist = list(TooDooList.keys())
            print(keylist)
            remove = input('Which TooDoo would you like to remove:\n').upper()                  # 
            if remove in TooDooList.keys(): 
                TooDooList.pop(remove, " Please check spelling and reenter TooDoo you would like to remove")            # Use .pop() to eliminate keys by there inputs
                print(remove + ' has been removed from your TooDoo List!')
                break
            
        elif completion != "YES" or "NO":
            print("Please enter a valid response")
            continue
                          
        
def view_check():
    while True:
        print("Your current TooDoo List with Priority")                                                 # Print my current To Do list for the user to see
        for keys,values in TooDooList.items():
                    print(keys, ':', values)
        completed = input('''\n
Have you completed any tasks you want to check off the list!?
    Yes     or      No
''').upper()
        if completed == 'YES':                                                                          # Ask if task is completed
            keylist = list(TooDooList.keys())
            print(keylist)
            checked = input("\nAwesome! Which TooDoo would you like to check off\n").title()                # If Yes, I compare input to keys in my to do list
            if checked in TooDooList.keys():
                TooDooList[checked] = "Done XX"
                print("Awesome!! We will mark ", checked, " as done!")                                      # Once key is verified, I will change its value to XXDoneXX 
                break
        elif completed == 'NO':                                     # If the user selects no, they are sent to main
             return main()
        else:
             print('Enter a valid input!')
             continue
             



main()


