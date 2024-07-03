class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name}在汪汪叫！")

class Cat:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name}在喵喵叫！")

class Bird:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name}在啾啾叫！")

class Pig:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name}在哼哼叫！")

class Zoo:
    def __init__(self, list):
        self.list = list

    def __len__(self):
        return len(self.list)

    def make_sound(self):
        for animal in self.list:
            animal.bark()