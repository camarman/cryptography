# Lorentz Force Trajectory Calculator

# defining constant values as 1
q = -1  # charge of the particle
dt = 0.01 # time interval
m = 1  # mass of the particle

file = open("LorentzForceTrajectory.txt", "w")

Ex, Ey, Ez = (input(
    'Enter the X,Y,Z components of the Electric field respectively in V/m: ')).split(',')
Bx, By, Bz = (
    input('Enter the X,Y,Z components of the Magnetic field in Tesla: ')).split(',')

# assigning the input parameters into a vector
E0 = [Ex, Ey, Ez]
B0 = [Bx, By, Bz]


# turning data to the float
E = [float(i) for i in E0]
B = [float(i) for i in B0]


Vi = [0, 0, 0]   # initial velocity
Ri = [0, 0, 0]  # initial position


def acceleration(V, B):
    """
    Acceleration calculator

    Args:
        V [list]: The velocity vector given as a list
        B [list]: The magnetic field vector given as a list
                
    Returns:
        A: The acceleration of the particle given as a vector
    """
    Ax = (q/m) * (E[0] + (V[1] * B[2] - V[2] * B[1]))
    Ay = (q/m) * (E[1] + (V[2] * B[0] - V[0] * B[2]))
    Az = (q/m) * (E[2] + (V[0] * B[1] - V[1] * B[0]))
    A = [Ax, Ay, Az]
    return A


A0 = acceleration(Vi, B)  # calculating the initial acceleration
for n in range(1200):
    # defining the x component of the position
    Xn = Ri[0] + dt * Vi[0] + 1/2 * dt**2 * A0[0]
    # defining the y component of the position
    Yn = Ri[1] + dt * Vi[1] + 1/2 * dt**2 * A0[1]
    # defining the z component of the position
    Zn = Ri[2] + dt * Vi[2] + 1/2 * dt**2 * A0[2]
    
    # printing these components into the file
    file.write('%.5f %4.5f %4.5f\n' % (Xn, Yn, Zn))
    
    # taking these values to an array
    Rn = [Xn, Yn, Zn]  
    
    # defining an array that will calculate the acceleration for the next steps
    W = [Vi[i] + dt * A0[i] for i in range(3)]
    
    l = acceleration(W, B)
    Vtemporary_x = Vi[0] + 1/2 * dt * (A0[0] + l[0])
    Vtemporary_y = Vi[1] + 1/2 * dt * (A0[1] + l[1])
    Vtemporary_z=  Vi[2] + 1/2 * dt * (A0[2] + l[2])
    Vtemporary = [Vtemporary_x, Vtemporary_x,
                  Vtemporary_x]  # temporary velocity
    C = acceleration(Vtemporary, B)
    Vnext_x = Vi[0] + 1/2 * dt * (A0[0] + C[0])
    Vnext_y = Vi[1] + 1/2 * dt * (A0[1] + C[1])
    Vnext_z = Vi[2] + 1/2 * dt * (A0[2] + C[2])
    Vnext = [Vnext_x, Vnext_y, Vnext_z]  # the next velocity
    
    # defining the cross product corresponding to the next velocity
    A0 = acceleration(Vnext, B)
    Vi = Vnext
    Ri = Rn
    W = []
    
file.close()
