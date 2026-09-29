
from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Session, select

from database import create_db_and_tables, get_session
from models import Item, ItemCreate


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="College Lost & Found API",
    description="API to report and manage lost and found items",
    version="1.0.0",
    lifespan=lifespan
)



@app.post("/items", response_model=Item, status_code=201)
def create_item(
    item: ItemCreate,
    session: Annotated[Session, Depends(get_session)]
):
    db_item = Item(**item.model_dump())

    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


# GET API - Retrieve all items
@app.get("/items", response_model=list[Item])
def get_items(
    session: Annotated[Session, Depends(get_session)]
):
    items = session.exec(select(Item)).all()
    return items


# GET API - Retrieve item by ID
@app.get("/items/{item_id}", response_model=Item)
def get_item(
    item_id: int,
    session: Annotated[Session, Depends(get_session)]
):
    item = session.get(Item, item_id)

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return item


# PUT API - Update an existing item
@app.put("/items/{item_id}", response_model=Item)
def update_item(
    item_id: int,
    updated_item: ItemCreate,
    session: Annotated[Session, Depends(get_session)]
):
    item = session.get(Item, item_id)

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    item_data = updated_item.model_dump(exclude={"id"})

    for key, value in item_data.items():
        setattr(item, key, value)

    session.add(item)
    session.commit()
    session.refresh(item)

    return item


# DELETE API - Delete an item
@app.delete("/items/{item_id}")
def delete_item(
    item_id: int,
    session: Annotated[Session, Depends(get_session)]
):
    item = session.get(Item, item_id)

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    session.delete(item)
    session.commit()

    return {"message": "Item deleted successfully"}


# GET API - Filter items by status
@app.get("/items/status/{status}", response_model=list[Item])
def get_items_by_status(
    status: str,
    session: Annotated[Session, Depends(get_session)]
):
    allowed_statuses = ["Lost", "Found", "Returned"]

    if status not in allowed_statuses:
        raise HTTPException(
            status_code=400,
            detail="Status must be Lost, Found, or Returned"
        )

    items = session.exec(
        select(Item).where(Item.status == status)
    ).all()

    return items


# GET API - Filter items by category
@app.get("/items/category/{category}", response_model=list[Item])
def get_items_by_category(
    category: str,
    session: Annotated[Session, Depends(get_session)]
):
    items = session.exec(
        select(Item).where(Item.category == category)
    ).all()

    return items