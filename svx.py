import matplotlib.pyplot as plt


def frange(start, end, step):
    tmp = start
    while(tmp < end):
        yield tmp
        tmp += step

"""
Spherical Aberration
"""
def get_S1(height_of_paraxial_ray, power, refractive_index, shape_factor, conjugate_variable):
    return float(height_of_paraxial_ray**4 * power**3 / 4) * float( ( ( (refractive_index+2)/ ( refractive_index * (refractive_index-1)**2 ) ) * ( (shape_factor - ((2 * (refractive_index**2 - 1) * conjugate_variable )/ (refractive_index+2)) )**2 ) ) + ( (refractive_index/(refractive_index-1))**2 - ((refractive_index/(refractive_index+2)) * conjugate_variable**2) ) )

"""
Coma Aberration
"""
def get_S2(unknown_H, height_of_paraxial_ray, power, refractive_index, shape_factor, conjugate_variable):
    return float(0.5 * unknown_H * height_of_paraxial_ray**2 * power**2) * float(((refractive_index+1)*shape_factor)/(refractive_index * (refractive_index-1)) - ((( (2 * refractive_index) + 1 ) / refractive_index ) * conjugate_variable))


def actual_plot(unknown_H, height_of_paraxial_ray, power, refractive_index, conjugate_variable, fig1, fig2):
    x = []
    y = []
    start_x = -5
    interval = 0.5
    end_x = 5
    ax1 = fig1.add_subplot(111)
    for i in frange(start_x, end_x, interval):
        x.append(i)
        y.append(get_S1(height_of_paraxial_ray, power, refractive_index, i, conjugate_variable) * 0.128)

    ax1.plot(x,y, label='K={}'.format(power))

    ax1.set_xlabel('Shape Factor')
    ax1.set_ylabel('Aberration S1/8 in units of wavelength')

    ax1.set_title('Spherical Aberration: S1/8 for Y={}'.format(conjugate_variable))

    z = []
    for i in x:
       z.append(get_S2(unknown_H, height_of_paraxial_ray, power, refractive_index, i, conjugate_variable) * 0.5)

    ax2 = fig2.add_subplot(111)

    ax2.plot(x, z, label='K={}'.format(power))

    ax2.set_xlabel('Shape Factor')
    ax2.set_ylabel('Aberration S2/2 in units of wavelength')
    ax2.set_title('Coma Aberration: S2/2 for Y={}'.format(conjugate_variable))


def plot(unknown_H, height_of_paraxial_ray, power_list, refractive_index, conjugate_variable_list):

    for conjugate_variable in conjugate_variable_list:
        fig1 = plt.figure()
        fig2 = plt.figure()
        for power in power_list:
            actual_plot(unknown_H, height_of_paraxial_ray, power, refractive_index, conjugate_variable, fig1, fig2)

        fig1.legend()
        fig2.legend()

        fig1.show()
        fig2.show()