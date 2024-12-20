import dataclasses
import re

@dataclasses.dataclass
class EnvironmentParameters:
    directory: str
    patterns2Search: list[re.Pattern]