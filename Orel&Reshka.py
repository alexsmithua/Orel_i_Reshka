#-*- coding: utf-8 -*-
import random
orel = 0
resh = 0
i = 0
while i<3:
    i += 1
    coin = random.randint(1,2)
    if coin == 1:
        orel += 1
    if coin == 2:
        resh += 1
print ("Решек", resh)
print ("Орлов", orel)
