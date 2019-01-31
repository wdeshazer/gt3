from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


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


def grid_visualize(data, plottype='contour'):
    try:
        psi_data = data.core.psi_data
    except ValueError:
        print('Data must contain core information')

    fig = plt.figure(figsize=(6, 6))
    if plottype == 'contour':
        CS = plt.contour(psi_data.R, psi_data.Z, psi_data.psi)
        plt.clabel(CS, inline=1, fontsize=10)
        plt.xlabel('Radius (R)')
        plt.ylabel('Axial Location (Z)')
    elif plottype == 'surf':
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(psi_data.R, psi_data.Z, psi_data.psi,
                               cmap=cm.coolwarm,
                               linewidth=0, antialiased=False)
        # Customize the z axis.
        ax.set_zlim(-1.01, 1.01)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

        # Add a color bar which maps values to colors.
        fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

    pass
