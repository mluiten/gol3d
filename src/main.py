'''
Created on 29 nov. 2010

@author: Terranca
'''

from cube import Cube

def update(cube):
    """ Progress the cube one time-tick
    """
    cells = cube.get_cells()
    
    for cell in cells:
        if len(cell.get_alive_neighbors()) > 2:
            print "%s has more than two alive neighbor" % str(cell.location)
        elif len(cell.get_alive_neighbors()) == 0:
            print "%s is all alone :-(" % str(cell.location)

if __name__ == '__main__':
    cube = Cube(3)
    update(cube)
    pass