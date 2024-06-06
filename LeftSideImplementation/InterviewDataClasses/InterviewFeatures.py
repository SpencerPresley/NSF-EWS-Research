from dataclasses import dataclass
from typing import List

@dataclass
class InterviewFeatures:
    likes: List[str]
    dislikes: List[str]
    wants_primary: List[str]
    wants_secondary: List[str]
    wants_tertiary: List[str]