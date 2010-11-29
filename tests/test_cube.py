'''
Created on 29 nov. 2010

@author: Terranca
'''
import unittest

from cube import Cube
from cell import Cell

class CubeTest(unittest.TestCase):
    """ Tests the Cube class """

    TEST_CUBE_DIMENSION = 3

    def setUp(self):
        self.cube = Cube(CubeTest.TEST_CUBE_DIMENSION)

    def tearDown(self):
        pass

    def testCellCount(self):
        self.assertEquals(CubeTest.TEST_CUBE_DIMENSION 
                          * CubeTest.TEST_CUBE_DIMENSION 
                          * CubeTest.TEST_CUBE_DIMENSION,
                          len(self.cube.get_cells()))

    def __awakenCell(self, cell):
        cell.state = Cell.LIVE

    def testForeachCellAndStateChange(self):
        for cell in self.cube.get_cells():
            self.assertEquals(Cell.DEAD, cell.state)
        
        self.cube.foreach_cell(self.__awakenCell)
        
        for cell in self.cube.get_cells():
            self.assertEquals(Cell.LIVE, cell.state)    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()