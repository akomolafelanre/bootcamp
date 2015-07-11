"""
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
  
"""
print "start"
def word(w):
  result = dict()
  a = w.split()
  print a

  for i in range(0, len(a)):
    c = result.get(a[i])
    if c == None:
      result[a[i]] = 1
    else:
      result[a[i]] += 1

  print result

word("this this this gain is how we row row")
print "Finish"