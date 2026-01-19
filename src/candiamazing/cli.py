"""
Command-line interface for the candiamazing package.

This module defines a small, example-driven CLI that exposes flux - magnitude
conversion utilities via subcommands. 

Try it with either

python ./src/candiamazing/cli.py --help
candiamazing --help

"""

import argparse

from candiamazing import utils


def build_parser() -> argparse.ArgumentParser:
    """
    Build and configure the top-level argument parser for the CLI.

    Returns
    -------
    argparse.ArgumentParser
        A fully configured parser with subcommands registered.

    Notes
    -----
    The parser includes:
    - A short description of the tool.
    - An epilog with runnable examples.
    - Two subcommands: 'flux_to_mag' and 'mag_to_flux'.

    The epilog uses ``RawDescriptionHelpFormatter`` so that newlines and
    indentation are preserved in the help output.
    """
    parser = argparse.ArgumentParser(
        description=(
            "Convert between fluxes and magnitudes using a simple magnitude system."
        ),
        epilog=(
            "Examples:\n"
            "  candiamazing flux_to_mag 3631 8.9\n"
            "  candiamazing mag_to_flux 10 8.9\n\n"
            "Run `candiamazing <command> -h` for command-specific help."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands",
        required=True,
    )
    add_flux_to_mag_subcommand(subparsers)
    add_mag_to_flux_subcommand(subparsers)

    return parser


def add_flux_to_mag_subcommand(subparsers: argparse._SubParsersAction) -> None:
    """Register the 'flux_to_mag' subcommand and its arguments."""

    parser_flux_to_mag = subparsers.add_parser(
        "flux_to_mag",
        help="Convert flux to magnitude",
    )
    parser_flux_to_mag.add_argument("flux", type=float, help="The flux value")
    parser_flux_to_mag.add_argument(
        "zeropoint",
        type=float,
        help="The zeropoint for the magnitude system",
    )
    parser_flux_to_mag.set_defaults(func=run_flux_to_mag)


def add_mag_to_flux_subcommand(subparsers: argparse._SubParsersAction) -> None:
    """Register the 'mag_to_flux' subcommand and its arguments."""
    
    parser_mag_to_flux = subparsers.add_parser(
        "mag_to_flux",
        help="Convert magnitude to flux",
    )
    parser_mag_to_flux.add_argument("mag", type=float, help="The magnitude value")
    parser_mag_to_flux.add_argument(
        "zeropoint",
        type=float,
        help="The zeropoint for the magnitude system",
    )
    parser_mag_to_flux.set_defaults(func=run_mag_to_flux)


def run_flux_to_mag(args: argparse.Namespace) -> int:
    """Execute the 'flux_to_mag' command."""
    mag = utils.flux_to_mag(args.flux, args.zeropoint)
    print(mag)
    return 0


def run_mag_to_flux(args: argparse.Namespace) -> int:
    """Execute the 'mag_to_flux' command."""
    flux = utils.mag_to_flux(args.mag, args.zeropoint)
    print(flux)
    return 0


def main(argv: list[str] | None = None) -> int:
    """Run the CLI entry point."""
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
     # Delegate to main() and return its exit code
    raise SystemExit(main())
