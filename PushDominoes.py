class Solution(object):
	def pushDominoes(self, dominoes):
		forces = [0]* len(dominoes)
		maxForce = len(dominoes)
		force = 0

		for i, d in enumerate(dominoes):
			if d == 'R':
				force = maxForce
			if d == 'L':
				force = 0
			else:
				force = max(0, force-1)
			forces[i] = force

		for i in range(len(dominoes)-1,-1,-1):
				d = dominoes[i]
				if d == 'L':
					force = maxForce
				if d == 'R':
					force = 0
				else:
					force = max(0, force-1)
				forces[i] -= force

		result = ''
		for f in forces:
			if f == 0:
				result += '.'
			elif f > 0:
				result += 'R'
			else:
				result += 'L'
		return result

print(Solution().pushDominoes('..R...L..R.'))