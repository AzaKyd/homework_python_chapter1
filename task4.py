def last_letter(x):
	return x[len(x)-1]



def test_last_letter():
  assert last_letter('hello!') == '!'
  assert last_letter('banana') == 'a'
  assert last_letter('8') == '8'
  assert last_letter('funnyguys') == 's'
  assert last_letter('101') == '1'
  print("YOUR CODE IS CORRECT!")
#test your code by un-commenting the line(s) below
test_last_letter()