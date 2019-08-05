my_name = "Terry Lin"

for i in my_name:
    print(i)

my_list = [2, 5, 6, 7, 10]

for number in my_list:
    print(number ** 2)

user_want = True
while user_want == True:
    print(10)
    user_input = (input('你要繼續嗎(y/n)'))
    if user_input == 'n':
        user_want = False
