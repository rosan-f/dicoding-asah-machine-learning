import matplotlib.pyplot as plt
import numpy as np

# Data sederhana
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])  

# Visualisasi
plt.scatter(X, y, color='blue', label='Data Points')  
plt.plot(X, y, color='red', label='Garis Linear')     
plt.xlabel('Luas Rumah')
plt.ylabel('Harga Rumah')
plt.title('Contoh Linear Relationship')
plt.legend()
plt.show()
