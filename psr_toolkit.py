print('\033[0;35;48m ____  ____  ____    \033[0;31;48m_____           _ _    _ _   ')
print('\033[0;35;48m|  _ \/ ___||  _ \  \033[0;31;48m|_   _|__   ___ | | | _(_) |_ ')
print('\033[0;35;48m| |_) \___ \| |_) |   \033[0;31;48m| |/ _ \ / _ \| | |/ / | __|')
print('\033[0;35;48m|  __/ ___) |  _ <    \033[0;31;48m| | (_) | (_) | |   <| | |_ ')
print('\033[0;35;48m|_|   |____/|_| \_\   \033[0;31;48m|_|\___/ \___/|_|_|\_\_|\__|')

def dm_calc():
    f_lo = float(1e-9*(input('Low frequency (f_lo) (Hz): ')))
    f_hi = float(1e-9*(input('High frequency (f_hi) (Hz): ')))
    
    t_lo = float(1000*(input('\nTime of arrival of low frequency (t_lo) (sec): ')))
    t_hi = float(1000*(input('Time of arrival of high frequency (t_hi) (sec): ')))
    
    if t_lo <= t_hi:
        print('\n\033[0;31;48m[*] Low frequency arrived first. Ignoring...\033[0;32;48m')
    
    deltaT = t_lo-t_hi
    DM = deltaT/(4.149*((1/(f_lo**2))-(1/(f_hi**2))))
    
    print('DeltaT = '+str(deltaT)+' ms\nDispersion Measure (DM) = '+str(DM)+' pc/cm^3')

def pdot_calc():
    P_f = float(input('Final period (P_f) (sec): '))
    P_0 = float(input('Initial period (P_0) (sec): '))
    
    t_f = float(input('\nFinal time (t_f) (sec): '))
    t_0 = float(input('Initial time (t_0) (sec): '))
    
    deltaP = P_f-P_0
    deltaT = t_f-t_0
    
    Pdot = deltaP/deltaT
    
    print('DeltaP = '+str(deltaP)+' sec\nDeltaT = '+str(deltaT)+' sec\nPeriod Derivative (P-dot) = '+str(Pdot)+' sec/sec')

def char_age_calc():
    P = float(input('Period (P) (sec): '))
    Pdot = float(input('Period Derivative (P-dot) (sec/sec): '))
    try:
        n = float(input('Braking index (n) (leave blank for n=3): '))
    except SyntaxError:
        n = float(3)
    
    tau = P/((n-1)*Pdot)

    print('Pulsar Characteristic Age (tau) = '+str(tau)+' sec = '+str(3.17098e-8*tau)+' yr')

def min_mean_density_calc():
    P = float(input('Period (P) (sec): '))
    
    rho = 3*3.14159265/6.674e-8*P**2
    
    print('Minimum Mean Density (rho) > '+str(rho)+' g/cm^3 = '+str(1000*rho)+' kg/m^3')

def max_radius_calc():
    M = float(input('Mass (M) (g): '))
    rho = float(input('Density (rho) (g/cm^3): '))
    
    R = (3*M/(4*3.14159265*rho))**(1/3)
    
    print('Maximum Radius (R) < '+str(R)+' cm = '+str(R/1000)+' km (Maximum Diameter (D) < '+str(2*R/1000)+' km)')

def min_mass_calc():
    R = float(input('Radius (R) (cm): '))
    rho = float(input('Density (rho) (g/cm^3): '))
    
    M = R**3*4*3.14159265*rho/3
    
    print('Minimum Mass (M) > '+str(M)+' g = '+str(M/1000)+' kg')

def moment_of_inertia_calc():
    M = float(input('Mass (M) (g): '))
    R = float(input('Radius (R) (cm)'))
    
    I = (float(2)/5)*M*R**2
    
    print('Moment of Inertia (I) = '+str(I)+' g*cm^2 = '+str(10**-7*I)+' kg*m^2')

def e_rot_calc():
    I = float(input('Moment of Inertia (I) (g*cm^2): '))
    P = float(input('Period (P) (sec): '))
    
    E_rot = 2*3.14159265**2*I/P**2
    
    print('Rotational Kinetic Energy (E_rot) = '+str(E_rot)+' ergs')

while True:
    print('\n\033[1;33;48m\033[4;33;48mPulsar Tools:\033[0;32;48m')
    print('\033[1;32;48m1)\033[0;32;48m Dispersion Measure (DM)')
    print('\033[1;32;48m2)\033[0;32;48m Period Derivative (Pdot)')
    print('\033[1;32;48m3)\033[0;32;48m Characteristic Age (tau)')
    print('\033[1;32;48m4)\033[0;32;48m Minimum Mean Density (rho)')
    print('\033[1;32;48m5)\033[0;32;48m Maximum Radius (R)')
    print('\033[1;32;48m6)\033[0;32;48m Minimum Mass (M)')
    print('\033[1;32;48m7)\033[0;32;48m Moment of Inertia (I)')
    print('\033[1;32;48m8)\033[0;32;48m Rotational Kinetic Energy (E_rot)\n')

    print('\033[1;31;48m99) [Exit]\n')
    
    choice = input('\033[0;36;48mCalculate... \033[1;36;48m[1-8]\033[1;36;48m: \033[0;32;48m')
    print('\033[0;33;48m')
    if choice == 1:
        dm_calc()
    elif choice == 2:
        pdot_calc()
    elif choice == 3:
        char_age_calc()
    elif choice == 4:
        min_mean_density_calc()
    elif choice == 5:
        max_radius_calc()
    elif choice == 6:
        min_mass_calc()
    elif choice == 7:
        moment_of_inertia_calc()
    elif choice == 8:
        e_rot_calc()
    elif choice == 99:
        break

print('\033[0m')
