
from .execute_queries import execute_query
from .weather_import import get_weather_data
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

create_location_query = """
    CREATE TABLE IF NOT EXISTS locations (
        location_id SERIAL PRIMARY KEY,
        city_name VARCHAR(100) NOT NULL,
        latitude DECIMAL(9,6) NOT NULL,
        longitude DECIMAL(9,6) NOT NULL,
        timezone VARCHAR(50) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(city_name)
    );
    """

create_daily_query = """
    CREATE TABLE IF NOT EXISTS daily_weather (
        daily_id SERIAL PRIMARY KEY,
        location_id INTEGER REFERENCES locations(location_id),
        date DATE NOT NULL,
        temp_max DECIMAL(5,2) NOT NULL,
        temp_min DECIMAL(5,2) NOT NULL,
        humidity DECIMAL(5,2) NOT NULL,
        wind_speed DECIMAL(5,2) NOT NULL,
        wind_gust DECIMAL(5,2),
        wind_dir DECIMAL(5,2),
        precipitation DECIMAL(5,2) DEFAULT 0,
        uv_index DECIMAL(4,2),
        cloud_cover DECIMAL(5,2),
        dew DECIMAL(5,2),
        conditions VARCHAR(100),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(location_id, date)
    );
    """    

create_hourly_query = """
    CREATE TABLE IF NOT EXISTS hourly_weather (
        hourly_id SERIAL PRIMARY KEY,
        daily_id INTEGER REFERENCES daily_weather(daily_id),
        datetime TIMESTAMP NOT NULL,
        temp DECIMAL(5,2) NOT NULL,
        humidity DECIMAL(5,2) NOT NULL,
        wind_speed DECIMAL(5,2) NOT NULL,
        wind_gust DECIMAL(5,2),
        wind_dir DECIMAL(5,2),
        cloud_cover DECIMAL(5,2),
        conditions VARCHAR(100),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(daily_id, datetime)
    );
    """

def create_table(query):
    return execute_query(query, "created locations table")

def create_tables():
    logger.info("Starting database create tables initialization...")
    if create_table(create_location_query):
        if create_table(create_daily_query):
            if create_table(create_hourly_query):
                logger.info("Database create tables completed successfully!")
                return True
    
    logger.error("Database initialization failed!")
    return False

# if __name__ == "__main__":
#     initialize_database()

def initialize_database():
    if create_tables():
        get_weather_data()
        logger.info("successfully finish data base initialization...")

        
    