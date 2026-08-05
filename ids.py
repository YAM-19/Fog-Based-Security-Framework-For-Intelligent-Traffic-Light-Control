def detect_intrusion(vehicle_count, speed):
    if vehicle_count > 150:
        return "Possible DoS Attack"
    if speed < 5:
        return "Sensor Spoofing Detected"
    return "No Intrusion"
