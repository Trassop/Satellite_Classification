# Selecting relevant columns and handling missing values
satellite_data = load_data()
columns_required = ["Class of Orbit", "Type of Orbit", "Perigee (Kilometers)", "Apogee (Kilometers)", "Inclination (Degrees)"]
processed_data = satellite_data[columns_required].copy()
