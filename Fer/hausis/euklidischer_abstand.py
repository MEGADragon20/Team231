import numpy as np

# Auf den 30.09.2024

# Erhält ein numpy-Array punkte, das zwei Punkte im Koordinatensystem (beliebiger Dimension von mindestens 1) enthält.
# punkte enthält also genau zwei Zeilen.
# Zurückgegeben wird der euklidische Abstand zwischen den beiden in punkte gespeicherten Punkten.
def euklidischer_abstand(punkte: np.ndarray) -> np.double:
    return np.sqrt((punkte[0][0]-punkte[1][0])**2+(punkte[0][1]-punkte[1][1])**2)



# Beispiel:
punkte_beispiel = np.array([[1, 1], [4, 5]]) # Ein Array mit den beiden Punkten (1, 1) und (4, 5)
print(euklidischer_abstand(punkte_beispiel)) # 5.0