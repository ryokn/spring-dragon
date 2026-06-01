"""Kanagawa Dragon をベースにした Spring Dragon テーマ生成スクリプト"""

import json
import os

# パレット（Kanagawa Dragon の色を抽出・整理）
PALETTE = {
    # 背景（Spring Night の色を使用、暗い順）
    "bg0":       "#132132",  # 最暗背景（ドロップダウン、ステータスバー）
    "bg1":       "#213243",  # エディタ背景（一段暗く）
    "bg2":       "#334152",  # 非アクティブタブ（エディタより明るく）
    "bg3":       "#3a4b5c",  # アクティビティバー、ペイン
    "bg4":       "#435060",  # ホバー、選択、行ハイライト
    "bg5":       "#536273",  # ボーダー、単語ハイライト
    # 前景
    "fg":        "#C5C9C5",  # メイン前景
    "fg2":       "#C8C093",  # ステータスバー前景
    "dimmed":    "#A6A69C",  # 薄い前景（引数等）
    "weakfg":    "#9E9B93",  # 区切り文字
    "faintfg":   "#737C73",  # コメント、行番号
    # シンタックス
    "blue":      "#8BA4B0",  # 関数
    "cyan":      "#8EA4A2",  # クラス、CSS
    "teal":      "#6A9589",  # テキストリンク
    "green":     "#8A9A7B",  # 文字列、追加 diff
    "purple":    "#8992A7",  # キーワード、ストレージ
    "violet":    "#A292A3",  # 数値
    "pink":      "#B6927B",  # 定数、列挙体
    "tan":       "#C4B28A",  # 演算子、タグ、プロパティ
    "red":       "#C4746E",  # マクロ、エラー系
    "brightblue":"#7FB4CA",  # ターミナル明るい青
    # アクセント・UI
    "accent":    "#658594",  # バッジ、ハイライト前景
    "selection": "#223249",  # UI背景（補完ポップアップ等）
    "sakura":    "#70495d",  # テキスト選択背景（Spring Night yaezakura）
    "find":      "#2D4F67",  # 検索マッチ背景
    # Git / 診断
    "added":     "#76946A",
    "modified":  "#DCA561",
    "deleted":   "#C34043",
    "error":     "#E82424",
    "warning":   "#f0aa8a",  # Spring Night orange（落ち着いたオレンジ）
}

