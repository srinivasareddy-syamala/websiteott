import streamlit as st
import pandas as pd
import os

# Path for the counter file
counter_file = "counter.txt"

# Initialize counter if it doesn't exist
if not os.path.exists(counter_file):
    with open(counter_file, 'w') as f:
        f.write("0")

# Read the current counter value
with open(counter_file, 'r') as f:
    visitor_count = int(f.read().strip())

# Increment the counter
visitor_count += 1

# Update the counter value in the file
with open(counter_file, 'w') as f:
    f.write(str(visitor_count))

# Streamlit native theming for modern UI
st.set_page_config(page_title="OTT Subscription Plans", layout="wide")

# WhatsApp chat link
whatsapp_number = "+9163256467"
whatsapp_link = f"https://wa.me/{whatsapp_number[1:]}"

# Header section with WhatsApp link
st.title("OTT Subscription Plans")
st.markdown(
    f"""
    <p style="font-size:16px;">
        Contact us at <strong>{whatsapp_number}</strong> 
        <a href="{whatsapp_link}" target="_blank" style="text-decoration:none;">
            <img src="https://img.icons8.com/color/48/000000/whatsapp.png" alt="WhatsApp" style="vertical-align:middle; margin-left:8px;">
        </a>
    </p>
    """,
    unsafe_allow_html=True
)
st.markdown(f"**Number of visitors:** {visitor_count}")

# OTT plans data
ott_data = [
    {"Platform": "Netflix 4k", "Monthly": 100, "3 Months": 200, "6 Months": 500, "12 Months": 700},
    {"Platform": "Amazon Prime Video 4k", "Monthly": 100, "3 Months": 300, "6 Months": 500, "12 Months": 700},
    {"Platform": "Disney+ 4k", "Monthly": 100, "3 Months": 300, "6 Months": 500, "12 Months": 800},
    {"Platform": "You Tube Premium 4k", "Monthly": 349, "3 Months": 1047, "6 Months": 2094, "12 Months": 4188},
    {"Platform": "HBO Max", "Monthly": 449, "3 Months": 1347, "6 Months": 2694, "12 Months": 5388},
    {"Platform": "Apple TV+", "Monthly": 299, "3 Months": 897, "6 Months": 1794, "12 Months": 3588},
    {"Platform": "Peacock", "Monthly": 249, "3 Months": 747, "6 Months": 1494, "12 Months": 2988},
]

# Convert data to a pandas DataFrame
df = pd.DataFrame(ott_data)

# Add a column for 2 devices (₹50 extra cost)
df["Monthly (2 Devices)"] = df["Monthly"] + 50
df["3 Months (2 Devices)"] = df["3 Months"] + 50
df["6 Months (2 Devices)"] = df["6 Months"] + 50
df["12 Months (2 Devices)"] = df["12 Months"] + 50

# Sidebar filters
with st.sidebar:
    st.header("Filter Plans")
    platform_filter = st.multiselect("Select Platform(s):", options=df["Platform"].unique(), default=df["Platform"].unique())
    duration_filter = st.radio("Filter by Duration:", ["All", "Monthly", "3 Months", "6 Months", "12 Months"])
    device_filter = st.radio("Select Device Type:", ["1 Device", "2 Devices"])

# Apply filters
filtered_df = df[df["Platform"].isin(platform_filter)]

if duration_filter != "All":
    columns_to_keep = ["Platform", duration_filter] if device_filter == "1 Device" else ["Platform", f"{duration_filter} (2 Devices)"]
    filtered_df = filtered_df[columns_to_keep]
else:
    columns_to_keep = ["Platform", "Monthly", "3 Months", "6 Months", "12 Months"] if device_filter == "1 Device" else \
        ["Platform", "Monthly (2 Devices)", "3 Months (2 Devices)", "6 Months (2 Devices)", "12 Months (2 Devices)"]
    filtered_df = filtered_df[columns_to_keep]

# Clean column names for better display
filtered_df.columns = [col.replace(" (2 Devices)", "") for col in filtered_df.columns]

# Display table
st.subheader("Available Subscription Plans")
st.dataframe(filtered_df.style.set_table_styles([
    {'selector': 'th', 'props': [('font-family', 'Roboto, sans-serif'), ('font-size', '14px'), ('background-color', '#14213d'), ('color', 'white')]},
    {'selector': 'td', 'props': [('font-family', 'Roboto, sans-serif'), ('font-size', '12px')]},
]))

# Footer section with WhatsApp link
st.markdown("---")
st.markdown(
    f"""
    <p style="font-size:14px; text-align:center;">
        For more details, call us at <strong>{whatsapp_number}</strong> 
        <a href="{whatsapp_link}" target="_blank" style="text-decoration:none;">
            <img src="https://img.icons8.com/color/48/000000/whatsapp.png" alt="WhatsApp" style="vertical-align:middle; margin-left:8px;">
        </a>
    </p>
    """,
    unsafe_allow_html=True
)
