import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib

st.set_page_config( page_title="Project Layout", page_icon="📈")

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

st.title('Project layout and organisation')

st.write("Before we dig deeper into each of the **DeReLiCT** headings, let's first look at one way of organising your work.")

md_layout_01 = """
- One thing that always confused me was the best way to keep all my work tidy
- In general, my work involved:
	1. Building some form of numerical model that was somewhat generic/modular.
    2. Applying that model to specific parameters and testing various inputs/outputs.
- I tended to bump into a few questions or problems that I didn't see an obvious solution to:
	- I want to keep my codebase nice and tidy and comprehensible, but I also tend to produce lots and lots of analysis scripts, notebooks and figures as I analyse my results;
    - I want to compare my models to analytical cases to check their validity, again producing lots of various outputs, figures etc.;
    - I don't want to accidentally modify some of my numerical model code when trying to analyse my results at a later stage;
    - I want to update my core code, fix some problems and add some functionality; how do I keep track of what results I produced with which version of my code?
    - Other people would probably be able to use my model, or adapt it for their own projects, but they won't want to sift through all my iterative work in the meantime.
"""
st.write(md_layout_01)

st.header("Two-repository project layout")

font_css = """
<style>
button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
  font-size: 18px;
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

tablist = ["\u2001  Why?  \u2001","\u2001  **Package repo**  \u2001", "\u2001 **Application repo** \u2001"]

tab0, tab1, tab2 = st.tabs(tablist)
