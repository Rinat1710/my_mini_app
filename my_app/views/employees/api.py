from fastapi import APIRouter,HTTPException,status


from .schemas import Employee,EmployeeCreate

from . import crud

router1=APIRouter(prefix="/employees",tags=["Employees"])

@router1.post("", response_model = Employee)
def empoloyee_create(empl: EmployeeCreate):
    return crud.empoloyee_create(empl)
@router1.get("", response_model=list)#????
def get_list():
    return crud.get_list()

@router1.get("/{employee_id}",response_model=Employee,
             responses={
                 status.HTTP_404_NOT_FOUND: {
                     "description": "user not found",
                     "content": {
                         "apllication/json": {
                             "schema": {
                                 "title": "not found",
                                 "type": "object",
                                 "properties": {
                                     "detail": {
                                         "title": "Detail",
                                         "type": "string",
                                         "example": "user #123 not found",
                                     }
                                 }
                             }
                         }
                     }
                 }

             })


def get_employee_by_id(employee_id:int)->Employee | None:
    employee=crud.get_employee_by_id(employee_id=employee_id)
    if employee:
        return employee
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'user #{employee_id} not found!')


@router1.delete("/{employee_id}",status_code=status.HTTP_204_NO_CONTENT,
                responses={
                 status.HTTP_204_NO_CONTENT: {
                     "description": "user deleted",
                     "content": {
                         "apllication/json": {
                             "schema": {
                                 "title": "deleted",
                                 "type": "object",
                                 "properties": {
                                     "detail": {
                                         "title": "Detail",
                                         "type": "string",
                                         "example": "user #123 deleted",
                                     }
                                 }
                             }
                         }
                     }
                 }

             })
def delete_employee_by_id(employee_id: int):
        crud.delete_employee_by_id(employee_id=employee_id)