# L0 底线用例：方法缺失

from animals import Zoo, Dog, Cat, Bird, Pig

zoo = Zoo([Dog("旺财"), Cat("咪咪"), Bird("小鸟")])
zoo.append(Pig("佩奇"))
assert(len(zoo) == 4)
print("动物园里有：", len(zoo), " 只动物")
zoo.make_sound()