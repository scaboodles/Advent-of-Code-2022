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
    
    def try_drop(self, cave):
        would_be_occupied = self.get_occupied(self.y - 1)
        if cave.overlaps(would_be_occupied):
            return False
        else:
            self.y -= 1
            return True

    def settle(self,cave):
        return cave.add_occupied(self.get_occupied(self.y))
    
    def get_occupied(self, abs_y):
        for x in range(self.width):
            for y in range(self.height):
                if self.rock_lines[y][x] == "#":
                    yield self.x + x, abs_y + self.height - y


    @property
    def width(self):
        return max(map(lambda rl: len(rl), self.rock_lines))

    @property
    def height(self):
        return len(self.rock_lines)

class Cave:
    def __init__(self):
        self.grid = set([(x,-1) for x in range(7)])
        print(self.grid)

    def highest_point(self):
        if len(self.grid):
            return 1 + max(*map(lambda pos:pos[1], self.grid))

    def add_occupied(self, positions):
        self.grid.update(positions)

    def overlaps(self, positions):
        return self.grid.intersection(set(positions))

    def print_cave(self):
        for y in range(self.highest_point(), -1, -1):
            line = ""
            for x in range(7):
                line += "#" if self.has((x,y)) else " "
            # print(line)
                
    def has(self, item):
        return item in self.grid

def part_1(rock_input, jets):
    rocks_chars = rock_input.rstrip().split("\n\n")
    cave = Cave()
    jet_index = 0
    for i in range(2022):
    # for i in range(1):
        step = i%len(rocks_chars)
        rock = Rock(cave, rocks_chars[step])
        while True:
            rock.jet(jets[jet_index])
            jet_index = (jet_index + 1) % len(jets)
            if not rock.try_drop(cave):
                break
            
        rock.settle(cave) 
        # print("~~~~~~~~~~~~~")
        # cave.print_cave()
    return cave.highest_point()

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
