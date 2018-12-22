from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-o", "--output", help="Output file location")
    parser.add_argument("-i", "--input", help="Input file location")
    args = parser.parse_args()

    if hasattr(args, "input"):
        print(f"I'll read from {args.input}")
    else:
        print("No input file specified")

    if hasattr(args, "output"):
        print(f"I'll print to {args.output}")
    else:
        print("No output file specified")
