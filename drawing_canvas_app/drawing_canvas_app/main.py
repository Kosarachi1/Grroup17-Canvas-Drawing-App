import argparse
from app import DrawingApp
import unittest

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()

    if args.test:
        import tests
    else:
        app = DrawingApp()
        app.mainloop()

if __name__ == "__main__":
    main()
