'''
Created on 29 nov. 2010

@author: Terranca
'''
import unittest

from cell import Cell

class CellTest(unittest.TestCase):
    """ Tests the Cell class """

    def setUp(self):
        self.cell = Cell(1,1,1)
        self.cell2 = Cell(0, 1, 2)

    def tearDown(self):
        pass


    def testCellLocation(self):
        self.assertEqual(self.cell.location, (1, 1, 1))
        self.assertEqual(self.cell2.location, (0, 1, 2))
   
    def testAddNeighbor(self):       
        self.cell.add_neighbor(self.cell2)
        
        self.assertListEqual(self.cell.get_neighbors(), [self.cell2])
        
        cell3 = Cell(2,2,2)
        self.cell.add_neighbor(cell3)
        
        self.assertIn(self.cell2, self.cell.get_neighbors())
        self.assertIn(cell3, self.cell.get_neighbors())
        
        self.assertNotIn(self.cell, self.cell.get_neighbors())
        
    def testDeadNeighbors(self):
        self.cell.add_neighbor(self.cell2)
        self.cell2.state = Cell.DEAD
        
        self.assertIn(self.cell2, self.cell.get_dead_neighbors())
        self.assertEqual([], self.cell.get_alive_neighbors())
        
    def testAliveNeighbors(self):
        self.cell.add_neighbor(self.cell2)
        self.cell2.state = Cell.LIVE
        
        self.assertIn(self.cell2, self.cell.get_alive_neighbors())
        self.assertEqual([], self.cell.get_dead_neighbors())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()