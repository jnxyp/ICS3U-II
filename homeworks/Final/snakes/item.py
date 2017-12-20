class Item:
    pt = 0

    def __init__(self, pt: int):
        self.pt = pt

    def get_pt(self) -> int:
        return self.pt

    def set_pt(self, pt: int):
        self.pt = pt


class Food(Item):
    def __init__(self, pt: int = 1):
        super().__init__(pt)


class Wall(Item):
    def __init__(self, pt: int = 1):
        super().__init__(pt)


class Air(Item):
    def __init__(self):
        super().__init__(0)
