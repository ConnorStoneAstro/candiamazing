import argparse
import sys

from candiamazing import utils  # Import your local core module


def main(args=None):
    """
    The main entry point for the CLI.
    """
    # 1. Create the top-level parser
    parser = argparse.ArgumentParser(description="A simple teaching example CLI tool.")

    # 2. Create subparsers for separate commands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # --- Command: flux_to_mag ---
    # Example usage: candiamazing flux_to_mag 3631 8.9
    parser_flux_to_mag = subparsers.add_parser("flux_to_mag", help="Convert flux to magnitude")
    parser_flux_to_mag.add_argument("flux", type=float, help="The flux value")
    parser_flux_to_mag.add_argument(
        "zeropoint", type=float, help="The zeropoint for the magnitude system"
    )
    # Map this subparser to the actual function
    parser_flux_to_mag.set_defaults(func=run_flux_to_mag)

    # --- Command: mag_to_flux ---
    # Example usage: candiamazing mag_to_flux 10 8.9
    parser_mag_to_flux = subparsers.add_parser("mag_to_flux", help="Convert magnitude to flux")
    parser_mag_to_flux.add_argument("mag", type=float, help="The magnitude value")
    parser_mag_to_flux.add_argument(
        "zeropoint", type=float, help="The zeropoint for the magnitude system"
    )
    # Map this subparser to the actual function
    parser_mag_to_flux.set_defaults(func=run_mag_to_flux)

    # 3. Parse arguments
    # If no arguments are provided, print help
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args is None:
        args = sys.argv[1:]
    args = parser.parse_args(args)

    # 4. Execute the mapped function
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


# --- Wrapper Functions ---
# These wrappers bridge the gap between argparse 'args' namespace
# and the clean arguments your core functions expect.


def run_flux_to_mag(args):
    mag = utils.flux_to_mag(args.flux, args.zeropoint)
    print(mag)


def run_mag_to_flux(args):
    flux = utils.mag_to_flux(args.mag, args.zeropoint)
    print(flux)


if __name__ == "__main__":
    main()
