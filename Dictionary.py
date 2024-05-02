# empty_dict = {}
# print(empty_dict)


# john_dict = {
#     'name': 'John',
#     'age': 30,
#     'city': 'New York',
# }

# print(john_dict['name'], john_dict['age'])

# # retreiving all values
# for item, value in john_dict.items():
#     print(item ,value)
    
# print(john_dict['city'])

# # add items in dict
# john_dict['gender'] = 'Male'

# for item, value in john_dict.items():
#     print(item ,value)
    
# # delete any key-item
# del john_dict['city']


# # removes all items

# john_dict.clear()


# for item, value in john_dict.items():
#     print(item ,value)
    

def show(category):
    for item, value in cricket[category].items():
        print(item, value)

def batsman():
    key = input("Enter batsman name: ")
    value = input("Enter the value: ")
    cricket['batsman'][key] = value
    
def bowler():
    key = input("Enter bowler name: ")
    value = input("Enter the value: ")
    cricket['bowler'][key] = value

def allrounder():
    key = input("Enter allrounder name: ")
    value = input("Enter the value: ")
    cricket['allrounder'][key] = value

cricket = {
    'batsman': {},
    'bowler': {},
    'allrounder': {}
}

while True:
    print("Select option to edit:")
    print("1. Batsman")
    print("2. Bowler")
    print("3. All Rounder")

    op = input("Enter option: ")

    if op == '1':
        batsman()
        show('batsman')
        
    if op == '2':
        bowler()
        show('bowler')

    if op == '3':
        allrounder()    
        show('allrounder')
