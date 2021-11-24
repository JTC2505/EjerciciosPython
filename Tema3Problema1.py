import matplotlib.pyplot as plt

fig, ax = plt.subplots()

nombres = ['Juan','Ana','Pablo','Ximena','Jorge']
datos = [90,188,78,194,93]
ax.pie(datos, labels = nombres)
plt.title('Resultados Votaciones Escolares Colegio -Las Flores-')

plt.show()
