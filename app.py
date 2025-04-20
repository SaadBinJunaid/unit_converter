import streamlit as st

# Custom CSS styling for gradient background and UI
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to right, #6A11CB, #2575FC);
            color: white;
        }

        div.stButton > button {
            background-color: #FFD700;
            color: black;
            border-radius: 10px;
            font-weight: bold;
            padding: 10px 20px;
        }
        div.stButton > button:hover {
            background-color: #FFC107;
        }

        .stSelectbox, .stTextInput {
            border-radius: 10px;
            padding: 5px;
        }

        label {
            color: white !important;
            font-weight: bold;
        }
        
        div[data-testid="stNotification"], div.stAlert {
            background-color: white !important;
            color: black !important;
            font-weight: bold;
            padding: 15px;
            border-radius: 10px;
            border: 2px solid #FFD700;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.title("🚀 Google-Like Unit Converter ⚡")

# Define unit categories and conversion factors
unit_categories = {
    "Length": {
        "meters": 1,
        "kilometers": 1000,
        "miles": 1609.34,
        "feet": 0.3048,
        "inches": 0.0254,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "yards": 0.9144,
    },
    "Weight": {
        "kilograms": 1,
        "grams": 0.001,
        "pounds": 0.453592,
        "ounces": 0.0283495,
        "tons": 1000,
    },
    "Temperature": "special",  # handled separately
    "Volume": {
        "liters": 1,
        "milliliters": 0.001,
        "gallons": 3.78541,
        "cups": 0.24,
    },
    "Time": {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600,
        "days": 86400,
        "weeks": 604800,
        "months": 2.628e+6,
        "years": 3.154e+7,
    },
    "Speed": {
        "meters per second": 1,
        "kilometers per hour": 0.277778,
        "miles per hour": 0.44704,
        "knots": 0.514444,
    },
    "Energy": {
        "joules": 1,
        "calories": 4.184,
        "kilowatt-hours": 3.6e+6,
        "electronvolts": 1.602e-19,
    },
    "Pressure": {
        "pascals": 1,
        "bars": 100000,
        "atmospheres": 101325,
        "psi": 6894.76,
    },
    "Data Storage": {
        "bytes": 1,
        "kilobytes": 1024,
        "megabytes": 1024 ** 2,
        "gigabytes": 1024 ** 3,
        "terabytes": 1024 ** 4,
        "petabytes": 1024 ** 5,
    },
}

# Dropdown to select category
category = st.selectbox("Select unit type:", list(unit_categories.keys()))

# Determine units based on category
if category == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
else:
    units = list(unit_categories[category].keys())

# Dropdowns for from/to units
from_unit = st.selectbox("Convert from:", units)
to_unit = st.selectbox("Convert to:", units)

# Input for value to convert
value_input = st.text_input("Enter value:", value="1")

# Validate input
try:
    if "." in value_input:
        value = float(value_input)
    else:
        value = int(value_input)
except ValueError:
    st.error("Please enter a valid number.")
    st.stop()

# Conversion logic
def convert_units(category, value, from_unit, to_unit):
    if category == "Temperature":
        if from_unit == to_unit:
            return value
        if from_unit == "Celsius":
            return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15)
        if from_unit == "Fahrenheit":
            return (value - 32) * 5/9 if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15)
        if from_unit == "Kelvin":
            return value - 273.15 if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32)
    else:
        base_value = value * unit_categories[category][from_unit]
        return base_value / unit_categories[category][to_unit]

# Button and result
if st.button("Convert"):
    if value > 0 or category == "Temperature":  # allow 0 or negatives for temp
        result = convert_units(category, value, from_unit, to_unit)
        st.success(f"Converted value: {result:.4f} {to_unit}")
    else:
        st.error("Please enter a valid number greater than 0.")
