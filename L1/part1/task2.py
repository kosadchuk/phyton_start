import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('f_name')
parser.add_argument('x')
parser.add_argument('y')
args = parser.parse_args()

math_function = getattr(math, args.f_name)
if args.f_name in ['pow', 'copysign', 'fmod', 'log', 'atan2', 'hypot']:
    print(math_function(float(args.x), float(args.y)))
elif args.f_name == 'pi':
    print(math.pi)
elif args.f_name == 'e':
    print(math.e)
elif args.f_name == 'add':
    print(float(args.x) + float(args.y))
elif args.f_name == 'sub':
    print(float(args.x) - float(args.y))
elif args.f_name == 'multiply':
    print(float(args.x) * float(args.y))
elif args.f_name == 'division':
    print(float(args.x) / float(args.y))
else:
    print(math_function(float(args.x)))

