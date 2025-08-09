from csp import Constraint, CSP
from typing import Optional

class MapColoringConstraint(Constraint[str, str]):
    def __init__(self, place1: str, place2: str) -> None:
        super().__init__([place1, place2])
        self.place1: str = place1
        self.place2: str = place2

    def satisfied(self, assignment: dict[str, str]) -> bool:
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        return assignment[self.place1] != assignment[self.place2]

if __name__ == "__main__":
    variables: list[str] = ["Western Australia", "Northern Territory", "South Australia",
                            "Queensland", "New South Wales", "Victoria", "Tasmania"]
    
    domains: dict[str, list[str]] = {}

    for variable in variables:
        domains[variable] = ['red', 'green', 'blue']

    csp: CSP[str, str] = CSP(variables, domains)
    print(csp.variables)
    csp.add_constraint(MapColoringConstraint("Western Australia", "Northern Territory"))
    csp.add_constraint(MapColoringConstraint("Western Australia", "South Australia"))
    csp.add_constraint(MapColoringConstraint("Northern Territory", "South Australia"))
    csp.add_constraint(MapColoringConstraint("Northern Territory", "Queensland"))
    csp.add_constraint(MapColoringConstraint("South Australia", "New South Wales"))
    csp.add_constraint(MapColoringConstraint("South Australia", "Queensland"))
    csp.add_constraint(MapColoringConstraint("South Australia", "Victoria"))
    csp.add_constraint(MapColoringConstraint("Queensland", "New South Wales"))
    csp.add_constraint(MapColoringConstraint("New South Wales", "Victoria"))
    csp.add_constraint(MapColoringConstraint("Victoria", "Tasmania"))

    solution: Optional[dict[str, str]] = csp.backtracking_search()
    if solution is None:
        print("no solution found")
    else:
        print(solution)