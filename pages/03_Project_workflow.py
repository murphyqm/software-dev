import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import altair as alt
import matplotlib

st.set_page_config( page_title="Project Workflow", page_icon="📈")
st.write("If you're starting a new project, here's a workflow you can use",
         "to build a robust, tidy Python project.")
st.write("Remember to use `git` to version control all your work.")
st.header("Part One: your Python package")
st.divider()
st.header("1. Brainstorm and gather requirements")
st.header("2. Create package repository and directory structure")
st.header("3. Create a dev env")
st.header("4. Write Pseudocode and code")
st.header("5. Write test suite")
st.header("6. Write documentation")
st.header("7. Build package with `pyproject.toml`")
st.header("8. Build automated workflows")
st.header("9. Export/record dev env/dependencies")
st.header("10. Create a release on GitHub, with a DOI")
st.divider()
st.header("Part Two: using the package for research")
st.divider()
st.header("11. Create project repository and directory structure")
st.header("12. Create a research env with the new package")
st.header("13. Do analysis/research work")
st.header("14. Export/record research env")
st.header("15. Create release with DOI")