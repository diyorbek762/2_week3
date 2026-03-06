class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    # TODO: Implement __str__
    def __str__(self):
        print(f"{self.name} --- {self.quantity}")
    
    # TODO: Implement __add__
    # Hint: 'other' is the object on the right side of the '+'
    # Check if self.name == other.name first!
        

# Test it:
p1 = Product("Apple", 10)
p2 = Product("Apple", 20)
p3 = p1 + p2
print(p3) # Should print: Product: Apple (30 units)