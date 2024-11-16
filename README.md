# InfluxDB Setup

This project uses InfluxDB to store and manage time-series data.

## Prerequisites

- Python 3.x
- Docker and Docker Compose
- Git

## Setup Instructions

### 1. Environment Setup

Create a `.env` file in the project root:

### 2. Virtual Environment

Create and activate a Python virtual environment:

### 3. Docker Setup

Start the InfluxDB container:

The InfluxDB interface will be available at: http://localhost:8086

### 4. Security Notes

- Keep your `.env` file secure and never commit it to version control
- Add the following to your `.gitignore`:
  ```
  .env
  venv/
  ```

## Usage
```bash
# Create a local virtual environment
python3 -m venv localenv

source localenv/bin/activate

pip install -r requirements.txt

# Run the test script
python push/test_push_data.py
```


## Development

To deactivate the virtual environment:
```bash
deactivate
```
    