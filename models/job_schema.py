from pydantic import BaseModel
from typing import List, Optional


class Job(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    responsibilities: List[str] = []
    requirements: List[str] = []
    skills: List[str] = []