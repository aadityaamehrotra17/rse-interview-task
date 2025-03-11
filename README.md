# FruityVice Lookup API
- Lookup fruit information by name
- Display fruit details (name, ID, family, sugar, carbohydrates)
- Output in human-readable or machine-readable (JSON) format

## Installation

Clone this repository:

```bash
git clone https://github.com/aadityaamehrotra17/rse-interview-task.git
cd rse-interview-task
```

Install dependencies:

```bash
pip install requests
```

## Usage

### Command Line

Basic usage:

```bash
python fruity.py Banana
```

Specify output format:

```bash
python fruity.py Banana --format machine
```

Use a custom API URL:

```bash
python fruity.py Banana --api-url https://xyz.com
```

### As a Library

```python
from fruity import FruitAPI

api = FruitAPI()
fruit_name = "banana"
fruit_data = api.get_fruit_info(fruit_name)
print(api.format_display(fruit_data, output_format="machine"))
```