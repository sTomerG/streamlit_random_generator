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
