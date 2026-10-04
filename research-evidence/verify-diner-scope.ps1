$ErrorActionPreference = 'Stop'
$repoPath = 'D:\the next level\valiris-restaurants'
$sourceRows = Get-Content -LiteralPath 'D:\the next level\research-evidence\m0-capability-source.json' -Raw | ConvertFrom-Json
$matrixText = Get-Content -LiteralPath "$repoPath\docs\product\m0-capability-matrix.md" -Raw
$journeyText = Get-Content -LiteralPath "$repoPath\docs\product\m0-journeys-and-criteria.md" -Raw
$parents = [regex]::Matches($matrixText, '(?m)^\| (B\d\.\d{2}) / L(\d+) \|(.+)\|\r?$')
if ($parents.Count -ne 72 -or ($parents.Groups | Where-Object Name -eq '1' | Select-Object -ExpandProperty Value -Unique).Count -ne 72) { throw 'Parent count/uniqueness' }
$treatments = @{}
foreach ($row in $parents) {
    $sourceRow = $sourceRows | Where-Object id -eq $row.Groups[1].Value
    if ($sourceRow.line -ne [int]$row.Groups[2].Value) { throw "Source line: $($row.Value)" }
    $cells = $row.Value.Trim().Trim('|').Split('|') | ForEach-Object { $_.Trim() }
    if ($cells.Count -ne 7 -or $cells[6] -notmatch '^A / D[12]') { throw "Parent structure/approval: $($row.Value)" }
    $treatments[$cells[3]]++
}
if ($treatments['Included'] -ne 36 -or $treatments['Configurable'] -ne 30 -or $treatments['Connection-dependent'] -ne 6) { throw 'Treatment totals' }
if ([regex]::Matches($matrixText, '(?m)^\| B3\.11-(?:AUDIO|3D) / L110 \|[^\r\n]+\| Later \|').Count -ne 2) { throw 'Media deferrals' }
if ($matrixText -notmatch '(?m)^\| S1 / §3, L55 \|[^\r\n]+\| Excluded \|' -or $matrixText -notmatch '(?m)^\| S2 / §5, L120 \|[^\r\n]+\| Configurable \|') { throw 'Supplementary decisions' }
$coverageText = ($journeyText -split '## 4\. Coverage map')[1] -split '## 5\. Proposed review' | Select-Object -First 1
$covered = [System.Collections.Generic.HashSet[string]]::new()
foreach ($entry in [regex]::Matches($coverageText, 'B(\d)\.(\d{2})(?:–B\d\.(\d{2}))?')) {
    $lastOrdinal = if ($entry.Groups[3].Success) { [int]$entry.Groups[3].Value } else { [int]$entry.Groups[2].Value }
    for ($ordinal = [int]$entry.Groups[2].Value; $ordinal -le $lastOrdinal; $ordinal++) { [void]$covered.Add(('B{0}.{1:00}' -f $entry.Groups[1].Value, $ordinal)) }
}
if ($covered.Count -ne 72 -or ($sourceRows | Where-Object { -not $covered.Contains($_.id) })) { throw 'Journey coverage' }
if ($journeyText -notmatch 'R17' -or [regex]::Matches($journeyText, '\*\*J15\.\d:').Count -ne 6) { throw 'Account journey criteria' }
$changedPaths = @(& git -C $repoPath diff --name-only docs/m0-execution-brief) + @(& git -C $repoPath ls-files --others --exclude-standard)
$markdownPaths = $changedPaths | Where-Object { $_ -like '*.md' } | Select-Object -Unique
$linkCount = 0
foreach ($relativePath in $markdownPaths) {
    $absolutePath = Join-Path $repoPath $relativePath
    $contentText = Get-Content -LiteralPath $absolutePath -Raw
    if ($contentText -match '(Co-authored-by:|Generated with|AI assistant|AI agent|GPT-|Codex|ChatGPT)') { throw "Attribution in $relativePath" }
    $tableWidth = 0
    foreach ($line in ($contentText -split '\r?\n')) {
        if ($line.StartsWith('|')) {
            $width = [regex]::Matches($line, '\|').Count
            if ($tableWidth -ne 0 -and $width -ne $tableWidth) { throw "Table width in $relativePath" }
            $tableWidth = $width
        } else { $tableWidth = 0 }
    }
    foreach ($link in [regex]::Matches($contentText, '\]\(([^)]+)\)')) {
        $target = $link.Groups[1].Value
        if ($target -match '^(https?://|#)') { continue }
        $localTarget = ($target -split '#')[0]
        if (-not (Test-Path -LiteralPath (Join-Path (Split-Path $absolutePath) $localTarget))) { throw "Link in ${relativePath}: $target" }
        $linkCount++
    }
}
$historicalChanges = & git -C $repoPath diff HEAD -- docs/adr/0008-first-launch-capability-commitment.md docs/research
if ($historicalChanges) { throw 'Accepted ADR/source modified' }
& git -C $repoPath diff --check
if ($LASTEXITCODE -ne 0) { throw 'Whitespace' }
"PASS: 72 exact accepted parents (36/30/6); 2 media deferrals; S1 excluded/S2 accepted; 72/72 coverage plus J15.1-6/R17; $($markdownPaths.Count) PR Markdown files/$linkCount local targets; tables/attribution/whitespace; prior ADR/sources unchanged."
