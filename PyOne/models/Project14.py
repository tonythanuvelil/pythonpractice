# Custom Types

# Geometric Points


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


pt = Point(2.5, 6)
print("(", pt.x, ",", pt.y, ")", sep="")


class EmployeeRecord:
    def __init__(self, n, i, r):
        self.name = n
        self.id = i
        self.pay_rate = r


rec = EmployeeRecord('Tony', 33, 90)
print(rec.name, rec.id, rec.pay_rate)
