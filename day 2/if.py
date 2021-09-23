is_hot = True
is_cold = False

if is_hot:
      print("It is a hot day")
      print("Have some cool drinks")
elif is_cold:
      print("It is a cool day")
      print("Have some hot drinks")
else:
      print("It's neither cold nor hot")
      print("Enjoy")


mat = 90
eng = 30

if mat>=40 and eng>=40:
      print("pass in both mat and eng")
elif mat<40 or eng<40:
      print("fail in either mat or eng")


name = 'Pugazhenthi'
if not len(name) < 5:
      print('name is not less than 5 characters long')