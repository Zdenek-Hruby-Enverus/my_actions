import os
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("--iso", type=str, required=True)
parser.add_argument("--type", type=str, required=True)
parser.add_argument("--point", type=str, required=True)

my_args = parser.parse_args()

env_file = os.getenv('GITHUB_ENV')

types_dict = {
    "LOAD": "Load",
    "SOLAR": "Solar",
    "WIND": "Wind"
}

points_dict = {
    "TOTAL": "Total",
    "ZONE_SOUTH": "Zone/South"
}

if __name__ == '__main__':
    ensemble_path = f"./models/{my_args.iso}/{types_dict.get(my_args.type)}/{points_dict.get(my_args.point)}/ENSEMBLE.json"

    with open(env_file, 'a') as f:
        f.write(f"ENSEMBLE_FILE_PATH={ensemble_path}")
