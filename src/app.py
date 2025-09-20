import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from .model import CanvasModel
from .tools import Tool, FreehandCmd, LineCmd, RectCmd, PaintCmd

class DrawingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Drawing Canvas App')
        self.geometry('1000x700')
        self.model = CanvasModel(width=900, height=600)
        self.current_tool = Tool.FREEHAND
        self.current_color = '#000000'
        self.brush_size = 3
        self._build_ui()
        self._bind_events()
        self._reset_temp()

    def _build_ui(self):
        toolbar = tk.Frame(self, bd=2, relief=tk.RAISED)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # Tools
        tk.Button(toolbar, text='Freehand',
            command=lambda: self._select_tool(Tool.FREEHAND)).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(toolbar, text='Line',
            command=lambda: self._select_tool(Tool.LINE)).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(toolbar, text='Rect',
            command=lambda: self._select_tool(Tool.RECT)).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(
            toolbar, text="Paint", command=lambda: self._select_tool(Tool.PAINT)
        ).pack(side=tk.LEFT, padx=2, pady=2)

        # Color picker
        self.color_btn = tk.Button(toolbar, text='Color', command=self._choose_color)
        self.color_indicator = tk.Canvas(toolbar, width=24, height=24)
        self.color_indicator.create_rectangle(0,0,24,24, fill=self.current_color, outline='')
        self.color_btn.pack(side=tk.LEFT, padx=6)
        self.color_indicator.pack(side=tk.LEFT)

        # Undo/Redo/Save
        tk.Button(toolbar, text='Undo', command=self._undo).pack(side=tk.RIGHT, padx=2)
        tk.Button(toolbar, text='Redo', command=self._redo).pack(side=tk.RIGHT, padx=2)
        tk.Button(toolbar, text='Save PNG', command=self._save_png).pack(side=tk.RIGHT, padx=6)
        tk.Button(toolbar, text='Clear', command=self._clear).pack(side=tk.RIGHT, padx=2)

        # Canvas
        self.canvas = tk.Canvas(self, bg=self.model.bg, width=self.model.width, height=self.model.height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Status bar
        self.status = tk.Label(self, text='Tool: Freehand | Color: black')
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def _bind_events(self):
        self.canvas.bind('<ButtonPress-1>', self._on_press)
        self.canvas.bind('<B1-Motion>', self._on_move)
        self.canvas.bind('<ButtonRelease-1>', self._on_release)
        self.bind_all('<Control-z>', lambda e: self._undo())
        self.bind_all('<Control-y>', lambda e: self._redo())

    def _reset_temp(self):
        self._temp_points = []
        self._temp_item = None
        self._start_xy = None

    def _select_tool(self, tool):
        self.current_tool = tool
        self.status.config(text=f'Tool: {tool} | Color: {self.current_color}')

    def _choose_color(self):
        c = colorchooser.askcolor(color=self.current_color, parent=self)
        if c and c[1]:
            self.current_color = c[1]
            self.color_indicator.delete('all')
            self.color_indicator.create_rectangle(0,0,24,24, fill=self.current_color, outline='')
            self.status.config(text=f'Tool: {self.current_tool} | Color: {self.current_color}')

    def _on_press(self, event):
        x, y = event.x, event.y
        self._start_xy = (x, y)
        if self.current_tool == Tool.FREEHAND:
            self._temp_points = [(x, y)]
            self._temp_item = self.canvas.create_line(x, y, x+1, y+1,
                fill=self.current_color, width=self.brush_size,
                capstyle=tk.ROUND, smooth=True)
        elif self.current_tool == Tool.LINE:
            self._temp_item = self.canvas.create_line(x,y,x,y,
                fill=self.current_color, width=self.brush_size)
        elif self.current_tool == Tool.RECT:
            self._temp_item = self.canvas.create_rectangle(x,y,x,y,
                outline=self.current_color, width=self.brush_size)
        elif self.current_tool == Tool.PAINT:
            # find item under cursor, read its tag (which is string index)
            item_id_tuple = self.canvas.find_closest(x, y)
            if not item_id_tuple:
                return
            # ensure we have an integer id (find_closest returns a tuple of int)
            item_id = item_id_tuple[0] if isinstance(item_id_tuple, tuple) else item_id_tuple
            try:
                # gettags can return empty tuple
                tags = self.canvas.gettags(item_id)
            except tk.TclError:
                tags = ()
            if tags:
                tag0 = tags[0]
                try:
                    target_index = int(tag0)
                    paint_cmd = PaintCmd(
                        target_index=target_index, color=self.current_color
                    )
                    self.model.add_cmd(paint_cmd)
                    self.model.render_to_tk(self.canvas)
                except ValueError as e:
                    print("Paint error (parsing tag):", e)

    def _on_move(self, event):
        x, y = event.x, event.y
        if self.current_tool == Tool.FREEHAND and self._temp_item:
            self._temp_points.append((x, y))
            pts = sum([[px, py] for (px, py) in self._temp_points], [])
            self.canvas.coords(self._temp_item, *pts)
        elif self.current_tool in (Tool.LINE, Tool.RECT) and self._temp_item and self._start_xy:
            x0, y0 = self._start_xy
            self.canvas.coords(self._temp_item, x0, y0, x, y)

    def _on_release(self, event):
        x, y = event.x, event.y
        if self.current_tool == Tool.FREEHAND and self._temp_points:
            cmd = FreehandCmd(points=self._temp_points.copy(),
                              color=self.current_color, width=self.brush_size)
            self.model.add_cmd(cmd)
        elif self.current_tool == Tool.LINE and self._start_xy:
            x0,y0 = self._start_xy
            cmd = LineCmd(xy=(x0,y0,x,y),
                          color=self.current_color, width=self.brush_size)
            self.model.add_cmd(cmd)
        elif self.current_tool == Tool.RECT and self._start_xy:
            x0,y0 = self._start_xy
            cmd = RectCmd(xy=(x0,y0,x,y),
                          outline=self.current_color, width=self.brush_size)
            self.model.add_cmd(cmd)

        self.model.render_to_tk(self.canvas)
        self._reset_temp()

    def _undo(self):
        self.model.undo()
        self.model.render_to_tk(self.canvas)

    def _redo(self):
        self.model.redo()
        self.model.render_to_tk(self.canvas)

    def _save_png(self):
        fn = filedialog.asksaveasfilename(defaultextension='.png',
                                          filetypes=[('PNG files','*.png')])
        if not fn: return
        try:
            self.model.save_png(fn)
            messagebox.showinfo('Saved', f'Saved to {fn}')
        except Exception as e:
            messagebox.showerror('Save error', str(e))

    def _clear(self):
        self.model.clear()
        self.model.render_to_tk(self.canvas)
