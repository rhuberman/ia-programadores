from fastapi import FastAPI
from typing import List

app = FastAPI(    title="Api IA para Programadores",
    description="API IA para Programadores",
    version="1.0.0",
    contact={
        "name": "Ricardo Huberman",
        "url": "https://tu-sitio-web.com",
        "email": "ricardo.huberman@camuzzigas.com.ar",
    },)

def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

@app.post("/bubble_sort")
def sort_numbers(numbers: List[int]) -> List[int]:
    sorted_numbers = bubble_sort(numbers)
    return sorted_numbers

# Para ejecutar la aplicación, usa el siguiente comando en la terminal:
# uvicorn nombre_del_archivo:app --reload