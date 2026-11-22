import random

class SecretCalculator:
    def __init__(self, value_a, value_b):
        self._value_a = value_a
        self._value_b = value_b

    def _calculate_result(self):
        sign = random.choice(["+", "-", "*"])

        if sign == "+":
            return self._value_a + self._value_b
        elif sign == "-":
            return self._value_a - self._value_b
        else:
            return self._value_a * self._value_b

    def __str__(self):
        return f"Розрахунок дав такі результати: {self._calculate_result()}"

if __name__ == "__main__":
    calculator = SecretCalculator(1000, 7)
    print(calculator)