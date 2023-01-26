import random

runningsku = random.randint(1001,100000000001)
shoppingcart = []
total_items = 0
transaction_id = 100010100101001
check_list = []

while True:
    class Fruit: 
        def __init__(self,fruit,fruit_quantity, fruit_cost, runningsku): 
            self.fruit = fruit 
            self.fruit_quantity = fruit_quantity
            self.fruit_cost = fruit_cost * 1.07
            self.sku = runningsku
        def show(self): 
            print("Type:",self.fruit, "Qty:", fruit_quantity, "Cost:", fruit_cost, "sku:", runningsku)

    fruit = input("What fruit do you want? ")

    fruit_quantity = int (input("How many do you want? "))

    fruit_cost = float(input("How much does one cost? "))
    check_list.append(fruit)
    if fruit not in check_list:
        sku = Fruit(fruit, fruit_quantity, fruit_cost, runningsku )
        shoppingcart.append({"fruit": fruit, "qty": fruit_quantity, "sku": runningsku})
        sku.show()
        runningsku += 1101
    else:
        runningsku = shoppingcart['sku']
        sku = Fruit(fruit, fruit_quantity, fruit_cost, runningsku )
        shoppingcart.append({"fruit": fruit, "qty": fruit_quantity, "sku": runningsku})
        sku.show() 


    
    
    

