import streamlit as st
import functions as f
st.title("Art Prompt App")
st.subheader("These are your Art Prompts")

APrompts = f.get_prompts()


def add_prompt():
    prompt = st.session_state["new_prompt"] + "\n"
    APrompts.append(prompt)
    f.write_prompts(APrompts)


for P in APrompts:
    st.checkbox(P)

st.text_input(label="enter a prompt", placeholder="like happy chaos... introduce drama", on_change=add_prompt,
              key="new_prompt")
