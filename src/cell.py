'''
Created on 29 nov. 2010

@author: Terranca
'''

class Cell(object):    
    """ Represents a single cell in the game of life cube
    
    Also contains links to its neighbors
    """
    
    COLOR = (255, 255, 255)
    
    def __new__(cls, *args, **kwargs):
        if cls == Cell:
            raise TypeError("Can't initiate Cell directly")
        else:
            return object.__new__(cls, *args, **kwargs)

    def __init__(self, location=None, copy=None, neighborhood=None):
        if copy:
            self.location = copy.location
            self.neighborhood = copy.neighborhood
        elif location:
            self.location = location
        else:
            raise ValueError('At least one of location/copy needs to be provided')
        
        if neighborhood:
            self.neighborhood = neighborhood
        
    def get_neighbors(self):
        return self.neighborhood(self)
    
    def get_alive_neighbors(self):
        return [n for n in self.neighbors if str(n).startswith('alive')]
    
    def get_dead_neighbors(self):
        return [n for n in self.neighbors if str(n).startswith('dead')]
    
    def tick(self):
        pass
    
    def factory(self, cell):
        from cells.dead_cell import DeadCell
        from cells.red_cell import RedCell
        
        values = {'dead': DeadCell,
                  'red': RedCell}
        
        return values.get(cell)(copy=self)
        

    neighbors = property(get_neighbors)
    neighbors_alive = property(get_alive_neighbors)