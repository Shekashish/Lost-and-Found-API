# Lost and Found API

A REST API built using FastAPI, SQLModel, and SQLite
to manage lost and found items.

## Features

- Create a new item
- View all items
- View an item by ID
- Update an item
- Delete an item
- Filter items by status
- Filter items by category
- Input validation and error handling

## Technologies Used

- Python
- FastAPI
- SQLModel
- SQLite
- Uvicorn

## Setup Instructions

1. Clone this repository.
2. Create a virtual environment:

   python -m venv venv

3. Activate it on Windows:

   .\venv\Scripts\Activate.ps1

4. Install dependencies:

   pip install -r requirements.txt

5. Run the application:

   python -m uvicorn main:app --reload

6. Open the API documentation:

   http://127.0.0.1:8000/docs

The SQLite database is created automatically when the
application starts.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /items | Create an item |
| GET | /items | Get all items |
| GET | /items/{item_id} | Get item by ID |
| PUT | /items/{item_id} | Update an item |
| DELETE | /items/{item_id} | Delete an item |
| GET | /items/status/{status} | Filter by status |
| GET | /items/category/{category} | Filter by category |

## Screenshots

API testing screenshots are available in the
`screenshots` folder.