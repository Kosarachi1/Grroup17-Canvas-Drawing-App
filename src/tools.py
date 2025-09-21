import enum


class Tool(enum.Enum):
    FREEHAND = 1
    LINE = 2
    RECT = 3
    PAINT = 4


class FreehandCmd:
    def __init__(self, points, color, width):
        self.points = points  # list of (x,y)
        self.color = color
        self.width = width

    def render_tk(self, canvas, tag=None):
        if len(self.points) > 1:
            flat = sum(([x, y] for x, y in self.points), [])
            # tags argument expects tuple or string; pass tag if provided
            kwargs = {
                "fill": self.color,
                "width": self.width,
                "capstyle": "round",
                "smooth": True,
            }
            if tag is not None:
                kwargs["tags"] = (tag,)
            canvas.create_line(*flat, **kwargs)

    def render_pil(self, draw):
        if len(self.points) > 1:
            draw.line(self.points, fill=self.color, width=self.width)


class LineCmd:
    def __init__(self, xy, color, width):
        self.xy = xy
        self.color = color
        self.width = width

    def render_tk(self, canvas, tag=None):
        kwargs = {"fill": self.color, "width": self.width}
        if tag is not None:
            kwargs["tags"] = (tag,)
        canvas.create_line(*self.xy, **kwargs)

    def render_pil(self, draw):
        draw.line(self.xy, fill=self.color, width=self.width)


class RectCmd:
    def __init__(self, xy, outline, width, fill=None):
        self.xy = xy
        self.outline = outline
        self.width = width
        self.fill = fill

    def render_tk(self, canvas, tag=None):
        kwargs = {"outline": self.outline, "width": self.width}
        if self.fill is not None:
            kwargs["fill"] = self.fill
        if tag is not None:
            kwargs["tags"] = (tag,)
        canvas.create_rectangle(*self.xy, **kwargs)

    def render_pil(self, draw):
        draw.rectangle(self.xy, outline=self.outline, fill=self.fill, width=self.width)


class PaintCmd:
    """A paint command records: which command index to change, and the color to set.
    On render, model will call apply(commands) so it mutates the target command.
    """

    def __init__(self, target_index, color):
        self.target_index = target_index
        self.color = color

    def render_tk(self, canvas, tag=None):
        # PaintCmd itself does not draw anything
        pass

    def render_pil(self, draw):
        # PaintCmd itself does not draw anything
        pass

    def apply(self, commands):
        # Defensive: ensure index is in range and target is not itself a PaintCmd
        if not (0 <= self.target_index < len(commands)):
            return
        target = commands[self.target_index]
        # If the target is another PaintCmd, skip
        if hasattr(target, "apply"):
            return
        # Try to set sensible attributes: fill (rects), outline (rects), color (lines/freehand)
        if hasattr(target, "fill"):
            try:
                target.fill = self.color
            except AttributeError:
                pass
        if hasattr(target, "outline"):
            try:
                target.outline = self.color
            except AttributeError:
                pass
        if hasattr(target, "color"):
            try:
                target.color = self.color
            except AttributeError:
                pass
