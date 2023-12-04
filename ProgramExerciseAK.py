class shopping:
    def __init__(self,fname,famount):
        self.foodname = fname
        self.foodamount = famount
        self.__price = self.__pricelist()
        self.finalprice = self.calculatedprice()

    def __pricelist(self):
        if self.foodname == "Dry Cured Iberian Ham":
            self.__price = 177.80
        elif self.foodname == "Wagyu Steaks":
            self.__price = 450.00
        elif self.foodname == "Matsutake Mushroom":
            self.__price = 272.00
        elif self.foodname == "Kopi Luwak Coffee":
            self.__price = 306.50
        elif self.foodname == "Moose Cheese":
            self.__price = 487.20
        elif self.foodname == "White Truffles":
            self.__price = 3600.00
        elif self.foodname == "Blue Fin Tuna":
            self.__price = 3603.00
        elif self.foodname == "Le Bonnotte Potatoes":
            self.__price = 270.81

        else:
            self.__price = 0
        
        return self.__price
    
    def calculatedprice(self):
        calculated = self.foodamount * self.__price
        
        return calculated

    
    def __str__(self):
        return f"food: {self.foodname}, amount: {self.foodamount}, Calculated price: {self.calculatedprice()}"

    
