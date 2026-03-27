import streamlit as st

# Setup the page layout
st.set_page_config(page_title="African Cuisine Profit Simulator", layout="wide")

st.title("🍲 Efo Riro & Egusi Profit Simulator")
st.markdown("Adjust your live market prices on the left to instantly see how it affects your bottom line.")

# --- SIDEBAR: LIVE INPUT VARIABLES ---
st.sidebar.header("🛒 Market Prices (Current)")
meat_price_kg = st.sidebar.number_input("Assorted Meat (£/kg)", value=6.00, step=0.50)
spinach_price_kg = st.sidebar.number_input("Fresh Spinach (£/kg)", value=5.00, step=0.50)
egusi_price_kg = st.sidebar.number_input("Egusi Seeds (£/kg)", value=18.00, step=0.50)
palm_oil_price_l = st.sidebar.number_input("Palm Oil (£/Litre)", value=4.00, step=0.50)

st.sidebar.markdown("---")
st.sidebar.header("🏢 Overhead & Hidden Costs")
hourly_wage = st.sidebar.number_input("Your Hourly Wage (£)", value=11.44, step=0.50)
packaging_cost = st.sidebar.number_input("Takeaway Box + Bag (£)", value=0.45, step=0.05)
delivery_fee_pct = st.sidebar.slider("Deliveroo/UberEats Fee (%)", 0, 40, 30) 

# --- MAIN DASHBOARD ---
col1, col2 = st.columns(2)

# --- EFO RIRO SIMULATION ---
with col1:
    st.header("🟢 Efo Riro (10 Portions)")
    efo_prep_time = st.number_input("Hours to Cook Efo", value=2.0, step=0.5)
    efo_selling_price = st.number_input("Selling Price (£) - Efo", value=12.00, step=0.50)

    # The Math Engine
    efo_meat_cost = meat_price_kg * 1.5
    efo_spinach_cost = spinach_price_kg * 1.5
    efo_oil_cost = palm_oil_price_l * 0.25
    efo_base_flavor = 6.50 # Static estimate for aromatics/seasoning

    efo_raw_batch = efo_meat_cost + efo_spinach_cost + efo_oil_cost + efo_base_flavor
    efo_labor = efo_prep_time * hourly_wage

    efo_cost_per_portion = (efo_raw_batch + efo_labor) / 10
    efo_total_cost = efo_cost_per_portion + packaging_cost

    # Calculate after the delivery app takes its cut
    efo_net_revenue = efo_selling_price * (1 - (delivery_fee_pct / 100))
    efo_profit = efo_net_revenue - efo_total_cost
    efo_food_cost_pct = (efo_total_cost / efo_selling_price) * 100

    # Display Results
    st.markdown(f"**Total Cost to make 1 portion:** £{efo_total_cost:.2f}")
    st.markdown(f"**Actual Profit per portion:** £{efo_profit:.2f}")

    if efo_food_cost_pct > 35:
        st.error(f"Cost Margin: {efo_food_cost_pct:.1f}% (Dangerously High! Raise prices or cut meat weight.)")
    else:
        st.success(f"Cost Margin: {efo_food_cost_pct:.1f}% (Healthy & Profitable)")

# --- EGUSI SOUP SIMULATION ---
with col2:
    st.header("🟠 Egusi Soup (10 Portions)")
    egusi_prep_time = st.number_input("Hours to Cook Egusi", value=2.5, step=0.5)
    egusi_selling_price = st.number_input("Selling Price (£) - Egusi", value=13.00, step=0.50)

    # The Math Engine
    egusi_meat_cost = meat_price_kg * 1.5
    egusi_seed_cost = egusi_price_kg * 0.5
    egusi_oil_cost = palm_oil_price_l * 0.25
    egusi_base_flavor = 5.50

    egusi_raw_batch = egusi_meat_cost + egusi_seed_cost + egusi_oil_cost + egusi_base_flavor
    egusi_labor = egusi_prep_time * hourly_wage

    egusi_cost_per_portion = (egusi_raw_batch + egusi_labor) / 10
    egusi_total_cost = egusi_cost_per_portion + packaging_cost

    # Calculate after the delivery app takes its cut
    egusi_net_revenue = egusi_selling_price * (1 - (delivery_fee_pct / 100))
    egusi_profit = egusi_net_revenue - egusi_total_cost
    egusi_food_cost_pct = (egusi_total_cost / egusi_selling_price) * 100

    # Display Results
    st.markdown(f"**Total Cost to make 1 portion:** £{egusi_total_cost:.2f}")
    st.markdown(f"**Actual Profit per portion:** £{egusi_profit:.2f}")

    if egusi_food_cost_pct > 35:
        st.error(f"Cost Margin: {egusi_food_cost_pct:.1f}% (Dangerously High! Raise prices or cut meat weight.)")
    else:
        st.success(f"Cost Margin: {egusi_food_cost_pct:.1f}% (Healthy & Profitable)")
