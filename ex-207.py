import json

FILE_PATH = './ex-207.json'

class Person:
    year = 2023
    
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Doroth', 35)
p2 = Person('Phillip', 18)
p3 = Person('Jhon', 55)

db = [vars(p1), p2.__dict__, vars(p3)]

with open(FILE_PATH, 'w+') as file:
    json.dump(db, file, ensure_ascii=False, indent=2)