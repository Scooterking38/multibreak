# multibreak

A Python module to break out of multiple nested loops using `break(n)`.

## Architecture Overview

The `multibreak` repository is structured as follows:

- **src/multibreak/__init__.py**: This file imports the main functionality from `multibreak.py`.
- **src/multibreak/multibreak.py**: Contains the core logic for breaking out of nested loops. It defines a custom exception `BreakLevel` and two functions: `break_` to initiate breaking, and `handle_break` as a decorator to manage break levels.

## Tech Stack

- **Programming Language**: Python
- **Build System**: Hatchling
- **License**: MIT

## Getting Started / Setup Guide

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mrwe3838/multibreak.git
   cd multibreak
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8 or higher installed. Then, install the required dependencies using Hatchling:
   ```bash
   pip install hatchling
   ```

3. **Build and Install the Package**:
   Build and install the package locally:
   ```bash
   hatch build
   pip install .
   ```

4. **Usage Example**:
   Here's how you can use the `multibreak` module in your Python code:

   ```python
   from multibreak import break_, handle_break

   @handle_break
   def nested_loops():
       for i in range(3):
           print(f"Outer loop: {i}")
           for j in range(3):
               print(f"  Inner loop: {j}")
               if some_condition:
                   break_(2)  # Break out of both loops

   nested_loops()
   ```

This setup allows you to effectively manage and exit multiple nested loops using a simple API.