EDITOR_COLORS = {
    # エディタ基本
    "editor.background":                      PALETTE["bg1"],
    "editor.foreground":                      PALETTE["fg"],
    "editor.lineHighlightBackground":         PALETTE["bg4"],
    "editorCursor.background":                PALETTE["bg1"],
    "editorCursor.foreground":                PALETTE["fg"],
    "editorLineNumber.foreground":            PALETTE["bg5"],
    "editorLineNumber.activeForeground":      PALETTE["warning"],
    "editorWhitespace.foreground":            PALETTE["bg1"],

    # 選択・ハイライト
    "editor.selectionBackground":             PALETTE["sakura"],
    "editor.selectionHighlightBackground":    PALETTE["sakura"] + "55",
    "editor.selectionHighlightBorder":        PALETTE["bg5"],
    "editor.wordHighlightBackground":         PALETTE["bg4"] + "4D",
    "editor.wordHighlightBorder":             PALETTE["bg5"],
    "editor.wordHighlightStrongBackground":   PALETTE["bg4"] + "4D",
    "editor.wordHighlightStrongBorder":       PALETTE["bg5"],

    # 検索
    "editor.findMatchBackground":             PALETTE["find"],
    "editor.findMatchBorder":                 PALETTE["warning"],
    "editor.findMatchHighlightBackground":    PALETTE["find"] + "80",

    # ブラケット
    "editorBracketMatch.background":          PALETTE["bg0"],
    "editorBracketMatch.border":              PALETTE["bg5"],
    "editorBracketHighlight.foreground1":     PALETTE["purple"],
    "editorBracketHighlight.foreground2":     PALETTE["pink"],
    "editorBracketHighlight.foreground3":     PALETTE["blue"],
    "editorBracketHighlight.foreground4":     PALETTE["violet"],
    "editorBracketHighlight.foreground5":     PALETTE["tan"],
    "editorBracketHighlight.foreground6":     PALETTE["cyan"],
    "editorBracketHighlight.unexpectedBracket.foreground": PALETTE["red"],
    "editorBracketPairGuide.activeBackground1": PALETTE["purple"],
    "editorBracketPairGuide.activeBackground2": PALETTE["pink"],
    "editorBracketPairGuide.activeBackground3": PALETTE["blue"],
    "editorBracketPairGuide.activeBackground4": PALETTE["violet"],
    "editorBracketPairGuide.activeBackground5": PALETTE["tan"],
    "editorBracketPairGuide.activeBackground6": PALETTE["cyan"],

    # インデントガイド
    "editorIndentGuide.background1":          PALETTE["bg3"],
    "editorIndentGuide.activeBackground1":    PALETTE["bg4"],

    # エラー・警告
    "editorError.foreground":                 PALETTE["error"],
    "editorWarning.foreground":               PALETTE["warning"],

    # ルーラー・ガター
    "editorRuler.foreground":                 PALETTE["bg4"],
    "editorGutter.addedBackground":           PALETTE["added"],
    "editorGutter.modifiedBackground":        PALETTE["modified"],
    "editorGutter.deletedBackground":         PALETTE["deleted"],

    # ホバー・ウィジェット
    "editorHoverWidget.background":           PALETTE["bg1"],
    "editorHoverWidget.border":               PALETTE["bg3"],
    "editorHoverWidget.highlightForeground":  PALETTE["accent"],
    "editorWidget.background":                PALETTE["bg1"],
    "editorMarkerNavigation.background":      PALETTE["bg4"],

    # インレイヒント
    "editorInlayHint.foreground":             PALETTE["faintfg"],
    "editorInlayHint.background":             PALETTE["bg1"],

    # diff
    "diffEditor.insertedTextBackground":      PALETTE["added"] + "80",

    # タブ・エディタグループ
    "editorGroupHeader.tabsBackground":       PALETTE["bg0"],
    "editorGroup.border":                     PALETTE["bg0"],
    "tab.activeBackground":                   PALETTE["bg3"],
    "tab.activeForeground":                   PALETTE["blue"],
    "tab.inactiveBackground":                 PALETTE["bg2"],
    "tab.border":                             PALETTE["bg3"],
    "tab.hoverBackground":                    PALETTE["bg4"],
    "tab.unfocusedHoverBackground":           PALETTE["bg1"],

    # サイドバー
    "sideBar.background":                     PALETTE["bg1"],
    "sideBar.foreground":                     PALETTE["fg"],
    "sideBar.border":                         PALETTE["bg0"],
    "sideBarSectionHeader.background":        PALETTE["bg4"],
    "sideBarSectionHeader.foreground":        PALETTE["fg"],

    # アクティビティバー
    "activityBar.background":                 PALETTE["bg3"],
    "activityBar.foreground":                 PALETTE["fg"],
    "activityBarBadge.background":            PALETTE["accent"],
    "activityBarBadge.foreground":            PALETTE["fg"],

    # ステータスバー
    "statusBar.background":                   PALETTE["bg5"],
    "statusBar.foreground":                   PALETTE["fg"],
    "statusBar.border":                       PALETTE["bg5"],
    "statusBar.noFolderBackground":           PALETTE["bg5"],
    "statusBar.debuggingBackground":          PALETTE["error"],
    "statusBar.debuggingForeground":          PALETTE["fg"],
    "statusBarItem.hoverBackground":          PALETTE["bg3"],
    "statusBarItem.remoteBackground":         PALETTE["find"],
    "statusBarItem.remoteForeground":         PALETTE["fg"],

    # タイトルバー
    "titleBar.activeBackground":              PALETTE["bg4"],
    "titleBar.activeForeground":              PALETTE["fg"],
    "titleBar.inactiveBackground":            PALETTE["bg1"],
    "titleBar.inactiveForeground":            PALETTE["fg"],

    # パネル
    "panel.border":                           PALETTE["bg0"],
    "panelSectionHeader.background":          PALETTE["bg1"],

    # ターミナル
    "terminal.background":                    PALETTE["bg1"],
    "terminal.foreground":                    PALETTE["fg"],
    "terminal.border":                        PALETTE["bg0"],
    "terminal.selectionBackground":           PALETTE["sakura"],
    "terminal.ansiBlack":                     PALETTE["bg0"],
    "terminal.ansiRed":                       PALETTE["red"],
    "terminal.ansiGreen":                     PALETTE["green"],
    "terminal.ansiYellow":                    PALETTE["tan"],
    "terminal.ansiBlue":                      PALETTE["blue"],
    "terminal.ansiMagenta":                   PALETTE["violet"],
    "terminal.ansiCyan":                      PALETTE["cyan"],
    "terminal.ansiWhite":                     PALETTE["fg2"],
    "terminal.ansiBrightBlack":               PALETTE["dimmed"],
    "terminal.ansiBrightRed":                 "#E46876",
    "terminal.ansiBrightGreen":               "#87A987",
    "terminal.ansiBrightYellow":              "#E6C384",
    "terminal.ansiBrightBlue":                PALETTE["brightblue"],
    "terminal.ansiBrightMagenta":             "#938AA9",
    "terminal.ansiBrightCyan":                "#7AA89F",
    "terminal.ansiBrightWhite":               PALETTE["fg"],

    # ポップアップ・補完
    "editorSuggestWidget.background":         PALETTE["selection"],
    "editorSuggestWidget.border":             PALETTE["selection"],
    "editorSuggestWidget.selectedBackground": PALETTE["find"],

    # 入力・ドロップダウン
    "input.background":                       PALETTE["bg0"],
    "dropdown.background":                    PALETTE["bg0"],
    "dropdown.border":                        PALETTE["bg0"],

    # ボタン
    "button.background":                      PALETTE["bg3"],
    "button.foreground":                      PALETTE["fg2"],
    "button.secondaryBackground":             PALETTE["selection"],
    "button.secondaryForeground":             PALETTE["fg"],
    "checkbox.border":                        PALETTE["selection"],

    # スクロールバー
    "scrollbar.shadow":                       PALETTE["bg4"],
    "scrollbarSlider.background":             PALETTE["bg5"] + "66",
    "scrollbarSlider.hoverBackground":        PALETTE["bg5"] + "80",
    "scrollbarSlider.activeBackground":       PALETTE["bg3"] + "80",

    # ミニマップ・Git
    "minimapGutter.addedBackground":          PALETTE["added"],
    "minimapGutter.modifiedBackground":       PALETTE["modified"],
    "minimapGutter.deletedBackground":        PALETTE["deleted"],

    # Git 装飾
    "gitDecoration.ignoredResourceForeground": PALETTE["faintfg"],

    # リスト・ツリー
    "list.activeSelectionBackground":         PALETTE["bg4"],
    "list.activeSelectionForeground":         PALETTE["fg"],
    "list.inactiveSelectionBackground":       PALETTE["bg3"],
    "list.inactiveSelectionForeground":       PALETTE["fg"],
    "list.focusBackground":                   PALETTE["bg3"],
    "list.focusForeground":                   PALETTE["fg"],
    "list.hoverBackground":                   PALETTE["bg4"],
    "list.hoverForeground":                   PALETTE["fg"],
    "list.highlightForeground":               PALETTE["blue"],
    "list.warningForeground":                 PALETTE["warning"],

    # ピーク表示
    "peekView.border":                        PALETTE["bg5"],
    "peekViewEditor.background":              PALETTE["bg3"],
    "peekViewEditor.matchHighlightBackground": PALETTE["find"],
    "peekViewResult.background":              PALETTE["bg4"],

    # メニュー
    "menubar.selectionBackground":            PALETTE["bg0"],
    "menubar.selectionForeground":            PALETTE["fg"],
    "menu.background":                        PALETTE["bg4"],
    "menu.border":                            PALETTE["bg0"],
    "menu.foreground":                        PALETTE["fg"],
    "menu.selectionBackground":               PALETTE["bg0"],
    "menu.selectionForeground":               PALETTE["fg"],
    "menu.separatorBackground":               PALETTE["bg5"],

    # その他
    "focusBorder":                            PALETTE["selection"],
    "foreground":                             PALETTE["fg"],
    "descriptionForeground":                  PALETTE["fg"],
    "badge.background":                       PALETTE["bg3"],
    "settings.focusedRowBackground":          PALETTE["bg4"],
    "settings.headerForeground":              PALETTE["fg"],
    "debugToolBar.background":                PALETTE["bg0"],
    "textBlockQuote.background":              PALETTE["bg1"],
    "textBlockQuote.border":                  PALETTE["bg0"],
    "textLink.foreground":                    PALETTE["teal"],

    "walkThrough.embeddedEditorBackground":   PALETTE["bg1"],
}

