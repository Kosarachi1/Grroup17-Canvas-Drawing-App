"""model file"""
import traceback
from PIL import Image, ImageDraw
from .history import History


class CanvasModel:
    def __init__(self, width=800, height=600, bg="white"):
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

    def save_png(self, filename):
        img = Image.new("RGB", (self.width, self.height), self.bg)
        draw = ImageDraw.Draw(img)

        commands = self.history.items()

        # Apply PaintCmd modifiers
        for cmd in commands:
            if hasattr(cmd, "apply"):
                try:
                    cmd.apply(commands)
                except (AttributeError, TypeError, ValueError) as e:
                    print("Error applying paint for png:", e)
                    traceback.print_exc()

        # Render drawable commands
        for cmd in commands:
            if hasattr(cmd, "apply"):
                continue
            try:
                cmd.render_pil(draw)
            except (AttributeError, TypeError, ValueError) as e:
                print("Error rendering to PIL:", e)
                traceback.print_exc()

        img.save(filename)

    def render_to_tk(self, canvas):
        canvas.delete("all")

        # Get all the commands currently in history
        commands = self.history.items()
        # Apply modifier commands first (like PaintCmd)
        for cmd in commands:
            if hasattr(cmd, "apply"):
                try:
                    cmd.apply(commands)
                except (AttributeError, TypeError, ValueError) as e:
                    print("Error while applying command:", e)
                    traceback.print_exc()
        # Render normal commands
        for i, cmd in enumerate(commands):
            if hasattr(cmd, "apply"):
                continue  # skip modifiers
            try:
                cmd.render_tk(canvas, tag=str(i))
            except TypeError:
                # fallback for legacy render_tk
                try:
                    cmd.render_tk(canvas)
                except (AttributeError, TypeError, ValueError) as e:
                    print("Error rendering command:", e)
                    traceback.print_exc()
