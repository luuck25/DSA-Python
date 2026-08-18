"""
=============================================================================
  VIRTUAL ENVIRONMENTS IN PYTHON
=============================================================================
  An isolated Python installation per project.
  Each project gets its own packages without affecting others.
"""


# ═══════════════════════════════════════════════════════════════════════════
# WHY USE A VIRTUAL ENVIRONMENT?
# ═══════════════════════════════════════════════════════════════════════════
#
#   Project A needs requests==2.25
#   Project B needs requests==2.31
#
#   Without venv → they conflict on the same system Python
#   With venv    → each has its own independent site-packages


# ═══════════════════════════════════════════════════════════════════════════
# CREATE & ACTIVATE (macOS / Linux)
# ═══════════════════════════════════════════════════════════════════════════
#
#   # Create
#   python3 -m venv myenv              # creates a folder called "myenv"
#
#   # Activate
#   source myenv/bin/activate          # prompt changes to (myenv) $
#
#   # Install packages (goes into myenv only)
#   pip install requests
#
#   # Deactivate (go back to system Python)
#   deactivate


# ═══════════════════════════════════════════════════════════════════════════
# CREATE & ACTIVATE (Windows)
# ═══════════════════════════════════════════════════════════════════════════
#
#   python -m venv myenv
#   myenv\Scripts\activate             # backslash, not forward slash
#   deactivate


# ═══════════════════════════════════════════════════════════════════════════
# COMMON COMMANDS INSIDE VENV
# ═══════════════════════════════════════════════════════════════════════════
#
#   pip list                           # see installed packages
#   pip freeze > requirements.txt      # save dependencies to file
#   pip install -r requirements.txt    # install from file (recreate env)
#   which python                       # shows path inside venv (not system)
#   python --version                   # confirm Python version


# ═══════════════════════════════════════════════════════════════════════════
# FOLDER STRUCTURE CREATED
# ═══════════════════════════════════════════════════════════════════════════
#
#   myenv/
#   ├── bin/            # (Scripts/ on Windows) — python, pip, activate
#   ├── lib/            # site-packages (installed packages go here)
#   ├── include/
#   └── pyvenv.cfg      # config (which base Python was used)


# ═══════════════════════════════════════════════════════════════════════════
# BEST PRACTICES
# ═══════════════════════════════════════════════════════════════════════════
#
#   • DON'T commit myenv/ to git       → add to .gitignore
#   • DO commit requirements.txt       → others recreate env from it
#   • One venv per project             → avoids dependency conflicts
#   • Name it venv or .venv            → convention, auto-detected by VS Code
#   • VS Code: Cmd+Shift+P → "Python: Select Interpreter" → pick your venv


# ═══════════════════════════════════════════════════════════════════════════
# FULL WORKFLOW EXAMPLE
# ═══════════════════════════════════════════════════════════════════════════
#
#   # Start new project
#   mkdir my_project && cd my_project
#   python3 -m venv venv
#   source venv/bin/activate
#
#   # Install what you need
#   pip install flask requests
#
#   # Save dependencies
#   pip freeze > requirements.txt
#
#   # Share with teammate — they run:
#   python3 -m venv venv
#   source venv/bin/activate
#   pip install -r requirements.txt


# ═══════════════════════════════════════════════════════════════════════════
# VENV vs OTHER TOOLS
# ═══════════════════════════════════════════════════════════════════════════
#
#   | Tool       | What it does                                    |
#   |------------|-------------------------------------------------|
#   | venv       | Built-in, simple, one Python version per env    |
#   | virtualenv | Third-party, faster than venv, more features    |
#   | conda      | Manages Python versions + non-Python deps       |
#   | pipenv     | venv + pip + Pipfile (lock file for deps)       |
#   | poetry     | Modern dep management + packaging + venv        |
#   | pyenv      | Switch between Python VERSIONS (not packages)   |
#
#   For interviews/quick projects: venv is enough.
#   For production: poetry or pipenv for lockfiles.
