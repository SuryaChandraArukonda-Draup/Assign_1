import json


class Search:
    def search():
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