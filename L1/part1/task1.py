import argparse

parser = argparse.ArgumentParser()
parser.add_argument('x', type=int)
parser.add_argument('action')
parser.add_argument('y', type=int)
args = parser.parse_args()

if args.action == '+':
    print('Result: ', args.x + args.y)
elif args.action == '-':
    print('Result: ', args.x - args.y)
elif args.action == '*':
    print('Result: ', args.x * args.y)
elif args.action == '/':
    if args.y == 0:
        print('Error!\nDivision by zero')
    else:
        print('Result: ', args.x / args.y)
else:
    print('Wrong action!\nPlease, try something from \'+\', \'-\', \'*\', \'/\'')
