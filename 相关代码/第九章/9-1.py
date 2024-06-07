class Restaurant():
    def __init__(self, name, cuisine_type):
        """初始化餐馆。"""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """显示餐馆信息摘要。"""

        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """显示一条消息，指出餐馆正在营业。"""

        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")
restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
