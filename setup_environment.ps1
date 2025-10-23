$ErrorActionPreference = "Stop"

# Create venv if it doesn't exist
if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
}

# Activate it
Write-Host "Activating virtual environment..."
& .\venv\Scripts\Activate.ps1

# Install dependencies
if (Test-Path "requirements.txt") {
    Write-Host "Installing requirements..."
    pip install -r requirements.txt
} else {
    # Write-Host "No requirements.txt found — skipping install."
}
Write-Host "Installed. Enjoy!! :)"

