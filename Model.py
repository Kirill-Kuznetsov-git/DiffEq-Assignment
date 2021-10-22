import numpy as np
from random import randint


class Equation:
    def __init__(self, x0, y0, X, N):
        self.x0 = x0
        self.X = X
        self.y0 = y0
        self.N = N
        self.cache_indexes_values = []
        self.cache_equation_values = []
        self.x = np.linspace(self.x0, self.X, self.N)
        self.vision = True

    def calculate_prime(self, x, y):
        return 1 / x + 2 * y / (x * np.log(x))

    def get_equation(self):
        if [self.x0, self.y0, self.X, self.N] in self.cache_indexes_values:
            return self.cache_equation_values[self.cache_indexes_values.index([self.x0, self.y0, self.X, self.N])]

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

        if len(self.cache_indexes_values) >= 10:
            rand_int = randint(0, len(self.cache_indexes_values) - 1)
            self.cache_equation_values[rand_int] = [self.x0, self.y0, self.X, self.N]
            self.cache_equation_values[rand_int] = [self.x, y]
        else:
            self.cache_indexes_values.append([self.x0, self.y0, self.X, self.N])
            self.cache_equation_values.append([self.x, y])
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

    # def get_lte(self) -> list:
    #     res = []
    #     solv = self.get_equation()
    #     for i in range(len(solv[1])):
    #
    #
    # def get_gte(self, n0) -> list:
    #     res = []
    #     for i in range(n0, self.N):
    #         res.append(max(self.get_lte(i)))
    #     return res

    def get_equation(self):
        self.y = [self.y0]
        self.x_current = self.x0
        return super().get_equation()

    def add_to_cache(self):
        if len(self.cache_indexes_values) >= 10:
            rand_int = randint(0, len(self.cache_indexes_values) - 1)
            self.cache_equation_values[rand_int] = [self.x0, self.y0, self.X, self.N]
            self.cache_equation_values[rand_int] = [self.x, self.y]
        else:
            self.cache_indexes_values.append([self.x0, self.y0, self.X, self.N])
            self.cache_equation_values.append([self.x, self.y])


class EulerMethod(NumericalMethod):
    def __init__(self, x0, y0, X, N):
        super().__init__(x0, y0, X, N)

    def get_equation(self):
        res = super().get_equation()
        if res: return res
        h = (self.X - self.x0) / self.N
        for i in range(self.N - 1):
            self.y.append(self.y[-1] + h * self.calculate_prime(self.x_current, self.y[-1]))
            self.x_current += (self.X - self.x0) / self.N

        self.add_to_cache()
        return [self.x, self.y]


class ImprovedEulerMethod(NumericalMethod):
    def __init__(self, x0, y0, X, N):
        super().__init__(x0, y0, X, N)

    def get_equation(self):
        res = super().get_equation()
        if res: return res
        h = (self.X - self.x0) / self.N
        for i in range(self.N - 1):
            self.y.append(self.y[-1] + h * self.calculate_prime(self.x_current + h / 2,
                                                                self.y[-1] + h / 2 * self.calculate_prime(
                                                                    self.x_current, self.y[-1])))
            self.x_current += (self.X - self.x0) / self.N

        self.add_to_cache()
        return [self.x, self.y]


class RungeMethod(NumericalMethod):
    def __init__(self, x0, y0, X, N):
        super().__init__(x0, y0, X, N)

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

        self.add_to_cache()
        return [self.x, self.y]
