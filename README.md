# WasherAutoMacro

WasherAutoMacro is a Python script aimed at automating actions in mobile games through mirroring software on a computer. It uses keyboard hotkeys to trigger macros that perform clicks on predefined screen positions, incorporating randomness to mimic human behavior more closely.

## Features

- Easy configuration through a JSON file.
- Supports multiple macros with randomized click positions.
- Logs actions for easy tracking.

## Getting Started

### Setting up the Environment

Ensure Python is installed on your machine and set up a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```

### Installing Dependencies

install the necessary dependencies from the `requirements.txt`file:

```bash
pip install -r requirements.txt
```

### Configuring Macros

Edit the `config.json` file to set up your macros. Each macro should have a key (used to trigger it) and a position (defined by the top left and the bottom right corners of the click area).

- You can use WasherFindKey.py script to find the ID of your keys.
- You can use WasherFindPosition.py script to find the cursor's position when you click.

### Running the script

Run the main script:

```bash
python WasherAutoMacro.py
```

## Contributing

Feel free to fork the project, submit pull requests, open issues for suggestions, or report bugs.

## License

This project is open-sourced under the MIT License.
