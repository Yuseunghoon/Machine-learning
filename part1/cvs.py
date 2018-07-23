#product
product_info=[]
#buylist=[]
class product:
    global product_info
    def insert(self, name, price, amount, type):
       product_info.append({'name':name, 'amount':amount,'price':price,'type':type})

class customer():
    buylist=[]
    def buy(self, name, amount):
        global product_info
        search_price=0
        for x in product_info:
            if x['name'] == name:
                search_price=x['price']

        self.buylist.append({'name':name, 'amount':amount,'price':search_price, 'total':search_price*amount})
        print(self.buylist)

    def total(self):
        sum=0
        for x in self.buylist:
            sum+=x['total']
        return sum

#class manange(product):

snack=product()
snack.insert('cookie', 1000, 10, 'snack')
drink=product()
drink.insert('soda', 2000, 5, 'drink')
print(product_info)

person=customer()
person.buy('cookie',2)
person.buy('soda',1)
print(person.total())



