import streamlit as st

APIS = {
    'ride_hailing': {
        'base_url': 'https://uber-ride-api.p.rapidapi.com/',
        'headers': {'X-RapidAPI-Key': st.secrets["RAPIDAPI_KEY"]}
    },
    'ecommerce': {
        'fake_store': 'https://fakestoreapi.com/'
    }
}
