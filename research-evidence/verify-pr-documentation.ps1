param([string]$Base = 'origin/main')
$ErrorActionPreference = 'Stop'
git diff "$Base...HEAD" --check
if ($LASTEXITCODE -ne 0) { throw 'Whitespace failed' }
$paths = git diff "$Base...HEAD" --name-only -- '*.md'
$linkCount = 0
foreach ($path in $paths) {
    $textBody = Get-Content -LiteralPath $path -Raw
    if ($textBody -match '(?m)^(<<<<<<< |=======\s*$|>>>>>>> )') { throw "Conflict markers: $path" }
    if ($textBody -match 'Co-authored-by:|Generated with|AI agent|Codex|ChatGPT') { throw "Attribution: $path" }
    $width = 0
    foreach ($line in ($textBody -split '\r?\n')) {
        if ($line.StartsWith('|')) {
            $nextWidth = [regex]::Matches($line, '\|').Count
            if ($width -ne 0 -and $width -ne $nextWidth) { throw "Table width: $path" }
            $width = $nextWidth
        } else { $width = 0 }
    }
    foreach ($link in [regex]::Matches($textBody,'\]\(([^)]+)\)')) {
        $target = $link.Groups[1].Value
        if ($target -match '^(https?://|#|mailto:)') { continue }
        $localTarget = ($target -split '#')[0]
        if (-not (Test-Path -LiteralPath (Join-Path (Split-Path (Join-Path $PWD $path)) $localTarget))) { throw "Missing local target ${path}: $target" }
        $linkCount++
    }
}
"PASS: $($paths.Count) Markdown files / $linkCount local targets; tables, conflict markers, attribution and whitespace."
