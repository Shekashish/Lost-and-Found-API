
from sqlmodel import Session, SQLModel, create_engine

# SQLite database URL
sqlite_url = "sqlite:///lost_found.db"

# Create database engine
engine = create_engine(
    sqlite_url,
    echo=True,
    connect_args={"check_same_thread": False}
)

# Create database tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Create a database session
def get_session():
    with Session(engine) as session:
        yield session