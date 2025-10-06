from group import Group


class Stadium:
    def __init__(self) -> None:
        self.groups = [
            Group("front", 300, 400.0),
            Group("middle", 1500, 100.0),
            Group("back", 200, 60.0),
        ]


stadium = Stadium()
