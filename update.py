import random

card_dict = {'PU星5鯖':8, '星5鯖':2, '星5礼装':40, '星4鯖':30, '星4礼装':120, '星3鯖':400, '星3礼装(カス)':800}

value_list = list(card_dict.values())

l = []
res = []

g_dice = random.randint(1,120)
if g_dice <= value_list[0]:
    l.append("PU星5鯖")
elif g_dice <= value_list[1]:
    l.append('星5鯖')
elif g_dice <= value_list[2]:
    l.append('星5礼装')
elif g_dice <= value_list[3]:
    l.append('星4鯖')
elif g_dice <= value_list[4]:
    l.append('星4礼装')


for i in range(9):
    dice = random.randint(1,800)
    if dice <= value_list[0]:
        l.append("PU星5鯖")
    elif dice <= value_list[1]:
        l.append('星5鯖')
    elif dice <= value_list[2]:
        l.append('星5礼装')
    elif dice <= value_list[3]:
        l.append('星4鯖')
    elif dice <= value_list[4]:
        l.append('星4礼装')
    elif dice <= value_list[5]:
        l.append('星3鯖')
    else:
        l.append('星3礼装(カス)')
print(l)
