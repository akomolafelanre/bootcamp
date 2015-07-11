'''
def countdown(n):
	print "Count Down"
	while n > 0:
		yield n
		n -= 1
c = countdown(10)
while c > 1:
	print c.next()
'''
class BinarySearch(list):
 	"""docstring for ClassName"""
	def __init__(self,a,b):
		data = range(0,a,b)
		super(BinarySearch, self).__init__(data)
		self.mylength = len(data)

	def bsearch(self,val):
		count = 1
		index = None
		result = dict()
		result['count'] = count
		lst = self
		end_point = self.mylength
		mid_point = end_point// 2
		start_point = 0
		if lst[0] == val:
			result['index'] = 0
			return result
		if lst[end_point - 1] == val:
			result['index'] = end_point - 1
			return result
		para = True
		while (start_point <= mid_point) and para:
			count += 1
			if lst[mid_point] == val:
				result['index'] = mid_point
				para = False
				return result
			else:
				if lst[mid_point] > val:
					end_point = mid_point + 1
					mid_point = mid_point//2
				else:
					start_point = mid_point + 1
					mid_point += (end_point - mid_point)//2

		result['count'] = count
		result['index'] = index
		return result		

nb = BinarySearch(10,1)
print nb
print nb.bsearch(0)