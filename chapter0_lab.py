#0.5.1 find num of mins in week
hour = 60
day = 24
week = 7
mins_in_week = hour * day * week
print(mins_in_week, 'num mins in week')

#0.5.2 find remainder w/out %
num_div = 2304811//43
remainder = 2304811 - (43 * num_div)
print(remainder, 'remainder')

#0.5.3 eval boolean expression
print(((673 + 909)//3) == 0)

#0.5.4 predict value of expression with x = -9 and y = 1/2. Pred: 2 actual answer 1
#thought that -9 + 10 was less than zero. sad
x = -9
y = 1/2

#0.5.4 predict value of expression with x = -9 and y = 1/2. Pred: 2 actual answer 1
#thought that -9 + 10 was less than zero. sad
x = -9
y = 1/2
print(2**(y+1/2) if x + 10 < 0 else 2**(y-1/2))
print(2**(y+1/2) if x + 10 < 0 else 2**(y-1/2))

#0.5.5 write a comprehension that squares each value in {1,2,3,4,5}
print([x**2 for x in {1,2,3,4,5}])

#0.5.6 write a comprehension that raises 2 to the powers in set {0,1,2,3}
print([2**x for x in {0,1,2,3}])

#0.5.7 alter the sets used from {1,2,3} & {2,3,4} so that the image is 9 values instead of 7
print(len([x*y for x in {1,2,3} for y in {4,5,6}]))

#0.5.8 replace the sets in the comprehension from {1,2,3} and {2,3,4} so that the image is |5|
#with non-overlapping values
print(len({x*y for x in {0,1,2} for y in {4,8,16}}))

#0.5.9 without using the intersection operator, find the intersection between two sets
print({x for x in {1,2,3,4} if x in {3,4,5,6}})

#0.5.10 write an expression whose value is the average of the list [20, 10, 15, 75]
l = [20, 10, 15, 75]
print(sum(l)/len(l))

#0.5.11 write a double list comprehension whose output is a list containing the cartesian
#product of ['a', 'b', 'c'] and [1,2,3]
print([[x,y] for x in ['a', 'b', 'c'] for y in [1,2,3]])

#0.5.12 write an expression that sums a bunch of lists //
lofl = [[.25, .75, .1], [-1, 0], [4,4,4,4]]
#print(sum([sum([x],[]) for x in lofl]), [])  almost working, syntax issue

#
