from fastapi import FastAPI


from views.api import router

from  views.employees.api import router1


app=FastAPI()

app.include_router(router)
app.include_router(router1)

