from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

data_list = [
    {"key": "Item 1", "value": "Value 1"},
    {"key": "Item 2", "value": "Value 2"},
    {"key": "Item 3", "value": "Value 3"},
]


class Item(BaseModel):
    key: str
    value: str


@app.get("/api/data")
def get_data():
    return data_list


@app.post("/api/data")
def add_data(item: Item):
    print("I made it to the backend")
    if any(d["key"] == item.key for d in data_list):
        raise HTTPException(status_code=400, detail="Item with this key already exists")
    data_list.append({"key": item.key, "value": item.value})
    return {"message": f"Added {item.key} with value {item.value}"}
