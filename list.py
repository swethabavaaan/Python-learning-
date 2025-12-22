# x = ['apple','banana','milk','potato']
# # print('apple' in x)
# # print(x[0])
# # print(x.index('milk'))
# # print(x[0:])
# x.append('Lady\'s_finger')
# # print(x)
# x +=['fish', 'rice']

# x.extend(['chicken'])
# x.insert(0,'capsicum')
# # x[2:2] = ['coffee', 'Tea']
# x[1:3] = ['brinjal','cauliflower']
# print(x)

# y = [2,15,23,85,102,56,5,8,45]
# # y.sort(reverse=True)
# # y.reverse()
# print(sorted(y,reverse=True))
# print(y)
# ycopy=y.copy()
# print(ycopy)
########################################################3
#############  TUPLE   ################################
# tuple = ('t',8,9,0)
# print(type(tuple))
# z=[(tuple)]
# z.append(15)
# print(z)
# newtuple =(z)
# print(newtuple)
# print(type(newtuple))
###################################################
#############Dictionaries######################
car ={
    "color" : "red",
    "type" : "SUV",
    "number" :16295
}
print(car)
car2 =dict(brand="sunny", model="model_3")
print(car2)
print(type(car))
print(car["color"])
print(car.get("type"))