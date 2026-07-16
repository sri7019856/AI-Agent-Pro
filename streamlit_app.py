import streamlit as st
import folium
from streamlit_folium import st_folium

from src.chat.chat_service import get_ai_response
from src.tools.maps_tool import get_route


# ---------------------------------------------------
# Display Route on Map
# ---------------------------------------------------
def display_route(route):

    m = folium.Map(
        location=route["start"],
        zoom_start=7,
    )

    # Start Marker
    folium.Marker(
        route["start"],
        popup=route["origin"],
        tooltip="Start",
        icon=folium.Icon(color="green"),
    ).add_to(m)

    # Destination Marker
    folium.Marker(
        route["end"],
        popup=route["destination"],
        tooltip="Destination",
        icon=folium.Icon(color="red"),
    ).add_to(m)

    # Route Line
    coords = [
        [lat, lon]
        for lon, lat in route["geometry"]
    ]

    folium.PolyLine(
        coords,
        weight=5,
        color="blue",
    ).add_to(m)

    st_folium(
        m,
        width=900,
        height=500,
    )


# ---------------------------------------------------
# Streamlit Config
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
)

st.title("🤖 AI Assistant")


# ---------------------------------------------------
# Username
# ---------------------------------------------------
username = st.text_input(
    "Username",
    value="guest"
)


# ---------------------------------------------------
# Chat Memory
# ---------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# ---------------------------------------------------
# Chat Input
# ---------------------------------------------------
prompt = st.chat_input("Ask me anything...")


# ---------------------------------------------------
# Process User Input
# ---------------------------------------------------
if prompt:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    # -----------------------------------------------
    # MAP REQUEST
    # -----------------------------------------------
    if "route from" in prompt.lower():

        try:

            text = prompt.lower().replace("route from", "")

            origin, destination = text.split("to")

            route = get_route(
                origin.strip(),
                destination.strip(),
            )

            with st.chat_message("assistant"):

                st.write(f"📍 **From:** {route['origin']}")
                st.write(f"🏁 **To:** {route['destination']}")
                st.write(f"📏 **Distance:** {route['distance']:.1f} km")
                st.write(f"⏱ **Duration:** {route['duration']:.1f} minutes")

                display_route(route)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content":
                        f"Route from {route['origin']} to {route['destination']}\n"
                        f"Distance: {route['distance']:.1f} km\n"
                        f"Duration: {route['duration']:.1f} minutes"
                }
            )

        except Exception as e:

            st.error(e)

    # -----------------------------------------------
    # NORMAL AI CHAT
    # -----------------------------------------------
    else:

        with st.spinner("Thinking..."):

            answer = get_ai_response(
                username,
                prompt,
            )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        with st.chat_message("assistant"):
            st.write(answer)