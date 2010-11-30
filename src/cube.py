'''
Created on 29 nov. 2010

@author: Terranca
'''

from cells import dead_cell
from cell import Cell

def manhattan(cell, cube):
    """ A simple neighboring algorithm that defines the cell's 
    neighbors as defined in the manhattan neighborhood
    """
    x, y, z = cell.location
    
    return filter(lambda x: x is not None, 
                  (cube.get_cell(x+1, y, z), cube.get_cell(x-1, y, z),
                   cube.get_cell(x, y+1, z), cube.get_cell(x, y-1, z),
                   cube.get_cell(x, y, z+1), cube.get_cell(x, y, z-1)))
                        
class Cube(object):
    ''' Represents a full cube
    '''
    def __init__(self, dimension, neighborhood = None):
        self.dimension = dimension
        
        # Default neighboring algorithm
        if neighborhood is None:
            neighborhood = manhattan
        
        # Initiate the cube
        self.cells = []
        for z in range(dimension):
            self.cells.append([])
            for y in range(dimension):
                self.cells[z].append([])
                for x in range(dimension):
                    self.cells[z][y].append(dead_cell.DeadCell((x, y, z),
                                                               neighborhood=lambda x: neighborhood(x, self)))                 
                        
    def foreach_cell(self, fn, *args, **kwargs):
        """ Executes fn for every cell in the cube
        
        If fn returns an instance of Cell, the cell will be replaced
        """
        for z in range(self.dimension):
            for y in range(self.dimension):
                for x in range(self.dimension):
                    val = fn(self.cells[z][y][x], *args, **kwargs)
                    if isinstance(val, Cell):
                        self.cells[z][y][x] = val
        
    def get_cells(self):
        return [x for z in self.cells for y in z for x in y]
    
    def get_cell(self, x, y, z):
        if (x >= self.dimension or y >= self.dimension or z >= self.dimension) \
            or (x < 0 or y < 0 or z < 0):
            return None
        
        return self.cells[z][y][x]
    
    def set_cell(self, location, cell):
        self.cells[location[2]][location[1]][location[0]] = cell