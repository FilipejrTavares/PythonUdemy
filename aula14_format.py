

a= 'A'

b= 'BBBB'

c= 1.111111111

formato_1 = 'a={} b={} c={:.2f} and not c={}'.format(a,b,c,a)

formato_2 = 'a={0} b={1} c={2:.2f} and not c={0}'.format(a,b,c)

formato_3 = 'a={0} b={1} c={num_3:.2f} and not c={0}'.format(a,b,num_3 = c)

print(formato_1)
print(formato_2)
print(formato_3)