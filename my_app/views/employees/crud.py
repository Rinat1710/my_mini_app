
from fastapi import HTTPException,status
from .schemas import EmployeeCreate,Employee
from pydantic import BaseModel
class EmployeeStorage(BaseModel):#Схема хранилища записей о соотрудниках
    last_id :int =0
    employees : dict[int,Employee] = {}

    @property
    def next_id(self):
        self.last_id+=1
        return self.last_id



employee_storage=EmployeeStorage()#Само хранилище , созданное по схеме
def empoloyee_create(empl : EmployeeCreate)-> Employee:
    employee_id = employee_storage.next_id
    employee_user = Employee(id=employee_id , **empl.dict())
    employee_storage.employees[employee_id] = employee_user
    return employee_user

def get_list()->list[Employee]:
    return list(employee_storage.employees.values())

def get_employee_by_id(employee_id:int)->Employee | None:
    employee=employee_storage.employees.get(employee_id)
    return employee

def delete_employee_by_id(employee_id:int):
    if employee_storage.employees[employee_id]:
        del employee_storage.employees[employee_id]
