from random import randint


class Die():
    """一个表示骰子的类。"""

    def __init__(self, sides=6):
        """初始化骰子。"""

        self.sides = sides

    def roll_die(self):
        """返回一个位于1和骰子面数之间的随机数。"""

        return randint(1,
                       self.sides)


# 创建一个6面的骰子，再掷10次并显示结果。
d6 = Die()
results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
    print("10 rolls of a 6-sided die:")
    print(results)
#创建一个10面的骰子，再掷10次并显示结果。
d10 = Die(sides=10)
results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
    print("\n10 rolls of a 10-sided die:")
    print(results)
# 创建一个20面的骰子，再掷10次并显示结果。
d20 = Die(sides=20)
results = []
for roll_num in range(10):
    result = d20.roll_die() 
    results.append(result)
    print("\n10 rolls of a 20-sided die:")
    print(results)

