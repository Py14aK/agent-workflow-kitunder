# install.ps1  (agent-skills-kit, 2026-10-28)
# Copies the skills in .\skills into a folder GitHub Copilot (VS Code), Kilo Code and Codex all read.
#
#   Personal, all your projects:   powershell -ExecutionPolicy Bypass -File .\install.ps1
#   One repository only:           powershell -ExecutionPolicy Bypass -File .\install.ps1 -Project C:\path\to\repo
#   Preview without copying:       add -WhatIf
#   Replace existing copies:       add -Force   (old copy is moved to .backup_<timestamp> first)
[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$Project = "",
    [switch]$Force
)
$ErrorActionPreference = "Stop"
$src = Join-Path $PSScriptRoot "skills"
if (-not (Test-Path $src)) { throw "Cannot find $src. Run this script from the unzipped kit folder." }

if ($Project) {
    if (-not (Test-Path $Project)) { throw "Project folder not found: $Project" }
    $dest = Join-Path $Project ".agents\skills"
} else {
    $dest = Join-Path $HOME ".agents\skills"
}
$stamp = Get-Date -Format "yyyyMMdd_HHmmss"
New-Item -ItemType Directory -Force -Path $dest | Out-Null

$installed = 0; $skipped = 0
foreach ($skill in Get-ChildItem -Directory $src) {
    $target = Join-Path $dest $skill.Name
    if (Test-Path $target) {
        if (-not $Force) { Write-Host "skip     $($skill.Name) (already there)"; $skipped++; continue }
        $bk = Join-Path $dest ".backup_$stamp"
        if ($PSCmdlet.ShouldProcess($target, "back up")) {
            New-Item -ItemType Directory -Force -Path $bk | Out-Null
            Move-Item $target $bk
        }
    }
    if ($PSCmdlet.ShouldProcess($target, "install")) {
        Copy-Item -Recurse $skill.FullName $target
        Write-Host "install  $($skill.Name)"
    }
    $installed++
}
Write-Host ""
Write-Host "Done: $installed installed, $skipped skipped -> $dest"
Write-Host "Reload VS Code (Developer: Reload Window). In Copilot Chat use Agent mode; type / to see skills."
