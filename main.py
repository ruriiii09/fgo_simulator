#金枠が2枚以上でないFGOガチャシミュレーター

import random

kaku = list(range(0,4))
dice = list(range(0,3))
sp = ['PU星5鯖','星5鯖','星4鯖','星4礼装']
n = ['星3鯖','星5礼装','星3礼装(カス)']

w = [0.8, 0.2, 3, 12]
w2 = [40, 4,40]

#確定枠
s = random.choices(kaku, k = 1 , weights = w)

for i in kaku:
  print(sp[i], ':', s.count(i))

#確定以外
s2 = random.choices(dice, k = 9 , weights = w2)

for j in dice:
  print(n[j], ':', s2.count(j))
