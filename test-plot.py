from pathlib import Path

import streamlit as st

st.title("Test sankey")

available_sankeys = list([1, 2])
sankey = st.selectbox("Select a sankey", available_sankeys)

sankey_path = Path("Sankeys") / f"test_sankey{sankey}.svg"
with sankey_path.open(encoding="utf8") as file:
	svg_content = file.read()

st.markdown(f'<div style="justify-content: center;">{svg_content}</div>', unsafe_allow_html=True)


