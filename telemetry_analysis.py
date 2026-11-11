import os
import fastf1
import fastf1.plotting
import matplotlib.pyplot as plt
import numpy as np

# 1. Configuración de entorno y caché local
os.makedirs('cache', exist_ok=True)
fastf1.Cache.enable_cache('cache') 
fastf1.plotting.setup_mpl(misc_mpl_mods=False)

# 2. Carga de la sesión (Pole Position GP de España 2024)
YEAR = 2024
GRAND_PRIX = 'Spanish Grand Prix'
SESSION_TYPE = 'Q'

session = fastf1.get_session(YEAR, GRAND_PRIX, SESSION_TYPE)
session.load()

# 3. Extracción de vueltas rápidas (Actualizado a pick_drivers para evitar warnings)
driver_ref = 'NOR'
driver_cmp = 'VER'

lap_ref = session.laps.pick_drivers(driver_ref).pick_fastest()
lap_cmp = session.laps.pick_drivers(driver_cmp).pick_fastest()

# 4. Obtención de telemetría completa
tel_ref = lap_ref.get_telemetry()
tel_cmp = lap_cmp.get_telemetry()

# 5. Cálculo del delta de tiempo continuo mediante interpolación (NumPy)
ref_d = tel_ref['Distance'].values
cmp_d = tel_cmp['Distance'].values
ref_t = tel_ref['Time'].dt.total_seconds().values
cmp_t = tel_cmp['Time'].dt.total_seconds().values

# Interpolamos el tiempo del coche 2 a las distancias exactas del coche 1
cmp_t_interp = np.interp(ref_d, cmp_d, cmp_t)
delta_time = cmp_t_interp - ref_t

# 6. Configuración visual del análisis
color_ref = fastf1.plotting.get_driver_color(driver_ref, session=session)
color_cmp = fastf1.plotting.get_driver_color(driver_cmp, session=session)

fig, ax = plt.subplots(4, 1, figsize=(13, 9), sharex=True, 
                       gridspec_kw={'height_ratios': [2.5, 1.2, 1.2, 1.5]})
fig.patch.set_facecolor('#0e1117')

for a in ax:
    a.set_facecolor('#161b22')
    a.grid(True, linestyle='--', alpha=0.3, color='#8b949e')
    a.tick_params(colors='#c9d1d9', labelsize=9)
    for spine in a.spines.values():
        spine.set_color('#30363d')

# Subplot 1: Velocidad (km/h)
ax[0].plot(tel_ref['Distance'], tel_ref['Speed'], color=color_ref, label=f"{driver_ref} ({lap_ref['LapTime'].total_seconds():.3f}s)", lw=1.6)
ax[0].plot(tel_cmp['Distance'], tel_cmp['Speed'], color=color_cmp, label=f"{driver_cmp} ({lap_cmp['LapTime'].total_seconds():.3f}s)", lw=1.6)
ax[0].set_ylabel('Speed (km/h)', color='#c9d1d9', fontsize=10, fontweight='bold')
ax[0].legend(loc='lower right', facecolor='#0e1117', edgecolor='#30363d', labelcolor='#c9d1d9')
ax[0].set_title(f"{YEAR} {GRAND_PRIX} - Q3 Telemetry Delta: {driver_ref} vs {driver_cmp}", color='#ffffff', fontsize=13, fontweight='bold', pad=12)

# Subplot 2: Posición de acelerador (%)
ax[1].plot(tel_ref['Distance'], tel_ref['Throttle'], color=color_ref, lw=1.4)
ax[1].plot(tel_cmp['Distance'], tel_cmp['Throttle'], color=color_cmp, lw=1.4)
ax[1].set_ylabel('Throttle (%)', color='#c9d1d9', fontsize=10, fontweight='bold')

# Subplot 3: Freno (Activación binaria/presión)
ax[2].plot(tel_ref['Distance'], tel_ref['Brake'], color=color_ref, lw=1.4)
ax[2].plot(tel_cmp['Distance'], tel_cmp['Brake'], color=color_cmp, lw=1.4)
ax[2].set_ylabel('Brake', color='#c9d1d9', fontsize=10, fontweight='bold')

# Subplot 4: Delta Time (Segundos)
ax[3].plot(tel_ref['Distance'], delta_time, color='#ffffff', lw=1.8)
ax[3].axhline(0, color='#8b949e', linestyle=':', alpha=0.8)
ax[3].set_ylabel(f"Delta to {driver_ref} (s)", color='#c9d1d9', fontsize=10, fontweight='bold')
ax[3].set_xlabel('Lap Distance (m)', color='#c9d1d9', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('telemetry_comparison.png', dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
print("Análisis generado con éxito: telemetry_comparison.png")