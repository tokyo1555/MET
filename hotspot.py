import matplotlib.pyplot as plt

# Heures testées
heures = [14, 15, 17, 18, 20, 21, 22, 23]

# Pour chaque heure : RTT moyen extrait du fichier (ou None si 100% de pertes)
rtt_aves = [None, 63.441, 174.715, 153.168, 86.157, 203.979, 151.902, 88.353]

# Taux de perte de paquets (%)
loss = [100, 3, 3, 0, 3, 17, 1, 1]

# On ignore None pour la courbe RTT
heures_valides = [heures[i] for i in range(len(rtt_aves)) if rtt_aves[i] is not None]
rtt_valides = [rtt for rtt in rtt_aves if rtt is not None]

plt.plot(heures_valides, rtt_valides, marker='o')
plt.xlabel('Heure')
plt.ylabel('RTT moyen (ms)')
plt.title('Évolution du RTT moyen par heure (SFR)')
plt.grid()
plt.show()

plt.plot(heures, loss, 'gs-', label='Perte %')
plt.xlabel('Heure')
plt.ylabel('Taux de perte (%)')
plt.title('Perte de paquets selon l\'heure (SFR)')
plt.ylim(0, 110)
plt.grid()
plt.show()
