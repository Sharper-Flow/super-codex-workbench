#requires -version 5.1
<#!
.SYNOPSIS
  One‑shot Windows setup for a great terminal + WSL2 developer experience (2025‑ready).

.DESCRIPTION
  What this script does (idempotent where practical):
  - Ensures Windows features for WSL2 and virtualization are enabled
  - Installs/updates: Windows Terminal, CaskaydiaCove Nerd Font, Starship prompt
  - Adds a sleek dark grey color scheme to Windows Terminal and sets font face
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

function Enable-WSLFeatures {
  Write-Host '[WSL] Enabling required Windows features...' -ForegroundColor Cyan
  Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux -NoRestart -All | Out-Null
  Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -NoRestart -All | Out-Null
}

function Install-WindowsTerminal {
  Write-Host '[Terminal] Installing/Updating Windows Terminal...' -ForegroundColor Cyan
  winget install --id Microsoft.WindowsTerminal -e --source winget --silent --accept-package-agreements --accept-source-agreements | Out-Null
}

function Install-NerdFont {
  Write-Host '[Font] Installing CaskaydiaCove Nerd Font...' -ForegroundColor Cyan
  # Primary package (Nerd Fonts official)
  $ok = $true
  try {
    winget install --id NerdFonts.CaskaydiaCove -e --source winget --silent --accept-package-agreements --accept-source-agreements | Out-Null
  } catch { $ok = $false }
  if (-not $ok) {
    Write-Warning 'Failed to install NerdFonts.CaskaydiaCove via winget. You can manually install the font from https://www.nerdfonts.com/font-downloads'
  }
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
  try {
    wsl --install -d Ubuntu
  } catch {
    Write-Warning 'wsl --install failed or already installed. Continuing.'
  }
  try { wsl --set-default-version 2 } catch {}
}

function Provision-WSLUbuntu {
  Write-Host '[WSL] Provisioning packages inside Ubuntu...' -ForegroundColor Cyan
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

function Set-WindowsTerminal-ThemeAndFont {
  Write-Host '[Terminal] Applying dark grey color scheme and Nerd Font...' -ForegroundColor Cyan
  $settingsPath = Join-Path $env:LOCALAPPDATA 'Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json'
  if (-not (Test-Path $settingsPath)) {
    Write-Warning "Windows Terminal settings not found at $settingsPath. Launch Windows Terminal once and re-run to apply theming."
    return
  }
  $json = Get-Content $settingsPath -Raw | ConvertFrom-Json
  if (-not $json.schemes) { $json | Add-Member -Name schemes -MemberType NoteProperty -Value @() }
  $schemeName = 'CodexDarkGrey'
  $scheme = $json.schemes | Where-Object { $_.name -eq $schemeName }
  if (-not $scheme) {
    $new = [PSCustomObject]@{
      name = $schemeName
      background = '#1f2428'
      foreground = '#d1d5da'
      black = '#000000'
      blue = '#79b8ff'
      cyan = '#56d4dd'
      green = '#85e89d'
      purple = '#b392f0'
      red = '#f97583'
      white = '#e5e5e5'
      yellow = '#ffea7f'
      brightBlack = '#586069'
      brightBlue = '#c8e1ff'
      brightCyan = '#a5f0ff'
      brightGreen = '#bef5cb'
      brightPurple = '#d1bcf9'
      brightRed = '#fdaeb7'
      brightWhite = '#ffffff'
      brightYellow = '#fffbdd'
    }
    $json.schemes += $new
  }

  # Apply to profiles: PowerShell and Ubuntu, set fontFace
  foreach ($p in $json.profiles.list) {
    $name = $p.name
    if ($name -match 'PowerShell' -or $name -match 'Ubuntu') {
      $p.font = @{ face = 'CaskaydiaCove Nerd Font' }
      $p.colorScheme = $schemeName
      $p.useAcrylic = $true
      $p.acrylicOpacity = 0.9
    }
  }

  # Set default profile
  if ($DefaultProfile -eq 'Ubuntu') {
    $ubuntu = $json.profiles.list | Where-Object { $_.name -match 'Ubuntu' } | Select-Object -First 1
    if ($ubuntu) { $json.defaultProfile = $ubuntu.guid }
  } else {
    $ps = $json.profiles.list | Where-Object { $_.name -match 'PowerShell' } | Select-Object -First 1
    if ($ps) { $json.defaultProfile = $ps.guid }
  }

  $json | ConvertTo-Json -Depth 10 | Set-Content -Path $settingsPath -Encoding UTF8
}

# Main
Assert-Admin
Ensure-WinGet
Enable-WSLFeatures
Install-WindowsTerminal
Install-NerdFont
Install-Prompt -Type $Prompt
Install-WSL
if ($ProvisionWSL) { Provision-WSLUbuntu }
Set-WindowsTerminal-ThemeAndFont

Write-Host "`n[Done] Close and reopen Windows Terminal to see the theme and font. If Ubuntu prompts for a UNIX user, complete that first." -ForegroundColor Green
