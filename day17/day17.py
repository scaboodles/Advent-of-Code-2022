class Rock:
    def __init__(self, cave, rock_chars):
        self.rock_lines = rock_chars.split("\n")
        self.y = cave.highest_point() + 2 + self.height
        self.x = 2

    def is_stopped(self):
        return self.y == self.height

    def try_jet(self, dir, cave):
        x = self.x
        match dir:
            case "<":
                x = max(x - 1, 0)
            case ">":
                x = min(x + 1, 7 - self.width)
        would_be_occupied = self.get_occupied(x, self.y)

        if not cave.overlaps(would_be_occupied):
            self.x = x
    

    def try_drop(self, cave):
        would_be_occupied = self.get_occupied(self.x, self.y - 1)
        if cave.overlaps(would_be_occupied):
            return False
        else:
            self.y -= 1
            return True

    def settle(self,cave):
        return cave.add_occupied(self.get_occupied(self.x, self.y))
    
    def get_occupied(self, abs_x, abs_y):
        for x in range(self.width):
            for y in range(self.height):
                if self.rock_lines[y][x] == "#":
                    yield abs_x + x, abs_y - y

    @property
    def width(self):
        return max(map(lambda rl: len(rl), self.rock_lines))

    @property
    def height(self):
        return len(self.rock_lines)

class Cave:
    def __init__(self):
        self.grid = set([(x,-1) for x in range(7)])

    def highest_point(self):
        highest = 1+max(*map(lambda pos:pos[1], self.grid))
        return highest

    def add_occupied(self, positions):
        self.grid.update(positions)
        maxes = [-1 for i in range(7)]
        for x,y in self.grid:
            if maxes[x] < y:
                maxes[x] = y 
        min_height = min(*maxes)
        self.grid = set(filter(lambda pos:pos[1]>=min_height, self.grid))


    def overlaps(self, positions):
        return self.grid.intersection(set(positions))

    def print_cave(self):
        for y in range(self.highest_point(), -1, -1):
            line = ""
            for x in range(7):
                line += "#" if self.has((x,y)) else " "
            print(line)
                
    def has(self, item):
        return item in self.grid

def print_rock_frame(cave, rock):
    for y in range(cave.highest_point() + 2 + rock.height, -1, -1):
        line = ""
        for x in range(7):
            if (x,y) in rock.get_occupied(rock.x, rock.y):
                line+="@"
            elif cave.has((x,y)):
                line+="#"
            else:
                line+="."
        print(line)

    
def part_1(rock_input, jets):
    rocks_chars = rock_input.rstrip().split("\n\n")
    cave = Cave()
    jet_index = 0
    for i in range(1000000000000):
        if i % 1000 == 0:
            print(i)
            print(len(cave.grid))
    # for i in range(4):
        step = i%len(rocks_chars)
        rock = Rock(cave, rocks_chars[step])
        while True:
            # print_rock_frame(cave, rock)
            # print("~~~~~~~~~~~~~")
            rock.try_jet(jets[jet_index], cave)
            jet_index = (jet_index + 1) % len(jets)
            if not rock.try_drop(cave):
                break
        # print_rock_frame(cave, rock)
        # print("~~~~~~~~~~~~~")
            
        rock.settle(cave) 
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
    file = open("./input.txt", "r").read().rstrip()
    return file

print(f"part 1 result: {part_1(get_rocks(), get_jets())}")
