import ephem

jupiter = ephem.Sirius('2019/05/30')
const = ephem.constellation(jupiter)
print(const)