preco = float(input())
v_per = float(input())

precod = preco-(preco*v_per/100)
precom = preco+(preco*v_per/100)

print(('{:.2f}'.format(precom)))
print(('{:.2f}'.format(precod)))


