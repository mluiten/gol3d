'''
Created on 29 nov. 2010

@author: Terranca
'''

class Cell(object):    
    """ Represents a single cell in the game of life cube
    
    Also contains links to its neighbors
    """

    LIVE = 1
    DEAD = 0

    def __init__(self, x, y, z):
        self.state = Cell.DEAD
        self.location = (x, y, z)
        self.__neighbors = []
        
    def get_neighbors(self):
        return self.__neighbors
    
    def add_neighbor(self, neighbor):
        if neighbor is not None:
            self.__neighbors.append(neighbor)
    
    def get_alive_neighbors(self):
        return [n for n in self.neighbors if n.state == Cell.LIVE]
    
    def get_dead_neighbors(self):
        return [n for n in self.neighbors if n.state == Cell.DEAD]

    neighbors = property(get_neighbors)
    neighbors_alive = property(get_alive_neighbors)