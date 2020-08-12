class ShoppingCart:
    # write your code here
   def __init__(self, 
                 total = 0, 
                 emp_discount = None, 
                 items = [],
                 discounts = 0):
      self.total = total
      self.employee_discount = emp_discount
      self.items = items
      self.discounts = discounts

   def add_item(self, name, price, quantity=1):
      self.items.append({'name':name, 'price':price, 'quantity':quantity})
      self.total += (price * quantity)
      return self.total
   def mean_item_price(self):
      allPrices = []
      for x in self.items:
         for y in range(x['quantity']):
            allPrices.append(x['price'])
      allPrices.sort()
      return sum(allPrices)/len(allPrices)

   def median_item_price(self):
      allPrices = []
      for x in self.items:
         for y in range(x['quantity']):
            allPrices.append(x['price'])
      allPrices.sort()
      if len(allPrices) % 2 == 1:
         return allPrices[int((len(allPrices)+1)/2)]
      else:
         return (allPrices[int(len(allPrices)/2)]+allPrices[int((len(allPrices)+2)/2)])/2
   def apply_discount(self):
      if self.discounts == 0:
         return 'sorry, no discounta available.'
      else:
         self.discounts = (100 - self.discounts)/100
         self.total = self.total * self.discounts
         self.discounts = 0
         return (self.total * self.discounts)

   def void_last_item(self):
      if len(self.items) == 0:
         print(self.items)
         print('test')
         return 'No items'
      else:
         print(self.items[len(self.items)-1]['price'])
         self.total -= (self.items[len(self.items)-1]['price']*self.items[len(self.items)-1]['quantity'])
         self.items.pop()