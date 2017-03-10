def to_celsius(temp):
    return (temp - 32)*5/9

def avg_temperature(filename):
    tmins = []
    tmaxs = []

    with open('temperature.csv', 'r') as f:
        for line in f:
            tmin, tmax = map(float, line.split(','))
            tmins.append(to_celsius(tmin))
            tmaxs.append(to_celsius(tmax))

    with open('temperature_celsius.csv', 'w') as f:
        for tmin, tmax in zip(tmins, tmaxs):
            f.write('{:.2f},{:.2f}\n'.format(tmin, tmax))

    avg_temp = (sum(tmins) + sum(tmaxs))/(len(tmins) + len(tmaxs))

    return avg_temp

if __name__ == '__main__':
    print('The average temperature is {:.2f} degrees celsius.'.format(avg_temperature('temperatures.csv')))
