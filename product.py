class Product(object):
    def __init__(self, price, item_name, weight, brand, status, tax):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
        self.tax = self.price*0.08
        
    def sell(self):
        self.status = "sold"
        return self
    def addTax(self):
        if self.status == "sold":
            self.price += self.price * 0.08 
        return self
    def returnItem(self,reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
            self.tax = 0
            return self
        if reason_for_return == "like new":
            self.status = "for sale"
            return self
        if reason_for_return == "opened":
            self.status = "used"
            self.price = self.price * 0.8
            return self
            
    def displayInfo(self):
        print "Price: $", self.price
        print "Item Name: ", self.item_name
        print "Weight: ", self.weight
        print "Brand: ", self.brand
        print "Status: ", self.status
        print "Total: $", self.price + self.tax,"\n"
        return self

product1 = Product(5, "soda", "0.1 lb", "coke", "for sale", " ")
# product1.displayInfo()
# product1.sell().displayInfo()
product1.addTax().sell().displayInfo()
# product1.returnItem("defective").displayInfo()
# product1.returnItem("like new").displayInfo()
# product1.returnItem("opened").displayInfo()

