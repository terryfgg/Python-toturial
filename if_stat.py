know_person = ['gigi', 'terry', 'mark', 'david', 'mike', 'selena']
person = str(input('輸入你所認識的人'))
if person in know_person:
    print('你找到認識的{}了'.format(person))
else:
    print('抱歉這裡沒有你認識的{}'.format(person))