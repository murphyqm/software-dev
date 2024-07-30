import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import altair as alt
import matplotlib

st.set_page_config(page_title="DeReLiCT Code", page_icon="📈")

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

st.title("Applying the FAIR principles to your code: DeReLiCT!")
st.write("Basic steps to help avoid total code collapse. Add some scaffolding to your scientific code with the",
         "**DeReLiCT** acronym: **De**pendencies, **Re**pository, **Li**cense, **C**itation, **T**esting.")

st.write("*Note that the examples given are specific to Python, but similar methods/approaches/tools can be used for/applied to projects using different languages.*")

font_css = """
<style>
button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
  font-size: 24px;
}
</style>
"""

st.markdown("""
<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 2px;
    }

	.stTabs [data-baseweb="tab"] {
		height: 50px;
        white-space: pre-wrap;
		background-color: #F0F2F6;
		border-radius: 4px 4px 0px 0px;
		gap: 1px;
		padding-top: 10px;
		padding-bottom: 10px;
    }

	.stTabs [aria-selected="true"] {
  		background-color: #FFFFFF;
	}

</style>""", unsafe_allow_html=True)

st.write(font_css, unsafe_allow_html=True)

tablist = ["\u2001  **De**  \u2001", "\u2001 **Re** \u2001", "\u2001 **Li** \u2001", "\u2001 **C** \u2001", "\u2001 **T** \u2001", "\u2001 More! \u2001"]



tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(tablist)

md_dependencies = """
## Dependencies

> Dependencies are the versions of different packages/modules that your code depends on, for example the version of Python you are using, and any libraries you have to import, like `matplotlib`, `scipy`, `tensorflow` etc.

Dependencies are an important thing to keep track of when building scientific code. How many different external libraries does your code depend on? What versions of these libraries does it need? How do you install and update these different libraries?

### Package management

In Python, there are lots of different ways to install and manage packages and dependencies. These different tools generally invovle using virtual environments
in order to keep the dependencies for different projects separate and tidy.
Some package installation and management tools include:

- [Conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)/[Mamba](https://mamba.readthedocs.io/en/latest/)
    - If using Conda/Mamba we recommend installing with [Miniforge](https://github.com/conda-forge/miniforge)
- [pip](https://packaging.python.org/en/latest/key_projects/#pip)
- [pixi](https://packaging.python.org/en/latest/key_projects/#pip)
- [Poetry](https://python-poetry.org/)

You can read more about Python package management tool recommendations [here](https://packaging.python.org/en/latest/guides/tool-recommendations/). The package management tool you use will vary depending on whether you want to build your code into a package itself, or are relying primarily on external libraries. Some of these package managers include entire workflows for building and publishing Python packages, while others focus on organising pre-existing packages.

Due to its widespread use in the research community, our examples are going to use
`conda` in conjunction with some other tools for package building.
"""

md_repository = """
"""

md_license = """

"""

md_citation = """
"""

md_testing = """

"""

md_more = """

"""

with tab1:
    
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQF-shEdPlDcEvzPGuAkdgCsMTTPRQKB_b4YqbKhLzg8lBuCkDHYtBBbWmxrufmbK02FWqHEV7T0CP9/embed?start=false&loop=false&delayms=3000", height=450)
    st.write(md_dependencies)

with tab2:
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSMwoFMvL_BAK_-pdifK_8jVjJ_UAOfGsh5g-HFsTqrOZ6ZYVpXL179fFOJdsRs4n64Ns3rPjY0RJn8/embed?start=false&loop=false&delayms=3000", height=450)
    st.write(md_repository)

with tab3:
    st.write(md_license)

with tab4:
    st.write(md_citation)

with tab5:
    st.write(md_testing)