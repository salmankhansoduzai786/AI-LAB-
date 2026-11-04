class ClassroomAgent:
    """Stateful smart-classroom controller."""

    def __init__(self):
        self.previous_mode = None

    def act(self, temp, occupied):

        # Occupancy has priority
        if not occupied:
            target_mode = "ECO"

        elif temp > 26:
            target_mode = "COOL"

        elif temp < 20:
            target_mode = "WARM"

        else:
            target_mode = "IDLE"

        # Check whether command is repeated
        send_command = target_mode != self.previous_mode

        previous_mode = self.previous_mode

        # Remember the new target mode
        self.previous_mode = target_mode

        return previous_mode, target_mode, send_command


# Main program
if __name__ == "__main__":

    agent = ClassroomAgent()

    percepts = [
        (29, True),
        (29, True),
        (20, True),
        (26, True),
        (19, True),
        (29, False)
    ]

    print("Step | Previous | Percept       | Target | Action")
    print("-" * 58)

    for step, (temp, occupied) in enumerate(percepts, 1):

        previous, target, send = agent.act(temp, occupied)

        action = "SEND COMMAND" if send else "NO COMMAND"

        print(
            f"{step:>4} | {str(previous):<8} | "
            f"({temp:>2}, {str(occupied):<5}) | "
            f"{target:<6} | {action}"
        )