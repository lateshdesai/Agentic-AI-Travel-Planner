import streamlit as st
from agent.travel_agent import travel_agent

st.title("🧳 Agentic AI Travel Planner")

query = st.text_input("Enter your travel request:")

if st.button("Plan My Trip"):
    result = travel_agent(query)

    if "error" in result:
        st.error(result["error"])
    else:
        st.subheader("✈️ Flight Selected")
        st.json(result["flight"])

        st.subheader("🏨 Hotel Recommended")
        st.json(result["hotel"])

        st.subheader("📍 Places to Visit")
        for i, place in enumerate(result["places"], 1):
            st.write(f"Day {i}: {place['name']} ({place['type']}, Rating: {place['rating']})")

        st.subheader("🌦️ Weather Forecast")
        for w in result["weather"]:
            st.write(f"{w['date']}: {w['temperature']}°C")

        st.subheader("💰 Estimated Budget")
        st.success(f"₹ {result['budget']}")
