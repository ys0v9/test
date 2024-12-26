class Book: #클래스의 첫 글자는 대문자로 약속
    def  __init__(self, title, price):
        self.title=title
        self.price=price
    def get_title(self):
        return self.title
    def set_title(self,title):
        self.title=title
book1=Book(title='처음배우는 파이썬', price=20000)
book1.set_title('또 다시 배워보는 파이썬')
title=book1.get_title()
print(title)