import streamlit as st

st.set_page_config(page_title="Pro Food Simulator V2", layout="wide")

st.title("🍲 Advanced Recipe & Fraction Cost Simulator")
st.markdown("This version tracks every penny, from a single paper bag to a strip of cling film, plus your in-house delivery.")

# --- SIDEBAR: BULK INVENTORY & FRACTIONS ---
st.sidebar.header("📦 Bulk Inventory Prices")
palm_oil_4l = st.sidebar.number_input("Palm Oil (£ for 4 Litres)", value=10.50, step=0.50)
meat_price_kg = st.sidebar.number_input("Beef (£ per kg)", value=10.50, step=0.50)
spinach_price_kg = st.sidebar.number_input("Spinach (£ per kg)", value=5.00, step=0.50)

st.sidebar.markdown("---")
st.sidebar.header("🥡 Micro-Packaging Costs")
bag_250_cost = st.sidebar.number_input("Paper Bags (£ for 250)", value=17.00)
foil_roll_cost = st.sidebar.number_input("Foil Roll (£)", value=6.99)
foil_plates_per_roll = st.sidebar.number_input("Plates covered per Foil Roll", value=100)
cling_roll_cost = st.sidebar.number_input("Cling Film Roll (£)", value=10.00)
cling_plates_per_roll = st.sidebar.number_input("Plates covered per Cling Roll", value=150)
plastic_bowl_cost = st.sidebar.number_input("Plastic Takeaway Bowl (£)", value=0.15)

st.sidebar.markdown("---")
st.sidebar.header("🚗 In-House Delivery")
delivery_charge = st.sidebar.number_input("Fee charged to Customer (£)", value=3.99)
driver_pay_per_drop = st.sidebar.number_input("What you pay Driver per drop (£)", value=4.00)

# --- MAIN DASHBOARD ---
col1, col2 = st.columns(2)

with col1:
    st.header("🟢 Efo Riro Batch Calculator")
    
    batch_size = st.number_input("Plates per Batch", value=17, min_value=1)
    selling_price = st.number_input("Selling Price per Plate (£)", value=12.00, step=0.50)
    
    st.subheader("Recipe Quantities Used")
    meat_used_kg = st.number_input("Beef used (kg)", value=1.0)
    spinach_used_kg = st.number_input("Spinach used (kg)", value=0.5)
    palm_oil_used_l = st.number_input("Palm Oil used (Litres)", value=0.25)
    seasoning_cost_batch = st.number_input("Iru, Maggi, Crayfish (Total £ per batch)", value=4.50)
    
    st.subheader("Labor")
    prep_time = st.number_input("Hours to Cook Batch", value=2.0)
    hourly_wage = st.number_input("Worker Hourly Wage (£)", value=11.44)

    # --- THE MATH ENGINE ---
    # Ingredients
    cost_meat = meat_used_kg * meat_price_kg
    cost_spinach = spinach_used_kg * spinach_price_kg
    cost_oil = palm_oil_used_l * (palm_oil_4l / 4.0)
    total_ingredients_batch = cost_meat + cost_spinach + cost_oil + seasoning_cost_batch
    ingredients_per_plate = total_ingredients_batch / batch_size
    
    # Labor
    labor_per_plate = (prep_time * hourly_wage) / batch_size
    
    # Micro-Packaging per plate
    cost_per_bag = bag_250_cost / 250
    cost_per_foil = foil_roll_cost / foil_plates_per_roll
    cost_per_cling = cling_roll_cost / cling_plates_per_roll
    packaging_per_plate = cost_per_bag + cost_per_foil + cost_per_cling + plastic_bowl_cost
    
    # Final Plate Math
    total_cost_per_plate = ingredients_per_plate + labor_per_plate + packaging_per_plate
    food_profit = selling_price - total_cost_per_plate
    food_cost_pct = (total_cost_per_plate / selling_price) * 100
    
    # Delivery Math
    delivery_net = delivery_charge - driver_pay_per_drop
    total_net_profit = food_profit + delivery_net

with col2:
    st.header("📊 Your True Margins")
    
    st.markdown(f"**Cost to make 1 plate:** £{total_cost_per_plate:.2f}")
    st.markdown(f"  - *Ingredients: £{ingredients_per_plate:.2f}*")
    st.markdown(f"  - *Labor: £{labor_per_plate:.2f}*")
    st.markdown(f"  - *Packaging (inc. bags/foil): £{packaging_per_plate:.2f}*")
    
    st.markdown("---")
    st.markdown(f"**Food Profit per plate:** £{food_profit:.2f}")
    st.markdown(f"**Delivery Net:** £{delivery_net:.2f} per order")
    
    st.markdown(f"### **Total Profit in your pocket:** £{total_net_profit:.2f}")
    
    if food_cost_pct > 35:
        st.error(f"Food Cost Margin: {food_cost_pct:.1f}% (A bit high, consider adjusting prices or portions!)")
    else:
        st.success(f"Food Cost Margin: {food_cost_pct:.1f}% (Healthy & Profitable!)")
