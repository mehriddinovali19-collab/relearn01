class Products:
    def __init__(self, name, price, quantity):
        self.name = name 
        self.price = price 
        self.quantity = quantity
    

    def total_price(self):
        return self.price * self.quantity
    

class Store:
    def __init__(self):
        self.products = []
    


    def add_product(self, product):
        self.products.append(product)



    def most_expensive(self):
        eng_qimmat = max(self.products, key=lambda p: p.price)
        print(f"Eng qimmat: {eng_qimmat.name} — {eng_qimmat.price} so'm")
        
    
    def all_products(self):
        for product in self.products:
             print(f"{product.name} — {product.price} so'm | Soni: {product.quantity} | Jami: {product.total_price()} so'm")
    
    

    def total_price(self):
        total = sum(p.total_price() for p in self.products)
        print(f"Total price: {total} so'm")




dokon = Store()
dokon.add_product(Products("Olma", 5000, 3))
dokon.add_product(Products("Nok", 12000, 2))
dokon.add_product(Products("Banan", 8000, 5))
dokon.add_product(Products("Uzum", 15000, 1))
dokon.add_product(Products("Gilos", 20000, 2))

dokon.all_products()
dokon.most_expensive()
dokon.total_price()