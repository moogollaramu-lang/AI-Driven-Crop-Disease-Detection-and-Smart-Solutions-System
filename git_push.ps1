# Load environment variables from .env file
if (Test-Path .env) {
    Get-Content .env | ForEach-Object {
        if ($_ -match "^\s*([^#=]+)\s*=\s*(.*)\s*$") {
            $name = $Matches[1].Trim()
            $value = $Matches[2].Trim()
            [System.Environment]::SetEnvironmentVariable($name, $value)
        }
    }
}

$token = [System.Environment]::GetEnvironmentVariable("GITHUB_TOKEN")
if (-not $token) {
    Write-Error "GITHUB_TOKEN not found in environment or .env file."
    exit 1
}

$git = "C:\Users\LAB2_PC14\AppData\Local\Microsoft\WinGet\Packages\Git.MinGit_Microsoft.Winget.Source_8wekyb3d8bbwe\cmd\git.exe"
if (-not (Test-Path $git)) {
    Write-Error "MinGit executable not found at $git."
    exit 1
}

Write-Host ">>> Initializing local Git repository..."
& $git init

Write-Host ">>> Configuring local Git identity..."
& $git config --local user.name "moogollaramu-lang"
& $git config --local user.email "moogollaramu@users.noreply.github.com"

Write-Host ">>> Checking out to main branch..."
& $git checkout -b main

# Remove remote if it already exists
& $git remote remove origin 2>$null

Write-Host ">>> Adding remote origin with authentication token..."
$remoteUrl = "https://moogollaramu-lang:$token@github.com/moogollaramu-lang/AI-Driven-Crop-Disease-Detection-and-Smart-Solutions-System.git"
& $git remote add origin $remoteUrl

Write-Host ">>> Adding all project files (respecting .gitignore)..."
& $git add .

Write-Host ">>> Committing files..."
& $git commit -m "Upload all project files including ML model weights"

Write-Host ">>> Pushing to GitHub (this may take a moment for the 44.8MB model)..."
& $git push -f origin main

Write-Host ">>> Cleaning up remote URL to remove token from local git config..."
& $git remote remove origin
& $git remote add origin "https://github.com/moogollaramu-lang/AI-Driven-Crop-Disease-Detection-and-Smart-Solutions-System.git"

Write-Host "=============================================="
Write-Host "🎉 Push completed successfully!"
Write-Host "=============================================="
