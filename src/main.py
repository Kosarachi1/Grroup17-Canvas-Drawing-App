import argparse
from .app import DrawingApp
import sys
import pytest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true", help="Run test suite instead of app")
    args = parser.parse_args()

    if args.test:
        # run pytest programmatically, exit with the right status code
        sys.exit(pytest.main(["-v", "src/tests"]))
    else:
        app = DrawingApp()
        app.mainloop()

if __name__ == "__main__":
    main()
