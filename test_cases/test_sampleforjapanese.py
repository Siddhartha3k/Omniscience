import json
import shlex

file0 = open("D:/git/Omniscience/Forms_actual_data_json_file/acc_test_4.json", 'r', encoding="utf8")
#file0 = open("D:/git/Omniscience/Forms_actual_data_json_file/acc_test_4.json", 'r', encoding="utf8")
json_input0 = file0.read()
input_body0 = json.loads(json_input0)
json_data0 = list(input_body0.values())

list2='\n'
y=list2.join(json_data0)
x=y.split()
#print(x)



file1 = open("D:/git/Omniscience/data/all_keys_english.json", 'r', encoding="utf8")
json_input = file1.read()
input_body = json.loads(json_input)
english_data = list(input_body.values())





al = []
for i in x:
    for j in english_data:
        if i in j:
            al.append(j)
al = list(set(al))
al =str(al)

#print(al.replace("\\n", " "))




actual_data3 = ["abc ABC", "def DEF", "lkj GHI"]
actual_data4 = ["ABC 123", "GHI 567", "DEF 345"]

lo="abc ABC"
li = "ABC 123"
print(lo.__contains__(li))

a=[]
k=[]
for i in actual_data3:
    for j in actual_data4:
        j.split(" ")
        k.append(j)
        if j in (i):
            a.append(i)

# print(a)
# print(k)

e_list = ["abc", "cda", "fgh", "hji"]
m = []
for item1 in enumerate((e_list), 1):
    m.append(item1)
print(m)


