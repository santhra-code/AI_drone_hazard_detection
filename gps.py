import time

# Simulated NMEA sentence
nmea_sentence = "$GPGGA,123456.00,3723.2475,N,12202.8934,W,1,12,1.0,100.0,M,0.0,M,,*6F"

# Function to parse GPGGA sentence
def parse_gpgga(sentence):
    parts = sentence.split(',')
    
    if parts[0] == "$GPGGA":
        time_utc = parts[1]
        latitude = parts[2]
        lat_direction = parts[3]
        longitude = parts[4]
        lon_direction = parts[5]
        fix_quality = parts[6]
        num_satellites = parts[7]
        altitude = parts[9]
        
        # Output parsed data
        print(f"Time (UTC): {time_utc}")
        print(f"Latitude: {latitude} {lat_direction}")
        print(f"Longitude: {longitude} {lon_direction}")
        print(f"Fix Quality: {fix_quality}")
        print(f"Satellites in use: {num_satellites}")
        print(f"Altitude: {altitude} meters")
    else:
        print("Not a GPGGA sentence")

# Simulate reading GPS data and parsing it, limiting to 10 iterations
for i in range(10):
    parse_gpgga(nmea_sentence)
    
    # Simulate a delay as if new GPS data is received
    time.sleep(1)