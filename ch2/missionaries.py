
MAX_NUM: int = 5

class MCState:
    def __init__(self, missionaries: int, cannibals: int, boat: bool) -> None:
        self.wm: int = missionaries
        self.wc: int = cannibals
        self.em: int = MAX_NUM - self.wm
        self.ec: int = MAX_NUM - self.wc
        self.boat: bool = boat
    
    @property
    def is_legal(self) -> bool:
        if self.wm < self.wc and self.wm > 0:
            return False
        if self.em < self.ec and self.em > 0:
            return False
        return True
    
    def goal_test(self) -> bool:
        return self.is_legal and self.em == MAX_NUM and self.ec == MAX_NUM
    
    def __str__(self) -> str:
        return (f"On the west bank there are {self.wm} missionaries and {self.wc} cannibals\n"
                f"On the east bank there are {self.em} missionaries and {self.ec} cannibals\n"
                f"The boat is on the {"west" if self.boat else "east"} bank")
    
mcs: MCState = MCState(5, 5, True)
print(mcs)