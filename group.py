class Group:
    def __init__(self, group_type: str, capacity: int, price: float) -> None:
        self.group_type = group_type
        self.capacity = capacity
        self.price = price
        self.remaining_capacity = self.capacity

    def has_capacity(self, tickets: int) -> bool:
        return tickets <= self.remaining_capacity

    def sell(self, tickets: int) -> None:
        self.remaining_capacity -= tickets
