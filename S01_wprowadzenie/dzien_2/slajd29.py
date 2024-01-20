class Figura:
    def pole(self):
        pass

class Kwadrat(Figura):
    def __init__(self, bok):
        self.bok = bok

    def pole(self):
        return self.bok ** 2


class Kolo(Figura):
    def __init__(self, promien):
        self.promien = promien

    def pole(self):
        return 3.14 * self.promien ** 2


figury = [Kwadrat(2), Kolo(3)]
print(figury)

for figura in figury:
    print(figura.pole())
