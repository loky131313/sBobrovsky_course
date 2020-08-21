def odometer(oksana):
    Distance = 0
    for values in oksana:
        speed_list = [values for i,values in enumerate(oksana) if not i%2]
    for speed in speed_list:
        Distance = Distance + speed
    return Distance
