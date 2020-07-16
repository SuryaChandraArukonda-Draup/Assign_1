
class AboutMe:


    def __init__(self, uid, name, profession, contact, skills, DOB, description):

        self.uid = uid
        self.name = name
        self.profession = profession
        self.contact = contact
        self.skills = skills
        self.DOB = DOB
        self.description = description

    def editdata(self):

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


def Query():

    #This function is used to print all the data in the database

    with open('sample.json') as f:
        for obj in f:
            data = json.loads(obj)
            for key, value in data.items():
                if key == 'uid':
                    pass
                else:
                    print(f'{key} : {value}', end=' ')
            print()


if __name__ == "__main__":
    option = True
    import random
    import string
    import json

    while option:
        print('Hello, choose an option!')
        print('1: Please, enter the details of new employee')
        print('2: Edit (UID required)')
        print('3: Check record (UID required)')
        print('4: Delete (UID required)')
        print('5: Show all records')
        print('6: Search by Name,profession or contact')
        print('7: Exit')
        choose = input("Select an option")

        if choose == "1":
            name = input('Enter your Name:')
            profession = input('Enter your profession:')
            contact = input('Enter your mobile no:')
            skills = input('Enter your Skills:')
            DOB = input('Enter your Date of Birth:')
            description = input('Describe yourself:')


            uid = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])

            obj= AboutMe(uid, name, profession, contact, skills, DOB, description)
            # Method used to convert object to dictionary
            # The data is then written on sample.json
            data = obj.__dict__
            print(f'Your unique identification number is: {uid}')
            print('Please save this id for future reference.')

            with open('sample.json', 'a') as file:
                json.dump(data, file)
                file.write('\n')

        elif choose == "2":
            # This variable is used to keep track whether data is available in database
            found = False
            uid = input('Please enter your unique identification number:')
            # This list is used to hold the data temporarily for editing
            datalist = []
            with open('sample.json') as file:
                for obj in file:
                    data = json.loads(obj)
                    if uid in data.values():
                        print(data)
                        found = True
                        objt = AboutMe(data['uid'], data['name'], data['profession'],
                                      data['contact'], data['skills'], data['DOB'],
                                      data['description'])
                    else:
                        datalist.append(data)

            if found:
                objt.editdata()
                data = objt.__dict__
                datalist.append(data)
                with open('sample.json', 'w') as file:
                    for data in datalist:
                        json.dump(data, file)
                        file.write('\n')

            else:
                print('Unique identification number is not found')

        elif choose == "3":
            uid = input('Enter your unique id:')
            found = False
            with open('sample.json') as file:
                for obj in file:
                    data = json.loads(obj)
                    if uid in data.values():
                        print(data)
                        found = True
            if not found:
                print('Sorry uid not found')

        elif choose == "4":
            found = False
            uid = input('Please enter your unique id:')
            datalist = []
            with open('sample.json') as file:
                for obj in file:
                    data = json.loads(obj)
                    if uid in data.values():
                        print(data)
                        found = True
                        objt = AboutMe(data['uid'], data['name'], data['profession'],
                                      data['contact'], data['skills'], data['DOB'],
                                      data['description'])
                    else:
                        datalist.append(data)

            if found:
                objt.delete()
                data = objt.__dict__
                datalist.append(data)
                with open('sample.json', 'w') as file:
                    for data in datalist:
                        json.dump(data, file)
                        file.write('\n')

        elif choose == "5":
            Query()

        elif choose == "6":
            var = False
            with open('sample.json') as file:
                userval = input('Enter the term for search: ')
                for obj in file:
                    found = False
                    data = json.loads(obj)
                    for key, value in data.items():
                        if key == 'uid':
                            continue
                        elif userval.lower() in value.lower():
                            found = True
                            break

                    if found:
                        var = True
                        for key, value in data.items():
                            if key == 'uid':
                                pass
                            else:
                                print(f'{key} : {value}', end=' ')
                        print()

            if not var:
                print('Records not matching')
        elif choose == "7":
            exit()

        else:
            print('Invalid entry')

        choose = input('Opt 1 to quit :')
        if choose == "1":
            option = False
        else:
            continue
