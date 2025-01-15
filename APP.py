import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

def main():
    st.set_page_config(page_title="Global Palliative Care Atlas", layout="wide")
    
    # Page title and introduction
    st.title("Global Palliative Care Atlas")
    st.write("""
    This interactive pilot application provides a virtual atlas of palliative care communities from around the world. 
    Currently, it uses sample data. Please use the sidebar to explore available filters or to upload additional data 
    in future versions. 
    """)

    # 1. Sample Data
    # --------------
    # Simulate a small dataset of palliative care communities:
    data = {
        "Community Name": ["Hope Hospice Center", "Canadian Comfort Care", "Amigos Solidarios"],
        "Country": ["Mexico", "Canada", "Peru"],
        "City": ["Mexico City", "Toronto", "Lima"],
        "Services Provided": [
            "In-home visits, Pain management, End-of-life support",
            "Bereavement counseling, Home-based palliative care, Respite care",
            "Hospice care, Psychosocial support, Family counseling"
        ],
        "Number of Volunteers": [35, 50, 20],
        "Contact Email": ["contact@hopehospice.mx", "info@cccare.ca", "amigos@solidarios.pe"],
        "Website": [
            "https://www.hopehospice.mx",
            "https://www.canadiancomfort.org",
            "https://www.amigos-solidarios.pe"
        ],
        "Latitude": [19.4326, 43.6532, -12.0464],
        "Longitude": [-99.1332, -79.3832, -77.0428]
    }

    df = pd.DataFrame(data)

    # 2. Sidebar for Filters and Other Functionalities
    # ------------------------------------------------
    st.sidebar.header("Filter & Exploration Options")
    
    # Filter by Country
    selected_country = st.sidebar.multiselect(
        "Select Country(ies):",
        options=df["Country"].unique(),
        default=df["Country"].unique()
    )
    
    # Filter by City
    # (Note: The available city options update based on the chosen country/ies)
    filtered_df_country = df[df["Country"].isin(selected_country)]
    selected_city = st.sidebar.multiselect(
        "Select City(ies):",
        options=filtered_df_country["City"].unique(),
        default=filtered_df_country["City"].unique()
    )
    
    # Filter the DataFrame using the selected country and city
    filtered_df = filtered_df_country[filtered_df_country["City"].isin(selected_city)]
    
    # 3. Display Filtered Data
    # ------------------------
    st.subheader("List of Palliative Care Communities")
    st.write("Below is the table of care communities based on your selected filters.")
    st.dataframe(filtered_df.reset_index(drop=True))
    
    # 4. Interactive Map
    # ------------------
    st.subheader("Interactive World Map of Palliative Care Communities")
    st.write("Use the map below to explore the approximate location of each community.")

    # Create a Folium map centered on a global perspective
    # (Alternatively, you could automatically center based on the data if you prefer)
    m = folium.Map(location=[20, 0], zoom_start=2)

    # Add markers for each location
    for idx, row in filtered_df.iterrows():
        popup_text = (
            f"<b>{row['Community Name']}</b><br>"
            f"Country: {row['Country']}<br>"
            f"City: {row['City']}<br>"
            f"Services: {row['Services Provided']}<br>"
            f"Volunteers: {row['Number of Volunteers']}<br>"
            f"Contact: {row['Contact Email']}<br>"
            f"<a href='{row['Website']}' target='_blank'>Website</a>"
        )
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=popup_text,
            tooltip=row["Community Name"]
        ).add_to(m)

    # Display the map in Streamlit using streamlit-folium
    st_map = st_folium(m, width=700, height=450)

    # 5. Additional Functionalities (Future Development)
    # --------------------------------------------------
    st.subheader("Future Features")
    with st.expander("Click to see what's coming next"):
        st.write("""
        - **Upload CSV or Excel files** containing more communities.
        - **Advanced Search** (e.g., filter by specific service categories, or by number of volunteers).
        - **Data Visualization** (e.g., bar charts, pie charts of services).
        - **User-Generated Feedback** to continuously update information about each community.
        - **Regional Analysis** with more detailed statistics.
        """)

    st.write("This is a pilot version. Explore the filters, interact with the map, and imagine how a complete atlas might look in the future!")

if __name__ == "__main__":
    main()
