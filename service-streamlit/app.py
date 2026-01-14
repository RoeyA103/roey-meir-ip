import pandas as pd
import streamlit as st
import hashlib
from numpy.random import default_rng
from requests import Session
import os

url = os.getenv("DATABASE_API_URL","http://redis-api-svc:8080/locations")

def get_color_from_ip(ip):
    hash_object = hashlib.md5(ip.encode())
    return f"#{hash_object.hexdigest()[:6]}"

st.set_page_config(page_title="IP Geolocation Map", layout="wide")
st.title("Live IP Connections")

rng = default_rng(0)
session = Session()

try:
    response = session.get(url, timeout=5)
    response.raise_for_status()
    coord = response.json()  # this is a LIST

    rows = []
    for item in coord:
        ip = item["ip"]
        lat = float(item["coordinates"]["lat"])
        lon = float(item["coordinates"]["lon"])

        jitter = rng.standard_normal(2) / 50

        rows.append({
            "lat": lat + jitter[0],
            "lon": lon + jitter[1],
            "ip": ip,
            "color": get_color_from_ip(ip)
        })

    df = pd.DataFrame(rows)

    if not df.empty:
        st.map(df, latitude='lat', longitude='lon', color='color')
        
        with st.expander("View Raw Data"):
            df_show= df[['ip', 'lat', 'lon']]
            st.dataframe(df_show)
    else:
        st.warning("No IP data found.")


except Exception as e:
    st.error(f"Failed to connect to the IP service: {e}")