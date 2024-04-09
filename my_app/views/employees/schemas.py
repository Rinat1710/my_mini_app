

from pydantic import BaseModel,EmailStr


class EmployeeBase(BaseModel):
    full_name :str
    email : EmailStr

class EmployeeCreate(EmployeeBase):#Создание записи о соотруднике
    pass

class Employee(EmployeeBase):#Получение записи о соотруднике по id
    id : int

