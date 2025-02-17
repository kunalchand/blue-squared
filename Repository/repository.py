from abc import ABC, abstractmethod
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from log.log_config import setup_logger
from Config.config import get_db_url

logger = setup_logger("Repository")

# Repository Interface (Abstract Base Class)
class RepositoryInterface(ABC):
    @abstractmethod
    def get_record(self, model_class, record_id):
        pass

# Base Repository class providing common functionality for database connection
class BaseRepository(RepositoryInterface):
    def __init__(self):
        # Dynamically get the DB URL by calling get_db_url()
        db_url = get_db_url()
        self.engine = create_engine(db_url)
        self.session = sessionmaker(bind=self.engine)()

        logger.info("Database connection established.")

    def get_record(self, model_class, record_id):
        # Fetch record using the model class and record ID
        logger.info(f"Fetching record with ID {record_id} from {model_class.__name__}.")
        record = self.session.query(model_class).filter(model_class.id == record_id).first()
        return record

# DatabaseRepository class for handling specific operations for different tables
class DatabaseRepository(BaseRepository):
    def __init__(self):
        super().__init__()  # Call the constructor of BaseRepository
        logger.info("DatabaseRepository initialized.")

    def get_record_from_table1(self, record_id):
        # Fetch record from table1 (Person)
        from Model.models import Person  # Import the Person model
        return self.get_record(Person, record_id)

    def get_record_from_table2(self, record_id):
        # Fetch record from table2 (Person2)
        from Model.models import Person2  # Import the Person2 model
        return self.get_record(Person2, record_id)
