import csv
import numpy as np
import matplotlib.pyplot as plt

def sigma(funct_list, x):
    return sum(f(x) for f in funct_list)

def bell(t1, t3, c):
    def f(t):
        if t <= t3 and t >= t1:
            return(c * (t - t1)**2 * (t - t3)**2)
        else:
            return(0)
    return f

def d_bell(t1, t3, c):
    def g(t):
        if t <= t3 and t >= t1:
            return 2*c * (t - t1) * (t - t3) * (2*t - t1 - t3)
        else:
            return 0
    return g

donations = open('days_gift_amount.csv', 'r')
reader = csv.reader(donations, delimiter=',')

offset = 100
profiles = dict()
d_profiles = dict()

for row in reader:
    funct_list = []
    d_funct_list = []
    x1 = []
    x3 = []
    b = []
    id_num = int(row[0])
    dates_list = row[1]
    dates = dates_list.split(",")
    amounts_list = row[2]
    amounts = amounts_list.split(",")

    slen = len(dates)
    if slen > 5:
        index = 0
        while (slen > index):
            left = int(dates[index]) - offset
            right = int(dates[index]) + offset

            t = int(dates[index])
            d = float(amounts[index])

            coeff = (30*d)/(right-left)**5

            x1.append(left)
            x3.append(right)
            b.append(coeff)
            funct_list.append(bell(x1[-1], x3[-1], b[-1]))
            d_funct_list.append(d_bell(x1[-1], x3[-1], b[-1]))
            
            index += 1
        
        profiles[id_num] = funct_list
        d_profiles[id_num] = d_funct_list

donor_list = list(profiles.keys())
d_donor_list = list(d_profiles.keys())

fx = plt.subplot(2, 1, 1)
fprimex = plt.subplot(2, 1, 2)

for j in range(2, 23):
    # accounts for first 20-ish donors with >5 donations
    x = np.arange(-100, 1000, 1)
    y = []
    dy = []
    for i in range(len(x)):
        y.append(sigma(profiles[donor_list[j]], x[i]))
        dy.append(sigma(d_profiles[d_donor_list[j]], x[i]))
    fx.plot(x, y)
    fprimex.plot(x, dy)

fx.set_title('Donor Donation Behavior')
fx.set_ylabel('Donation rate ($/day)')
fprimex.set_ylabel('Rate of Donation Rate (\$/day$^2$)')
fprimex.set_xlabel('Time (days)')
plt.savefig('2 through 23 donors donation behavior.png')
plt.show()

donations.close()

# potential idea: use a while loop to graph different functions
