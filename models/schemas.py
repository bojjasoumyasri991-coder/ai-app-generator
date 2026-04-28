from pydantic import BaseModel
from typing import List, Dict

class IntentModel(BaseModel):
    modules: List[str]
    roles: List[str]
    features: List[str]