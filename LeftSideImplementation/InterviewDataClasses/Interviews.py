from dataclasses import dataclass
from typing import Dict
from .Interview import Interview

@dataclass
class Interviews:
    interviews: Dict[str, Interview]