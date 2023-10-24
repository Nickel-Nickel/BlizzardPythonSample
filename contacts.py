# Nicholas Reeves, 10/18/2023

import json


class Contacts:

  def __init__(self, /, *, filename):
    """initializes contacts class instance"""

    self.confile = filename
    self.data = {}
    tempdic = {}
    try:
      with open(self.confile, 'r') as file:
        self.data = json.load(file)
    except FileNotFoundError:
      print("File not found!")

  def add_contact(self, /, *, id, first_name, last_name):
    """adds a new contact to the list"""

    if id in self.data:
      return ("error")

    print(f'Added: {first_name} {last_name}.')
    self.data[id] = [first_name, last_name]

    with open(self.confile, 'r') as file:
      file.write = self.data

    self.data = self.sort_contacts()

    tempdic = {id: self.data[id]}
    return tempdic

  def modify_contact(self, /, *, id, first_name, last_name):
    """modifies an existing contact"""

    if id not in self.data:
      return ("error")

    print(f'Modified: {first_name} {last_name}.')
    self.data[id] = [first_name, last_name]

    with open(self.confile, 'r') as file:
      file.write = self.data

    self.data = self.sort_contacts()

    tempdic = {id: self.data[id]}
    return tempdic

  def delete_contact(self, /, *, id):
    """delete a single contact from the list"""

    if id not in self.data:
      return ("error")

    tempdic = {id: self.data[id]}
    print(f'Deleted: {tempdic[id][0]} {tempdic[id][1]}.')
    del self.data[id]

    with open(self.confile, 'r') as file:
      file.write = self.data

    return tempdic

  def print_list(self):
    """print total list of contacts"""

    self.data = self.sort_contacts()
    print('\n==================== CONTACT LIST ====================')
    print('Last Name             First Name            Phone')
    print('====================  ====================  ==========')
    for key, value in (self.data.items()):
      print(f'{value[1]:22}{value[0]:22}{key}')

  def sort_contacts(self):
    """sort given list, by last name and then first name"""
    return dict(
        sorted(self.data.items(),
               key=lambda item: (item[1][1].lower(), item[1][0].lower())))
