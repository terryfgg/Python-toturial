
'''know_person = ['gigi', 'terry', 'mark', 'david', 'mike', 'selena']
person = str(input('輸入你所認識的人'))
if person in know_person:
    print('你找到認識的{}了'.format(person))
else:
    print('抱歉這裡沒有你認識的{}'.format(person))
'''


def who_you_know():
    people = input('你認識誰：')#數入英文人名（john, mary, mark)
    people_list = people.split(',')#以逗點隔開[john, mark, mary]


    people_without_space = []
    for person in people_list:
        people_without_space.append(person.strip())

    return people_without_space
def ask_user():
    person = input('請說你認識誰：')
    if person in who_you_know():
        print('有你認識的{}'.format(person))

ask_user()