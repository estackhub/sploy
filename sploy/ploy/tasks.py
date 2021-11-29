
from sploy.sploy.api.allot import validate_files_space_limit, validate_db_space_limit

def daily():
    validate_files_space_limit()
    validate_db_space_limit()