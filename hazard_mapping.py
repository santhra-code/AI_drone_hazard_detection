import folium

# Create map
hazard_map = folium.Map(location=[11.0168, 76.9558], zoom_start=12)  # Set initial location

# Add hazards
hazards = [(11.0168, 76.9558), (11.0170, 76.9560)]  # Example hazard coordinates
for hazard in hazards:
    folium.Marker(hazard, popup="Hazard Detected").add_to(hazard_map)

# Save map
hazard_map.save("hazard_map.html")