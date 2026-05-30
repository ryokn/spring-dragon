# Spring Dragon

A dark VS Code color theme that fuses **[Spring Night](https://github.com/rhysd/vim-color-spring-night)**'s deep blue backgrounds with **[Kanagawa Dragon](https://github.com/rebelot/kanagawa.nvim)**'s muted, nature-inspired syntax colors.

## Features

- Deep blue backgrounds from Spring Night (`#213243` editor, `#132132` chrome)
- Calm syntax palette from Kanagawa Dragon (muted blues, greens, purples)
- Status bar styled after Spring Night
- Bracket pair colorization with soft, cohesive colors
- Semantic highlighting disabled for consistent rendering regardless of language server state

## Color Palette

| Role | Color | Usage |
|------|-------|-------|
| Background | `#213243` | Editor, sidebar |
| Chrome | `#132132` | Status bar, dropdowns |
| Panels | `#3a4b5c` | Activity bar, section headers |
| Foreground | `#C5C9C5` | Normal text |
| String | `#8A9A7B` | String literals |
| Function | `#8BA4B0` | Function names |
| Keyword | `#8992A7` | Keywords, control flow |
| Type | `#8EA4A2` | Types, classes |
| Number | `#A292A3` | Numeric literals |
| Constant | `#B6927B` | Boolean, language constants |
| Orange | `#f0aa8a` | Warnings (Spring Night orange) |
| Status bar | `#536273` | Spring Night `bgstrong` |

## Installation

### From source

```bash
git clone https://github.com/ryokn/spring-dragon
cp -r spring-dragon/vscode-spring-dragon ~/.vscode/extensions/spring-dragon-1.0.0
```

Reload VS Code: `Ctrl+Shift+P` → `Developer: Reload Window`

Then select the theme: `Ctrl+Shift+P` → `Preferences: Color Theme` → **Spring Dragon**

## Customization

Colors are managed in `convert.py`. Edit the `PALETTE` or `EDITOR_COLORS` / `TOKEN_COLORS` sections, then regenerate:

```bash
python convert.py
rm -rf ~/.vscode/extensions/spring-dragon-1.0.0
cp -r vscode-spring-dragon ~/.vscode/extensions/spring-dragon-1.0.0
```

To inspect any token's scope in VS Code: `Ctrl+Shift+P` → `Developer: Inspect Editor Tokens and Scopes`

## Credits

- Background colors inspired by [vim-color-spring-night](https://github.com/rhysd/vim-color-spring-night) by [@rhysd](https://github.com/rhysd) (MIT)
- Syntax colors inspired by [Kanagawa Dragon](https://github.com/metaphore/kanagawa-vscode) (MIT)

## License

MIT
