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

# Title of the app with responsive styling
st.markdown(
    """
    <style>
    .main {background-color: #f0f2f6;}
    .sidebar .sidebar-content {background-color: #14213d; color: white;}
    h1 {color: #e63946;}
    @media screen and (max-width: 768px) {
        h1 {
            font-size: 24px;
        }
        .sidebar .sidebar-content {
            font-size: 14px;
        }
        .main {
            padding: 0 15px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display visitor count
st.markdown(
    f"""
    <div style="background-color:#14213d; color:white; padding:10px; border-radius:5px; text-align:center;">
        <h2 style="font-size: 20px;">Welcome to OTT Subscription Plans</h2>
        <p style="font-size:16px;">Number of visitors: <strong>{visitor_count}</strong></p>
    </div>
    """,
    unsafe_allow_html=True
)

# Header with contact details
st.markdown(
    """
    <div style="background-color:#14213d; color:white; padding:10px; border-radius:5px;">
        <h1 style="text-align:center; font-size: 28px;">OTT Subscription Plans</h1>
        <h1 style="text-align:center; font-size:16px;">
            Contact us at <strong>+91-9963256467</strong>
           
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)

# OTT plans data
ott_data = [
    {"Platform": "Netflix", "Monthly": 499, "3 Months": 1497, "6 Months": 2994, "12 Months": 5988},
    {"Platform": "Amazon Prime Video", "Monthly": 249, "3 Months": 747, "6 Months": 1494, "12 Months": 2988},
    {"Platform": "Disney+", "Monthly": 399, "3 Months": 1197, "6 Months": 2394, "12 Months": 4788},
    {"Platform": "Hulu", "Monthly": 349, "3 Months": 1047, "6 Months": 2094, "12 Months": 4188},
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

# Sidebar for filtering
st.sidebar.header("Filter Plans")
platform_filter = st.sidebar.multiselect("Select Platform(s):", options=df["Platform"].unique(), default=df["Platform"].unique())
duration_filter = st.sidebar.radio("Filter by Duration:", ["All", "Monthly", "3 Months", "6 Months", "12 Months"])
device_filter = st.sidebar.radio("Select Device Type:", ["1 Device", "2 Devices"])

# Apply platform filter
filtered_df = df[df["Platform"].isin(platform_filter)]

# Apply duration filter
if duration_filter != "All":
    if device_filter == "1 Device":
        columns_to_keep = ["Platform", duration_filter]
    else:
        columns_to_keep = ["Platform", f"{duration_filter} (2 Devices)"]
    filtered_df = filtered_df[columns_to_keep]
else:
    if device_filter == "1 Device":
        filtered_df = filtered_df[["Platform", "Monthly", "3 Months", "6 Months", "12 Months"]]
    else:
        filtered_df = filtered_df[["Platform", "Monthly (2 Devices)", "3 Months (2 Devices)", "6 Months (2 Devices)", "12 Months (2 Devices)"]]

# Rename columns for clarity
filtered_df.columns = filtered_df.columns.str.replace(r" \(2 Devices\)", "")

# Add colors to the table based on the platform
platform_colors = {
    "Netflix": "#FF6347",  # Tomato
    "Amazon Prime Video": "#1E90FF",  # Dodger Blue
    "Disney+": "#FF69B4",  # Hot Pink
    "Hulu": "#32CD32",  # Lime Green
    "HBO Max": "#8A2BE2",  # Blue Violet
    "Apple TV+": "#808080",  # Gray
    "Peacock": "#FFD700",  # Gold
}

def highlight_platform(platform):
    return f"background-color: {platform_colors.get(platform, 'white')}; color: white;"

styled_df = filtered_df.style.applymap(lambda x: highlight_platform(x) if x in platform_colors else "")

# Display the styled table
st.subheader("Subscription Plans")
st.write(styled_df.to_html(escape=False), unsafe_allow_html=True)

# Footer with contact details
st.markdown(
    """
    <div style="background-color:#14213d; color:white; padding:10px; border-radius:5px; text-align:center; margin-top:20px;">
        <p style="font-size:14px;">For more information, call us at <strong>+91-1234567890</strong> or email: 
        <a href="mailto:support@ottplans.com" style="color:lightblue;">support@ottplans.com</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
