import sys
import os

def main():
	if(not len(sys.argv) == 3 or
	  (not sys.argv[1] == '--format' and not sys.argv[1] == '-F') or
	  (not sys.argv[2] == 'label' and not sys.argv[2] == 'bottle' and
	  	not sys.argv[2] == 'bottle_thumb')):
		print('usage: {0} --format | -F <label> | <bottle> | <bottle_thumb>'.format(sys.argv[0]))
		return

	for f in os.listdir('.'):
		if '_label' in f:
			os.rename(f, f.replace('_label', '_{0}'.format(sys.argv[2])))
		elif '_bottle' in f:
			os.rename(f, f.replace('_bottle', '_{0}'.format(sys.argv[2])))
		elif '_bottle_thumb' in f:
			os.rename(f, f.replace('_bottle_thumb', '_{0}'.format(sys.argv[2])))
		else:
			os.rename(f, f.replace('.png', '_{0}.png'.format(sys.argv[2])))

if __name__ == "__main__":
	main()
