from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("--name", type=str, required=True)
parser.add_argument("--place", type=str, required=True)

my_args = parser.parse_args()

if __name__ == "__main__":
    print(f"Hello {my_args.name} from {my_args.place}.")
