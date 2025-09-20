# Grroup17-Canvas-Drawing-App.
Drawing Canvas App

A Python-based drawing application with freehand drawing, basic shapes, color selection, undo/redo functionality, and PNG export capabilities. Built with Tkinter for the GUI and designed with a modular, object-oriented architecture.

📋 Project Summary
This application provides a simple but functional drawing canvas where users can:

Draw freehand with a pen tool
Create basic shapes (lines, rectangles)
Choose drawing colors
Paint drawing
Undo and redo drawing operations
Save drawings as PNG files
Clear the entire canvas

The project demonstrates advanced Python concepts including object-oriented programming, abstract base classes, the command pattern for undo/redo, exception handling, and GUI development with Tkinter.


🚀 Quick Start
Prerequisites
Python Version Requirement:

Python 3.10 is required for this project (as specified in Pipfile)
If you have a different Python version installed (e.g., 3.13), you'll need to install Python 3.10 alongside it

Installing Python 3.10

Download Python 3.10 from the official website:

Visit: https://www.python.org/downloads/release/python-3100/
Download the appropriate installer for your operating system


Windows Installation:

   Run the installer
   ✅ Important: Check "Add Python to PATH"
   ✅ Important: Check "tcl/tk and IDLE" (ensures Tkinter GUI support)
   Choose "Install Now" or customize installation location


macOS Installation:
   # Using Homebrew (recommended)
   brew install python@3.10
   
   # Or download from python.org and install

Linux Installation:

   # Ubuntu/Debian
   sudo apt update
   sudo apt install python3.10 python3.10-venv python3.10-dev python3.10-tk
   
   # CentOS/RHEL/Fedora
   sudo dnf install python3.10 python3.10-tkinter

Verify Installation:

   # Should show Python 3.10.x
   python3.10 --version  
   python3.10 -c "import tkinter; print('Tkinter available')"


Setup Instructions

Clone the Repository:

   git clone https://github.com/your-team/group17-drawing-canvas.git
   cd group17-drawing-canvas

Install pipenv (if not already installed):

   pip install pipenv
   # or if you have multiple Python versions:
   python3.10 -m pip install pipenv

Create Virtual Environment with Python 3.10:

  # Tell pipenv to use Python 3.10 specifically
   pipenv --python 3.10
   
   # Install dependencies (both production and development)
   pipenv install --dev 


Activate the Virtual Environment:

   pipenv shell     

Verify Setup:

   # Check Python version in the virtual environment
   # Should show Python 3.10.x
   python --version
   
   # Test Tkinter availability
   python -c "import tkinter; print('GUI support ready')"
   
   # Run tests to ensure everything works
   pytest -v  


Run the Application:

  python -m src.main   


Alternative Setup (if pipenv issues occur):
If you encounter issues with pipenv, you can use the traditional venv approach:
  # Create virtual environment with Python 3.10
  python3.10 -m venv drawing_app_env

  # Activate environment
  # On Windows:
  drawing_app_env\Scripts\activate

  # On macOS/Linux:
  source drawing_app_env/bin/activate

  # Install dependencies
  pip install pillow pytest pytest-cov

  # Run application
  python -m src.main 

🧪 Testing
  Run the test suite to verify everything works correctly:
  # Run all tests
  pipenv run pytest
  
  # Run with verbose output
  pipenv run pytest -v
  
  # Run with coverage report
  pipenv run pytest --cov=src
  
  # Run specific test file
  pipenv run pytest tests/test_app.py  

🎯 Usage

  Launch the application using the command above
  Select a tool from the toolbar (Pen, Line, Rectangle)
  Choose a color using the Color button
  Draw on the canvas by clicking and dragging
  Use Undo/Redo to manage your drawing history
  Save your work as a PNG file using the Save button
  Clear the canvas to start fresh   


