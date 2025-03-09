from employee import Employee
import pytest

# 11-3
@pytest.fixture
def employee():
    employee = Employee('john', 50000)
    return employee

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.name == 'john'
    assert employee.salary == 55000

def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.name == 'john'
    assert employee.salary == 60000