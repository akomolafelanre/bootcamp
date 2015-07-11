class BinarySearch(list):
  """docstring for ClassName"""
  def __init__(self,a,b):
    data = []
    data.append(b)
    current_length = 1
    while current_length < a:
      data.append(data[current_length-1] + b)
      current_length += 1
    super(BinarySearch, self).__init__(data)
    self.length = len(data)

  def search(self,val):
    count = 0
    index = None
    result = dict()
    result['count'] = count
    result['index'] = "Not in list"
    lst = self
    end_point = self.length - 1
    mid_point = end_point// 2
    start_point = 0
    para = True
    while (start_point <= mid_point) and para:
      count += 1
      if (start_point == mid_point) and (lst[start_point] > val):
        result['index'] = "Not in List"
        result['count'] = count
        para = False
        return result
      if (lst[mid_point] > val) and (mid_point - start_point == 1):
        result['index'] = 'Not in list'
        result['count'] = count
        para = False
        return result
      if lst[start_point] == val:
        result['index'] = start_point
        result['count'] = count
        para = False
        return result
      if lst[end_point] == val:
        result['index'] = end_point
        result['count'] = count
        para = False
        return result
      if lst[mid_point] == val:
        result['index'] = mid_point
        result['count'] = count
        para = False
        return result
      else:
        if lst[mid_point] > val:
          end_point = mid_point + 1
          mid_point = ((end_point - start_point)//2) + start_point
        else:
          start_point = mid_point + 1
          mid_point += (end_point - mid_point)//2
    result['count'] = count
    return result

if __name__ == "__main__":
  a = BinarySearch(100,10)
  print a
  print a.search(880)