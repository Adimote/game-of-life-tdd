import random

MAX_AGE = 10


class Cell:
    def __init__(self, alive=False, age=0):
        self.alive = alive
        self.age = age
        self.max_age = random.randint(0, 100)

    def next_state(self, number_of_alive_neighbours: int):
        if number_of_alive_neighbours > 1:
            print(number_of_alive_neighbours)
        if self.age > self.max_age:
            return False
        if number_of_alive_neighbours < 2:
            return False
        elif number_of_alive_neighbours > 3:
            return False
        elif number_of_alive_neighbours == 3:
            return True
        else:  # number_of_alive_neighbours == 2
            return self.alive

    def next_state_cell(self, number_of_alive_neighbours):
        alive = self.next_state(number_of_alive_neighbours)
        if alive:
            age = self.age + 1
        else:
            age = 0
        return Cell(alive=alive, age=age)

    def __repr__(self):
        return str(self.alive)


class Universe:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self.gen_grid(width, height)

    def gen_grid(self, width, height):
        grid = []
        for row in range(height):
            new_row = []
            for col in range(width):
                new_row.append(Cell())
            grid.append(new_row)
        return grid

    def get_grid_pos(self, x, y):
        if x > self.width - 1 or y > self.height-1 or x < 0 or y < 0:
            return Cell()
        return self.grid[x % self.width][y % self.height]

    def get_neighbours(self, x, y):
        return [
            self.get_grid_pos(x - 1, y - 1),
            self.get_grid_pos(x, y - 1),
            self.get_grid_pos(x + 1, y - 1),
            self.get_grid_pos(x + 1, y),
            self.get_grid_pos(x + 1, y + 1),
            self.get_grid_pos(x, y + 1),
            self.get_grid_pos(x - 1, y + 1),
            self.get_grid_pos(x - 1, y),
        ]

    def tick(self):
        new_grid = self.gen_grid(self.width, self.height)
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                neighbours = self.get_neighbours(x, y)
                new_grid[x][y] = cell.next_state_cell(
                    len([x for x in neighbours if x.alive]))

        for row in self.grid:
            print(row)

        self.grid = new_grid

if __name__ == "__main__":
    universe = Universe(10,10)
    universe.grid[1][2] = Cell(True)
    universe.grid[2][1] = Cell(True)
    universe.grid[3][2] = Cell(True)
    universe.tick()
    print("")
    universe.tick()
