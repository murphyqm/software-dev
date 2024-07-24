import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib

st.set_page_config( page_title="Two repo layout", page_icon="📈")

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

st.title('Two-repository project layout')

st.write("Basic steps to help avoid total code collapse. Add some scaffolding to your scientific code with the",
         "**DeReLiCT** acronym: **De**pendencies, **Re**pository, **Li**cense, **C**itation, **T**esting.",
         "Click through the tabs below to find out more.")

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
