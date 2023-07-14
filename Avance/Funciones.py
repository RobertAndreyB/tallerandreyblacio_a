import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Datos de carga y deformación de la viga
carga = np.array([0, 10, 20, 30, 40, 50])  # Carga aplicada (en kN)
deformacion = np.array([0, 1, 3, 6, 10, 15])  # Deformación registrada (en mm)

# Cálculo de la deformación promedio y máxima
deformacion_promedio = np.mean(deformacion)  # Deformación promedio (en mm)
deformacion_maxima = np.max(deformacion)  # Deformación máxima (en mm)

# Creación de un DataFrame con los datos
datos = pd.DataFrame({'Carga (kN)': carga, 'Deformación (mm)': deformacion})

# Gráfica lineal carga vs. deformación
plt.plot(carga, deformacion, 'o-')
plt.xlabel('Carga (kN)')
plt.ylabel('Deformación (mm)')
plt.title('Análisis de carga y deformación en la viga')
plt.grid(True)
plt.show()