TOKEN_COLORS = [
    {
        "name": "Comment",
        "scope": ["comment", "punctuation.definition.comment"],
        "settings": {"foreground": PALETTE["faintfg"]},
    },
    {
        "name": "Variable",
        "scope": ["variable", "string constant.other.placeholder"],
        "settings": {"foreground": PALETTE["fg"]},
    },
    {
        "name": "Constant name (readonly variable)",
        "scope": [
            "variable.other.constant",
            "variable.other.enummember",
            "constant.other",
        ],
        "settings": {"foreground": PALETTE["fg"]},
    },
    {
        "name": "Invalid",
        "scope": ["invalid", "invalid.illegal"],
        "settings": {"foreground": PALETTE["error"]},
    },
    {
        "name": "Storage - Type",
        "scope": ["storage.type"],
        "settings": {"foreground": PALETTE["purple"]},
    },
    {
        "name": "Storage - Modifier",
        "scope": ["storage.modifier"],
        "settings": {"foreground": PALETTE["purple"]},
    },
    {
        "name": "Function declaration keyword (def/fn/func)",
        "scope": [
            "storage.type.function",
            "storage.type.class",
            "keyword.declaration.function",
            "keyword.declaration.class",
        ],
        "settings": {"foreground": PALETTE["purple"]},
    },
    {
        "name": "Control Keyword",
        "scope": [
            "keyword.control.flow",
            "keyword.control.conditional",
            "keyword.control.loop",
        ],
        "settings": {"foreground": PALETTE["purple"], "fontStyle": "bold"},
    },
    {
        "name": "Keyword",
        "scope": [
            "keyword.control",
            "keyword.other.template",
            "keyword.other.substitution",
            "keyword.other",
        ],
        "settings": {"foreground": PALETTE["purple"]},
    },
    {
        "name": "Try/Catch Keyword",
        "scope": ["keyword.control.trycatch"],
        "settings": {"foreground": PALETTE["red"], "fontStyle": "bold"},
    },
    {
        "name": "Import",
        "scope": [
            "keyword.control.import",
            "keyword.import",
            "meta.import",
        ],
        "settings": {"foreground": PALETTE["pink"]},
    },
    {
        "name": "Operator",
        "scope": ["keyword.operator", "keyword.other.unit"],
        "settings": {"foreground": PALETTE["tan"]},
    },
    {
        "name": "Punctuation",
        "scope": [
            "punctuation",
            "punctuation.definition.tag",
            "punctuation.section.embedded",
            "meta.brace",
            "keyword.operator.type.annotation",
            "keyword.operator.namespace",
        ],
        "settings": {"foreground": PALETTE["weakfg"]},
    },
    {
        "name": "String",
        "scope": [
            "string",
            "punctuation.definition.string",
            "constant.other.symbol",
            "constant.other.key",
            "entity.other.inherited-class",
            "markup.inline.raw.string",
        ],
        "settings": {"foreground": PALETTE["green"]},
    },
    {
        "name": "String escape / Regexp",
        "scope": [
            "constant.character.escape",
            "string.regexp",
        ],
        "settings": {"foreground": "#949FB5"},
    },
    {
        "name": "Number",
        "scope": ["constant.numeric"],
        "settings": {"foreground": PALETTE["violet"]},
    },
    {
        "name": "Boolean / Language constant",
        "scope": ["constant.language", "constant.language.boolean"],
        "settings": {"foreground": PALETTE["pink"]},
    },
    {
        "name": "Constant",
        "scope": [
            "constant",
            "support.constant",
            "constant.character",
            "constant.escape",
        ],
        "settings": {"foreground": PALETTE["pink"]},
    },
    {
        "name": "Function",
        "scope": [
            "entity.name.function",
            "meta.function-call",
            "variable.function",
            "support.function",
        ],
        "settings": {"foreground": PALETTE["blue"]},
    },
    {
        "name": "Macro",
        "scope": ["entity.name.function.macro"],
        "settings": {"foreground": PALETTE["red"]},
    },
    {
        "name": "Type / Class",
        "scope": [
            "entity.name",
            "support.type",
            "support.class",
            "support.type.sys-types",
        ],
        "settings": {"foreground": PALETTE["cyan"]},
    },
    {
        "name": "Namespace / Module",
        "scope": [
            "entity.name.type.module",
            "entity.name.namespace",
        ],
        "settings": {"foreground": PALETTE["tan"]},
    },
    {
        "name": "Tag",
        "scope": ["entity.name.tag", "meta.tag.sgml"],
        "settings": {"foreground": PALETTE["tan"]},
    },
    {
        "name": "Tag attribute",
        "scope": ["entity.other.attribute-name"],
        "settings": {"foreground": PALETTE["purple"]},
    },
    {
        "name": "CSS Class",
        "scope": ["entity.other.attribute-name.class"],
        "settings": {"foreground": PALETTE["tan"]},
    },
    {
        "name": "Property",
        "scope": ["variable.other.property"],
        "settings": {"foreground": PALETTE["tan"]},
    },
    {
        "name": "Enum Member",
        "scope": ["variable.other.enummember"],
        "settings": {"foreground": PALETTE["pink"]},
    },
    {
        "name": "Language variable (self/this)",
        "scope": ["variable.language"],
        "settings": {"foreground": PALETTE["red"]},
    },
    {
        "name": "CSS property",
        "scope": [
            "source.css support.type.property-name",
            "source.sass support.type.property-name",
            "source.scss support.type.property-name",
        ],
        "settings": {"foreground": PALETTE["cyan"]},
    },
    {
        "name": "Diff inserted",
        "scope": ["markup.inserted"],
        "settings": {"foreground": PALETTE["added"]},
    },
    {
        "name": "Diff deleted",
        "scope": ["markup.deleted"],
        "settings": {"foreground": PALETTE["deleted"]},
    },
    {
        "name": "Diff changed",
        "scope": ["markup.changed"],
        "settings": {"foreground": PALETTE["modified"]},
    },
    {
        "name": "Markdown heading",
        "scope": [
            "markdown.heading",
            "entity.name.section.markdown",
            "markup.heading.markdown",
        ],
        "settings": {"foreground": PALETTE["blue"]},
    },
    {
        "name": "Markup italic",
        "scope": ["markup.italic"],
        "settings": {"fontStyle": "italic", "foreground": PALETTE["red"]},
    },
    {
        "name": "Markup bold",
        "scope": ["markup.bold", "markup.bold string"],
        "settings": {"fontStyle": "bold"},
    },
    {
        "name": "Markup link",
        "scope": ["string.other.link.title.markdown"],
        "settings": {"foreground": PALETTE["pink"]},
    },
    {
        "name": "Markup underline",
        "scope": ["markup.underline"],
        "settings": {"fontStyle": "underline", "foreground": "#949FB5"},
    },
    {
        "name": "Markdown separator",
        "scope": ["meta.separator"],
        "settings": {"fontStyle": "bold", "foreground": PALETTE["weakfg"]},
    },
    {
        "name": "JSON Key - Level 0",
        "scope": [
            "source.json meta.structure.dictionary.json support.type.property-name.json"
        ],
        "settings": {"foreground": PALETTE["violet"]},
    },
    {
        "name": "JSON Key - Level 1",
        "scope": [
            "source.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json support.type.property-name.json"
        ],
        "settings": {"foreground": PALETTE["tan"]},
    },
    {
        "name": "JSON Key - Level 2",
        "scope": [
            "source.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json meta.structure.dictionary.value.json meta.structure.dictionary.json support.type.property-name.json"
        ],
        "settings": {"foreground": PALETTE["pink"]},
    },
]


