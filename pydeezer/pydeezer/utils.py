from datetime import datetime

DATETIME_FORMAT = "%Y-%m-%d"

def read_datetime(string : str) -> datetime:
    return datetime.strptime(string,DATETIME_FORMAT)