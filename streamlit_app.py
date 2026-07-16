import streamlit as st
import folium
from streamlit_folium import st_folium

from src.chat.chat_service import get_ai_response
from src.tools.maps_tool import get_route
from src.tools.speech_tool import speak


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
# Sidebar Settings
# ---------------------------------------------------
st.sidebar.title("⚙ Assistant Settings")

voice_enabled = st.sidebar.checkbox(
    "🔊 Enable Voice",
    value=False,
)

voice_speed = st.sidebar.slider(
    "Speech Speed",
    min_value=100,
    max_value=250,
    value=170,
)

voice_volume = st.sidebar.slider(
    "Volume",
    min_value=0.0,
    max_value=1.0,
    value=1.0,
)


# ---------------------------------------------------
# Username
# ---------------------------------------------------
username = st.text_input(
    "Username",
    value="guest",
)


# ---------------------------------------------------
# Chat Memory
# ---------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display Previous Messages
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

    # Store User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    # ------------------------------------------------
    # Route Request
    # ------------------------------------------------
    if "route from" in prompt.lower():

        try:

            text = prompt.lower().replace("route from", "")

            origin, destination = text.split("to")

            route = get_route(
                origin.strip(),
                destination.strip(),
            )

            response = (
                f"Route from {route['origin']} to {route['destination']}\n"
                f"Distance: {route['distance']:.1f} km\n"
                f"Duration: {route['duration']:.1f} minutes"
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": response,
                }
            )

            with st.chat_message("assistant"):

                st.write(f"📍 **From:** {route['origin']}")
                st.write(f"🏁 **To:** {route['destination']}")
                st.write(f"📏 **Distance:** {route['distance']:.1f} km")
                st.write(f"⏱ **Duration:** {route['duration']:.1f} minutes")

                display_route(route)

            if voice_enabled:
                speak(
                    response,
                    rate=voice_speed,
                    volume=voice_volume,
                )

        except Exception as e:
            st.error(e)

    # ------------------------------------------------
    # Normal AI Chat
    # ------------------------------------------------
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

        if voice_enabled:
            speak(
                answer,
                rate=voice_speed,
                volume=voice_volume,
            )