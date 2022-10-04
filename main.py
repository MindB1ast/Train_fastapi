from fastapi import FastAPI, Query
from pydantic import BaseModel
import functions
from typing import List, Union
import squate


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class Equation_variables(BaseModel):
    A: float
    B: float
    C: float
    Is_complex: bool


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.get("/")
def root():
    return {"message": "Hello, World!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/functions/antistr/")
def get_antistr(string: str):
    return {"answer": functions.antistr(string)}


@app.get("/functions/sum")
def get_sum(array: List[Union[int, float]] = Query(None)):
    return {"answer": functions.sum(array)}


@app.get("/functions/triangle/")
def get_triangle(high: int):
    return {"answer": functions.triangle(high)}


@app.get("/functions/counter/")
def get_counter(string: str):
    return {"answer": functions.counter(string)}


@app.get("/functions/tokamel/")
def get_tokamel(string: str):
    return {"answer": functions.tokamel(string)}


@app.get("/functions/convert/")
def get_convert(number: int):
    return {"answer": functions.convert(number)}


@app.get("/functions/sorta/")
def get_sorta(to_sort: List[int] = Query(None)):
    return {"answer": functions.sorta(to_sort)}


@app.post("/equation/")
def get_square(args: Equation_variables):
    x1, x2 = squate.solve_complex(args.A, args.B, args.C) if args.Is_complex else squate.solve(args.A, args.B, args.C)
    if x1 is None:
        return {"answer": "Error"}
    else:
        if x1 == x2:
            return {"x1==x2": str(complex(x1).real)+str(complex(x1).imag)}
        else:
            return {"x1": str(complex(x1).real)+str(complex(x1).imag)+"i", "x2": str(complex(x2).real)+str(complex(x2).imag)+"i"}
