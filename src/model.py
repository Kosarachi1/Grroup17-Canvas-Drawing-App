import tkinter as tk
from PIL import Image, ImageDraw
from .history import History
from .tools import FreehandCmd, LineCmd, RectCmd
from .errors import FileSaveError

class CanvasModel:
    def __init__(self, width=800, height=600, bg='white'):
        self.width = width
        self.height = height
        self.bg = bg
        self.history = History()

    def add_cmd(self, cmd):
        self.history.push(cmd)

    def undo(self):
        return self.history.undo()

    def redo(self):
        return self.history.redo()

    def clear(self):
        self.history.clear()

    def to_serializable(self):
        return [c.to_dict() for c in self.history.items()]

    def save_png(self, path):
        img = Image.new('RGB', (self.width, self.height), self.bg)
        draw = ImageDraw.Draw(img)
        for c in self.history.items():
            if isinstance(c, FreehandCmd):
                if len(c.points) >= 2:
                    draw.line(c.points, fill=c.color, width=c.width)
            elif isinstance(c, LineCmd):
                draw.line(c.xy, fill=c.color, width=c.width)
            elif isinstance(c, RectCmd):
                draw.rectangle(c.xy, outline=c.outline, width=c.width)
        try:
            img.save(path, 'PNG')
        except Exception as e:
            raise FileSaveError(str(e)) from e

    def render_to_tk(self, tk_canvas: tk.Canvas):
        tk_canvas.delete('all')
        for c in self.history.items():
            if isinstance(c, FreehandCmd):
                pts = sum([[x,y] for (x,y) in c.points], [])
                if len(pts) >= 4:
                    tk_canvas.create_line(*pts, fill=c.color,
                        width=c.width, capstyle=tk.ROUND, smooth=True)
            elif isinstance(c, LineCmd):
                tk_canvas.create_line(*c.xy, fill=c.color, width=c.width)
            elif isinstance(c, RectCmd):
                tk_canvas.create_rectangle(*c.xy, outline=c.outline,
                        width=c.width)
