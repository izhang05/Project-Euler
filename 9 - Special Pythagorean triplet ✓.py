"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""
for c in range(334,500):
	for b in range(1,334):
		if c**2 == b**2 + (1000-c-b)**2:
			print((1000-c-b)*b*c)
			print(1000-c-b, b, c)