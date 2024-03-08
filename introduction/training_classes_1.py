class Tombol():#class
    def __init__(self, title_text, x_num, y_num): #constructor
        self.title = title_text#property
        self.x = x_num#property
        self.y = y_num#property
        self.appearance = True
    def hide(self):#method
        self.appearance = False
    def show(self):
        self.appearance = True
    def print_status(self):
        print('Widget data:')
        print(self.title, self.x, self.y, self.appearance)
    def coba(self):
        print("ini coba")

def inifungsi():#fungsi
    pass
ok_button = Tombol('ok bang yabes', 999, 111)
# print(ok_button.title)
# print(ok_button.x)
# print(ok_button.y)
ok_button.print_status()
ok_button.hide()
ok_button.print_status()

# ok_button.show()
# ok_button.print_status()
# ok_button.coba()
