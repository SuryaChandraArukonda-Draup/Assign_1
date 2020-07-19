import json
from Details.Details import Details
from AboutMe.AboutMe import AboutMe


class ToDelete(Details, AboutMe):
    def todelete():
        found = False
        uid = input('Please enter your unique id:')
        datalist = []
        with open('../sample.json') as file:
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
            with open('../sample.json', 'w') as file:
                for data in datalist:
                    json.dump(data, file)
                    file.write('\n')

