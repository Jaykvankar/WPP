class Converter:
    factors = {
        "inches": 1, "feet": 1/12, "yards": 1/36, "miles": 1/63360,
        "kilometers": 1/39370.1, "meters": 1/39.3701, "centimeters": 1/0.393701, "millimeters": 1/0.0393701
    }

    def __init__(self, length, unit):
        self.len_inches = length / self.factors.get(unit, 1)
    
    def inches(self): return self.len_inches * self.factors["inches"]
    def feet(self): return self.len_inches * self.factors["feet"]
    def yards(self): return self.len_inches * self.factors["yards"]
    def miles(self): return self.len_inches * self.factors["miles"]
    def kilometers(self): return self.len_inches * self.factors["kilometers"]
    def meters(self): return self.len_inches * self.factors["meters"]
    def centimeters(self): return self.len_inches * self.factors["centimeters"]
    def millimeters(self): return self.len_inches * self.factors["millimeters"]


c = Converter(9, "inches")
print(c.feet())
