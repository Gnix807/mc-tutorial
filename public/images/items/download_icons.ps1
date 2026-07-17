$ErrorActionPreference = "SilentlyContinue"
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

foreach ($key in $items.Keys) {
    $wikiName = $items[$key]
    $url = "https://minecraft.wiki/images/${wikiName}.png"
    $destFile = Join-Path $destDir "${key}.png"
    
    Write-Host "Downloading ${key}.png from ${url}..."
    
    # Try downloading with User-Agent to prevent 403 blocks
    $webClient = New-Object System.Net.WebClient
    $webClient.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    try {
        $webClient.DownloadFile($url, $destFile)
        if (Test-Path $destFile) {
            Write-Host "Success: ${key}.png downloaded." -ForegroundColor Green
        } else {
            Write-Host "Failed: ${key}.png file not saved." -ForegroundColor Red
        }
    } catch {
        Write-Host "Error downloading ${key}.png: $_" -ForegroundColor Red
    }
}
