from lists import lists_generator

a = lists_generator.generate()

# b não é um novo objeto, é apenas uma referência (setinha nova) para o mesmo objeto, no mesmo local
# da memória.
b = a

a.pop()
print(b)

print(a is b)
print(id(a))
print(id(b))

# Para de fato copiar e ter um novo objeto, é necessário usar o comando .copy()
b = a.copy()
print(a is b)
print(id(a))
print(id(b))