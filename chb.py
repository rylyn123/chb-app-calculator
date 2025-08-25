import streamlit as st

def calculate_chb(length, height, size):
    if size == "4 inch":
        thickness = 0.10
        vol_chb = 0.008
    elif size == "6 inch":
        thickness = 0.15
        vol_chb = 0.012
    else:
        return None

    wall_volume = length * height * thickness
    num_chb = wall_volume / vol_chb
    return round(num_chb)

st.set_page_config(page_title="CHB Calculator", page_icon="🧱", layout="centered")

st.title("🧱 Concrete Hollow Block (CHB) Calculator")
st.write("Simple tool to estimate CHB requirements for masonry walls.")

# --- Inputs ---
length = st.number_input("Wall Length (m)", min_value=0.0, step=0.1, format="%.2f")
height = st.number_input("Wall Height (m)", min_value=0.0, step=0.1, format="%.2f")
size = st.selectbox("CHB Size", ["4 inch", "6 inch"])

# --- Button ---
if st.button("Calculate"):
    result = calculate_chb(length, height, size)
    if result:
        st.success(f"Estimated Quantity of CHB: **{result} pcs**")
    else:
        st.error("Please select CHB size.")
