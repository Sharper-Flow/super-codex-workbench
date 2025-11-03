#requires -version 5.1
<#!
.SYNOPSIS
  One‑shot Windows setup for a great terminal + WSL2 developer experience (2025‑ready).

.DESCRIPTION
  What this script does (idempotent where practical):
  - Ensures Windows features for WSL2 and virtualization are enabled
  - Installs/updates: Windows Terminal and your preferred prompt
  - Installs WSL (Ubuntu latest LTS) and sets WSL default to version 2
  - Optionally provisions minimal tools in the Ubuntu distro

.PARAMETER ProvisionWSL
  If set, runs minimal provisioning inside Ubuntu (ripgrep, curl, git, uv installer).

.PARAMETER DefaultProfile
  Which terminal profile to set as default: "PowerShell" or "Ubuntu" (WSL).
  Default: "PowerShell"

.PARAMETER Prompt
  Which prompt to install/configure: "starship" (default) or "oh-my-posh".
  Note: Starship is fast, cross-shell, and remains an excellent choice in 2025.

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File .\windows-setup.ps1 -ProvisionWSL -DefaultProfile Ubuntu

.NOTES
  Run this script in an elevated (Administrator) PowerShell. If not elevated, the script will prompt.
!#>

[CmdletBinding()]
param(
  [switch]$ProvisionWSL,
  [ValidateSet('PowerShell','Ubuntu')]
  [string]$DefaultProfile = 'PowerShell',
  [ValidateSet('starship','oh-my-posh')]
  [string]$Prompt = 'starship'
)

function Assert-Admin {
  $id = [Security.Principal.WindowsIdentity]::GetCurrent()
  $p = New-Object Security.Principal.WindowsPrincipal($id)
  if (-not $p.IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)) {
    Write-Warning 'This script should be run as Administrator. Relaunching with elevation...'
    $psi = New-Object System.Diagnostics.ProcessStartInfo PowerShell
    $psi.Arguments = "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`" $($MyInvocation.UnboundArguments -join ' ')"
    $psi.Verb = 'runas'
    try { [Diagnostics.Process]::Start($psi) | Out-Null } catch { throw }
    exit
  }
}

function Ensure-WinGet {
  if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
    Write-Warning 'winget not found. Install from Microsoft Store (App Installer), then re-run.'
    throw 'winget missing'
  }
}

function Test-RebootPending {
  try {
    $keys = @(
      'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending',
      'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired'
    )
    foreach ($k in $keys) { if (Test-Path $k) { return $true } }
  } catch { }
  return $false
}

function Enable-WSLFeatures {
  Write-Host '[WSL] Enabling required Windows features...' -ForegroundColor Cyan
  $r1 = Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux -NoRestart -All
  $r2 = Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -NoRestart -All
  $script:RebootNeeded = ($r1.RestartNeeded -or $r2.RestartNeeded -or (Test-RebootPending))
}

function Install-WindowsTerminal {
  Write-Host '[Terminal] Installing/Updating Windows Terminal...' -ForegroundColor Cyan
  winget install --id Microsoft.WindowsTerminal -e --source winget --silent --accept-package-agreements --accept-source-agreements | Out-Null
}

 

function Install-Prompt {
  param([string]$Type)
  switch ($Type) {
    'starship' {
      Write-Host '[Prompt] Installing Starship...' -ForegroundColor Cyan
      winget install --id Starship.Starship -e --source winget --silent --accept-package-agreements --accept-source-agreements | Out-Null
      $cfgDir = Join-Path $env:USERPROFILE '.config'
      $null = New-Item -ItemType Directory -Path $cfgDir -Force -ErrorAction SilentlyContinue
      $cfg = Join-Path $cfgDir 'starship.toml'
      if (-not (Test-Path $cfg)) {
        @"
add_newline = true
format = "[❯](bold dimmed white) $all"
[character]
success_symbol = "[❯](bold green)"
error_symbol = "[❯](bold red)"
"
        "@ | Out-File -FilePath $cfg -Encoding utf8
      }
      $profilePath = "$PROFILE"
      if (-not (Test-Path $profilePath)) { $null = New-Item -ItemType File -Path $profilePath -Force }
      if (-not (Get-Content $profilePath | Select-String -SimpleMatch 'starship init powershell' -Quiet)) {
        Add-Content $profilePath "`n# Starship prompt`nInvoke-Expression (& starship init powershell)"
      }
    }
    'oh-my-posh' {
      Write-Host '[Prompt] Installing Oh My Posh...' -ForegroundColor Cyan
      winget install --id JanDeDobbeleer.OhMyPosh -e --source winget --silent --accept-package-agreements --accept-source-agreements | Out-Null
      $profilePath = "$PROFILE"
      if (-not (Test-Path $profilePath)) { $null = New-Item -ItemType File -Path $profilePath -Force }
      if (-not (Get-Content $profilePath | Select-String -SimpleMatch 'oh-my-posh init pwsh' -Quiet)) {
        Add-Content $profilePath "`n# Oh My Posh`noh-my-posh init pwsh --config `$env:POSH_THEMES_PATH\\jandedobbeleer.omp.json | Invoke-Expression"
      }
    }
  }
}

