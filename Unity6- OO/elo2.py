def SeatingStudents(arr):

  total_desks = arr[0]

  occupied_desks = set(arr[1:])

  count = 0

  # code goes here
  
  for i in range(1, total_desks,2):
    if i not in occupied_desks and (i + 1) not in occupied_desks:
      count += 1
  for i in range(1, total_desks - 1):
     if i not in occupied_desks and (i + 2) not in occupied_desks:
      count += 1
  return count
# keep this function call here 
print(SeatingStudents([6,4]))
print(SeatingStudents([8,1,8]))