class User():
    """一个表示用户的简单类。"""
    def __init__(self, first_name, last_name, username, email, location):
          """初始化用户。"""


          self.first_name = first_name.title()
          self.last_name = last_name.title()
          self.username = username
          self.email = email
          self.location = location.title()


    def describe_user(self):
           """显示用户信息摘要。"""


           print(f"\n{self.first_name} {self.last_name}")
           print(f" Username: {self.username}")
           print(f" Email: {self.email}")
           print(f" Location: {self.location}")


    def greet_user(self):
        print(f"\nWelcome back, {self.username}!")

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()
willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()
