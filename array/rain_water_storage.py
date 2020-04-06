# Rain Water Storage Problems

arr = [6, 12, 3, 6, 7, 3, 1, 7, 11, 4]
m_l, m_r, s = ([], [], [])

i = 0
while i < len(arr):
  m_l.append(-1), m_r.append(-1), s.append(0)
  i+=1

i = len(arr) - 1
m = 0
while i >= 0:
  if arr[i] >= m:
    m = arr[i]
  m_r[i] = m
  i -= 1

i = 0
m = 0
while i < len(arr):
  if arr[i] >= m:
    m = arr[i]
  m_l[i] = m
  i += 1

i = 0
while i < len(arr):
  s[i] = (min(m_l[i], m_r[i]) - arr[i])
  i += 1

print("Buildings = ", arr)
print("L max =     ", m_l)
print("R max =     ", m_r)
print("Storage =   ", s)
print("total =     ", sum(s))