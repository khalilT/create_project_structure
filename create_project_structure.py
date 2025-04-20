import os

def create_folder_structure(base_dir):
    """Creates the folder structure for the project."""
    folders = [
        os.path.join(base_dir, "src"),
        os.path.join(base_dir, "src", "utils"),
        os.path.join(base_dir, "scripts"),
        os.path.join(base_dir, "data"),
        os.path.join(base_dir, "notebooks"),
        os.path.join(base_dir, "figures"),
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    
    # Add __init__.py to src
    init_file = os.path.join(base_dir, "src", "__init__.py")
    with open(init_file, "w") as f:
        f.write("# src package initialization\n")

    # Add .gitignore file
    gitignore_content = '''# Ignore Python cache files
__pycache__/
*.pyc
*.pyo

# Ignore virtual environments
venv/
.env/

# Ignore data files
/data/*
!/data/.gitkeep

# Ignore Jupyter Notebook checkpoints
/notebooks/*
!notebooks/.gitkeep
**/.ipynb_checkpoints/

# Ignore metadata generation
create_project_structure.py
generate_readme_info.py
README_template.md

# Ignore system files
.DS_Store
Thumbs.db'''
    gitignore_file = os.path.join(base_dir, ".gitignore")
    with open(gitignore_file, "w") as f:
        f.write(gitignore_content)

    print("Folder structure created, including __init__.py and .gitignore.")


def create_paths_py(src_utils_dir):
    """Creates the paths.py file in src/utils."""
    paths_content = '''import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

DATA_PATHS = {
    "remote_data": "/path/to/cluster/data1",
}

def get_path(name):
    """
    Retrieve the path for a given dataset name.
    Raises KeyError if the name is not found.
    """
    if name in DATA_PATHS:
        return DATA_PATHS[name]
    raise KeyError(f"No path found for dataset '{name}'")
'''
    paths_file = os.path.join(src_utils_dir, "paths.py")
    with open(paths_file, "w") as f:
        f.write(paths_content)
    print("paths.py created.")


def create_functions_py(src_utils_dir):
    """Creates the functions.py file in src/utils."""
    functions_content = '''# Module containing utility functions
'''
    functions_file = os.path.join(src_utils_dir, "functions.py")
    with open(functions_file, "w") as f:
        f.write(functions_content)
    print("functions.py created.")


def create_constants_py(src_utils_dir):
    """Creates the constants.py file in src/utils."""
    constants_content = '''# Module containing project constants
'''
    constants_file = os.path.join(src_utils_dir, "constants.py")
    with open(constants_file, "w") as f:
        f.write(constants_content)
    print("constants.py created.")


def create_generate_readme_info(base_dir):
    """Creates the generate_readme_info.py script in the base directory."""
    readme_generator_content = '''import os
import platform
import sys
from datetime import datetime
import subprocess

# Use importlib.metadata instead of deprecated pkg_resources
try:
    from importlib.metadata import distributions
except ImportError:
    distributions = None

def generate_session_info():
    """Generate session info including Python version, platform, and more."""
    try:
        raw = subprocess.check_output(["R", "--version"], text=True)
        # e.g. "R version 4.2.1 (2022-06-23)"
        first_line = raw.splitlines()[0]
        version_token = first_line.split()[2]
        r_version = f"{first_line} (parsed: {version_token})"
    except FileNotFoundError:
        r_version = "R is not installed or not found in PATH."
    except subprocess.CalledProcessError as e:
        r_version = f"Error calling R: {e}"

    info = {
        "Python Version": sys.version.replace("\\n", " "),
        "Platform": platform.platform(),
        "OS": platform.system(),
        "Architecture": platform.architecture()[0],
        "Processor": platform.processor(),
        "Generated On": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "R Version": r_version,
    }
    return info

def generate_requirements(output_path="requirements.txt"):
    """Generate a requirements.txt file for the current environment."""
    if distributions is None:
        # Fallback to pip freeze for older Pythons
        reqs = subprocess.check_output([sys.executable, "-m", "pip", "freeze"], text=True)
        lines = reqs.splitlines()
    else:
        pkgs = [(dist.metadata["Name"], dist.version) for dist in distributions()]
        lines = [f"{name}=={version}" for name, version in sorted(pkgs, key=lambda x: x[0].lower())]

    with open(output_path, "w") as f:
        for line in lines:
            f.write(line + "\\n")
    print(f"Requirements file generated at {output_path}")

def generate_readme_content(readme_template_path, output_path):
    """Generate README.md with session info included."""
    with open(readme_template_path, "r") as f:
        readme_content = f.read()

    session_info = generate_session_info()
    session_info_text = "\\n".join(f"- **{key}**: {value}" for key, value in session_info.items())

    readme_content += "\\n\\n## **Session Info**\\n\\n" + session_info_text

    with open(output_path, "w") as f:
        f.write(readme_content)
    print(f"README file generated at {output_path}")

if __name__ == "__main__":
    TEMPLATE_PATH = "README_template.md"
    README_PATH = "README.md"
    REQUIREMENTS_PATH = "requirements.txt"

    generate_requirements(REQUIREMENTS_PATH)
    generate_readme_content(TEMPLATE_PATH, README_PATH)
'''
    readme_generator_file = os.path.join(base_dir, "generate_readme_info.py")
    with open(readme_generator_file, "w") as f:
        f.write(readme_generator_content)
    print("generate_readme_info.py created.")


def create_readme_template(base_dir):
    """Creates the README_template.md file in the base directory."""
    readme_template_content = '''# Project Name

A Python project for centralized and FAIR data path management.

## **Overview**

This project simplifies data handling with centralized path management.

## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject

