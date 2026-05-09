from pydantic import BaseModel
from typing import List, Optional


class Experience(BaseModel):
    company: Optional[str] = None
    role: Optional[str] = None
    duration: Optional[str] = None
    description: Optional[str] = None


class Education(BaseModel):
    institution: Optional[str] = None
    degree: Optional[str] = None
    year: Optional[str] = None


class Resume(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    skills: List[str] = []
    experience: List[Experience] = []
    education: List[Education] = []