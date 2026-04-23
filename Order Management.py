import streamlit as st
import pandas as pd

# 1. Mock Data Setup
clients = {
    "Global Ventures LLC": "Qualified",
    "Local Retail Co.": "Non-Qualified"
}

securities = pd.DataFrame({
    "Security Name": ["Apple Inc. (AAPL)", "SM Prime Holdings (SMPH)", "Tesla Motors (TSLA)", "BDO Unibank (BDO)"],
    "Type": ["Offshore", "Local", "Offshore", "Local"],
    "Currency": ["USD", "PHP", "USD", "PHP"]
})

# 2. UI Layout
st.title("Order Management System Prototype")
st.subheader("New Order Entry")

# Client Selection
selected_client = st.selectbox("Select Client:", list(clients.keys()))
client_status = clients[selected_client]

st.info(f"Client Status: **{client_status}**")

# 3. Core Business Logic Validation
if client_status == "Qualified":
    # Show all securities (Offshore & Local)
    available_securities = securities
else:
    # Filter to show ONLY Local securities
    available_securities = securities[securities["Type"] == "Local"]

# 4. Order Form
st.markdown("### Select Security")
selected_security = st.selectbox("Available Securities:", available_securities["Security Name"])

# Display currency and type dynamically
sec_details = available_securities[available_securities["Security Name"] == selected_security].iloc[0]
st.write(f"**Security Type:** {sec_details['Type']}")
st.write(f"**Settlement Currency:** {sec_details['Currency']}")

quantity = st.number_input("Quantity", min_value=1, step=1)

if st.button("Place Order"):
    st.success(f"Order validated and placed: {quantity} shares of {selected_security} for {selected_client}.")
