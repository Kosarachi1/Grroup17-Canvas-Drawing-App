import unittest, os, tempfile
from history import History
from model import CanvasModel
from tools import LineCmd, RectCmd
from PIL import Image

class HistoryTests(unittest.TestCase):
    def test_push_undo_redo(self):
        h = History()
        h.push('a'); h.push('b')
        self.assertEqual(h.items(), ['a','b'])
        u = h.undo(); self.assertEqual(u,'b')
        self.assertEqual(h.items(), ['a'])
        r = h.redo(); self.assertEqual(r,'b')
        self.assertEqual(h.items(), ['a','b'])

class SaveTests(unittest.TestCase):
    def test_save_png(self):
        m = CanvasModel(width=200, height=150)
        m.add_cmd(LineCmd(xy=(10,10,190,10), color='#ff0000', width=3))
        m.add_cmd(RectCmd(xy=(20,20,100,80), outline='#0000ff', width=2))
        tf = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
        tf.close()
        try:
            m.save_png(tf.name)
            self.assertTrue(os.path.getsize(tf.name) > 0)
            Image.open(tf.name)  # should open successfully
        finally:
            os.unlink(tf.name)

if __name__ == "__main__":
    unittest.main()
