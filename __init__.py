import copy
import os
import sys

match sys.platform:
    case 'linux':
        clear_command = 'clear'
    case 'win32':
        clear_command = 'cls'


class Grid:
    def __init__(self, width: int, height: int, default: int):
        self.width = width
        self.height = height
        self.default = default
        self.extra = dict()

        self.grid = {(x + 1, y + 1): self.default for x in range(self.width) for y in range(self.height)}

    def setCell(self, item_pos_tuple, value):
        self.grid[item_pos_tuple] = value

    def setCells(self, items_pos_value_dict):
        for i in items_pos_value_dict:
            self.grid[i] = items_pos_value_dict[i]

    def getGrid(self):
        return self.grid

    def getExtra(self, key=None):
        if key is None:
            return self.extra
        else:
            return self.extra[key]

    def setExtra(self, key, value):
        self.extra[key] = value

    def getCell(self, item_pos_tuple):
        return self.grid[item_pos_tuple]

    def copyGrid(self):
        return copy.copy(self.grid)

    def displayCells(self, cell_character_dict: dict, show_row: bool = False, show_column: bool = False):
        line = ''
        line_count = 0
        if show_row:
            screen = '0|'
            line_count = 1
        else:
            screen = ''
        num = 1
        if show_column:
            for i in range(self.width):
                if num >= 10:
                    num = 0
                screen += str(num) + ' '
                num += 1

        for cell in self.grid.values():
            for value in cell_character_dict.keys():
                if cell == value:
                    line += cell_character_dict[value] + ' '

            if (len(line) / 2) % self.width == 0:
                if show_row:
                    if line_count >= 10:
                        line_count = 0
                    screen += ' \n' + str(line_count) + '|' + line
                    line_count += 1
                else:
                    screen += ' \n' + line
                line = ''

        os.system(clear_command)
        print(f'{screen}\n')

    def getNeighbors(self, item_pos_tuple: tuple, immediate: bool = False):
        pos = item_pos_tuple
        nw, n, ne, w, e, sw, s, se = None, None, None, None, None, None, None, None

        if pos[0] != 1:
            if pos[1] != 1:
                nw = self.grid[(pos[0]-1, pos[1]-1)]
            n = self.grid[(pos[0]-1, pos[1])]
            if pos[1] != self.width:
                ne = self.grid[(pos[0]-1, pos[1] + 1)]

        if pos[1] != 1:
            w = self.grid[(pos[0], pos[1]-1)]

        if pos[1] != self.width:
            e = self.grid[(pos[0], pos[1]+1)]

        if pos[0] != self.height:
            s = self.grid[(pos[0]+1, pos[1])]
            if pos[1] != 1:
                sw = self.grid[(pos[0] + 1, pos[1] - 1)]
            if pos[1] != self.width:
                se = self.grid[(pos[0]+1, pos[1]+1)]

        if not immediate:
            slot_neighbors = {
                'NW': nw, 'N': n, 'NE': ne,
                'W': w, 'E': e,
                'SW': sw, 'S': s, 'SE': se,
            }
        else:
            slot_neighbors = {'N': n, 'W': w, 'E': e, 'S': s}
        return slot_neighbors
