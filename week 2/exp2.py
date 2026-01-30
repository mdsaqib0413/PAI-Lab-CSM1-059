import heapq

class State:
    def __init__(self, jug1, jug2, parent=None, action="Initial"):
        self.jug1 = jug1
        self.jug2 = jug2
        self.parent = parent
        self.action = action
        self.g = parent.g + 1 if parent else 0

    def __lt__(self, other):
        h_self = min(abs(self.jug1 - target), abs(self.jug2 - target))
        h_other = min(abs(other.jug1 - target), abs(other.jug2 - target))
        return (self.g + h_self) < (other.g + h_other)

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))


def solve_water_jug_problem(capacity1, capacity2, target):
    initial_state = State(0, 0)
    open_list = []
    heapq.heappush(open_list, initial_state)
    closed_set = set()

    while open_list:
        current_state = heapq.heappop(open_list)

        if (current_state.jug1, current_state.jug2) in closed_set:
            continue
        closed_set.add((current_state.jug1, current_state.jug2))

        # Goal check
        if current_state.jug1 == target or current_state.jug2 == target:
            path = []
            while current_state:
                path.append(current_state.action)
                current_state = current_state.parent
            return path[::-1]

        # Fill jug1
        if current_state.jug1 < capacity1:
            heapq.heappush(
                open_list,
                State(capacity1, current_state.jug2, current_state, "Fill jug1 completely")
            )

        # Fill jug2
        if current_state.jug2 < capacity2:
            heapq.heappush(
                open_list,
                State(current_state.jug1, capacity2, current_state, "Fill jug2 completely")
            )

        # Empty jug1
        if current_state.jug1 > 0:
            heapq.heappush(
                open_list,
                State(0, current_state.jug2, current_state, "Empty jug1")
            )

        # Empty jug2
        if current_state.jug2 > 0:
            heapq.heappush(
                open_list,
                State(current_state.jug1, 0, current_state, "Empty jug2")
            )

        # Pour jug1 → jug2
        if current_state.jug1 > 0 and current_state.jug2 < capacity2:
            pour_amount = min(current_state.jug1, capacity2 - current_state.jug2)
            heapq.heappush(
                open_list,
                State(
                    current_state.jug1 - pour_amount,
                    current_state.jug2 + pour_amount,
                    current_state,
                    f"Pour jug1 to jug2 ({pour_amount}L)"
                )
            )

        # Pour jug2 → jug1
        if current_state.jug2 > 0 and current_state.jug1 < capacity1:
            pour_amount = min(current_state.jug2, capacity1 - current_state.jug1)
            heapq.heappush(
                open_list,
                State(
                    current_state.jug1 + pour_amount,
                    current_state.jug2 - pour_amount,
                    current_state,
                    f"Pour jug2 to jug1 ({pour_amount}L)"
                )
            )

    return None


def main():
    global target
    capacity1 = 4
    capacity2 = 3
    target = 2

    solution = solve_water_jug_problem(capacity1, capacity2, target)

    if solution:
        print(f"Solution found in {len(solution) - 1} steps:")
        for step, action in enumerate(solution, 1):
            print(f"Step {step}: {action}")
    else:
        print("No solution found")


if __name__ == "__main__":
    main()
