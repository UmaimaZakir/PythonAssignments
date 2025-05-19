import streamlit as st

st.set_page_config(page_title=" Unit Converter App", layout="centered")

# Title and subtitle
st.markdown("<h1 style='text-align: center; color: teal;'> Unit Converter App</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Convert Length, Weight, and Temperature units easily</h4>", unsafe_allow_html=True)
st.write("---")

Units = {
    "Length": ["CM", "Inch", "Feet", "Meter"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Weight": ["Gm", "Kilogram", "Pound"]
}

# Input container
with st.container():
    st.markdown("<h4 style='color: teal;'>🔧 Choose Conversion Options</h4>", unsafe_allow_html=True)
    category = st.selectbox("Select Category", list(Units.keys()))
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From Unit", Units[category])
    with col2:
        to_unit = st.selectbox("To Unit", Units[category])
    value = st.number_input("Enter Value", value=0.0, step=0.1)

# Conversion logic
def unit_conversion(category, from_unit, to_unit, value):
    if category == "Length":
        conversions = {
            "CM": 1,
            "Inch": 2.54,
            "Feet": 30.48,
            "Meter": 100
        }
        return value * conversions[from_unit] / conversions[to_unit]

    elif category == "Weight":
        conversions = {
            "Gm": 1,
            "Kilogram": 1000,
            "Pound": 453.592
        }
        return value * conversions[from_unit] / conversions[to_unit]

    elif category == "Temperature":
        if from_unit == to_unit:
            return value
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
    return None

# Result box
if st.button("🔄 Convert"):
    result = unit_conversion(category, from_unit, to_unit, value)
    if result is not None:
        with st.container():
            st.markdown("<div style='padding:20px; background-color:#e0f7fa; border-radius:10px;'>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color: teal;'>✅ Result: {result:.2f} {to_unit}</h3>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.error("❌ Conversion not possible.")
