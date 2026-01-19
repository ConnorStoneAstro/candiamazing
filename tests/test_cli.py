import pytest

from candiamazing.cli import main


def test_cli_flux_to_mag_integration(monkeypatch, capsys):
    """
    Test the 'flux_to_mag' command using monkeypatch to simulate arguments.
    """
    # 1. Define the arguments as they would appear in sys.argv
    # Note: sys.argv[0] is always the script name (e.g., 'candiamazing')
    test_args = ["candiamazing", "flux_to_mag", "100.0", "25.0"]

    # 2. Use monkeypatch to temporarily replace sys.argv with our list
    monkeypatch.setattr("sys.argv", test_args)

    # 3. Run the main function
    main()

    # 4. Capture the printed output
    captured = capsys.readouterr()

    # 5. Verify the output contains the correct magnitude (approx 20.0)
    assert "20.0" in captured.out


def test_cli_missing_argument(monkeypatch, capsys):
    """
    Test that the CLI correctly errors out when arguments are missing.
    """
    # Simulate missing the zeropoint argument
    test_args = ["candiamazing", "flux_to_mag", "100.0"]

    monkeypatch.setattr("sys.argv", test_args)

    # We expect the program to exit with a system error code (usually 2)
    with pytest.raises(SystemExit) as excinfo:
        main()

    assert excinfo.value.code != 0

    # Optional: Check that argparse printed an error message to stderr
    captured = capsys.readouterr()
    assert "error" in captured.err


def test_cli_help(monkeypatch, capsys):
    """
    Test that the help flag works and prints usage info.
    """
    test_args = ["candiamazing", "--help"]

    monkeypatch.setattr("sys.argv", test_args)

    # Help also triggers a SystemExit (with code 0 for success), so we must catch it
    with pytest.raises(SystemExit) as excinfo:
        main()

    assert excinfo.value.code == 0

    captured = capsys.readouterr()
    assert "Available commands" in captured.out
