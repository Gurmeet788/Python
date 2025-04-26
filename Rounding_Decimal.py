import numpy as np

decimal = np.array([3.1565,65.145,-4.2545])
round_decimal = np.round(decimal, decimals = 1)
print(round_decimal)

# this round function do roundoff of number upto decimals = n;

floor_decimal = np.floor(decimal) # always rounds down.
print(floor_decimal) 

ceil_decimal = np.ceil(decimal) #  – always rounds up.
print(ceil_decimal)

trunc_decimal = np.trunc(decimal) # – chops off the decimal part (toward zero).
print(trunc_decimal)

#So for positive numbers, trunc = floor.
#The difference between them only matters for negative numbers.
#trunc → Always toward zero.
#floor → Always toward minus infinity (more negative).