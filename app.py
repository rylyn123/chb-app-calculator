import streamlit as st

# --- Header (Logo + Banner) ---
col1, col2 = st.columns([1,3])
with col1:
    st.image("ENHINYERO SIBIL2024.png", width=120)   # Logo
with col2:
    st.image("1.jpg", width=500)   # Banner
    st.markdown("<p style='text-align:center; font-size:20px; color:#DAA520;'>#BuildwithAnEngineer</p>", unsafe_allow_html=True)

st.markdown("---")

# --- Wall Input (Height & Length) ---
st.subheader("Wall Dimensions")
st.markdown("""
    <style>
    div[data-baseweb="input"] input {
        color: gray;
    }
    </style>
    """, unsafe_allow_html=True)
wall_height = st.number_input("Wall Height (m)", value=3.0, step=0.1)
wall_length = st.number_input("Wall Length (m)", value=3.0, step=0.1)

# --- CHB Thickness Option ---
chb_size = st.radio("Select CHB Thickness", ["4 inch", "6 inch"])

# --- Thickness Buttons for Fillet & Plaster ---
st.subheader("Set Thickness")
fillet_thickness = st.number_input("Fillet Thickness (mm)", value=38.0, step=0.01)   # 38mm default
plaster_thickness = st.number_input("Plaster Thickness (mm)", value=25.0, step=0.01) # 25mm default

# --- Calculate Button ---
if st.button("Calculate"):
    # Wall Area
    wall_area = wall_height * wall_length

    # Base CHB volume conversion per sqm (approx values gihatag nimo)
    if chb_size == "4 inch":
        chb_volume_per_sqm = 0.00324
        fillet_area_factor = 0.04
        pouring_factor = 0.0162
    else:  # 6 inch
        chb_volume_per_sqm = 0.0036
        fillet_area_factor = 0.06
        pouring_factor = 0.264

    # Plaster always same area factor
    plaster_area_factor = 0.16

    # --- CHB quantity ---
    chb_volume = wall_area * 12.5

    # --- Fillet Mix ---
    fillet_volume = fillet_area_factor * (fillet_thickness / 1000) * chb_volume
    
    # --- Pouring Mix ---
    Pouring_volume = pouring_factor * chb_volume
    # --- Plaster Mix ---
    plaster_volume = plaster_area_factor * (plaster_thickness / 1000) * chb_volume

    # --- Output Results ---
    st.success(f"Wall Area: {wall_area:.2f} sqm")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.info("🔹 Quantity of CHB")
        st.write(f"Quantity: {chb_volume:.1f} pcs")

    with col2:
        st.info("🔹 Fillet Mix")
        st.write(f"Volume: {fillet_volume:.4f} m³")
        st.write(f"Cement: {fillet_volume*9:.2f} bags")
        st.write(f"Sand: {fillet_volume*0.5:.2f} m³")

    with col3:
        st.info("🔹 Plaster Mix")
        st.write(f"Volume: {plaster_volume:.4f} m³")
        st.write(f"Cement: {plaster_volume*9:.2f} bags")
        st.write(f"Sand: {plaster_volume*0.5:.2f} m³")

    with col4:
        st.info("🔹 Pouring Mix")
        st.write(f"Volume: {Pouring_volume:.4f} m³")
        st.write(f"Cement: {Pouring_volume*9:.2f} bags")
        st.write(f"Sand: {Pouring_volume*0.5:.2f} m³")
        st.write(f"Gravel: {Pouring_volume*1:.2f} m³")
        
        

