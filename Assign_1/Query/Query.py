import json


class Query:
    def Query1():

        # This function is used to print all the data in the database

        with open('../sample.json') as f:
            for obj in f:
                data = json.loads(obj)
                for key, value in data.items():
                    if key == 'uid':
                        pass
                    else:
                        print(f'{key} : {value}', end=' ')
                print()