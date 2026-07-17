Move-Item -Path 'content/docs/ch01-getting-started/01-buy-and-install.md' -Destination 'content/docs/ch01-newcomer/01-buy-and-install.md' -Force
Move-Item -Path 'content/docs/ch01-getting-started/02-launcher-and-versions.md' -Destination 'content/docs/ch01-newcomer/02-launcher-and-versions.md' -Force
Move-Item -Path 'content/docs/ch01-getting-started/03-game-settings.md' -Destination 'content/docs/ch01-newcomer/03-game-settings.md' -Force
Move-Item -Path 'content/docs/ch02-survival/01-first-day.md' -Destination 'content/docs/ch01-newcomer/04-first-day.md' -Force
Move-Item -Path 'content/docs/ch02-survival/02-gathering-and-crafting.md' -Destination 'content/docs/ch01-newcomer/05-gathering-and-crafting.md' -Force

Move-Item -Path 'content/docs/ch02-survival/04-nether-and-end.md' -Destination 'content/docs/ch02-general/03-nether-and-end.md' -Force
Move-Item -Path 'content/docs/ch02-survival/05-villagers.md' -Destination 'content/docs/ch02-general/04-villagers.md' -Force
Move-Item -Path 'content/docs/ch02-survival/07-enchanting.md' -Destination 'content/docs/ch02-general/05-enchanting.md' -Force
Move-Item -Path 'content/docs/ch02-survival/04-farming.md' -Destination 'content/docs/ch04-farming/01-farming.md' -Force

Move-Item -Path 'content/docs/ch04-redstone/01-basics.md' -Destination 'content/docs/ch05-redstone/01-basics.md' -Force
Move-Item -Path 'content/docs/ch04-redstone/02-logic-circuits.md' -Destination 'content/docs/ch05-redstone/02-logic-circuits.md' -Force
Move-Item -Path 'content/docs/ch04-redstone/03-auto-farms.md' -Destination 'content/docs/ch05-redstone/03-auto-farms.md' -Force

Move-Item -Path 'content/docs/ch05-multiplayer/01-ways-to-connect.md' -Destination 'content/docs/ch06-multiplayer/01-ways-to-connect.md' -Force
Move-Item -Path 'content/docs/ch05-multiplayer/02-server-setup.md' -Destination 'content/docs/ch06-multiplayer/02-server-setup.md' -Force
Move-Item -Path 'content/docs/ch05-multiplayer/03-realms.md' -Destination 'content/docs/ch06-multiplayer/03-realms.md' -Force

Move-Item -Path 'content/docs/ch07-commands/01-basic-commands.md' -Destination 'content/docs/ch07-technical/01-basic-commands.md' -Force
Move-Item -Path 'content/docs/ch07-commands/02-command-blocks.md' -Destination 'content/docs/ch07-technical/02-command-blocks.md' -Force
Move-Item -Path 'content/docs/ch07-commands/03-datapacks.md' -Destination 'content/docs/ch07-technical/03-datapacks.md' -Force
Move-Item -Path 'content/docs/ch07-commands/04-command-reference.md' -Destination 'content/docs/ch07-technical/04-command-reference.md' -Force
Move-Item -Path 'content/docs/ch07-commands/05-functions-and-advanced.md' -Destination 'content/docs/ch07-technical/05-functions-and-advanced.md' -Force

Remove-Item -Path 'content/docs/ch01-getting-started' -Recurse -Force
Remove-Item -Path 'content/docs/ch02-survival' -Recurse -Force
Remove-Item -Path 'content/docs/ch04-redstone' -Recurse -Force
Remove-Item -Path 'content/docs/ch05-multiplayer' -Recurse -Force
Remove-Item -Path 'content/docs/ch06-mods' -Recurse -Force
Remove-Item -Path 'content/docs/ch07-commands' -Recurse -Force
