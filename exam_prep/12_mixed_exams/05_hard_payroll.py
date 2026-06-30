"""
MIXED EXAMS - HARD: Employee Payroll System
Hint: combine records + files + arithmetic + subprograms

An employee is a dict: {"id": int, "name": str, "hours": float, "rate": float}

Write functions:
  1. calc_salary(employee) — returns hours * rate
  2. add_employee(employees, emp) — appends to list, returns it
  3. total_payroll(employees) — sum of all salaries
  4. highest_paid(employees) — returns employee with highest salary
  5. save_payroll(employees, filename) — writes each employee to CSV
     in format: id,name,hours,rate,salary
  6. load_payroll(filename) — reads CSV back into list of employee dicts
     (including the computed salary)

Examples:
  emp1 = {"id": 1, "name": "Ali", "hours": 40, "rate": 15}
  calc_salary(emp1) -> 600
"""

def calc_salary(emp):
    pass

def add_employee(employees, emp):
    pass

def total_payroll(employees):
    pass

def highest_paid(employees):
    pass

def save_payroll(employees, filename):
    pass

def load_payroll(filename):
    pass


if __name__ == "__main__":
    import os
    emp1 = {"id": 1, "name": "Ali", "hours": 40, "rate": 15}
    emp2 = {"id": 2, "name": "Sara", "hours": 35, "rate": 20}
    
    assert calc_salary(emp1) == 600
    assert calc_salary(emp2) == 700
    
    employees = []
    add_employee(employees, emp1)
    add_employee(employees, emp2)
    assert len(employees) == 2
    
    assert total_payroll(employees) == 1300
    assert highest_paid(employees)["name"] == "Sara"
    
    fname = "_test_payroll.csv"
    save_payroll(employees, fname)
    loaded = load_payroll(fname)
    assert len(loaded) == 2
    assert loaded[0]["salary"] == 600
    assert loaded[1]["salary"] == 700
    os.remove(fname)
    print("All tests passed!")
