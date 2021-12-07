import itertools

memoize = {}

def sim(valid, ndice, target):
	if target <= 0 and not valid[0]: return 1; # already won
	if ndice == 0: return 0; # lost
	if (ndice, target) + tuple(valid) in memoize:
		return memoize[(ndice, target) + tuple(valid)]
	arrangements = [1, 1, 2, 6, 24, 120, 720, 5040, 40320][ndice]
	prob = 0
	for roll in itertools.combinations_with_replacement(range(6), ndice):
		# if ndice == 6: print(roll);
		vals = [0] * 6
		weight = arrangements
		for d in roll:
			vals[d] += 1
			weight //= vals[d]
		subprob = 0
		for v in range(6):
			thisdie = (v if v > 0 else 5) * vals[v]
			if vals[v] > 0 and valid[v]:
				valid[v] = False
				subprob = max(subprob, 
							  sim(valid, ndice-vals[v], target-thisdie))
				valid[v] = True
		prob += subprob * weight / (6**ndice)
	memoize[(ndice, target) + tuple(valid)] = prob
	return prob

def precompute():
	return [sim([True]*6, 8, i) for i in range(1, 41)]

# print(precompute())

scoreprob = [0.9934260978934274, 0.9934260978934274, 0.9934260978934274, 0.9934260978934274, 0.9934260978934274, 0.9934247686293667, 0.9934165972110645, 0.9934002819443735, 0.993362459507627, 0.9932673271661979, 0.9930229839754583, 0.992575738946647, 0.9917243682786526, 0.9898606162424026, 0.9860079561222602, 0.9810130309722187, 0.9725513758120986, 0.9598255703513153, 0.9421533972031426, 0.9188722841064351, 0.8930267371507452, 0.8556015864378085, 0.8077385074741936, 0.748373333869838, 0.6803307111795139, 0.6069901896971672, 0.5247594468429354, 0.4354204654105095, 0.34629328714934277, 0.26378951946478807, 0.19401493580508045, 0.1358125206427488, 0.08677521589317928, 0.05261759391422358, 0.02890750536794545, 0.015678145193880083, 0.0075024119324905245, 0.0026855223142036996, 0.0009558554428783947, 0.00014610790700164605]
for c in range(int(input())):
	n = int(input())
	print(scoreprob[n-1])
