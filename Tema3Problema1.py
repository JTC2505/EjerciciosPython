## Referencia: Visite: https://numython.github.io/posts/2016/02/graficas-de-barras-en-matplotlib/
import matplotlib.pyplot as plt



#fig = plt.figure(u'Gráfica de barras') # Figure
##ax = fig.add_subplot(111) # Axes

fig, ax = plt.subplots()

nombres = ['Juan','Ana','Pablo','Ximena','Jorge']
datos = [90,188,78,194,93]
ax.pie(datos, labels = nombres)
plt.title('Resultados Votaciones Escolares Colegio -Las Flores-')

plt.show()
