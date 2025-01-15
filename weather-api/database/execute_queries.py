from .db_connection import get_connection
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def execute_query(query, description):

    connection = get_connection()
    if not connection:
        logger.error("Failed to establish database connection.")
        return False

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        logger.info(f"Successfully {description}")
        return True

    except Exception as e:
        logger.error(f"Error {description}: {e}")
        connection.rollback()
        return False

    finally:
        cursor.close()
        connection.close()



