list1 = ['n', 'e', 'w', 'l', 'i', 's', 't']
list2 = ['n', 'e', 'w', 's', 't', 'r', 'i', 'n', 'g']

list_new = list1[:3] + list2[6:]
print(list_new)

spell = ['j', 'e', 's', 'u', 's']
spell[2:] = ['l', 'l', 'y']
print(spell)

piano = ['도', '레', '미', '파', '솔', '라', '시']
first_harmony = piano[0] + piano[2] + piano[4]
print(first_harmony)
second_harmony = piano[3] + piano[5] + piano[0]
print(second_harmony)
third_harmony = piano[4] + piano[6] + piano[1]
print(third_harmony)

# 연필 200
# 펜 800
# 지우개 500
# 자 300

pencilcase = {'pencil': 200, 'pen': 800, 'eraser': 500, 'ruler': 300}

money = pencilcase['pencil'] + pencilcase['ruler']
print(money)

reverse = pencilcase[200]
print(reverse)
