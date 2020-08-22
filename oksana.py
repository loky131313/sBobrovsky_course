def odometer(oksana):
    speed_list = [values for i,values in enumerate(oksana) if not i%2]
    time_list = [values for i,values in enumerate(oksana) if i%2]
    Distance = speed_list[0]*time_list[0]
    for i in range(1, (len(speed_list))):
        Distance += speed_list[i]*(time_list[i]-time_list[i-1])
        i += 1
    return Distance