def build_theme() -> dict:
    return {
        "name": "Spring Dragon",
        "type": "dark",
        "semanticHighlighting": False,
        "colors": EDITOR_COLORS,
        "tokenColors": TOKEN_COLORS,
    }


def build_package_json(theme_filename: str) -> dict:
    return {
        "name": "vscode-spring-dragon",
        "displayName": "Spring Dragon",
        "description": "Dark color theme based on Kanagawa Dragon with Spring Night backgrounds",
        "version": "1.0.0",
        "publisher": "dragon-night",
        "license": "MIT",
        "engines": {"vscode": "^1.70.0"},
        "categories": ["Themes"],
        "keywords": ["theme", "color-theme", "dark", "kanagawa", "dragon", "spring"],
        "contributes": {
            "themes": [
                {
                    "label": "Spring Dragon",
                    "uiTheme": "vs-dark",
                    "path": f"./themes/{theme_filename}",
                }
            ]
        },
    }


def main():
    out_dir = "vscode-spring-dragon"
    themes_dir = os.path.join(out_dir, "themes")
    theme_filename = "spring-dragon-color-theme.json"

    os.makedirs(themes_dir, exist_ok=True)

    theme_path = os.path.join(themes_dir, theme_filename)
    with open(theme_path, "w", encoding="utf-8") as f:
        json.dump(build_theme(), f, indent=2, ensure_ascii=False)
    print(f"生成: {theme_path}")

    pkg_path = os.path.join(out_dir, "package.json")
    with open(pkg_path, "w", encoding="utf-8") as f:
        json.dump(build_package_json(theme_filename), f, indent=2, ensure_ascii=False)
    print(f"生成: {pkg_path}")

    print("\n完了。反映するには:")
    print(f"  rm -rf ~/.vscode/extensions/spring-dragon-1.0.0")
    print(f"  cp -r {out_dir} ~/.vscode/extensions/spring-dragon-1.0.0")
    print("  VS Code: Ctrl+Shift+P → Developer: Reload Window")


if __name__ == "__main__":
    main()
