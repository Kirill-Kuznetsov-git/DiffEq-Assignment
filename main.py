import pandas as pd
import matplotlib.pyplot as plt


# y^ = (y^2 + xy - x^2) / x^2
# y = x * (1 + x^2 / 3) / (1 - x^2 / 3)
# y(1) = 2
class Equation:
    def __init__(self):
        pass

    def calculate_prime(self, x, y):
        return (y ** 2 + x * y - x ** 2) / x ** 2

    def calculate(self, x):
        return x * (1 + (x ** 2) / 3) / (1 - (x ** 2) / 3)


class EulerMethod:
    def __init__(self):
        pass

    def calculate(self, x_i, y_i, h):
        return y_i + h * Equation().calculate_prime(x_i, y_i)


class Error:
    def __init__(self):
        pass

    def calculate_lte(self, x_i, y_exact_i, y_exact_i_1, h):
        y_euler_i_1_with_exact = EulerMethod().calculate(x_i, y_exact_i, h)
        return abs(y_euler_i_1_with_exact - y_exact_i_1)

    def calculate_gte(self, x_i, y_euler_i, h, y_euler_i_1=None, y_exact_i_1=None):
        y_euler_i_1 = EulerMethod().calculate(x_i, y_euler_i, h) if y_euler_i_1 is None else y_euler_i_1
        y_exact_i_1 = Equation().calculate(x_i + h) if y_exact_i_1 is None else y_exact_i_1
        return abs(y_exact_i_1 - y_euler_i_1)


def main():
    df = pd.DataFrame(columns=['x', 'y_exact', 'y_euler', 'lte', 'gte'])
    h = float(input("Your step: "))

    x = 1
    y_exact = 2
    y_euler = 2
    lte = 0
    gte = 0
    n = int((1.5 - x) // h) + 1

    df.loc[0] = [x, y_exact, y_euler, lte, gte]

    for i in range(1, 50):
        x_new = x + h
        y_exact_new = Equation().calculate(x_new)
        y_euler_new = EulerMethod().calculate(x, y_euler, h)
        lte = Error().calculate_lte(x, y_exact, y_exact_new, h)
        gte = Error().calculate_gte(x, y_euler, h, y_euler_new, y_exact_new)

        x = x_new
        y_exact = y_exact_new
        y_euler = y_euler_new

        df.loc[i] = [x, y_exact, y_euler, lte, gte]

    print(df)
    plt.scatter(df.x, df.y_exact)
    plt.scatter(df.x, df.y_euler)
    plt.show()


if __name__ == '__main__':
    main()
