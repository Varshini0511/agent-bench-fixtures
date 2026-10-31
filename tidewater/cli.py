"""tidewater quote --weight 12 --zone inland --currency USD"""

import argparse

from tidewater.currency import convert
from tidewater.rates import compute_rate


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="tidewater")
    sub = parser.add_subparsers(dest="command", required=True)
    quote = sub.add_parser("quote", help="price a parcel")
    quote.add_argument("--weight", type=float, required=True)
    quote.add_argument("--zone", default="harbor")
    quote.add_argument("--currency", default="EUR")
    args = parser.parse_args(argv)
    price = convert(compute_rate(args.weight, args.zone), args.currency)
    print(f"{price:.2f} {args.currency}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
