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

# --- MIX ratio Option ---
options = [
    "M5 *(1:5:10) not advisable*",
    "M7.5 *(1:4:8)*",
    "M10 *(1:3:6)*",
    "M15 *(1:2:4)*",
    "M20 *(1:1.5:3)*",
    "M25 *(1:1:2)*"
]
mixture_ratio = st.radio("Select Mixture Ratio", options)

# --- Thickness Buttons for Fillet & Plaster ---
st.subheader("Set Thickness")
fillet_thickness = st.number_input("Fillet Thickness (mm)", value=38.0, step=0.01)   # 38mm default
plaster_thickness = st.number_input("Plaster Thickness (mm)", value=25.0, step=0.01) # 25mm default

# --- Mixture data (assumed units: cement = bags per m³, sand = m³ per m³, gravel = m³ per m³, water = L per m³) ---
mixture_data = {
    options[0]: {"cement": 4.0, "sand": 0.5,  "gravel": 0.96, "water": 7},
    options[1]: {"cement": 5.0,"sand": 0.5,  "gravel": 0.95, "water": 8},
    options[2]: {"cement": 6.0,"sand": 0.46,  "gravel": 0.92, "water": 11},
    options[3]: {"cement": 8.0, "sand": 0.44, "gravel": 0.90,   "water": 14},  # example values
    options[4]: {"cement": 10.0, "sand": 0.42, "gravel": 0.85,  "water": 18},  # example values
    options[5]: {"cement": 14.0, "sand": 0.385, "gravel": 0.8,   "water": 20},  # example values
}

# --- Calculate Button ---
if st.button("Calculate"):
    # Wall Area
    wall_area = wall_height * wall_length

    # Base CHB volume conversion per sqm (approx values you used earlier)
    if chb_size == "4 inch":
        chb_volume_per_sqm = 0.00324
        fillet_area_factor = 0.04
        pouring_factor = 0.0162
    else:  # 6 inch
        chb_volume_per_sqm = 0.0036
        fillet_area_factor = 0.06
        pouring_factor = 0.0264

    # --- CHB quantity (you used *12.5 earlier; keep if that's your pcs per sqm factor) ---
    chb_volume = wall_area * 12.5  # pcs

    # --- Volumes for fillet, pouring, plaster ---
    fillet_volume = fillet_area_factor * (fillet_thickness / 1000) * chb_volume
    pouring_volume = pouring_factor * chb_volume
    plaster_area_factor = 0.16
    plaster_volume = plaster_area_factor * (plaster_thickness / 1000) * chb_volume

    # --- Fetch selected mix data ---
    mix = mixture_data.get(mixture_ratio)
    if not mix:
        st.error("Mixture ratio not found. Please select a valid option.")
    else:
        # Calculate material quantities (scale per m³ factors by volume)
        # Fillet
        fillet_cement_bags = fillet_volume * mix["cement"]
        fillet_sand_m3 = fillet_volume * mix["sand"]
        fillet_water_l = fillet_volume * mix["water"]

        # Plaster
        plaster_cement_bags = plaster_volume * mix["cement"]
        plaster_sand_m3 = plaster_volume * mix["sand"]
        plaster_gravel_m3 = plaster_volume * mix["gravel"]
        plaster_water_l = plaster_volume * mix["water"]

        # Pouring
        pouring_cement_bags = pouring_volume * mix["cement"]
        pouring_sand_m3 = pouring_volume * mix["sand"]
        pouring_gravel_m3 = pouring_volume * mix["gravel"]
        pouring_water_l = pouring_volume * mix["water"]

        # --- Output Results ---
        st.success(f"Wall Area: {wall_area:.2f} sqm")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.info("🔹 Quantity of CHB")
            st.write(f"Quantity: {chb_volume:.1f} pcs")

        with col2:
            st.info("🔹 Fillet Mix")
            st.write(f"Volume: {fillet_volume:.4f} m³")
            st.write(f"Cement: {fillet_cement_bags:.2f} bags")
            st.write(f"Sand: {fillet_sand_m3:.3f} m³")
            st.write(f"Water: {fillet_water_l:.2f} L")

        with col3:
            st.info("🔹 Plaster Mix")
            st.write(f"Volume: {plaster_volume:.4f} m³")
            st.write(f"Cement: {plaster_cement_bags:.2f} bags")
            st.write(f"Sand: {plaster_sand_m3:.3f} m³")
            st.write(f"Water: {plaster_water_l:.2f} L")

        with col4:
            st.info("🔹 Pouring Mix")
            st.write(f"Volume: {pouring_volume:.4f} m³")
            st.write(f"Cement: {pouring_cement_bags:.2f} bags")
            st.write(f"Sand: {pouring_sand_m3:.3f} m³")
            st.write(f"Gravel: {pouring_gravel_m3:.3f} m³")
            st.write(f"Water: {pouring_water_l:.2f} L")


