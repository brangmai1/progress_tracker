from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Integer, Column, Boolean
from connect_database import get_engine
from tables import set_tables
from insert_data import set_data

Base = declarative_base()

class SetupStatus(Base):
    __tablename__ = "setup_status"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    setup_completed = Column(Boolean, default=False)

engine = get_engine()
Base.metadata.create_all(engine)

def setup_table_data(session):
    status = session.query(SetupStatus).filter_by(name = "initial_setup").first()
    if status:
        print("Initial data setup completed.")
        return 
    # Set up tables and data to mysql
    print("Setting up tables and data........")
    set_tables(session)
    set_data(session)
    setup_status = SetupStatus(name="initial_setup", setup_completed=True)
    session.add(setup_status)
    session.commit()
    

    


