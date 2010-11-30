'''
Created on 30 nov. 2010

@author: Terranca
'''

from cell import Cell

class RedCell(Cell):
    
    COLOR = (255, 0, 0)
    
    def __str__(self):
        return 'alive and red at %s' % str(self.location)
    
    def tick(self):
        """ Determine if the cell survives or dies """
        num_alive = len(self.get_alive_neighbors())  
        
        if num_alive >= 2 and num_alive <= 4:
            return self
        else:
            return self.factory('dead')