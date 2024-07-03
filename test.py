# L0 底线用例：简单的类缺失

from animals import Zoo, Dog, Cat, Bird

zoo = Zoo([Dog("旺财"), Cat("咪咪")], Bird("小鸟"))

print("动物园里有：", len(zoo), " 只动物")
zoo.make_sound()