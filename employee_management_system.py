import unittest
class Employee:
    def __init__(self, name, age, emp_id, department):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.department = department

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        if not self._is_valid_employee(employee):
            return "Invalid employee data"
        self.employees.append(employee)
        return "Employee added successfully"

    def get_employee_by_id(self, id):
        for employee in self.employees:
            if employee.id == id:
                return employee
        return None

    def delete_employee(self, id):
        for i, employee in enumerate(self.employees):
            if employee.id == id:
                del self.employees[i]
                return "Employee deleted successfully"
        return "Employee not found"

    def _is_valid_employee(self, employee):
        if not all([employee.name, employee.age, employee.emp_id, employee.department]):
            return False
        if not isinstance(employee.age, int) or employee.age < 0:
            return False
        return True


if __name__ == '__main__':
    unittest.main()