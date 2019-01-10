import matplotlib.pyplot as plt
from gt3 import gt3

fontsize = 16

d3d_144977_3000 = \
    gt3('144977_3000/togt3_d3d_144977_3000', mode='thermaliol')

forb_species_d3d = plt.figure(figsize=(6, 6))
ax1 = forb_species_d3d.add_subplot(1, 1, 1)
ax1.set_title(r'$F_{orb}$ on DIII-D for various species', fontsize=fontsize)
ax1.set_xlim(0, 1.0)
ax1.set_xlabel(r'normalized radius ($\rho$)')
ax1.plot(d3d_144977_3000.core.rho[:, 0], d3d_144977_3000.iol.forb_d_therm[:, 0], lw=2, label='Thermal Deuterium')
ax1.plot(d3d_144977_3000.core.rho[:, 0], d3d_144977_3000.iol.forb_t_therm[:, 0], lw=2, label='Thermal Tritium')
ax1.plot(d3d_144977_3000.core.rho[:, 0], d3d_144977_3000.iol.forb_c_therm[:, 0], lw=2, label='Thermal Carbon')
ax1.plot(d3d_144977_3000.core.rho[:, 0], d3d_144977_3000.iol.forb_a_therm[:, 0], lw=2, label='Thermal Alphas')
ax1.plot(d3d_144977_3000.core.rho[:, 0], d3d_144977_3000.iol.forb_a_fast[:, 0], lw=2, label='Fast Alphas')
ax1.legend()

plt.show()
