import pytest
from include.basics.employee import Employee


@pytest.fixture
def employee():
    emp = Employee("John", "Ford", 60_000)
    return emp

def test_give_default_raise(employee):
    default_raise_amount = 5000
    annual_salary_after_raise = employee.annual_salary + default_raise_amount
    employee.give_raise()
    assert annual_salary_after_raise == employee.annual_salary

def test_give_custom_raise(employee):
    custom_raise_amount = 8000
    annual_salary_after_raise = employee.annual_salary + custom_raise_amount
    employee.give_raise(custom_raise_amount)
    assert annual_salary_after_raise == employee.annual_salary
