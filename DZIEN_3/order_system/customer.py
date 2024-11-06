from dataclasses import dataclass, field
from typing import List
import datetime

@dataclass
class Customer:
    first_name: str
    last_name: str
    email: str

    def full_name(self)->str:
        return f"{self.first_name} {self.last_name}"
