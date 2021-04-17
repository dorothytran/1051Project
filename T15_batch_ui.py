# Written by Dorothy Tran
print('Please Enter The Filename: ')
infile = open(input())

for line in infile:
   
   lst = line.split()
   lst[0] = copy(load_image(lst[0]))
   COLOUR1 = 'cyan'
   COLOUR2 = 'yellow'
   COLOUR3 = 'magenta'
   THRESHOLD = 10 
   
   for i in range (2, len(lst)):
      if lst[i] == '2':
         lst[0] = two_tone(lst[0], COLOUR1, COLOUR2)
      elif lst[i] == '3':
         lst[0] = three_tone(lst[0], COLOUR1, COLOUR2, COLOUR3)
      elif lst[i] == 'X':
         lst[0] = extreme_contrast(lst[0])
      elif lst[i] == 'T':
         lst[0] = sepia(lst[0])
      elif lst[i] == 'P':
         lst[0] = posterize(lst[0])
      elif lst[i] == 'E':
         lst[0] = detect_edges(lst[0], THRESHOLD)
      elif lst[i] == 'I':
         lst[0] = detect_edges_better(lst[0], THRESHOLD)
      elif lst[i] == 'V':
         lst[0] = flip_vertical(lst[0])
      elif lst[i] == 'H':
         lst[0] = flip_horizontal(lst[0])
      else:
         print(lst[i],'is an invalid command, please review the accepted inputs')
      i += 1
   
   #saving the edited image with the filename          
   save_as(lst[0], lst[1])
   
#End Program
infile.close()
