class Delete:

    def delete(self):
        print('select the option you want to delete:')
        print('1: Name')
        print('2: Profession')
        print('3: contact')
        print('4: Skills')
        print('5: Date of Birth')
        print('6: description')
        choose = input('Select an option:')
        if choose == "1":
            self.name = None
        elif choose == "2":
            self.profession = None
        elif choose == "3":
            self.contact = None
        elif choose == "4":
            self.skills = None
        elif choose == "5":
            self.DOB = None
        elif choose == "6":
            self.description = None
        else:
            print('Invalid entry back to menu')
