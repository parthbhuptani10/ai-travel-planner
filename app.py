import streamlit as st
import pickle

# Page configuration
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🌍",
    layout="centered"
)

model = pickle.load(open("travel_model.pkl", "rb"))

st.title("🌍 AI Travel Planner for Students")
st.write("Plan your personalized trip using AI-powered recommendations.")

st.divider()

# Input Layout (2 Columns)
col1, col2 = st.columns(2)

with col1:
    place = st.text_input("🌍 Enter Destination (Goa, Paris, Tokyo, Jaipur)")

with col2:
    season = st.selectbox("🌤 Select Season", ["Summer", "Winter", "Monsoon"])

budget = st.number_input("💰 Enter Budget (₹)", min_value=1000)
days = st.number_input("📅 Number of Days", min_value=1)

season_map = {"Summer": 0, "Winter": 1, "Monsoon": 2}
season_value = season_map[season]

st.divider()

# Destination Database
place_data = {
    "Goa": {
        "description": "Goa is famous for beaches, nightlife, Portuguese heritage and water sports.",
        "attractions": ["Baga Beach", "Calangute Beach", "Fort Aguada", "Dudhsagar Falls"],
        "food": ["Goan Fish Curry", "Prawn Balchão", "Bebinca"],
        "experience": "Enjoy beach sunsets, water sports and vibrant nightlife."
    },
    "Paris": {
        "description": "Paris is known for art, fashion, romance and iconic landmarks.",
        "attractions": ["Eiffel Tower", "Louvre Museum", "Notre Dame Cathedral", "Seine River Cruise"],
        "food": ["Croissant", "Macarons", "French Cheese"],
        "experience": "Explore romantic streets and world-class museums."
    },
    "Tokyo": {
        "description": "Tokyo blends futuristic technology with traditional culture.",
        "attractions": ["Shibuya Crossing", "Tokyo Tower", "Sensoji Temple", "Akihabara"],
        "food": ["Sushi", "Ramen", "Tempura"],
        "experience": "Experience anime culture, temples and modern city life."
    },
    "Jaipur": {
        "description": "Jaipur is the Pink City known for royal heritage and architecture.",
        "attractions": ["Amber Fort", "Hawa Mahal", "City Palace", "Jantar Mantar"],
        "food": ["Dal Baati Churma", "Ghewar", "Laal Maas"],
        "experience": "Explore majestic forts and Rajasthani culture."
    }
}

if st.button("🚀 Generate Travel Plan"):

    prediction = model.predict([[budget, days, season_value]])
    category = prediction[0]

    # 🔥 Add this highlight box here
    st.markdown(
        f"""
        <div style='padding:15px; border-radius:10px; background-color:#1f3b4d; color:white;'>
        <h4>🌍 Destination: {place}</h4>
        <p>🎯 Travel Style: {category}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("🎯 Travel Style Recommendation")
    st.success(category)

    st.divider()

    if place in place_data:

        data = place_data[place]

        st.subheader(f"🌍 About {place}")
        st.write(data["description"])

        st.divider()

        st.subheader("📍 Top Attractions")
        for attr in data["attractions"]:
            st.write(f"• {attr}")

        st.divider()

        st.subheader("🍽 Famous Local Food")
        for food in data["food"]:
            st.write(f"• {food}")

        st.divider()

        st.subheader("✨ Special Experience")
        st.write(data["experience"])

        st.divider()

        # Budget Breakdown
        st.subheader("💰 Estimated Budget Breakdown")
        stay = int(budget * 0.4)
        food_cost = int(budget * 0.3)
        travel_cost = int(budget * 0.3)

        colA, colB, colC = st.columns(3)
        colA.metric("Stay", f"₹{stay}")
        colB.metric("Food", f"₹{food_cost}")
        colC.metric("Local Travel", f"₹{travel_cost}")

        st.divider()

        # Day-wise Itinerary
        st.subheader("📅 Suggested Day-wise Itinerary:")

        attractions = data["attractions"]
        extra_experiences = [
            "Explore local markets and shopping streets",
            "Try famous local food and cafes",
            "Attend cultural shows or local events",
            "Relax and enjoy scenic spots"
        ]

        for day in range(1, days + 1):

            if day <= len(attractions):
                st.write(f"Day {day}: Visit {attractions[day-1]} and explore nearby attractions.")
            else:
                extra_index = (day - len(attractions) - 1) % len(extra_experiences)
                st.write(f"Day {day}: {extra_experiences[extra_index]}.")

st.divider()
st.caption("Developed as part of AI & ML Virtual Internship Project")