from argparse import ArgumentParser
import logging


parser = ArgumentParser()
parser.add_argument("--name", type=str, required=True)
parser.add_argument("--place", type=str, required=True)

my_args = parser.parse_args()
a = 1
b = 0

if __name__ == "__main__":
    try:
        a/b
    except ZeroDivisionError as e:
        logging.error("Zero Devision Error Log")
        raise ZeroDivisionError("skldfjslfjlsdfj alksdjlkdsjf ejrwiojr")

    print(f"Hello {my_args.name} from {my_args.place}.")
