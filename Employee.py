import unittest

from employee_management_system import Employee, EmployeeManager

 
class TestEmployeeManager(unittest.TestCase):

    def test_add_employee_with_valid_data(self):
        manager = EmployeeManager()
        employee = Employee("Lojain Alqadi", 27, 1, "I.T")
        result = manager.add_employee(employee)
        self.assertEqual(result, "Employee added successfully")
        
    def add_employee_with_Not_valid_data(self):
        manager = EmployeeManager()
        employee = Employee("Lojain Alqadi")
        result = manager._is_valid_employee(employee)
        self.assertEqual(result, "Employee added successfully")
        
    def test_delete_employee(self):
        system = EmployeeManager()
        employee = system.delete_employee(1)
        self.assertIsNotNone(employee)


if __name__ == '__main__':
    unittest.main()
        
    
        
        

