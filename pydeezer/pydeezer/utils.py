from datetime import datetime

DATETIME_FORMAT = "%Y-%m-%d"
EPISODE_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

explicitness_mapping = {
    0: "Not Explicit",
    1: "Explicit",
    2: "Unknown",
    3: "Edited",
    4: 'Partially Explicit (Album "lyrics" only)',
    5: 'Partially Unknown (Album "lyrics" only)',
    6: "No Advice Available",
    7: 'Partially No Advice Available (Album "lyrics" only)'
}  

def read_datetime(string: str) -> datetime:
    try:
        return datetime.strptime(string, DATETIME_FORMAT)
    except:
        return datetime.strptime(string,EPISODE_DATETIME_FORMAT)

def explicitness_from_index(index : str):
    return explicitness_mapping.get(index)