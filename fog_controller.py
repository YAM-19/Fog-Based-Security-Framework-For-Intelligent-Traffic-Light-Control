def traffic_decision(vehicle_count):
    """
    Fog-based traffic decision logic
    """

    # Heavy traffic → keep green longer
    if vehicle_count > 100:
        return "GREEN EXTENDED"

    # Moderate traffic → normal green
    elif vehicle_count > 60:
        return "GREEN NORMAL"

    # Light traffic → prepare to stop (yellow)
    elif vehicle_count > 30:
        return "YELLOW"

    # Very low traffic → stop
    else:
        return "RED"
