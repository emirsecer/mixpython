from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# Veri noktaları oluşturma
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x ** 2 + y ** 2))

# 3 boyutlu figür oluşturma
fig = plt.figure()
ax = plt.axes(projection='3d')

# Noktaları görselleştirme
ax.plot_surface(x, y, z, cmap='viridis')

# Eksen etiketleri ekleme
ax.set_xlabel('X Ekseni')
ax.set_ylabel('Y Ekseni')
ax.set_zlabel('Z Ekseni')

# Grafik gösterimi
plt.show()
