# WasherAutoMacro

WasherAutoMacro is a Python script aimed at automating actions in mobile games through mirroring software on a computer. It uses keyboard hotkeys to trigger macros that perform clicks on predefined screen positions, incorporating randomness to mimic human behavior more closely.

## Features

- Easy configuration through a JSON file.
- Supports multiple macros with randomized click positions.
- Logs actions for easy tracking.

## Getting Started

### Installation

To get started with WasherAutoMacro, clone this repository and navigate into the project directory:

```bash
git clone https://github.com/Washer34/WasherAutoMacro.git
cd WasherAutoMacro
```

### Setting up the Environment

#### Prerequisites

- Ensure you have Python installed on your machine. [Download Python](https://www.python.org/downloads/)

#### Virtual Environment

##### Creating the Environment

```bash
python3 -m venv env
```

##### Activating the Environment

- On macOS and Linux:

```bash
source env/bin/activate
```

- On Windows:

```bash
.\env\Scripts\activate
```

### Installing Dependencies

install the necessary dependencies from the `requirements.txt`file:

```bash
pip install -r requirements.txt
```

### Configuring Macros

Edit the `config.json` file to set up your macros. Each macro should have a key (used to trigger it) and a position (defined by the top left and the bottom right corners of the click area).

- You can use `WasherFindKey.py` script to find the ID of your keys.
- You can use `WasherFindPosition.py` script to find the cursor's position when you click.

### Running the script

Run the main script:

```bash
python WasherAutoMacro.py
```

## Contributing

Feel free to fork the project, submit pull requests, open issues for suggestions, or report bugs.

## License

This project is open-sourced under the MIT License.
