import matplotlib.pyplot as plt 
import numpy as np


# Heures testées
heures = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

# Pour chaque heure : RTT moyen extrait du fichier (ou None si 100% de pertes)
rtt_aves = [17.385, 21.197, 22.434, 16.480, 25.563, 17.533, 33.681, 34.029, 18.641, 28.949]

# Taux de perte de paquets (%)
loss = [0,0,0,0,0,0,0,0,0,0]

# On ignore None pour la courbe RTT
heures_valides = [heures[i] for i in range(len(rtt_aves)) if rtt_aves[i] is not None]
rtt_valides = [rtt for rtt in rtt_aves if rtt is not None]

plt.plot(heures_valides, rtt_valides, marker='o')
plt.xlabel('Heure')
plt.ylabel('RTT moyen (ms)')
plt.title('Évolution du RTT moyen par heure (Wifi)')
plt.grid()
plt.show()

plt.plot(heures, loss, 'gs-', label='Perte %')
plt.xlabel('Heure')
plt.ylabel('Taux de perte (%)')
plt.title('Perte de paquets selon l\'heure (Wifi)')
plt.ylim(0, 110)
plt.grid()
plt.show()