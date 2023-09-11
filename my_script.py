import random
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--mu", type=int, default=0)
parser.add_argument("--sigma", type=int, default=1)

args = parser.parse_args()


if __name__ == "__main__":
    
    rn = random.gauss(mu=args.mu, sigma=args.sigma)

    print(f"My random number is: {rn}")
