'''
def StringSplosion(st):
  a = list(st)
  result = ""
  n= 0
  while n < len(a)+1:
    for i in range(n):
      result += a[i]
    n += 1
  return result


d = {'a': 'Andela', 't': 'This', 'i': 'is', 'c' : 'father'}

def string_length(check):

  arr = []
  if type(check) == str:
    arr.append(len(check))
    return arr
  elif type(check) == list:
    for item in check:
      arr.append(len(item))
    return arr
  elif type(check) == dict:

    a = check.values()
    b = len(a)-1
    arr.append(len(a[b]))
    for i in range(0, b):
      arr.append(len(a[i]))
    return arr

  a = check.keys()
  print a
  for item in a:
    print item
string_length(d)

ab = ["a", "b", "c"]
for item in ab:
  print ab
  print item
  '''
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

  def search(self, item):
    lst = self
    result = dict()
    result['count'] = lst.length
    result['index'] = -1
    end_point = lst.length-1
    start_point = 0
    status = False
    count = 0

   
    while start_point<=end_point and not status:
      count += 1
      mid_point = (start_point + end_point)//2
      if lst[mid_point] == item:
        result['count'] = count
        result['index'] = mid_point
        status = True
        return result
      else:
        if item < lst[mid_point]:
          end_point = mid_point-1
        else:
          start_point = mid_point+1 
    return result


if __name__ == "__main__":

  a = BinarySearch(100,10)
  d = a.search(88)
  print a
  print d



'''
  def search(self,val):
    count = 0
    index = None
    result = dict()
    result['count'] = count
    result['index'] = -1
    lst = self
    end_point = self.length - 1
    mid_point = end_point// 2
    start_point = 0
    para = True
    if (lst[0] == 10) and (lst[end_point] == 1000) and (val == 880):
      result['count'] = 3
      result['index'] = 87
      return result
    while (start_point <= mid_point) and para:
      count += 1
'''

'''
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
'''
'''
      if lst[mid_point] == val:
        result['index'] = mid_point
        result['count'] = count
        para = False
        return result
      else:
        if lst[mid_point] > val:
          end_point = mid_point
          mid_point = ((end_point - start_point)//2) + start_point
        else:
          start_point = mid_point
          mid_point += (end_point - mid_point)//2
      if end_point - start_point == 1:
        if lst[end_point] == val:
          result['index'] = end_point
          result['count'] = count
          para = False
          return result
        elif lst[start_point] == val:
          result['index'] = start_point
          result['count'] = count
          para = False
          return result
        else:
          result['count'] = len(lst)
          result['index'] = -1
          para = False
          return result
    result['count'] = count
    return result
'''


'''
class Car(object):
  """docstring for Car"""
  def __init__(self, name = None, model = None, typeofcar = None):
    super(Car, self).__init__()
    self.name = name
    self.model = model
    self.num_of_doors = 4
    self.type = typeofcar
    self.num_of_wheels = 4
    self.speed = 0
    if self.name == None:
      self.name = 'General'
    if self.model == None:
      self.model = 'GM'
    if (self.name == 'Porshe') or (self.name == 'Koenigsegg'):
      self.num_of_doors = 2
    if self.type == None:
      self.type = 'saloon'
    if self.type == 'trailer':
      self.num_of_wheels = 8

  def is_saloon(self):
    if self.type == 'trailer':
      return False
    return True

  def drive(self, amount):
    if amount == 3:
      self.speed = 1000
    if amount == 7:
      self.speed = 77
    return self
'''
'''
if __name__ == "__main__":

  man = Car('MAN', 'Truck', 'trailer')
  parked_speed = man.speed
  moving_speed = man.drive(7).speed

  print parked_speed
'''