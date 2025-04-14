# Odoo Test Environment

This repository provides a Docker-based development environment for Odoo 18 with custom module support.

## Features

- Docker-based Odoo 18 installation
- PostgreSQL database
- Custom module support
- Development mode with auto-reload

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. Clone this repository:
   ```bash
   git clone https://github.com/Bharath95/odoo-test.git
   cd odoo-test
   ```

2. Start the containers:
   ```bash
   docker-compose up -d
   ```

3. Access Odoo:
   - Open your browser and navigate to: http://localhost:8069
   - Default credentials:
     - Username: admin
     - Password: admin

4. Install custom modules:
   - Go to Apps menu
   - Update the Apps list
   - Install the "Custom Hello" module

## Directory Structure

```
odoo-test/
├── custom-addons/          # Directory for custom modules
│   └── custom_hello/      # Example custom module
├── docker-compose.yml     # Docker configuration
└── README.md             # This file
```

## Custom Module Development

1. Create new modules in the `custom-addons` directory
2. Each module should have its own subdirectory with:
   - `__manifest__.py` - Module metadata
   - `__init__.py` - Module initialization
   - `models/` - Python models
   - `views/` - XML views

## Code Quality

This repository uses Ruff for code quality checks and formatting. To run Ruff locally:

1. Install Ruff:
   ```bash
   pip install ruff
   ```

2. Run the checks:
   ```bash
   ruff check .
   ```

3. Format your code:
   ```bash
   ruff format .
   ```

The repository is configured with a pre-commit hook that will automatically run Ruff checks before any commit. If Ruff finds any errors, the commit will be blocked until the errors are fixed.

The configuration is already set up in `pyproject.toml`, so no additional setup is needed. Ruff will help maintain consistent code style and catch potential issues before pushing to the repository.

## Troubleshooting

1. If the containers don't start:
   ```bash
   docker-compose down
   docker-compose up -d
   ```

2. If you need to recreate the database:
   ```bash
   docker-compose down -v
   docker-compose up -d
   ```

## License

MIT License
