import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import altair as alt
import matplotlib

st.set_page_config(page_title="Sustainable Software Development", page_icon="🌠")

# with open( ".streamlit/style.css" ) as css:
#     st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

st.image("assets/cover_2.png")

md_header="""
#### Sustainable Software Development and Writing FAIR Research Code
"""

md_intro=""" 
Access this page at **software-dev.streamlit.app**
"""


# st.write(md_header)

st.write(md_intro)

st.subheader("Tutorial format")

md_intro_01="""
1. We will first look at general topics that are important, and then see how we can apply these to an actual project.
    - Day 1 will focus on concepts; you can then research more between sessions.
    - Day 2 will apply these concepts to a mini-project.
2. This webapp will stay live; however, I may update it and change the content going forward. Since it is on GitHub, you will be able to find older versions and can `fork` your own copy to snapshot it. Feel free to download the presentation pdfs.
3. This is intended as a life-raft to researchers adrift in a sea of messy code. We will be focusing on *good-enough* software dev practises, not *best* practices, because...

### Anything worth doing well, is worth doing poorly at first!

Perfectionism is the enemy of progress, and a bunch of other clichés.

- Sometimes online software development tutorials or articles assume you are starting from scratch in a completely new clean project, and don't give you any path to improve existing code;
- Sometimes tutorials/articles assume *all you are doing is software dev* and don't recognise that this is being balanced against other research work;
- Sometimes tutorials/articles are not tailored towards research project workflows.

To try to fill this gap, this session will hopefully:
- Introduce you to some practises/methods/tools that you can research further following the course;
- Provide *both* some good-practise workflows for starting a new research project, *as well as* some useful tools and advice for grappling with a pre-existing project;
- Instill the importance of good research computing practises, without overwhelming you to the point of sticking your head in the sand and avoiding it!
"""
st.write(md_intro_01)


st.header("Introduction presentation")
components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vSV0N_UzZEqwzBTMn8QE-u3Fsqbeb1-GUOVu9_CWLE031orIUhaPo1xYgjhWuuypMf8L9129SZrB6gE/embed?start=false&loop=false&delayms=60000", height=450)

md_intro_02="""
### Introduction session links

- [FAIR Principles](https://www.go-fair.org/fair-principles/)
- [Five Recommendations for FAIR Software](https://fair-software.nl/)
- [Software Sustainability Institute](https://www.software.ac.uk/)
- [Codespaces/devcontainer template repository](https://github.com/murphyqm/python-project-template)

"""

st.write(md_intro_02)


st.markdown('<p style="text-align: center;">Copyright © 2024 Maeve Murphy Quinlan</p>', unsafe_allow_html=True)


md_quick_links = """
## Useful links

- Python Project Template (GitHub): [bit.ly/python-template](https://bit.ly/python-template)
- GitHub Discussions (for polls etc.): [bit.ly/gh_discussions](https://bit.ly/gh_discussions)
"""

with st.sidebar:
    st.write(md_quick_links)