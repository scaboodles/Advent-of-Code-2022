class Rock:
    def __init__(self, cave, rock_chars):
        self.rock_lines = rock_chars.split("\n")
        self.y = cave.highest_point() + 3 + self.height
        self.x = 1

    def is_stopped(self):
        return self.y == self.height

    def jet(self, dir):
        match dir:
            case "<":
                self.x = max(self.x - 1, 0)
            case ">":
                self.x = min(self.x + 1, 6 - self.width)
    
    def drop(self):
        self.y -= 1 

    def settle(self,cave):
        return cave.add_occupied(self.get_occupied())
    
    def get_occupied(self):
        for x in range(self.width):
            for y in range(self.height):
                print(f"trying {x},{y} {self.width} {self.height}")
                print(f"{x},{y} {self.rock_lines[y]}")
                if self.rock_lines[y][x] == "#":
                    yield self.x + x, self.y + self.height - y


    @property
    def width(self):
        return max(map(lambda rl: len(rl), self.rock_lines))

    @property
    def height(self):
        return len(self.rock_lines)

class Cave:
    def __init__(self):
        self.grid = set()

    def highest_point(self):
        if len(self.grid):
            return max(*map(lambda pos:pos[1], self.grid))
        return 0

    def add_occupied(self, positions):
        self.grid.update(positions)

def part_1(rock_input, jets):
    rocks_chars = rock_input.rstrip().split("\n\n")
    cave = Cave()
    jet_index = 0
    for i in range(2022):
        step = i%len(rocks_chars)
        rock = Rock(cave, rocks_chars[step])
        print(f"ROCK {i}")
        print(rock.rock_lines)
        while not rock.is_stopped():
            rock.jet(jets[jet_index])
            rock.drop()
            jet_index = (jet_index + 1) % len(jets)
            
        rock.settle(cave) 

def get_rocks():
    return """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""


def get_jets():
    return ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

print(f"part 1 result: {part_1(get_rocks(), get_jets())}")
