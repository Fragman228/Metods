class Vektor:
    def __init__(self, cord_x, cord_y, cord_z):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.cord_z = cord_z

    def __str__(self):
        return self.cord_x, self.cord_y, self.cord_z

    def __sub__(self, other):
        return self.cord_x - other.cord_x, self.cord_y - other.cord_y, self.cord_z - other.cord_z
    def __add__(self, other):
        return self.cord_x + other.cord_x, self.cord_y + other.cord_y, self.cord_z + other.cord_z
    def __mul__(self, other):
        return self.cord_x * other.cord_x + self.cord_y * other.cord_y + self.cord_z * other.cord_z

vect1 = Vektor(1, 2, 3)
vect2 = Vektor(-1, 2, 4)
print(vect1.__add__(vect2))
print(vect1.__sub__(vect2))
print(vect1.__mul__(vect2))