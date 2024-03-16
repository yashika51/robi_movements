import random


class Robi:
    def __init__(self, initial_x=0, initial_y=0, initial_direction='T', bonus_x=None, bonus_y=None):
        self.x = initial_x
        self.y = initial_y
        self.direction = initial_direction
        self.bonus_x = bonus_x if bonus_x is not None else random.randint(-100, 100)
        self.bonus_y = bonus_y if bonus_y is not None else random.randint(-100, 100)
        self.passed_bonus = False

    def move(self, command):
        """ Below print statements could be used if needed to trace the whole flow of command
            print("Initial position:", self.x, self.y, self.direction)
            print("Bonus position:", self.bonus_x, self.bonus_y)
        """

        for instruction in command:
            if instruction == 'L':
                self.turn_left()
            elif instruction == 'R':
                self.turn_right()
            elif instruction == 'F':
                self.walk()

            # print("Current position:", self.x, self.y, self.direction)

            # Check if Robi has reached the bonus position
            if (self.x, self.y) == (self.bonus_x, self.bonus_y):
                self.passed_bonus = True
                break  # Exit the loop if bonus position reached

        print(self.return_result())

    def turn_left(self):
        directions = {'T': 'L', 'L': 'B', 'B': 'R', 'R': 'T'}
        self.direction = directions[self.direction]

    def turn_right(self):
        directions = {'T': 'R', 'R': 'B', 'B': 'L', 'L': 'T'}
        self.direction = directions[self.direction]

    def walk(self):
        direction_deltas = {'T': (0, 1), 'B': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
        dx, dy = direction_deltas[self.direction]
        new_x = self.x + dx
        new_y = self.y + dy

        # Check if Robi has passed the bonus position
        if not self.passed_bonus and (new_x, new_y) == (self.bonus_x, self.bonus_y):
            self.passed_bonus = True
        else:
            self.x = new_x
            self.y = new_y

    def return_result(self):
        passed_bonus_value = 1 if self.passed_bonus else 0
        result = f"Result: X:{self.x}; Y:{self.y}; D:{self.direction}; B:{passed_bonus_value}"
        return result
