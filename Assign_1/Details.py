import random
import string
import json
from Project.Assign_1.AboutMe import AboutMe


class Details(AboutMe):



    def details():
        name = input('Enter your Name:')
        profession = input('Enter your profession:')
        contact = input('Enter your mobile no:')
        skills = input('Enter your Skills:')
        DOB = input('Enter your Date of Birth:')
        description = input('Describe yourself:')

        uid = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])

        obj = AboutMe(uid, name, profession, contact, skills, DOB, description)
        # Method used to convert object to dictionary
        # The data is then written on sample.json
        data = obj.__dict__
        print(f'Your unique identification number is: {uid}')
        print('Please save this id for future reference.')

        with open('sample.json', 'a') as file:
            json.dump(data, file)
            file.write('\n')
