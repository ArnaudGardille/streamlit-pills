import streamlit as st

from streamlit_pills import pills

options = [
    "General widgets",
    "Charts",
    "Images",
    "Video",
    "Text",
    "Maps & geospatial",
    "Dataframes & tables",
    "Molecules & genes",
    "Graphs",
    "3D",
    "Code & editors",
    "Page navigation",
    "Authentication",
    "Style & layout",
    "Developer tools",
    "App builders",
    "Integrations with other tools",
    "Collections of components",
]

icons = [
    "🧰",
    "📊",
    "🌇",
    "🎥",
    "📝",
    "🗺️",
    "🧮",
    "🧬",
    "🪢",
    "🧊",
    "✏️",
    "📃",
    "🔐",
    "🎨",
    "🛠️",
    "🏗️",
    "🔌",
    "📦",
]

selected = pills("Select a category", options, icons, index=None)
st.write(selected)

st.button("foo")