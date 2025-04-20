#!/usr/bin/env python3
import os
import platform
import sys
from datetime import datetime
import subprocess

def create_folder_structure(base_dir):
    """Creates the folder structure for the project."""
    print(f"[INFO] Creating folders under {base_dir!r}")
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
        print(f"  ↳ ensured {folder}")

    # Add __init__.py to src
    init_file = os.path.join(base_dir, "src", "__init__.py")
    with open(init_file, "w") as f:
        f.write("# src package initialization\n")
    print(f"  ↳ wrote {init_file}")

    # Add .gitignore file
    gitignore_content = [
        "# Ignore Python cache files",
        "__pycache__/",
        "*.pyc",
        "*.pyo",
        "",
        "# Ignore virtual environments",
        "venv/",
        ".env/",
        "",
        "# Ignore data files",
        "/data/*",
        "!/data/.gitkeep",
        "",
        "# Ignore Jupyter Notebook checkpoints",
        "/notebooks/*",
        "!/notebooks/.gitkeep",
        "**/.ipynb_checkpoints/",
        "",
        "# Ignore metadata generation",
        "create_project_structure.py",
        "generate_readme_info.py",
        "README_template.md",
        "",
        "# Ignore system files",
        ".DS_Store",
        "Thumbs.db",
        ""
    ]
    gitignore_path = os.path.join(base_dir, ".gitignore")
    with open(gitignore_path, "w") as f:
        f.write("\n".join(gitignore_content))
    print(f"  ↳ wrote {gitignore_path}")

def create_paths_py(src_utils_dir):
    """Creates the paths.py file in src/utils."""
    print(f"[INFO] Creating paths.py in {src_utils_dir!r}")
    content = [
        "import os",
        "",
        "BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), \"..\"))",
        "",
        "DATA_PATHS = {",
        "    \"remote_data\": \"/path/to/cluster/data1\",",
        "}",
        "",
        "def get_path(name):",
        "    \"\"\"Retrieve the path for a given dataset name.\"\"\"",
        "    if name in DATA_PATHS:",
        "        return DATA_PATHS[name]",
        "    raise KeyError(f\"No path found for dataset '{name}'\")",
        ""
    ]
    path_file = os.path.join(src_utils_dir, "paths.py")
    with open(path_file, "w") as f:
        f.write("\n".join(content))
    print(f"  ↳ wrote {path_file}")

def create_functions_py(src_utils_dir):
    """Creates the functions.py file in src/utils."""
    print(f"[INFO] Creating functions.py in {src_utils_dir!r}")
    functions_file = os.path.join(src_utils_dir, "functions.py")
    with open(functions_file, "w") as f:
        f.write("# Module containing utility functions\n")
    print(f"  ↳ wrote {functions_file}")

def create_constants_py(src_utils_dir):
    """Creates the constants.py file in src/utils."""
    print(f"[INFO] Creating constants.py in {src_utils_dir!r}")
    constants_file = os.path.join(src_utils_dir, "constants.py")
    with open(constants_file, "w") as f:
        f.write("# Module containing project constants\n")
    print(f"  ↳ wrote {constants_file}")

def create_generate_readme_info(base_dir):
    """Creates the generate_readme_info.py script in the base directory."""
    print(f"[INFO] Creating generate_readme_info.py in {base_dir!r}")
    script_lines = [
        "import os",
        "import platform",
        "import sys",
        "from datetime import datetime",
        "import subprocess",
        "",
        "try:",
        "    from importlib.metadata import distributions",
        "except ImportError:",
        "    distributions = None",
        "",
        "def generate_session_info():",
        "    try:",
        "        raw = subprocess.check_output([\"R\", \"--version\"], text=True)",
        "        first_line = raw.splitlines()[0]",
        "        version_token = first_line.split()[2]",
        "        r_version = f\"{first_line} (parsed: {version_token})\"",
        "    except FileNotFoundError:",
        "        r_version = \"R is not installed or not found in PATH.\"",
        "    except subprocess.CalledProcessError as e:",
        "        r_version = f\"Error calling R: {e}\"",
        "",
        "    return {",
        "        'Python Version': sys.version.replace('\\n', ' '),",
        "        'Platform': platform.platform(),",
        "        'OS': platform.system(),",
        "        'Architecture': platform.architecture()[0],",
        "        'Processor': platform.processor(),",
        "        'Generated On': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),",
        "        'R Version': r_version,",
        "    }",
        "",
        "def generate_requirements(output_path='requirements.txt'):",
        "    if distributions is None:",
        "        reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'], text=True)",
        "        lines = reqs.splitlines()",
        "    else:",
        "        pkgs = [(dist.metadata['Name'], dist.version) for dist in distributions()]",
        "        lines = [f\"{name}=={version}\" for name, version in sorted(pkgs, key=lambda x: x[0].lower())]",
        "    with open(output_path, 'w') as f:",
        "        for line in lines:",
        "            f.write(line + '\\n')",
        "    print(f\"Requirements file generated at {output_path}\")",
        "",
        "def generate_readme_content(readme_template_path, output_path):",
        "    with open(readme_template_path, 'r') as f:",
        "        readme_content = f.read()",
        "    session_info = generate_session_info()",
        "    info_block = '\\n'.join(f\"- **{k}**: {v}\" for k, v in session_info.items())",
        "    with open(output_path, 'w') as f:",
        "        f.write(readme_content + '\\n\\n## **Session Info**\\n\\n' + info_block)",
        "    print(f\"README file generated at {output_path}\")",
        "",
        "if __name__ == '__main__':",
        "    generate_requirements('requirements.txt')",
        "    generate_readme_content('README_template.md', 'README.md')",
        ""
    ]
    script_path = os.path.join(base_dir, "generate_readme_info.py")
    with open(script_path, "w") as f:
        f.write("\n".join(script_lines))
    print(f"  ↳ wrote {script_path}")

def create_readme_template(base_dir):
    """Creates the README_template.md file in the base directory."""
    print(f"[INFO] Creating README_template.md in {base_dir!r}")
    lines = [
        "# Project Name",
        "",
        "A Python project for centralized and FAIR data path management.",
        "",
        "## **Overview**",
        "",
        "This project simplifies data handling with centralized path management.",
        "",
        "## **Installation**",
        "",
        "1. Clone the repository:",
        "   ```bash",
        "   git clone https://github.com/yourusername/yourproject.git",
        "   cd yourproject",
        "   ```",
        "",
        "2. Install dependencies:",
        "   ```bash",
        "   pip install -r requirements.txt",
        "   ```",
        ""
    ]
    template_path = os.path.join(base_dir, "README_template.md")
    with open(template_path, "w") as f:
        f.write("\n".join(lines))
    print(f"  ↳ wrote {template_path}")

def main():
    base_dir = os.getcwd()
    print(f"[INFO] Base directory is: {base_dir}\n")
    create_folder_structure(base_dir)
    utils_dir = os.path.join(base_dir, "src", "utils")
    create_paths_py(utils_dir)
    create_functions_py(utils_dir)
    create_constants_py(utils_dir)
    create_generate_readme_info(base_dir)
    create_readme_template(base_dir)
    print("\n[INFO] Project setup complete.")

if __name__ == "__main__":
    main()

