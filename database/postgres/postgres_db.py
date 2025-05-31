from sqlmodel import create_engine, Session, SQLModel
import os
import sys
from dotenv import load_dotenv
from utils.context import DEBUG
from typing import Optional, Callable, Generator, Any

load_dotenv()

POSTGRES_URL = None 

# os.getenv("POSTGRES_URL")

<<<<<<< HEAD
# Create SQLModel engine
if POSTGRES_URL is not None:  engine = create_engine(POSTGRES_URL, echo=False)
# else: sys.exit("Could not get postgres url from env variables")
else: pass
=======
if DEBUG < 2:
  # Create SQLModel engine
  if POSTGRES_URL is not None:  engine = create_engine(POSTGRES_URL, echo=False)
  else: sys.exit("Could not get postgres url from env variables")

>>>>>>> bbf4b069bc6bd329a35bf1719b5aca9e90e60d40

# Dependency to get DB session
def get_db() -> Any:
    with Session(engine) as session: yield session


# Function to create all tables
def create_db_and_tables() -> None: SQLModel.metadata.create_all(engine)


# Generate postgres db engine
def gen_db(db_gen:Callable[..., Generator[Session, Any, None]] = get_db) -> Optional[Session]:
  for l in db_gen():
    if isinstance(l, Session): return l
  return None
