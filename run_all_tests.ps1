# Stop on any error
$ErrorActionPreference = "Stop"

# Compile C code before running tests
Write-Host "Compiling main.c..."
gcc main.c -o main.exe
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Compilation failed. Exiting..." -ForegroundColor Red
    exit 1
}

# Get all Python test files in the tests folder
$TestFiles = Get-ChildItem -Path "tests" -Filter "test_*.py"

# Dictionary to store results
$Results = @{}

foreach ($file in $TestFiles) {
    # Delete test.db before each test
    if (Test-Path "test.db") {
        Write-Host "Deleting test.db before running $($file.Name)..."
        Remove-Item "test.db"
    }

    # Run pytest on the current test file
    Write-Host "Running pytest on $($file.FullName)..."
    pytest $file.FullName -v
    $ExitCode = $LASTEXITCODE

    if ($ExitCode -eq 0) {
        $Results[$file.Name] = "PASSED"
    } else {
        $Results[$file.Name] = "FAILED"
    }
}

# Final cleanup: delete test.db if it still exists
if (Test-Path "test.db") {
    Write-Host "Deleting test.db after all tests..."
    Remove-Item "test.db"
}

# Print summary with colors
Write-Host ""
Write-Host "================ Test Summary ================"
foreach ($key in $Results.Keys) {
    if ($Results[$key] -eq "PASSED") {
        Write-Host "$key : $($Results[$key])" -ForegroundColor Green
    } else {
        Write-Host "$key : $($Results[$key])" -ForegroundColor Red
    }
}
Write-Host "=============================================="
