import streamlit as st
import plotly.express as px
from backend import get_data

st.set_page_config(
    page_title="Weather Forecast",
    page_icon="🌤️",
    layout="wide"
)

st.title("Shonamma's Weather Forecast")
st.subheader("Weather Forecast for the Next Days")

place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5)

option = st.selectbox(
    "Select data to view",
    ("Temperature", "Sky")
)

st.subheader(f"{option} for the next {days} days in {place}")

try:
    if place:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [
                item["main"]["temp"]
                for item in filtered_data
            ]

            dates = [
                item["dt_txt"]
                for item in filtered_data
            ]

            figure = px.line(
                x=dates,
                y=temperatures,
                labels={
                    "x": "Date",
                    "y": "Temperature (°C)"
                },
                title=f"Temperature Forecast for {place}"
            )

            st.plotly_chart(figure, use_container_width=True)

        elif option == "Sky":
            sky_conditions = [
                item["weather"][0]["main"]
                for item in filtered_data
            ]

            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png"
            }

            image_paths = [
                images.get(condition, "images/cloud.png")
                for condition in sky_conditions
            ]

            st.image(image_paths, width=120)

except KeyError:
    st.error("No such place found.")
except Exception as e:
    st.error(f"Error: {e}")

st.markdown("---")
st.markdown(
    """
### Connect with Me

- GitHub: https://github.com/krshxcx
- LinkedIn: https://www.linkedin.com/in/saikrishna-durgam/
- Instagram: https://www.instagram.com/krshxcx
- Twitter: https://twitter.com/krshxcx
"""
)
