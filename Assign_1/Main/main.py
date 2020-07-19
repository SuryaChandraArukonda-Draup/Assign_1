from Query.Query import Query
from Search.Search import Search
from Details.Details import Details
from Delete.ToDelete import ToDelete
from check.Check import Check
from Edit.Edit import Edit

if __name__ == "__main__":
    option = True
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
            Details.details()

        if choose == "2":
            Edit.edit()

        elif choose == "3":
            Check.check()

        elif choose == "4":
            ToDelete.todelete()

        elif choose == "5":
            Query.Query1()

        elif choose == "6":
            Search.search()
        elif choose == "7":
            exit()

        else:
            print('Invalid entry')

        choose = input('Opt 1 to quit :')
        if choose == "1":
            option = False
        else:
            continue
