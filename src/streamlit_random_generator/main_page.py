# based on https://discuss.streamlit.io/t/pip-installing-from-github/21484/5
import subprocess
import sys
import time
import streamlit as st

try:
    import streamlit_random_generator

# This block executes only on the first run when your package isn't installed
except ModuleNotFoundError as e:
    sleep_time = 30
    dependency_warning = st.warning(
        f"Installing dependencies, this takes {sleep_time} seconds."
    )
    subprocess.Popen(
        [
            f"{sys.executable} -m pip install git+https://${{github_token}}@github.com/sTomerG/streamlit_random_generator.git",
        ],
        shell=True,
    )

    # wait for subprocess to install package before running your actual code below
    time.sleep(sleep_time)
    # remove the installing dependency warning
    dependency_warning.empty()

import streamlit as st
from streamlit_random_generator.functions import random_int

st.title("Generate a random number")
st.number_input(
    "Max of random number",
    on_change=random_int,
    args=(st.session_state["randint_upper_limit"],),
    key="randint_upper_limit",
    min_value=0,
)
st.button(
    "Generate",
    on_click=random_int,
    args=(st.session_state["randint_upper_limit"],),
)
if "generated_number" in st.session_state:
    st.write(st.session_state["generated_number"])
