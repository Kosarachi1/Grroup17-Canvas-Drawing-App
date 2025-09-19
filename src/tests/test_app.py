import pytest
import unittest, os, tempfile
from src.history import History
from src.model import CanvasModel
from src.tools import LineCmd, RectCmd
from src.app import DrawingApp
from src.tools import Tool
from PIL import Image


class TestHistoryTests(unittest.TestCase):
    """Test cases for Undo and redo function."""

    def test_push_undo_redo(self):
        h = History()
        h.push("a")
        h.push("b")
        self.assertEqual(h.items(), ["a", "b"])
        u = h.undo()
        self.assertEqual(u, "b")
        self.assertEqual(h.items(), ["a"])
        r = h.redo()
        self.assertEqual(r, "b")
        self.assertEqual(h.items(), ["a", "b"])


class TestSaveTests(unittest.TestCase):
    """Test cases for saving image"""
    def test_save_png(self):
        m = CanvasModel(width=200, height=150)
        m.add_cmd(LineCmd(xy=(10, 10, 190, 10), color="#ff0000", width=3))
        m.add_cmd(RectCmd(xy=(20, 20, 100, 80), outline="#0000ff", width=2))
        tf = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        tf.close()
        try:
            m.save_png(tf.name)
            self.assertTrue(os.path.getsize(tf.name) > 0)
            Image.open(tf.name)  # should open successfully
        finally:
            os.unlink(tf.name)


class TestDrawingApp:
    """Test cases for the drawing functions."""

    def test_select_tool_updates_status(self):
        app = DrawingApp()
        app._select_tool(Tool.LINE)
        assert app.current_tool == Tool.LINE
        status_text = app.status.cget("text")
        assert "Tool: line" in status_text
        assert f"Color: {app.current_color}" in status_text