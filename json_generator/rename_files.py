import sys
import os

def main():
	if(not len(sys.argv) == 3 or
	  (not sys.argv[1] == '--format' and not sys.argv[1] == '-F') or
	  (not sys.argv[2] == 'label' and not sys.argv[2] == 'bottle' and
	  	not sys.argv[2] == 'thumb')):
		print('usage: {0} --format | -F <label> | <bottle> | <thumb>'.format(sys.argv[0]))
		return

	for f in os.listdir('.'):
		os.rename(f, f.replace('.png', '_{0}.png'.format(sys.argv[2])))

if __name__ == "__main__":
	main()
