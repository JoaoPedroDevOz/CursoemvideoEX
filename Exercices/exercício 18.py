from math import radians, sin, cos, tan

ang = float(input('Enter a angle:'))

s = sin(radians(ang))
print('The angle {} has the sin {:.2f}'.format(ang, s))

c = cos(radians(ang))
print('The angle {} has the cosine {:.2f}'.format(ang, c))

tg = tan(radians(ang))
print('The angle {} has the tangent {:.2f}'.format(ang, tg))