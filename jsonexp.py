import json

employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'

employee_dict = json.loads(employee)
print(employee_dict)
print(type(employee_dict))


employee_json = json.dumps(employee_dict , indent=4)
print(employee_json)

jsonString = '{"a": "apple", "b": "bear", "c": "cat"}'
python_dict = json.loads(jsonString)
print(python_dict)

python_dict1 = {'a': 'apple', 'b': 'bear', 'c': 'cat',}  # comma in the end signifies invalid json
json_dict = json.dumps(python_dict, indent=4)
print(json_dict)