👥 Team Roles & Contributions
Role Assignments

  Coordinator/Lead[Ammar Sunusi Ahmad] => Project scheduling, deadline management, final submission coordination, team communication
  Developer (Core Logic)[Anih Kosarachi Clement] => Main application code, drawing canvas implementation, tool architecture, core functionality
  QA/CI & Tests[Okoye Mcpaul Emmanuel & Anih Kosarachi Clement] => Test suite development, continuous integration setup, code quality assurance, bug testing
  Docs/Presenter[Okoye Mcpaul Emmanuel & Abdulhamid Arome Abdullahi] => README documentation, demo video creation, final report writing, presentation materials 


Contribution Reflection

Commit History Analysis
Our commit history demonstrates collaborative development with contributions from all team members:

[Ammar Sunusi Ahmad] (Coordinator):

Initial project setup and repository structure
Project planning and milestone coordination
Final integration and release management
Key commits: 


[Anih Kosarachi Clement] (Developer):

Core canvas and drawing functionality implementation
Tool architecture and abstract base class design
Mouse event handling and drawing operations
Key commits: 


[Okoye Mcpaul Emmanuel & Anih Kosarachi Clement] (QA/Tests):

Test suite development for core functionality
GitHub Actions CI/CD pipeline setup
Code quality checks and bug identification
Key commits: 


[Okoye Mcpaul Emmanuel & Abdulhamid Arome Abdullahi] (Docs/Presenter):

Comprehensive documentation creation
Demo video production and editing
User experience testing and feedback
Key commits: 


Architecture
Project Structure

group17-drawing-canvas/
├── .github/
│   └── workflows/
│       └── ci.yml                 # GitHub Actions CI/CD
├── src/
│   ├── __init__.py
│   ├── main.py                    # Application entry point
│   ├── app.py                     # Main application window
│   ├── drawing_canvas.py          # Canvas component with drawing logic
│   ├── history.py                 # Undo/redo functionality
│   ├── errors.py                  # Custom exception classes
│   └── tools.py                   # Tools for handling drawing functions
│        
│       
├── tests/
│   ├── __init__.py
│   ├── test_app.py                # Canvas, history functionality tests
|
├── .gitignore                     # Git ignore patterns
├── Pipfile                        # Dependency specifications
├── Pipfile.lock                   # Locked dependency versions
└── README.md                      # This file


![the screenshot](https://github.com/Ammar0197/Group17-drawing-canvas-app/blob/e66e89d33c653a62c0e85f7f5bdfd7cbd3086146/trying%201.png)




🎬 Demo Video
[the link to the demo](https://drive.google.com/file/d/1xwQdm7_0KsDPrj3J-gAaB2OBCiSt87f8/view?usp=sharing) 

The demo video showcases:
Application startup and interface overview
Drawing with different tools (pen, line, rectangle)
Color selection and customization
Undo/redo functionality demonstration
Painting drawing
Saving drawings as PNG files
Error handling and edge cases

🚧 Known Issues & Limitations
Current Limitations

PNG export uses simplified conversion (full canvas-to-image conversion may need enhancement)
Limited shape tools (only line and rectangle currently implemented)
No brush size adjustment in current MVP
History is limited to 50 operations (configurable)

🔧 Troubleshooting
Common Issues
Issue: ModuleNotFoundError: No module named 'tkinter'
Solution:

  Ensure Python 3.10 was installed with Tkinter support
  On Linux: sudo apt-get install python3.10-tk
  Reinstall Python 3.10 with GUI components checked

Issue: pipenv: command not found
Solution:
  pip install pipenv
  # or
  python3.10 -m pip install pipenv
Issue: Pipenv uses wrong Python version
Solution:
  # Remove existing environment
  pipenv --rm
  # Recreate with specific Python version
  pipenv --python 3.10
  pipenv install --dev

Issue: Application window doesn't appear
Solution:

  Check if running in headless environment (needs display)
  Verify Tkinter installation: python -c "import tkinter; tkinter._test()"

Getting Help
If you encounter issues:

  Check the Issues page
  Verify your Python 3.10 and Tkinter installation
  Ensure all dependencies are installed: pipenv install --dev
  Try the alternative venv setup if pipenv fails  


Project Team: Group 17
Course: Advanced Python
Timeline:  -   
