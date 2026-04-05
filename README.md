# api-gatekeeper-models

Shared data models for the API Gatekeeper auth service.

## Installation

### Public repo
```bash
pip install git+https://github.com/jmazzahacks/api-gatekeeper-models.git
```

### Private repo (requires `CR_PAT` environment variable)
```bash
pip install git+https://${CR_PAT}@github.com/jmazzahacks/api-gatekeeper-models.git
```

### As a dependency in pyproject.toml
```toml
dependencies = [
    "api-gatekeeper-models @ git+https://{env:CR_PAT}@github.com/jmazzahacks/api-gatekeeper-models.git",
]
```

### As a dependency in requirements.txt
```
api-gatekeeper-models @ git+https://${CR_PAT}@github.com/jmazzahacks/api-gatekeeper-models.git
```

## Usage

```python
from api_gatekeeper_models import Client, Route, ClientPermission, RateLimit
from api_gatekeeper_models import HttpMethod, AuthType, ClientStatus, MethodAuth
```

## Development

### Setup

```bash
# Create virtual environment
python -m venv .

# Activate virtual environment
source bin/activate

# Install dependencies
pip install -r dev-requirements.txt
pip install -e .
```

## License

O'Saasy License

## Author

Jason Byteforge (jmazzahacks@users.noreply.github.com)
