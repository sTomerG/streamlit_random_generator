import streamlit as st
import numpy as np


def random_int(x: int):
    st.session_state["generated_number"] = np.random.randint(0, x + 1)
