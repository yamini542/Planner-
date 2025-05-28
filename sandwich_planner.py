import streamlit as st
import math

st.title("🥪 Sandwich Planner for Café Chefs")

# Input: number of people
num_people = st.number_input("Enter number of people:", min_value=6)

# Select portion type
portion_type = st.selectbox("Choose sandwich portion per person:", ["Light (4 triangles)", "Standard (6 triangles)"])

# Define sandwich types
sandwich_types = ["Egg Mayo", "Tuna Sweetcorn", "Ham & Emmental", "Mixed Cheese"]

# Calculate triangles per person
triangles_per_person = 4 if "Light" in portion_type else 6
total_triangles = num_people * triangles_per_person
triangles_per_type = total_triangles / 4
sandwiches_per_type = math.ceil(triangles_per_type / 4)
total_sandwiches = sandwiches_per_type * 4

# Output results
st.write("### 📊 Sandwich Plan Summary")
st.write(f"👥 People: **{num_people}**")
st.write(f"🥪 Portion Type: **{portion_type}**")
st.write(f"📐 Triangles Needed: **{total_triangles}**")
st.write(f"🍽 Triangles Per Sandwich Type: **{triangles_per_type:.1f}**")
st.write(f"🧑‍🍳 Whole Sandwiches Per Type (rounded up): **{sandwiches_per_type}**")
st.write(f"📦 Total Whole Sandwiches to Prepare: **{total_sandwiches}**")

st.markdown("---")

# Friendly note for the chef
st.write("### 👨‍🍳 Chef's Note:")
if portion_type.startswith("Light"):
    st.info(f"Hey Chef! 🧑‍🍳 Each person gets **4 triangles**. So make **{sandwiches_per_type} whole sandwiches** for **each type**.\nThis will give you **4 triangles per plate** evenly across the 4 types.")
else:
    st.info(f"Hey Chef! 🧑‍🍳 Each person gets **6 triangles**. So make **{sandwiches_per_type} whole sandwiches** for **each type**.\nThis will give you **6 triangles per person**, split across all 4 flavors.")

# Table Example
st.markdown("### 🧾 Example Sandwich Flavors:")
example_data = {
    "Sandwich Type": sandwich_types,
    "Triangles Needed": [math.ceil(triangles_per_type)] * 4,
    "Whole Sandwiches Needed": [sandwiches_per_type] * 4
}
st.table(example_data)
