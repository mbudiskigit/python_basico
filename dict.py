
cars = {}
cars['corola'] = "red"
cars['fit'] = "green"

print(cars)

print(cars.keys())

print(cars.values())

meses = dict(a="Janeiro", b="Fevereiro")

print(meses)

for key, value in cars.items():
    print(key + "=" + value)
