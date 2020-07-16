import json
from Project.Assign_1.AboutMe import AboutMe


class Edit(AboutMe):
    def edit():
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
            objt.edit_data()
            data = objt.__dict__
            datalist.append(data)
            with open('sample.json', 'w') as file:
                for data in datalist:
                    json.dump(data, file)
                    file.write('\n')

        else:
            print('Unique identification number is not found')
