class friedchicken:#類別firedchicken
    #定義建構子和五個屬性
    def __init__(self, name, price, parts, size, season):
        self.name = name
        self.price = price
        self.parts = parts
        self.size = size
        self.season = season
    #定義3個副函式
    def fooditems(self):
        print(f"It called {self.name} and sell {self.price}")
    
    def detail(self):
        print(f"{self.name} is made up of {self.size} {self.parts}")
    
    def time(self):
        print(f"{self.name} is {self.season} supply")

#建立4個炸雞物件
chicken1 = friedchicken("Original fried chicken", 160, "legs","middle","all season")
chicken2 = friedchicken("Garlic fried chicken", 180, "legs","large","spring and summer")
chicken3 = friedchicken("Italian fried chicken", 220, "chest","small","fall")
chicken4 = friedchicken("Cheese fried chicken", 180, "chest","middle","winter and spring")
#呼叫chicken1 3個副函式
chicken1.fooditems()
chicken1.detail()
chicken1.time()
#呼叫chicken2 3個副函式
chicken2.fooditems()
chicken2.detail()
chicken2.time()
#呼叫chicken3 3個副函式
chicken3.fooditems()
chicken3.detail()
chicken3.time()
#呼叫chicken4 3個副函式
chicken4.fooditems()
chicken4.detail()
chicken4.time()