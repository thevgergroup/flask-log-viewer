from app_logger.logger import configure_logger
import time
import random
import datetime

if __name__ == "__main__":
    # Example usage
    log_file_name = "tmp/foo.log"
    max_log_size = 10 * 1024 * 1024  # 10 MB
    max_backup_count = 5
    max_log_age_days = 7

    logger = configure_logger(log_file_name, max_log_size, max_backup_count, max_log_age_days)    
    while True:
        logger.info("Test log message " + str(datetime.datetime.now()))
        time.sleep(random.randint(1, 5))
