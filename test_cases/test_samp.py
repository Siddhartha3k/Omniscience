import allure

numList = ["LDL Low Confidence", "中性脂肪 Low Confidence", "血糖 Low Confidence"]
b = []
for i in numList:
    a = i.replace("Low Confidence", "")
    b.append(a)

# print(b)

q = 0
for letter in "abc":
    # print("{}-{}".format(q, letter))
    q += 1

# print(q)

index_count = 0
word = 'hello world'
for letter1 in word:
    # print(word[index_count])
    index_count += 1

for item in enumerate(word):
    #print(item)
    pass

for index, letter in enumerate("adasd"):
    # print(index)
    # print(letter)
    pass

list1 = [1, 2, 3,4,5]
list2 = [100, 200, 300]

list3= list1.__add__(list2)
print(list3)
for item in zip(list1, list2):
    print(item)
print(list(zip(list1, list2)))


for item in enumerate(list2):
    print(item)

actual_data3=["abc\nxyz", "qwe\ntuy", "lkj\nbyu"]
actual_data3 = str(actual_data3)
actual_data3 = actual_data3.replace('\\n', ':')
print(actual_data3)
actual_data3 = actual_data3.split(" ")
print(actual_data3)




actual_data3 = ["abc\nABC", "def\nDEF", "ghi\nGHI"]
actual_data4 = ["ABC\n123", "GHI\n567", "DEF\n345"]

actual_data5 = ["ABC", "GHI", "DEF"]


m=[]
for item1 in enumerate((actual_data3),1):
    m.append(item1)

#actual_data4= ["体重\n今回\n66.0", "血小板数\n今回\n24.7", "最高血圧\n今回\n143", "腹囲\n今回\n76.0", "血色素量\n今回\n15.0", "最高血圧2回目\n今回\n163", "白血球数\n今回\n5940", "赤血球数\n今回\n507","最低血庄\n今回\n90","最低血庄2回目\n今回\n99","今回\n2018-7-10"]
actual_data4= ["血小板数\n今回\n24.7", "最高血圧\n今回\n143", "体重\n今回\n66.0"]
actual_data3 = ["body weight\n体重", "platelet count\n血小板数", "Systolic blood pressure\n最高血圧", "waist circumference\n腹囲", "Hemoglobin amount\n血色素量","Systolic blood pressure2\n最高血圧2回目"]
# actual_data4 = ["白血球数\n891", "空腹時血糖値\n345\n567", "SIDHU\n420\n840", "MNO\n900"]

print(actual_data3)
print(actual_data4)
spl_word = '\n'
k = []
k2 = []
k3 = []
k4 = []
k5 =[]
k6 =[]
k7 =[]
for i in actual_data4:
    res = i.partition(spl_word)[0]
    k.append(res)

for i in actual_data4:
    for q in actual_data3:
        if i.partition(spl_word)[0] == q.partition(spl_word)[2]:
            k6.append(i.partition(spl_word)[2])
            k7.append(q.partition(spl_word)[0])

print("_____________")
print(k6)
print(k7)
print("-------------")
print(k)
for j in k:
    for l in actual_data3:
        if j in l:
            res2 = l.partition(spl_word)[0]
            res3 = l.partition(spl_word)[2]
            k4.append(res3)
            k2.append(res2)



for j in k:
    for l in actual_data3:
        if j in l:
            res2 = l.partition(spl_word)[0]
            res3 = l.partition(spl_word)[2]
            k4.append(res3)
            k2.append(res2)
            if j == res3:
                k5.append(res2)






print(k2)
print("*********")
print(k4)
print(k5)
for i in actual_data4:
    res = i.partition(spl_word)[2]
    k3.append(res)
print(k3)

print(list(zip(k5, k3)))
e_list = list(zip(k5, k3))

m = []
for item1 in enumerate((e_list), 1):
    m.append(item1)
m = str(m)
m = m.replace("\\n", ":")
m = m.replace("'", "")
m = m.replace(",", ".")
m = m.replace(").", "),")
m = m.replace(":", ", ")
m = m.replace("今回", "")

print(m)
