class EditData:

    def edit_data(self):
        print('select the option you want to edit:')
        print('1: Name')
        print('2: Profession')
        print('3: contact')
        print('4: Skills')
        print('5: Date of Birth')
        print('6: description')
        choose = input('Select an option')
        if choose == "1":
            name = input('Enter name:')
            self.name = name
        elif choose == "2":
            profession = input('Enter profession:')
            self.profession = profession
        elif choose == "3":
            contact = input('Enter Mobile no:')
            self.contact = contact
        elif choose == "4":
            skills = input('Enter skills:')
            self.skills = skills
        elif choose == "5":
            DOB = input('Enter Date of Birth:')
            self.DOB = DOB
        elif choose == "6":
            description = input('Enter description:')
            self.description = description
        else:
            print('Invalid entry back to menu')
