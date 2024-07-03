# L0 底线用例：类方法缺失

from animals import Zoo, Dog, Cat

zoo = Zoo([Dog("旺财"), Cat("咪咪")])

print("动物园里有：", len(zoo), " 只动物")
zoo.make_sound()