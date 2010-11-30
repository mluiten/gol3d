'''
Created on 30 nov. 2010

@author: Terranca
'''

from cell import Cell

from random import randrange

class DeadCell(Cell):
    """ A cell that is currently dead """
    
    COLOR = (0, 0, 0)
    
    def __str__(self):
        return 'dead at %s' % str(self.location)

    def tick(self):
        """ Determine if the cell is revived """
        num_alive = len(self.get_alive_neighbors())     
        
        # If the cell comes to life, determine the type by inspecting the 
        # neighbors who are alive
        if(num_alive == 3):
            self = type(self.get_alive_neighbors()[randrange(num_alive)])(copy=self)
            
        return self