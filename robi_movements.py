import random


class Robi:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.directions = ['T', 'R', 'B', 'L']
        self.direction_index = 0
        self.bonus_x = random.randint(-100, 100)
        self.bonus_y = random.randint(-100, 100)
        self.passed_bonus = False

    def move(self, command):
        for instruction in command:
            if instruction == 'L':
                self.turn_left()
            elif instruction == 'R':
                self.turn_right()
            elif instruction == 'F':
                self.walk()

    def turn_left(self):
        self.direction_index -= 1
        if self.direction_index < 0:
            self.direction_index = len(self.directions) - 1

    def turn_right(self):
        self.direction_index += 1
        if self.direction_index >= len(self.directions):
            self.direction_index = 0

    def walk(self):
        dx, dy = {'T': (0, 1), 'B': (0, -1), 'L': (-1, 0), 'R': (1, 0)}[self.directions[self.direction_index]]
        self.x += dx
        self.y += dy
        if not self.passed_bonus and (self.x, self.y) == (self.bonus_x, self.bonus_y):
            self.passed_bonus = True
