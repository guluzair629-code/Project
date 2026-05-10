import streamlit as st

# User Information Header
st.set_page_config(page_title="Mechanical Tool", layout="centered")
st.title("Mechanical Unit Converter & Material Density Checker")
st.markdown(f"### Developed by: **Uzair Gul**")
st.markdown(f"### Roll Number: **25-ME-88**")
st.divider()

# Sidebar for Navigation
option = st.sidebar.selectbox("Select Function", ("Unit Converter", "Density Checker"))

if option == "Unit Converter":
    st.header("⚙️ Mechanical Unit Converter")
    category = st.selectbox("Select Category", ["Length", "Force", "Pressure"])
    
    val = st.number_input("Enter Value", value=1.0)
    
    if category == "Length":
        u_from = st.selectbox("From", ["Meters", "Millimeters", "Inches", "Feet"])
        u_to = st.selectbox("To", ["Meters", "Millimeters", "Inches", "Feet"])
        # Conversion Factors to Meters
        factors = {"Meters": 1.0, "Millimeters": 0.001, "Inches": 0.0254, "Feet": 0.3048}
        result = val * factors[u_from] / factors[u_to]
        
    elif category == "Force":
        u_from = st.selectbox("From", ["Newtons", "Kilonewtons", "Pound-force"])
        u_to = st.selectbox("To", ["Newtons", "Kilonewtons", "Pound-force"])
        factors = {"Newtons": 1.0, "Kilonewtons": 1000.0, "Pound-force": 4.44822}
        result = val * factors[u_from] / factors[u_to]

    elif category == "Pressure":
        u_from = st.selectbox("From", ["Pascal", "Bar", "PSI"])
        u_to = st.selectbox("To", ["Pascal", "Bar", "PSI"])
        factors = {"Pascal": 1.0, "Bar": 100000.0, "PSI": 6894.76}
        result = val * factors[u_from] / factors[u_to]

    st.success(f"**Result:** {val} {u_from} = {result:.4f} {u_to}")

else:
    st.header("🧪 Material Density Checker")
    material_data = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Iron": 7870,
        "Concrete": 2400,
        "Water": 1000,
        "Titanium": 4500
    }
    
    material = st.selectbox("Choose a Material", list(material_data.keys()))
    density = material_data[material]
    
    st.info(f"The density of **{material}** is approximately **{density} kg/m³**.")
    
    # Simple Mass Calculation
    st.subheader("Calculate Mass")
    vol = st.number_input("Enter Volume (m³)", value=1.0)
    mass = vol * density
    st.write(f"Estimated Mass: **{mass:.2f} kg**")
