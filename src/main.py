'''
Created on 29 nov. 2010

@author: Terranca
'''

from cube import Cube
from cells import red_cell

from random import random

def random_red(cell):
    if random() > 0.8:
        cell = red_cell.RedCell(copy=cell)
    return cell

def update(cube):
    """ Progress the cube one time-tick
    """    
    for cell in cube.get_cells():
        cube.set_cell(cell.location, cell.tick())

def get_colors(cube):
    for cell in cube.get_cells():
        print cell.COLOR

if __name__ == '__main__':
    cube = Cube(7)
    cube.foreach_cell(random_red)
    #update(cube)
    get_colors(cube)
    print 'Number of cells: %d' % len(cube.get_cells())