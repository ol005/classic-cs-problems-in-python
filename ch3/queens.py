from csp import Constraint, CSP
from typing import Optional

class QueensConstraint(Constraint[int, int]):
    def __init__(self, columns: list[int]) -> None:
        super().__init__(columns)
        self.columns: list[int] = columns
    
    def satisfied(self, assignment: dict[int, int]) -> bool:
        for q1c, q1r in assignment.items():
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assignment:
                    q2r: int = assignment[q2c]
                    if q1r == q2r:
                        return False
                    if abs(q1r - q2r) == abs(q1c - q2c):
                        return False
        return True

if __name__ == "__main__":
    columns: list[int] = [1, 2, 3, 4, 5, 6, 7, 8] # variables
    rows: dict[int, list[int]] = {} # domains

    for col in columns:
        rows[col] = [1, 2, 3, 4, 5, 6, 7, 8]

    csp: CSP[int, int] = CSP(variables=columns, domains=rows)
    csp.add_constraint(QueensConstraint(columns))
    solution: Optional[dict[int, int]] = csp.backtracking_search()
    if solution is None:
        print("No solution found")
    else:
        print(solution)