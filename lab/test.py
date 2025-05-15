from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str | None = None
    signup_ts : datetime | None = None
    friends : list[int] = []
    
external_data = {
    "id": "123",
    # "name" : "bright arparwut",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}

test_user = User(**external_data)
if test_user.name is not None:
    print(test_user.name)
else:
    print("name is None!")