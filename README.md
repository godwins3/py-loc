# Line Counter

Line Counter is a Python package that counts the lines of code in a given repository. It supports multiple file types and provides options to exclude certain files or directories.

## Features

- Count lines of code in various file types.
- Exclude specific files or directories from the count.
- Option to exclude comments and blank lines.
- Generate a summary report.
- Command-line interface for easy usage.

## Installation

You can install Line Counter using pip:

```bash
pip install py-loc
```

## Usage

### Command-Line Interface

To use Line Counter from the command line, navigate to the root of your repository and run:

```bash
py-loc <directory> [options]
```

#### Options

- `<directory>`: The directory to scan for code files.
- `--file-types`: Specify file types to include in the line count (e.g., `.py .js`). Default is `.py`.
- `--exclude`: Specify directories or files to exclude from the line count.

### Example

Count lines of code in the `src` directory, including only Python and JavaScript files, and excluding the `tests` directory:

## Development

To contribute to the development of Line Counter, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/godwins3/py-loc.git
   ```

2. Navigate to the project directory:

   ```bash
   cd py-loc
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the tests:

   ```bash
   pytest
   ```

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue on GitHub or contact me at [praisegodwins4@gmail.com](mailto:praisegodwins4@gmail.com).
