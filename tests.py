from main import Cell, Universe


def test_tests():
    assert True


def test_state_birth():
    cell = Cell(alive=False)
    assert cell.next_state(3) == True


def test_state_overcrowding():
    cell = Cell(alive=True)
    assert cell.next_state(4) == False


def test_state_survival():
    cell = Cell(alive=True)
    assert cell.next_state(2) == True


def test_state_stay_dead():
    cell = Cell(alive=False)
    assert cell.next_state(2) == False


def test_state_starvation():
    cell = Cell(alive=True)
    assert cell.next_state(1) == False


def test_state_old_age():
    cell = Cell(alive=True, age=50)
    assert cell.next_state_cell(3).alive == False


def test_create_universe_set_alive():
    universe = Universe(10, 10)
    universe.grid[2][1] = Cell(True)
    assert universe.grid[2][1].alive == True
    assert universe.grid[1][1].alive == False


def test_get_all_neighbours():
    universe = Universe(10, 10)
    universe.grid[1][2] = Cell(True)
    universe.grid[3][2] = Cell(True)
    assert [x.alive for x in universe.get_neighbours(2, 2)] == [False, False, False, True,
                                                                False, False, False, True]


def test_get_all_neighbours_edge():
    universe = Universe(10, 10)
    universe.grid[1][9] = Cell(True)
    universe.grid[3][9] = Cell(True)
    assert [x.alive for x in universe.get_neighbours(2, 9)] == [False, False, False, True,
                                                                False, False, False, True]


def test_tick():
    universe = Universe(10, 10)
    universe.grid[1][9] = Cell(True)
    universe.grid[3][9] = Cell(True)
    universe.tick()
    assert universe.grid[1][9].alive == False
    assert universe.grid[3][9].alive == False
