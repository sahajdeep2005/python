dict={"name": "saju",
      "class":10,
      "sun":"math",
      "rollno.":10}
print(dict)
print(type(dict))

dict2={"name": "saju",
        "class":11,
         "sun":"sst",
        "rollno.":12}
print(dict2.keys())



dict1={"name": "saju",
       "class":11,
       "sun":"sst",
       "rollno.":12}
print(dict1.values())


dict1={"name": "saju",
       "class":11,
       "sun":"sst",
       "rollno.":12}
dict1['name']='raju'
print(dict1)
dict1['hobby']='cricket'
print(dict1)
#pop and update method


dict1={'apple':20,
      'mango':30,
       'orange':40,}

dict2={"cherry":40,
       "banana":70,
       "watermelon":10,}

dict1.update(dict2)
print(dict1)
dict1.pop("orange")
print(dict1)