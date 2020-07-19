import json


class Check:
    def check():
        uid = input('Enter your unique id:')
        found = False
        with open('../sample.json') as file:
            for obj in file:
                data = json.loads(obj)
                if uid in data.values():
                    print(data)
                    found = True
        if not found:
            print('Sorry uid not found')