function Install-WSL {
  Write-Host '[WSL] Installing Ubuntu (latest LTS) and setting WSL2...' -ForegroundColor Cyan
  if ($script:RebootNeeded) {
    Write-Warning 'A system restart is required before continuing with WSL installation. Please reboot and re-run this script.'
    return
  }
  try {
    wsl --install -d Ubuntu
  } catch {
    Write-Warning 'wsl --install failed or already installed. Continuing.'
  }
  try { wsl --set-default-version 2 } catch {}
}

function Provision-WSLUbuntu {
  Write-Host '[WSL] Provisioning packages inside Ubuntu...' -ForegroundColor Cyan
  # Ensure Ubuntu is installed and first-run has completed
  try {
    $distros = & wsl -l -q 2>$null
  } catch { $distros = '' }
  if (-not ($distros -match 'Ubuntu')) {
    Write-Warning 'Ubuntu distro not detected. Launch Ubuntu once to complete first-run, then re-run with -ProvisionWSL.'
    return
  }
  $cmd = @'
set -e
sudo apt-get update -y
sudo apt-get install -y \
  curl git ca-certificates gnupg lsb-release ripgrep \
  zsh fzf unzip build-essential \
  bat fd-find

# symlink fd and bat to expected names if necessary
mkdir -p "$HOME/.local/bin"
if command -v fdfind >/dev/null 2>&1 && [ ! -e "$HOME/.local/bin/fd" ]; then
  ln -sf "$(command -v fdfind)" "$HOME/.local/bin/fd"
fi
if command -v batcat >/dev/null 2>&1 && [ ! -e "$HOME/.local/bin/bat" ]; then
  ln -sf "$(command -v batcat)" "$HOME/.local/bin/bat"
fi

# Install uv (Python toolchain manager) for Linux (user local bin)
curl -LsSf https://astral.sh/uv/install.sh | sh
echo "export PATH=\"$HOME/.local/bin:$PATH\"" >> ~/.bashrc

# Install Starship prompt inside WSL for zsh
curl -fsSL https://starship.rs/install.sh | sh -s -- -y

# Install Oh My Zsh (unattended)
export RUNZSH=no
export CHSH=no
if [ ! -d "$HOME/.oh-my-zsh" ]; then
  sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" || true
fi

# ZSH plugins: autosuggestions & syntax highlighting
ZSH_CUSTOM="${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}"
mkdir -p "$ZSH_CUSTOM/plugins"
if [ ! -d "$ZSH_CUSTOM/plugins/zsh-autosuggestions" ]; then
  git clone https://github.com/zsh-users/zsh-autosuggestions "$ZSH_CUSTOM/plugins/zsh-autosuggestions"
fi
if [ ! -d "$ZSH_CUSTOM/plugins/zsh-syntax-highlighting" ]; then
  git clone https://github.com/zsh-users/zsh-syntax-highlighting "$ZSH_CUSTOM/plugins/zsh-syntax-highlighting"
fi

# Write a sane .zshrc if one doesn't exist
if [ ! -f "$HOME/.zshrc" ]; then
  cat > "$HOME/.zshrc" <<'ZRC'
# ~/.zshrc (Codex Workbench defaults)
export PATH="$HOME/.local/bin:$PATH"
export EDITOR=vim

# Oh My Zsh base
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="agnoster"
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
source "$ZSH/oh-my-zsh.sh"

# fzf keybindings & completion
if [ -f /usr/share/doc/fzf/examples/key-bindings.zsh ]; then
  source /usr/share/doc/fzf/examples/key-bindings.zsh
fi
if [ -f /usr/share/doc/fzf/examples/completion.zsh ]; then
  source /usr/share/doc/fzf/examples/completion.zsh
fi

# zsh completion
autoload -Uz compinit && compinit

# Starship prompt
eval "$(starship init zsh)"
ZRC
fi

# Try to set zsh as default shell (may require password)
if command -v chsh >/dev/null 2>&1; then
  if command -v zsh >/dev/null 2>&1; then
    chsh -s "$(command -v zsh)" "$USER" || true
  fi
fi
'@
  wsl -d Ubuntu -- bash -lc "$cmd"
}

 

# Main
Assert-Admin
Ensure-WinGet
Enable-WSLFeatures
Install-WindowsTerminal
Install-Prompt -Type $Prompt
Install-WSL
if ($ProvisionWSL) { Provision-WSLUbuntu }

if ($DefaultProfile -eq 'Ubuntu') {
  Write-Host "`n[Note] To make Ubuntu the default in Windows Terminal, open Settings > Default profile > Ubuntu." -ForegroundColor Yellow
}

Write-Host "`n[Done] Close and reopen Windows Terminal. If Ubuntu prompts for a UNIX user, complete that first." -ForegroundColor Green
