$ErrorActionPreference = "Continue"
$items = @{
    "oak_planks" = "Oak_Planks"
    "spruce_planks" = "Spruce_Planks"
    "birch_planks" = "Birch_Planks"
    "jungle_planks" = "Jungle_Planks"
    "acacia_planks" = "Acacia_Planks"
    "dark_oak_planks" = "Dark_Oak_Planks"
    "mangrove_planks" = "Mangrove_Planks"
    "cherry_planks" = "Cherry_Planks"
    "bamboo_planks" = "Bamboo_Planks"
    "crimson_planks" = "Crimson_Planks"
    "warped_planks" = "Warped_Planks"
    "stick" = "Stick"
    "coal" = "Coal"
    "charcoal" = "Charcoal"
    "cobblestone" = "Cobblestone"
    "raw_iron" = "Raw_Iron"
    "iron_ingot" = "Iron_Ingot"
    "wooden_pickaxe" = "Wooden_Pickaxe"
    "stone_pickaxe" = "Stone_Pickaxe"
    "iron_pickaxe" = "Iron_Pickaxe"
    "wooden_shovel" = "Wooden_Shovel"
    "stone_shovel" = "Stone_Shovel"
    "iron_shovel" = "Iron_Shovel"
    "wooden_axe" = "Wooden_Axe"
    "stone_axe" = "Stone_Axe"
    "iron_axe" = "Iron_Axe"
    "wooden_sword" = "Wooden_Sword"
    "stone_sword" = "Stone_Sword"
    "iron_sword" = "Iron_Sword"
    "wooden_hoe" = "Wooden_Hoe"
    "stone_hoe" = "Stone_Hoe"
    "iron_hoe" = "Iron_Hoe"
    "furnace" = "Furnace"
    "crafting_table" = "Crafting_Table"
}

$destDir = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not (Test-Path $destDir)) {
    New-Item -ItemType Directory -Force -Path $destDir
}

[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12

# Create empty.png if not exists
$emptyFile = Join-Path $destDir "empty.png"
if (-not (Test-Path $emptyFile)) {
    $transparentPngBase64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
    [IO.File]::WriteAllBytes($emptyFile, [Convert]::FromBase64String($transparentPngBase64))
    Write-Host "Created empty.png" -ForegroundColor Green
}

foreach ($key in $items.Keys) {
    $wikiName = $items[$key]
    $url = "https://minecraft.wiki/images/${wikiName}.png"
    $destFile = Join-Path $destDir "${key}.png"
    
    if ((Test-Path $destFile) -and ((Get-Item $destFile).Length -gt 0)) {
        Write-Host "Skipping ${key}.png (already exists)" -ForegroundColor Gray
        continue
    }
    
    Write-Host "Downloading ${key}.png from ${url}..."
    try {
        # Using Invoke-WebRequest with TimeoutSec and UserAgent
        Invoke-WebRequest -Uri $url -OutFile $destFile -TimeoutSec 8 -UserAgent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" -ErrorAction Stop
        Write-Host "Success: ${key}.png downloaded." -ForegroundColor Green
    } catch {
        Write-Host "Error downloading ${key}.png: $_" -ForegroundColor Red
    }
}
