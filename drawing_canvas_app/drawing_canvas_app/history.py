class History:
    def __init__(self):
        self._done = []
        self._undone = []

    def push(self, cmd):
        self._done.append(cmd)
        self._undone.clear()

    def undo(self):
        if not self._done:
            return None
        cmd = self._done.pop()
        self._undone.append(cmd)
        return cmd

    def redo(self):
        if not self._undone:
            return None
        cmd = self._undone.pop()
        self._done.append(cmd)
        return cmd

    def clear(self):
        self._done.clear()
        self._undone.clear()

    def items(self):
        return list(self._done)

    def __len__(self):
        return len(self._done)
