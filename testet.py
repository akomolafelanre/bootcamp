class BinarySearch(list):
 	"""docstring for ClassName"""
	def __init__(self,a,b):
		data = range(0,a,b)
		super(BinarySearch, self).__init__(data)
		self.mylength = len(data)

	def search(self,val):
		count = 1
		index = None
		result = dict()
		result['count'] = count
		lst = self
		end_point = self.mylength
		mid_point = end_point// 2
		start_point = 0
		para = True
		while (start_point <= mid_point) and para:
			count += 1
			if lst[mid_point] == val:
				result['index'] = mid_point + 1
				para = False
				return result
			else:
				if lst[mid_point] > val:
					end_point = mid_point + 1
					mid_point = mid_point//2
				else:
					start_point = mid_point + 1
					mid_point += (end_point - mid_point)//2

		return 	"Not in list"

nb = BinarySearch(10,1)
print nb
print nb.search(20)