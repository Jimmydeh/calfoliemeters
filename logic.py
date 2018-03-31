number_c = input('aantal cm folie: ')
number_b = input('diameter bok: ')
number_a = input('dikte folie in mm: ')

print int ((((number_c*2+number_b)*(number_c*2+number_b)*0.785)-(number_b*number_b)*0.785)/(number_a*10))
