import json

# some JSON:

json_string = '{ "name": "Jim & Por", "age": 26, "city": "Bangkok"} '

# parse x :
python_dict = json.loads(json_string)

# the result is a Python dictionary:
print(python_dict["name"])
print(python_dict["age"])
print(python_dict["city"])