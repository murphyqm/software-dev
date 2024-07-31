import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import altair as alt
import matplotlib
import re

st.set_page_config( page_title="Project Workflow", page_icon="📈")
st.write("If you're starting a new project, here's a workflow you can use",
         "to build a robust, tidy Python project.")
st.write("Remember to use `git` to version control all your work.")
st.header("Part One: your Python package")

brainstorm_md = """
- What's the main purpose of the code?
- What sort of inputs will it take?
    - What format or data type will these be?
- What sort of output will it produce?
- Who is going to use it?
- Where is it going to be used?
    - A local desktop machine?
    - A HPC system?
- What submodules or functions do you predict you'll need?
- What should you call your package?
"""


export_pip_version_numbers = """
# Extract installed pip packages
pip_packages=$(conda env export | grep -A9999 ".*- pip:" | grep -v "^prefix: ")

# Export conda environment without builds, and append pip packages
conda env export --from-history | grep -v "^prefix: " > new-environment.yml
echo "$pip_packages" >> new-environment.yml
"""

export_pip_no_version_numbers = """
# Extract installed pip packages
pip_packages=$(conda env export | grep -A9999 ".*- pip:" | grep -v "^prefix: " | cut -f1 -d"=")

# Export conda environment without builds, and append pip packages
conda env export --from-history | grep -v "^prefix: " > new-environment.yml
echo "$pip_packages" >> new-environment.yml
"""

st.subheader("1. Brainstorm and gather requirements")
with st.expander("What does your code need to do?"):
    st.write(brainstorm_md)
st.subheader("2. Create package repository and directory structure")
with st.expander("Use a basic Python package template"):
    st.write("##### 1. Choose your package/repository name")
    project_name = st.text_input("Enter your package name (lowercase letters and underscores only!):", "example_package")
    project_name = re.sub('\s+', '_', project_name)
    project_name = re.sub('-', '_', project_name)

    repo_name = re.sub('_', '-', project_name)
    st.write(f"Your package name: `{project_name}`. If this doesn't look right, please change your input!")

    st.write(f"##### 2. Create a git repository called `{repo_name}`")
    
    st.write(f"You can create `{repo_name}` on GitHub and then clone this new repository to your local machine, or you can create it locally (using `mkdir {repo_name}`, `cd {repo_name}`, and `git init`).")

    st.write(f"##### 3. Create a tidy folder structure")

    folder_structure = f"""
    {repo_name}/
    ├── src/  
    │   └── {project_name}/     
    │       ├── __init__.py      Makes the folder a package.
    │       └── source.py        An example module containing source code.
    ├── tests/
    |   ├── __init__.py          Sets up the test suite.
    │   └── test_source.py       A file containing tests for the code in source.py.
    ├── README.md                README with information about the project.
    ├── pyproject.toml           Metadata about the project and its dependencies.
    ├── environment.yml          Your development environment (or requirements.txt)
    └── CITATION.cff             Citation file that makes it easy for people to cite you!

    """

    str_chunk = f"""
mkdir tests
touch tests/__init__.py
echo -e 'import sys\nsys.path.append("src")' > tests/__init__.py
mkdir src/
mkdir src/{project_name}/
touch pyproject.toml
touch environment.yml
touch README.md
touch CITATION.cff
touch src/{project_name}/__init__.py
touch src/{project_name}/source.py
"""

    st.write(f"If `{repo_name}` is the root directory of your project, you might want a project structure that looks something like this:")

    st.code(folder_structure, language='text')

    st.write(f'To recreate the structure above, `cd` into your project directory (`{repo_name}`) and run the following commands (by copying and pasting the block below into the terminal):')
    st.code(str_chunk, language='bash')


dev_env_md = f"""
#### 1. Create your environment yml file

In `{repo_name}/environment.yml`, add the following content (replacing the dependencies with
those you need for your specific project):

```yml
name: {repo_name}-dev

dependencies:
# These dependencies are very useful for packaging and testing your code
  - python=3.12
  - pytest
  - setuptools
  - blackd
  - isort
# Remove these/replace these ones:
  - numpy
  - matplotlib
  - pandas
```
#### 2. Create your env from the yml file

You can now create the conda environment `{repo_name}-dev`:

```bash
conda env create --file environment.yml
```

#### 3. Export your env exactly

At a future point in time (for example, after completing benchmarking, when creating a release etc.) you may want to export your exact conda env, including every dependency and version. This can be done using the `export` command (changing `env-record.yml` to a filename of your choosing):

```bash
conda env export > env-record.yml
```

This file will contain the exact versions of all your dependencies (including pip dependencies, and build information) which is a useful record, but isn't user-friendly when it comes to rebuilding/reproducing an environment. See the notes below on environment files and distributing code to see alternative export methods.

"""

pseudocode_md = """

"""

st.subheader("3. Create a dev env")
with st.expander("Create a conda environment for development"):
    st.write(dev_env_md)
with st.expander("More detail on balancing `env.yml` files for development and `pyproject.toml` files for distributing code"):
    st.subheader("Managing dependencies")
    st.write("While developing your code, you may need other external Python packages, for example `numpy`, `matplotlib.pyplot`, or `scipy`. These are **dependencies**.",
    "While developing your code, you can use the dependency manager of your choice, such as `conda`, and then export your dependencies",
    "to an `environment.yml` file or a `requirements.txt` file.",
    "You can then add these dependencies to your `pyproject.toml` file when you are ready to share the code.")
    st.subheader("Example workflow using `conda`")
    st.write("When writing your code, you should work in a virtual environment, in this case using conda.",
    "First you should create an environment with the version of Python you need, and any initial packages you know you will require.")
    st.code("conda create -n ENV-NAME python=3.12 numpy", language="bash")
    st.write("Then, as needed, you can add packages (with the environment active):")
    st.code("conda install pytest", language="bash")
    st.write("When you are ready to package/release the code, you can export all your environments to an `environment.yml` file:")
    st.code("conda env export --from-history > environment.yml # again, from inside the activated env", language="bash")
    st.write("You can modify this file and remove packages that you were just using for development (for example, `pytest`).",
    "You should test the environment works and you code can run by installing the env (you may need to change it's name):")
    st.code("conda env create -f environment.yml", language="bash")
    st.write("if you have installed packages with pip from inside your conda env, you will need to add a few steps to add these requirements.",
    "[ekiwi111](https://github.com/conda/conda/issues/9628#issuecomment-1608913117) on GitHub provides the following code snippet:")
    st.code(export_pip_version_numbers, language="bash")
    st.write("For more flexibility in pip package versions, we can modify this to cut the pip version numbers out:")
    st.code(export_pip_no_version_numbers, language="bash")
    
st.subheader("4. Write Pseudocode and code")
with st.expander("Use comments to draft your code"):
    st.write(pseudocode_md)
st.subheader("5. Write test suite")
st.subheader("6. Write documentation")
st.subheader("7. Build package with `pyproject.toml`")
st.subheader("8. Build automated workflows")
st.subheader("9. Export/record dev env/dependencies")
st.subheader("10. Create a release on GitHub, with a DOI")
st.divider()
st.header("Part Two: using the package for research")
st.subheader("11. Create project repository and directory structure")
st.subheader("12. Create a research env with the new package")
st.subheader("13. Do analysis/research work")
st.subheader("14. Export/record research env")
st.subheader("15. Create release with DOI")