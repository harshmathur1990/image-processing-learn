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


def actual_plot(unknown_H, height_of_paraxial_ray, power, refractive_index, conjugate_variable):
    x = []
    y = []
    start_x = -5
    interval = 0.5
    end_x = 5
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    for i in frange(start_x, end_x, interval):
        x.append(i)
        y.append(get_S1(height_of_paraxial_ray, power, refractive_index, i, conjugate_variable) * 0.125)

    ax1.plot(x,y, label='S1/8')

    ax1.set_xlabel('Shape Factor')

    z = []
    for i in x:
       z.append(get_S2(unknown_H, height_of_paraxial_ray, power, refractive_index, i, conjugate_variable) * 0.5)

    ax2 = fig.add_subplot(111)

    ax2.plot(x, z, label='S2/2')

    ax2.set_xlabel('Shape Factor')

    fig.legend()

    fig.show()


def plot(unknown_H, height_of_paraxial_ray, power, refractive_index, conjugate_variable_list):
    for conjugate_variable in conjugate_variable_list:
        actual_plot(unknown_H, height_of_paraxial_ray, power, refractive_index, conjugate_variable)

