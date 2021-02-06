from math import pi, tan, cos

g = 9.81  # m/s^2
v0 = 44  # m/s
theta_deg = 80  # from horizontal (shooting upwards)
theta_rad = theta_deg*(pi/180)
x = 0.5  # m (horizontal distance travelled)
y0 = 1  # m (initial height)

vert_height_no_grav = y0 + (x * tan(theta_rad))
# print(vert_height_no_grav)

numerator = g * (x**2)
denominator = 2 * ((v0 * cos(theta_rad))**2)

y = vert_height_no_grav - (numerator/denominator)
print(y)
print(round(y,2))
