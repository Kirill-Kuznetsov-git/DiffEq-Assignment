import numpy as np
from random import randint


class Equation:
    def __init__(self, x0, y0, X, N):
        self.x0 = x0
        self.X = X
        self.y0 = y0
        self.N = N
        self.x = np.linspace(self.x0, self.X, self.N)
        self.vision = True

    def calculate_prime(self, x, y):
        return 1 / x + 2 * y / (x * np.log(x))

    def get_exact_value(self, x):
        pass

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
        super().get_equation()
        y = self.const * (np.log(self.x) ** 2) - np.log(self.x)
        return [self.x, y]

    def get_exact_value(self, x):
        return self.const * (np.log(x) ** 2) - np.log(x)

    def set_x0(self, x0):
        super().set_x0(x0)
        self.calculate_const()

    def set_y0(self, y0):
        super().set_y0(y0)
        self.calculate_const()


class NumericalMethod(Equation):
    def __init__(self, x0, y0, X, N, n0):
        super().__init__(x0, y0, X, N)
        self.x_current = x0
        self.y = [self.y0]
        self.n0 = n0

    def set_n0(self, n0):
        self.n0 = n0
        print(1)

    def get_equation(self):
        self.x_current = self.x0
        self.y = [self.y0]

    def get_lte(self, analytic_solution: AnalyticalSolution) -> list:
        errors = []
        h = (self.X - self.x0) / self.N
        self.x_current = self.x0
        for i in range(self.N):
            errors.append(abs(self.y[i] - analytic_solution.get_exact_value(self.x_current)))
            self.x_current += h
        return [analytic_solution.x, errors]

    def get_gte(self, analytic_solution: AnalyticalSolution):
        if self.n0 >= self.N:
            return [[0], [0]]
        errors = []
        n_old = self.N
        for i in range(int(self.N - self.n0)):
            self.set_N(self.n0 + i)
            errors.append(max(self.get_lte(analytic_solution)[1]))
        self.set_N(n_old)
        return [np.linspace(self.n0, self.N, int(self.N - self.n0)), errors]


class EulerMethod(NumericalMethod):
    def __init__(self, x0, y0, X, N, n0):
        super().__init__(x0, y0, X, N, n0)

    def get_equation(self):
        res = super().get_equation()
        if res: return res
        h = (self.X - self.x0) / self.N
        for i in range(self.N - 1):
            self.y.append(self.y[-1] + h * self.calculate_prime(self.x_current, self.y[-1]))
            self.x_current += (self.X - self.x0) / self.N

        return [self.x, self.y]


class ImprovedEulerMethod(NumericalMethod):
    def __init__(self, x0, y0, X, N, n0):
        super().__init__(x0, y0, X, N, n0)

    def get_equation(self):
        res = super().get_equation()
        if res: return res
        h = (self.X - self.x0) / self.N
        for i in range(self.N - 1):
            self.y.append(self.y[-1] + h * self.calculate_prime(self.x_current + h / 2,
                                                                self.y[-1] + h / 2 * self.calculate_prime(
                                                                    self.x_current, self.y[-1])))
            self.x_current += (self.X - self.x0) / self.N

        return [self.x, self.y]


class RungeMethod(NumericalMethod):
    def __init__(self, x0, y0, X, N, n0):
        super().__init__(x0, y0, X, N, n0)

    def get_equation(self):
        res = super().get_equation()
        if res: return res
        h = (self.X - self.x0) / self.N
        for i in range(self.N - 1):
            k1 = self.calculate_prime(self.x_current, self.y[-1])
            k2 = self.calculate_prime(self.x_current + h / 2, self.y[-1] + h / 2 * k1)
            k3 = self.calculate_prime(self.x_current + h / 2, self.y[-1] + h / 2 * k2)
            k4 = self.calculate_prime(self.x_current + h, self.y[-1] + h * k3)
            self.y.append(self.y[-1] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4))
            self.x_current += (self.X - self.x0) / self.N

        return [self.x, self.y]
