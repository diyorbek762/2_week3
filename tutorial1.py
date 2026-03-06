class Temperature:
    def __init__(self, celcius):
        self.celcius = celcius

    def __str__(self):
        return f"{self.celcius}°C"
    
    def __lt__(self, other):
        if isinstance(other, Temperature):
            return self.celcius < other.celcius
    
t1 = Temperature(15)
t2 = Temperature(30)
print(t1 < t2)
print(t2 < t1)
print(t1)