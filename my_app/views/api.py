from fastapi import APIRouter
from fastapi import APIRouter,HTTPException,status

from .employees.schemas import Employee,EmployeeCreate

from .employees.crud import delete_employee_by_id

router=APIRouter(prefix="/api",tags=["YUU"])

