class Number:
    def __init__(self, n) -> None:
        self.n = n

    def __add__(self, num):
        return self.n + num.n


n = Number(3)
m = Number(4)

print(n + m)