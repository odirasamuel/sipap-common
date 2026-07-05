# SIPAP Common Examples

This directory contains comprehensive working examples demonstrating the key features implemented in sipap-common following Sentinel patterns.

## Examples Overview

### 1. Telemetry Tracking (`telemetry_tracking.py`)
Demonstrates production-grade telemetry tracking with DynamoDB publishing:
- Creating telemetry records for successful predictions
- Tracking failed predictions with error context
- Batch telemetry publishing for efficiency
- DynamoDB serialization with Decimal conversion

**Key Features:**
- Fire-and-forget publishing (never blocks predictions)
- Comprehensive metrics (timing, status, sources, confidence)
- GSI composite keys for analytics

### 2. Exception-Carried Telemetry (`exception_telemetry.py`)
Shows how exceptions carry telemetry for complete observability:
- Attaching telemetry records to exceptions
- Preserving context on all code paths (success + failure)
- Extracting telemetry from caught exceptions
- Backward compatibility (telemetry optional)

**Key Features:**
- No telemetry loss on errors
- Complete error forensics
- Works with entire exception hierarchy
- Safe telemetry extraction methods

### 3. Template Rendering (`template_rendering.py`)
Demonstrates Jinja2 template rendering for configuration management:
- Environment variable substitution with `${ VARIABLE }` syntax
- Graceful degradation for missing variables
- YAML/JSON configuration rendering
- Reusable template environments

**Key Features:**
- Flexible configuration management
- Runtime environment-specific substitution
- Preserves literal braces in JSON/YAML
- Handles whitespace in variable names

## Setup Instructions

### Prerequisites
- Python 3.12 or higher
- sipap-common package installed

### Installation

1. **Navigate to repository:**
   ```bash
   cd /Users/charlesotuya/AI-Odi/sentinel/sipap/repos/sipap-common
   ```

2. **Activate virtual environment:**
   ```bash
   source .venv/bin/activate
   ```

3. **Install sipap-common in editable mode** (if not already installed):
   ```bash
   pip install -e .
   ```

4. **Verify installation:**
   ```bash
   python -c "from sipap_common import telemetry, exceptions; print('✅ sipap-common installed')"
   ```

## Running Examples

### Run Individual Examples

```bash
# Run telemetry tracking examples
python examples/telemetry_tracking.py

# Run exception telemetry examples
python examples/exception_telemetry.py

# Run template rendering examples
python examples/template_rendering.py
```

### Run All Examples

```bash
cd examples
for example in *.py; do
    echo "Running $example..."
    python "$example"
    echo ""
done
```

## Questions or Issues?

If you encounter issues or have questions about these examples:
1. Check the test suite in `tests/unit/` for additional usage patterns
2. Review docstrings in the source code for detailed API documentation
3. Refer to Sentinel's implementation for production patterns
