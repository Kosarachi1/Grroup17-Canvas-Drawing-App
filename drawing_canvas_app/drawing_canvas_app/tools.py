from dataclasses import dataclass
from typing import List, Tuple

class Tool:
    FREEHAND = 'freehand'
    LINE = 'line'
    RECT = 'rect'

@dataclass
class FreehandCmd:
    points: List[Tuple[int, int]]
    color: str
    width: int = 2

    def to_dict(self):
        return {'type': 'freehand', 'points': self.points,
                'color': self.color, 'width': self.width}

@dataclass
class LineCmd:
    xy: Tuple[int, int, int, int]
    color: str
    width: int = 2

    def to_dict(self):
        return {'type': 'line', 'xy': self.xy,
                'color': self.color, 'width': self.width}

@dataclass
class RectCmd:
    xy: Tuple[int, int, int, int]
    outline: str
    width: int = 2

    def to_dict(self):
        return {'type': 'rect', 'xy': self.xy,
                'outline': self.outline, 'width': self.width}
