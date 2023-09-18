def harita():
    import folium

    # Malatya merkezinin koordinatları
    map_malatya = folium.Map (location=[38.3553, 38.3095], zoom_start=10)

    # Restoranın konumu
    restoran_lat = 38.345
    restoran_lon = 38.302

    # Restoranı haritaya ekleme
    folium.Marker ([restoran_lat, restoran_lon], popup="Restoran").add_to (map_malatya)

    # Haritayı kaydetme
    map_malatya.save ("map.html")
