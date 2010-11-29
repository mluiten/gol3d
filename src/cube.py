'''
Created on 29 nov. 2010

@author: Terranca
'''

from cell import Cell

from random import random

def manhattan(cell, cube):
    """ A simple neighboring algorithm that defines the cell's 
    neighbors as defined in the manhattan neighborhood
    """
    x, y, z = cell.location
    
    cell.add_neighbor(cube.get_cell(x+1, y, z))
    cell.add_neighbor(cube.get_cell(x-1, y, z))
    cell.add_neighbor(cube.get_cell(x, y+1, z))
    cell.add_neighbor(cube.get_cell(x, y-1, z))
    cell.add_neighbor(cube.get_cell(x, y, z+1))
    cell.add_neighbor(cube.get_cell(x, y, z-1))

def random_alive(cell):
    if random() > 0.8:
        cell.state = Cell.LIVE
                        
class Cube(object):
    ''' Represents a full cube
    '''
    dimension = 7

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
                    self.cells[z][y].append(Cell(x=x, y=y, z=z))
       
        # Provide cells with their neighbors
        self.foreach_cell(neighborhood, cube=self)                    
                        
    def foreach_cell(self, fn, *args, **kwargs):
        for z in range(self.dimension):
            for y in range(self.dimension):
                for x in range(self.dimension):
                    fn(self.cells[z][y][x], *args, **kwargs)
        
    def get_cells(self):
        return [x for z in self.cells for y in z for x in y]
    
    def get_cell(self, x, y, z):
        if x >= self.dimension or y >= self.dimension or z >= self.dimension:
            return None
        
        return self.cells[z][y][x]