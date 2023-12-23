import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, slider, option box, etc.
st.title("Weather Forecast for the Next Days:")
place = st.text_input("Place:")
days = st.slider("Forecast days", min_value=1, max_value=5)
option = st.selectbox("Select data to view", ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {place}')

try:
    if place:
        # Get data from backend
        filtered_data = get_data(place, days)
        # Create graph/plot
        if option == 'Temperature':
            temperatures = [dict['main']['temp']/10 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={'x': "Dates", 'y': 'Temperature [C]'})
            st.plotly_chart(figure)
            
        if option == 'Sky':
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            images = {"Clear":'images/clear.png',
                    "Clouds":'images/cloud.png',
                    "Rain":'images/rain.png',
                    "Snow":'images/snow.png'}
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths,width=120)
except KeyError:
    st.subheader("No such Place on earth")
# Social media links
st.markdown(
    """
    <style>
    .social-media {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 50px;
    }
    .social-media a {
        margin: 0 30px;
        text-decoration: none;
        color: #4a4a4a;
    }
    </style>
    """
    , unsafe_allow_html=True)
st.markdown(
    """
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    </head>
    """
    , unsafe_allow_html=True)

st.markdown(
    """
    <div class="social-media">
        <a href="https://www.twitter.com/krshxcx"><i class="fab fa-twitter"></i></a>
        <a href="https://github.com/krshxcx"><i class="fab fa-github"></i></a>
        <a href="https://www.instagram.com/krshxcx"><i class="fab fa-instagram"></i></a>
        <a href="https://www.linkedin.com/in/saikrishna-durgam/"><i class="fab fa-linkedin"></i></a>
    </div>
    """
    , unsafe_allow_html=True)
                
