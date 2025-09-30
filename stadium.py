from group import Group


class Stadium:
    def __init__(self) -> None:
        self.group = Group("front", 300, 400.0)


stadium = Stadium()
