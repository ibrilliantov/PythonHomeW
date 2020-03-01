import ephem

mars = ephem.Mars("2000/01/01")
print(mars)

const = ephem.constellation(mars)
print(const)