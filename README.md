# Global Palliative Care Atlas

This repository hosts a pilot version of the **Global Palliative Care Atlas**, an interactive web application that highlights various palliative care communities around the world. Developed using [Streamlit](https://streamlit.io/), this project aims to provide an illustrative overview of how to compile, visualise, and disseminate information on palliative care initiatives in different regions.

---

## Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Prerequisites](#prerequisites)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Structure](#structure)  
7. [Customisation](#customisation)  
8. [Future Development](#future-development)  
9. [Contributing](#contributing)  
10. [Licence](#licence)  
11. [Contact](#contact)  

---

## Overview

This project has been created as a **pilot application** to demonstrate how one might showcase palliative care communities. The data included here is purely for illustrative purposes: three sample entries have been provided to exemplify how real-world data might be managed, filtered, and displayed.

The application allows users to:
- View a table of care communities filtered by country and city.
- Interact with a world map featuring location markers for each community.
- Learn about future enhancements that could be incorporated into a large-scale deployment.

---

## Features

- **Interactive Map**: A Folium-powered map visualises the geographical locations of care communities.  
- **Filter by Country and City**: Users may narrow their search based on country and city, providing a tailored view of the dataset.  
- **Sidebar Interface**: Streamlit’s sidebar functionality enables users to modify filters and explore the data seamlessly.  
- **University Logo**: Includes the `University_College_London_logo.svg.png` at the top of the page for branding or institutional acknowledgment.  
- **Future Enhancements**: The code outlines potential developments, such as the ability to upload additional datasets and advanced analytics.

---

## Prerequisites

- **Python** 3.7+ (It is often advisable to use Python 3.10 or 3.11 for improved library compatibility).
- A working internet connection to install the required Python packages.

---

## Installation

1. **Clone this Repository**  
   Open your terminal and run:
   ```bash
   git clone https://github.com/YourUsername/your-repo-name.git
   cd your-repo-name
Create and Activate a Virtual Environment (Recommended)

bash
Copiar código
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate.bat # On Windows
Install the Dependencies

bash
Copiar código
pip install -r requirements.txt
Usage
Ensure the Logo File is Present
The file University_College_London_logo.svg.png should be in the same directory as the main Python script (app.py or similarly named file).

Run the Application

bash
Copiar código
streamlit run app.py
If all dependencies are installed and compatible, Streamlit will open a local URL (e.g., http://localhost:8501) in your browser.

Explore the Atlas

Select various Countries and Cities from the sidebar to filter the table and the map.
Click markers on the map to view community information (e.g., website link, contacts, services offered).
Structure
A simplified outline of the repository:

bash
Copiar código
your-repo-name/
│
├── app.py
├── requirements.txt
├── University_College_London_logo.svg.png
├── README.md
└── (other files/folders as needed)
app.py: Main Streamlit application code.
requirements.txt: Lists all necessary Python packages and their versions.
University_College_London_logo.svg.png: University College London logo used for branding within the application.
Customisation
Data Input: Replace the sample dictionary in app.py with your own data source (e.g., CSV, Excel, or a database connection).
Map Centring and Zoom: In app.py, adjust the arguments within folium.Map(location=[20, 0], zoom_start=2) for region-specific applications.
Future Features: The Future Features section highlights opportunities for expansion, including data visualisation and user feedback modules.
Future Development
Whilst this is merely a pilot, several enhancements are envisioned:

Data Uploads: Enable users to upload additional CSV or Excel files containing new communities.
Advanced Analytics: Integrate charts and graphs for improved data interpretation.
User Feedback: Include forms or interactive widgets allowing users to contribute updated information.
Regional Analysis: Develop region-specific insights, possibly including heatmaps and demographic overlays.
