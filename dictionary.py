tel = {'jack':4098, 'sape':4139}
tel['guido'] = 4235
print(tel['jack'])
del tel['sape']
tel['irv'] = 2345
print(tel)
print(list(tel))
print(sorted(tel))
print('guido' in tel)

my_dict = dict([('caleb', 8897), ('ram',7664), ('jawa',9783)])
sqr_dict = {x: x**2 for x in (2,3,4)}
kwdarg_dict = dict(hi=22, hello=44, how=23)
print(kwdarg_dict)
print(sqr_dict)
print(my_dict)