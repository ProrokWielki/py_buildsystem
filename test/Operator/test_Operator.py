import unittest
from lib.Operator.Operator import Operator
 
class TestOperator(unittest.TestCase):
    def setUp(self):
        pass    
    
    def tearDown(self):
        #unittest.TestCase.tearDown(self)
        pass
    
    def add(self, a, b):
        return a+b
    
    def substruct_two(self, a):
        return a - 2
    
    def test_empty_constructor(self):
        self.operator = Operator()
        
        self.assertEqual(self.operator.function, 0)        
        
    def test_parametric_constructor(self):
        self.operator = Operator(self.add)
        
        self.assertEqual(self.operator.function, self.add)
        
    def test_set_function(self):
        self.operator = Operator()
        
        self.operator.set_function(self.add)
        
        self.assertEqual(self.operator.function, self.add)
        
    def test_perform(self):
        self.operator = Operator(self.add)
        
        self.assertEqual(self.operator.perform(2, 3), 5)
        
        
        self.operator.set_function(self.substruct_two)
        
        self.assertEqual(self.operator.perform(5), 3)
                
        
        