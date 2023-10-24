# Nicholas Reeves, 10/18/2023

import json
from contacts import *






#~~~~~~~~~~~~~~~~~~VARIABLES~~~~~~~~~~~~~~~~~~
runloop = True      #variable to force While loop below to run
usedfile = "basic.dat"
conlist = Contacts(filename = usedfile)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while runloop:
    print('\n        *** TUFFY TITAN CONTACT MAIN MENU\n',)
    print('1. Add contact')
    print('2. Modify contact')
    print('3. Delete contact')
    print('4. Print contact list')
    print('5. Set contact filename')
    print('6. Exit the program')

    option = input('\nEnter menu choice: ')

    match option:
        case '1':
            p = input('\nEnter phone number: ')      
            f = input('Enter first name: ')
            l = input('Enter last name: ')

            try:
                emtee = conlist.add_contact(id = p, first_name = f, last_name = l)
            except FileNotFoundError:
                pass
            else:
                if (emtee == "error"):
                    print('Phone number already exists.')
                else:
                    print('Added:', emtee[p][0], emtee[p][1] + '.')


        case '2':
            p = input('\nEnter phone number: ')      
            fn = input('Enter first name: ')
            ln = input('Enter last name: ')

            try:
                emtee = conlist.modify_contact(id = p, first_name = fn, last_name = ln)
            except FileNotFoundError:
                pass
            else:
                if (emtee == "error"):
                    print('Invalid phone number.')
                else:
                    print('Modified:', emtee[p][0], emtee[p][1] + '.')


        case '3':
            p = input('\nEnter phone number: ')
            try:
                emtee = conlist.delete_contact(id = p)
            except FileNotFoundError:
                pass
            else:
                if (emtee == "error"):
                    print('Invalid phone number.')
                else:
                    print('Deleted:', emtee[p][0], emtee[p][1]+'.')


        case '4':
            conlist.print_list()


        case '5':
            newfile = input('\nEnter new filename: ')
            conlist = Contacts(filename = newfile)

        case '6':
            break

        case _:
            print('Invalid option!')
