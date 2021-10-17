import numpy as np


class Equation:
    def __init__(self, x0, y0, X, N):
        self.x0 = x0
        self.X = X
        self.y0 = y0
        self.N = N

        self.x = np.linspace(self.x0, self.X, self.N)

    def calculate_prime(self, x, y):
        return 1/x + 2 * y / (x * np.log(x))

    def get_equation(self):
        pass

    def set_x0(self, x0):
        self.x0 = x0
        self.x = np.linspace(self.x0, self.X, self.N)

    def set_y0(self, y0):
        self.y0 = y0

    def set_N(self, N):
        self.N = N
        self.x = np.linspace(self.x0, self.X, self.N)

    def set_X(self, X):
        self.X = X
        self.x = np.linspace(self.x0, self.X, self.N)


class AnalyticalSolution(Equation):
    def __init__(self, x0, y0, X, N):
        super().__init__(x0, y0, X, N)
        self.const = (self.y0 + np.log(self.x0)) / (np.log(self.x0) ** 2)

    def calculate_const(self):
        self.const = (self.y0 + np.log(self.x0)) / (np.log(self.x0) ** 2)
        return self.const

    def get_equation(self):
        y = self.const * (np.log(self.x) ** 2) - np.log(self.x)
        return [self.x, y]

    def set_x0(self, x0):
        super().set_x0(x0)
        self.calculate_const()

    def set_y0(self, y0):
        super().set_y0(y0)
        self.calculate_const()


class NumericalMethod(Equation):
    def __init__(self, x0, y0, X, N):
        super().__init__(x0, y0, X, N)
        self.x_current = x0
        self.y = [y0]


class EulerMethod(NumericalMethod):
    def __init__(self, x0, y0, X, N):
        super().__init__(x0, y0, X, N)

    def get_equation(self):
        for i in range(self.N - 1):
            self.y.append(self.y[-1] + (self.X - self.x0) / self.N * self.calculate_prime(self.x_current, self.y[-1]))
            self.x_current += (self.X - self.x0) / self.N
        return [self.x, self.y]


class ImprovedEulerMethod(NumericalMethod):
    def __init__(self, x0, y0, X, N):
        super().__init__(x0, y0, X, N)

    def get_equation(self):
        h = (self.X - self.x0) / self.N
        for i in range(self.N - 1):
            current_prime = self.calculate_prime(self.x_current, self.y[-1])
            self.y.append(self.y[-1] +
                          h * (current_prime + self.calculate_prime(self.x_current + h, self.y[-1] + h * current_prime)) / 2)
            self.x_current += (self.X - self.x0) / self.N
        return [self.x, self.y]


class RungeMethod(NumericalMethod):
    def __init__(self, x0, y0, X, N):
        super().__init__(x0, y0, X, N)

    def get_equation(self):
        h = (self.X - self.x0) / self.N
        for i in range(self.N - 1):
            k1 = self.calculate_prime(self.x_current, self.y[-1])
            k2 = self.calculate_prime(self.x_current + h / 2, self.y[-1] + h / 2 * k1)
            k3 = self.calculate_prime(self.x_current + h / 2, self.y[-1] + h / 2 * k2)
            k4 = self.calculate_prime(self.x_current + h, self.y[-1] + h * k3)
            self.y.append(self.y[-1] + h / 6 * (k1 + 2 * k2 + 2 * k3 + 2 * k4))
            self.x_current += (self.X - self.x0) / self.N
        return [self.x, self.y]


class LTE:
    pass


class GTE:
    pass
