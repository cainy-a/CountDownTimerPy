import time
def countdown(n):
	while n > 0:
		n -= 1
def countdowntime(n):
	start = time.time()
	countdown(n)
	return time.time() - start

print("Countdown speed test. Python Interpreter Edition\nBy Cain Atkinson.\nPress enter to run test.")
input()

print("running 80 thousand test...")
_80k = countdowntime(80000)
print("Done.")

print("running 800 thousand test...")
_800k = countdowntime(800000)
print("Done.")

print("running 8 million test...")
_8m = countdowntime(8000000)
print("Done.")

print("running 80 million test...")
_80m = countdowntime(80000000)
print("Done.")

print("running 150 million test...")
_150m = countdowntime(150000000)
print("Done.")

print("running 300 million test...")
_300m = countdowntime(300000000)
print("Done.")

print("running 1 billion test...")
_1b = countdowntime(1000000000)
print("Done.")

choice = input("Run 10 billion test? (Note that this is very, very slow.)")
if input == "yes":
	print("running 10 billion test...")
	_10b = countdowntime(10000000000)
	print("Done.")
else:
	_10b = "---skipped---"
print("All tests done.")

print("80thousand test:  " + str(_80k) + " seconds")
print("800thousand test: " + str(_800k) + " seconds")
print("8million test:    " + str(_8m) + " seconds")
print("80million test:   " + str(_80m) + " seconds")
print("150million test:  " + str(_150m) + " seconds")
print("300million test:  " + str(_300m) + " seconds")
print("1billion test:    " + str(_1b) + " seconds")
print("10billion test:   " + str(_10b) + " seconds")
