#def dic(lst):
   #return lst["age"]

list_dic = [{"name": "Tanya", "age": 10, "grade": 8},
{"name": "Maks", "age": 5, "grade": 10}, {"name": "Roma", "age": 7, "grade": 7}]

list_dic.sort(key=lambda x: x["age"], reverse=True)

print(list_dic)
