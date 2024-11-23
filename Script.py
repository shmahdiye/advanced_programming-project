
def slope(x1, x2, y1, y2):
    return round((y2-y1) / (x2-x1), 2)


def get_point():
    while True:
        try:
            x = float(input("مختصات x نقطه را وارد کنید: "))
            y = float(input("مختصات y نقطه را وارد کنید: "))
            return x, y
        except ValueError:
            print("لطفاً عددی معتبر وارد کنید.")


p1 = get_point()
p2 = get_point()
m = slope(p1[0], p2[0], p1[1], p2[1])


def get_b(p, m):
    return p[1] - m*p[0]


b = get_b(p1, m)


def equation(m, b):
    eq = str(m) + "x + " + str(b)
    return eq


print(equation(m, b))


