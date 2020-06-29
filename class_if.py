class lunch:
  
    def __init__(self, menu):
        self.menu = menu
        
    def menu_price(self):
        if self.menu == 'menu_1':
            print("your lunch price is $12")

        elif self.menu == 'menu_2':
            print("your lunch price is $13.40")
        else:
            print("no such menu is available")

menu = lunch("menu_1")
menu_two = lunch('menu_2')
print(menu.menu_price())
print(menu_two.menu_price())



