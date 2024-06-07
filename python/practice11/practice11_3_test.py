import unittest
from practice11_3 import Employee

class TestEmployee(unittest.TestCase):
    
    def test_give_default_raise(self):
        emp = Employee('John', 'Doe', 60000)
        emp.give_raise()
        self.assertEqual(emp.annual_salary, 65000)

    def test_give_custom_raise(self):
        emp = Employee('Jane', 'Smith', 70000)
        emp.give_raise(10000)
        self.assertEqual(emp.annual_salary, 80000)

if __name__ == '__main__':
    unittest.main()
