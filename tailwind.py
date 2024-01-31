# -*- coding: utf-8 -*-
# @Author: Jingyuexing
# @Date:   2024-01-15 00:57:11
# @Last Modified by:   Jingyuexing
# @Last Modified time: 2024-01-29 15:43:50

import re
from typing import Any, Callable, Dict, List, Optional, Union


def accessNested(
    nest_obj: Dict[str, Any], keys: List[str], delimiter="-"
) -> Optional[Dict[str, Any]]:
    """
    访问嵌套字典的方法
    :param nest_obj: 嵌套字典
    :param keys: 由嵌套层级组成的键列表
    :param delimiter: 分隔符
    :return: 对应键路径下的值，如果路径无效则返回 None
    """
    current_dict = nest_obj
    for key in keys:
        if delimiter in key:
            sub_keys = key.split(delimiter)
            for sub_key in sub_keys:
                if sub_key in current_dict.keys():
                    current_dict = current_dict[sub_key]
                else:
                    return None
        else:
            if key in current_dict:
                current_dict = current_dict[key]
            else:
                return None

    return current_dict


class TailWindRules:
    rule: str
    func: Callable[[str], List[str]]

    def __init__(self, rule: str, fn: Callable[[str], List[str]]):
        self.rule = rule
        self.func = fn


class Tailwind:
    classTokens: Dict[str, List[str]]
    rules: List["TailWindRules"]
    root: Dict[str, Any]

    def __init__(self):
        self.classTokens = {}
        self.rules = []
        self.root = {}
        self.configure = {}
        self.boot()

    def addRule(self, rule: str, func: Callable[[Any], List[str]]):
        self.rules.append(TailWindRules(rule, fn=func))

    def parser(self, classNames: str):
        for i in classNames.split(" "):
            self.classTokens[i] = []

    def boot(self):
        def layout_flex(layout: str):
            return [f"display:{layout};"]

        def layout_padding(num: str):
            return [f"padding:{int(num) * 0.25}rem;"]

        def layout_justify(pos: str):
            if pos in ["between", "around", "evenly"]:
                return [f"justify-content: space-{pos};"]
            if pos in ["start", "end"]:
                return [f"justify-content: flex-{pos};"]
            return [f"justify-content:{pos};"]

        def layout_padding_x(num: str):
            return [
                f"padding-left:{int(num) * 0.25}rem;",
                f"padding-right:{int(num) * 0.25}rem;",
            ]

        def layout_padding_y(num: str):
            return [
                f"padding-top:{int(num) * 0.25}rem;",
                f"padding-bottom:{int(num) * 0.25}rem;",
            ]

        def layout_gap(num: str):
            return [f"gap:{int(num) * 0.25}rem;"]

        def layout_width(num, unit: str = "px"):
            return [f"width:{num}{unit};"]

        def layout_width_raw(fill: str):
            return [f"width:{fill};"]

        def layout_height(num, unit: str = "px"):
            return [f"height:{num}{unit};"]

        def layout_height_raw(fill: str):
            return [f"height:{fill};"]

        def layout_flex_direction(direction: str):
            directionMap = {
                "row": "row",
                "row-reverse": "row-reverse",
                "col": "column",
                "col-reverse": "column-reverse",
            }
            return [f"flex-direction:{directionMap[direction]};"]

        def layout_align_items(align: str):
            if align in ["start", "end"]:
                return [f"align-items: flex-{align};"]
            else:
                return [f"align-items: {align};"]

        def layout_display(display: str):
            return [f"display:{display};"]

        def layout_position(position: str):
            return [f"position:{position};"]

        def layout_place_items(items: str):
            return [f"place-items:{items};"]

        def layout_object_fit(fit: str):
            return [f"object-fit: {fit};"]

        def layout_overflow(mode: str):
            return [f"overflow: {mode};"]

        def self_layout(mode: str):
            if mode in ["end", "start"]:
                return [f"align-self: flex-{mode};"]
            return [f"align-self: {mode};"]

        def layout_column_span(num: str):
            if num == "full":
                return ["grid-column: 1 / -1;"]

            if num == "auto":
                return ["grid-column: auto;"]

            return [f"grid-column: span {num} / span {num};"]

        def layout_full(rule: str):
            if rule == "w":
                return layout_width(100, "%")
            else:
                return layout_height(100, "%")

        def grid_column_rows(mode: str, size: str):
            if mode == "rows":
                return [f"grid-template-rows: repeat({size}, minmax(0, 1fr));"]
            return [f"grid-template-columns: repeat({size}, minmax(0, 1fr));"]

        def grid_flow(mode: str):
            if mode == "col":
                return ["grid-auto-flow: column"]
            return [f"grid-auto-flow: {mode}"]

        def text_overflow(mode):
            return [f"text-overflow: {mode};"]

        def text_indent(mode: str):
            return [f"text-indent: {int(mode) * 0.25}rem;"]

        def text_size(size: str):
            return [f"font-size:{int(size) * 0.25}rem;"]

        def writing_mode(mode: str):
            key = "-".join(["writing", mode])
            val = accessNested(self.configure, [key])
            if val is not None:
                return [f"writing-mode:{val};"]
            return []

        def text_transform(mode: str):
            if mode == "normal-case":
                return ["text-transform: none;"]
            return [f"text-transform: {mode};"]

        def line_height(height: str):
            return [f"line-height: {int(height) * 0.25}rem;"]

        def line_height_config(mode: str):
            key = "-".join(["leading", mode])
            val = accessNested(self.configure, [key])
            if val is None:
                return []
            return [f"line-height: {val};"]

        def text_size_config(size: str):
            if size.isnumeric():
                return text_size(size)
            key = "-".join(["text", size])
            _val = accessNested(self.configure, [key])
            if _val is not None:
                _size = _val["size"]
                _line = _val["height"]
                return [
                    f"font-size:{_size * 0.25}rem;",
                    f"line-height:{_line * 0.25}rem;",
                ]
            return []

        def border_style(mode: str):
            return [f"border-style: {mode};"]

        self.addRule(r"p-(\d+)", layout_padding)
        self.addRule(r"px-(\d+)", layout_padding_x)
        self.addRule(r"py-(\d+)", layout_padding_y)
        self.addRule(r"(w|h)-full", layout_full)
        self.addRule(
            r"justify-(normal|start|end|center|right|left|between|around|evenly|stretch)",
            func=layout_justify,
        )
        self.addRule(
            r"flex-(row|row-reverse|col|col-reverse)", func=layout_flex_direction
        )

        self.addRule(r"items-(start|end|center|baseline|stretch)", layout_align_items)
        self.addRule(r"gap-(\d+)", layout_gap)
        self.addRule(
            r"place-items-(start|end|center|baseline|stretch)", layout_place_items
        )
        self.addRule(
            r"(block|inline-block|inline|grid|flex|inline-flex|table|inline-table|table-caption)",
            layout_display,
        )
        self.addRule(
            r"display-(block|inline-block|inline|grid|flex|inline-flex|table|inline-table|table-caption)",
            layout_display,
        )
        self.addRule(r"(static|fixed|absolute|relative|sticky)", layout_position)
        self.addRule(r"object-(contain|cover|fill|none|scale-down)", layout_object_fit)
        self.addRule(r"overflow-(auto|hidden|clip|visible|scroll)", layout_overflow)
        self.addRule(r"col-span-(\d+|auto|full)", layout_column_span)
        self.addRule(r"self-(auto|start|end|center|stretch|baseline)", self_layout)
        self.addRule(r"grid-(rows|cols)-(\d+)", grid_column_rows)
        self.addRule(r"grid-flow-(col|row|revert)", grid_flow)
        self.addRule(r"text-(ellipsis|clip)", text_overflow)
        self.addRule(r"text-([\w-]+)", text_size_config)
        self.addRule(r"indent-(\d+)", text_indent)
        self.addRule(r"writing-([a-zA-Z\-]+)", writing_mode)
        self.addRule(r"leading-(\d+)", line_height)
        self.addRule(r"leading-([a-zA-Z]+)", line_height_config)
        self.addRule(r"(uppercase|lowercase|capitalize|normal-case)", text_transform)
        self.addRule(r"border-(solid|dashed|dotted|double|hidden|none)", border_style)

    def generator(self, classNames: str):
        self.parser(classNames)
        for key in self.classTokens:
            for rule in self.rules:
                matchText = re.compile(rule.rule).search(key)
                if matchText:
                    self.classTokens[key] = rule.func(*list(matchText.groups()))

    def convert_class(self, classname: str):
        for char in classname:
            if char in ["[", "]", "#", ":", "(", ")", ",", "/", "!", "%", "@"]:
                classname = classname.replace(char, "\\" + char)
        return classname

    def __str__(self) -> str:
        css = []
        for className in self.classTokens:
            if len(self.classTokens[className]) > 0:
                css.append(
                    f".{self.convert_class(className)}{''.join(['{',''.join(self.classTokens[className]),'}'])}"
                )
        _root = []
        variable = self.__all_variable__()
        for var in variable:
            _root.append(f"--{var}:{variable[var]};")
        if len(_root) > 0:
            root_variable = ":root{variable}".format(
                variable="".join(["{", "".join(_root), "}"])
            )
        else:
            root_variable = ""
        return root_variable + "".join(css)

    def __all_variable__(self):
        def flatten_dict(d, parent_key="", delimiter="-"):
            result = {}

            for key, value in d.items():
                new_key = f"{parent_key}{delimiter}{key}" if parent_key else key

                if isinstance(value, dict):
                    result.update(flatten_dict(value, new_key, delimiter))
                else:
                    result[new_key] = value if value is not None else ""

            return result

        return flatten_dict(self.root)

    def variable(self, dic: Dict[str, Any]):
        for key in dic:
            self.root[key] = dic[key]

    def config(self, dic: Dict[str, Any]):
        self.configure = dic


TW = Tailwind()

TW.variable(
    {
        "theme": {
            "dark": {
                "background": "",
                "primary": "T",
                "secondary": "T",
                "warning": "T",
                "info": "T",
                "success": "T",
                "danger": "T",
            },
            "light": {
                "background": "",
                "primary": "T",
                "secondary": "T",
                "warning": "T",
                "info": "T",
                "success": "T",
                "danger": "T",
            },
        }
    }
)
TW.config(
    {
        "leading": {
            "none": 1,
            "tight": "",
            "snug": "",
            "normal": "",
            "relaxed": "",
            "loose": "",
        },
        "font": {
            "sans": """ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji" """,
            "serif": 'ui-serif, Georgia, Cambria, "Times New Roman", Times, serif',
            "mono": 'ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace',
        },
        "text": {
            "xs": {
                "size": 3,
                "height": 4,
            },
            "sm": {
                "size": 3.5,
                "height": 5,
            },
            "base": {
                "size": 4,
                "height": 6,
            },
            "lg": {
                "size": 3,
                "height": 7,
            },
            "xl": {
                "size": 3,
                "height": 8,
            },
            "2xl": {
                "size": 6,
                "height": 8,
            },
            "3xl": {
                "size": 7.5,
                "height": 9,
            },
            "4xl": {
                "size": 9,
                "height": 10,
            },
            "5xl": {
                "size": 12,
                "height": 4,
            },
            "6xl": {
                "size": 13,
                "height": 4,
            },
            "7xl": {
                "size": 18,
                "height": 4,
            },
            "8xl": {
                "size": 24,
                "height": 4,
            },
            "9xl": {
                "size": 32,
                "height": 4,
            },
        },
        "writing": {
            "vertical": "vertical-rl",
            "revert": "revert",
            "horizontal": "horizontal-tb",
        },
        "colors": {
            "inherit": "inherit",
            "current": "currentColor",
            "transparent": "transparent",
            "black": "#000",
            "white": "#fff",
            "slate": {
                50: "#f8fafc",
                100: "#f1f5f9",
                200: "#e2e8f0",
                300: "#cbd5e1",
                400: "#94a3b8",
                500: "#64748b",
                600: "#475569",
                700: "#334155",
                800: "#1e293b",
                900: "#0f172a",
                950: "#020617",
            },
            "gray": {
                50: "#f9fafb",
                100: "#f3f4f6",
                200: "#e5e7eb",
                300: "#d1d5db",
                400: "#9ca3af",
                500: "#6b7280",
                600: "#4b5563",
                700: "#374151",
                800: "#1f2937",
                900: "#111827",
                950: "#030712",
            },
            "zinc": {
                50: "#fafafa",
                100: "#f4f4f5",
                200: "#e4e4e7",
                300: "#d4d4d8",
                400: "#a1a1aa",
                500: "#71717a",
                600: "#52525b",
                700: "#3f3f46",
                800: "#27272a",
                900: "#18181b",
                950: "#09090b",
            },
            "neutral": {
                50: "#fafafa",
                100: "#f5f5f5",
                200: "#e5e5e5",
                300: "#d4d4d4",
                400: "#a3a3a3",
                500: "#737373",
                600: "#525252",
                700: "#404040",
                800: "#262626",
                900: "#171717",
                950: "#0a0a0a",
            },
            "stone": {
                50: "#fafaf9",
                100: "#f5f5f4",
                200: "#e7e5e4",
                300: "#d6d3d1",
                400: "#a8a29e",
                500: "#78716c",
                600: "#57534e",
                700: "#44403c",
                800: "#292524",
                900: "#1c1917",
                950: "#0c0a09",
            },
            "red": {
                50: "#fef2f2",
                100: "#fee2e2",
                200: "#fecaca",
                300: "#fca5a5",
                400: "#f87171",
                500: "#ef4444",
                600: "#dc2626",
                700: "#b91c1c",
                800: "#991b1b",
                900: "#7f1d1d",
                950: "#450a0a",
            },
            "orange": {
                50: "#fff7ed",
                100: "#ffedd5",
                200: "#fed7aa",
                300: "#fdba74",
                400: "#fb923c",
                500: "#f97316",
                600: "#ea580c",
                700: "#c2410c",
                800: "#9a3412",
                900: "#7c2d12",
                950: "#431407",
            },
            "amber": {
                50: "#fffbeb",
                100: "#fef3c7",
                200: "#fde68a",
                300: "#fcd34d",
                400: "#fbbf24",
                500: "#f59e0b",
                600: "#d97706",
                700: "#b45309",
                800: "#92400e",
                900: "#78350f",
                950: "#451a03",
            },
            "yellow": {
                50: "#fefce8",
                100: "#fef9c3",
                200: "#fef08a",
                300: "#fde047",
                400: "#facc15",
                500: "#eab308",
                600: "#ca8a04",
                700: "#a16207",
                800: "#854d0e",
                900: "#713f12",
                950: "#422006",
            },
            "lime": {
                50: "#f7fee7",
                100: "#ecfccb",
                200: "#d9f99d",
                300: "#bef264",
                400: "#a3e635",
                500: "#84cc16",
                600: "#65a30d",
                700: "#4d7c0f",
                800: "#3f6212",
                900: "#365314",
                950: "#1a2e05",
            },
            "green": {
                50: "#f0fdf4",
                100: "#dcfce7",
                200: "#bbf7d0",
                300: "#86efac",
                400: "#4ade80",
                500: "#22c55e",
                600: "#16a34a",
                700: "#15803d",
                800: "#166534",
                900: "#14532d",
                950: "#052e16",
            },
            "emerald": {
                50: "#ecfdf5",
                100: "#d1fae5",
                200: "#a7f3d0",
                300: "#6ee7b7",
                400: "#34d399",
                500: "#10b981",
                600: "#059669",
                700: "#047857",
                800: "#065f46",
                900: "#064e3b",
                950: "#022c22",
            },
            "teal": {
                50: "#f0fdfa",
                100: "#ccfbf1",
                200: "#99f6e4",
                300: "#5eead4",
                400: "#2dd4bf",
                500: "#14b8a6",
                600: "#0d9488",
                700: "#0f766e",
                800: "#115e59",
                900: "#134e4a",
                950: "#042f2e",
            },
            "cyan": {
                50: "#ecfeff",
                100: "#cffafe",
                200: "#a5f3fc",
                300: "#67e8f9",
                400: "#22d3ee",
                500: "#06b6d4",
                600: "#0891b2",
                700: "#0e7490",
                800: "#155e75",
                900: "#164e63",
                950: "#083344",
            },
            "sky": {
                50: "#f0f9ff",
                100: "#e0f2fe",
                200: "#bae6fd",
                300: "#7dd3fc",
                400: "#38bdf8",
                500: "#0ea5e9",
                600: "#0284c7",
                700: "#0369a1",
                800: "#075985",
                900: "#0c4a6e",
                950: "#082f49",
            },
            "blue": {
                50: "#eff6ff",
                100: "#dbeafe",
                200: "#bfdbfe",
                300: "#93c5fd",
                400: "#60a5fa",
                500: "#3b82f6",
                600: "#2563eb",
                700: "#1d4ed8",
                800: "#1e40af",
                900: "#1e3a8a",
                950: "#172554",
            },
            "indigo": {
                50: "#eef2ff",
                100: "#e0e7ff",
                200: "#c7d2fe",
                300: "#a5b4fc",
                400: "#818cf8",
                500: "#6366f1",
                600: "#4f46e5",
                700: "#4338ca",
                800: "#3730a3",
                900: "#312e81",
                950: "#1e1b4b",
            },
            "violet": {
                50: "#f5f3ff",
                100: "#ede9fe",
                200: "#ddd6fe",
                300: "#c4b5fd",
                400: "#a78bfa",
                500: "#8b5cf6",
                600: "#7c3aed",
                700: "#6d28d9",
                800: "#5b21b6",
                900: "#4c1d95",
                950: "#2e1065",
            },
            "purple": {
                50: "#faf5ff",
                100: "#f3e8ff",
                200: "#e9d5ff",
                300: "#d8b4fe",
                400: "#c084fc",
                500: "#a855f7",
                600: "#9333ea",
                700: "#7e22ce",
                800: "#6b21a8",
                900: "#581c87",
                950: "#3b0764",
            },
            "fuchsia": {
                50: "#fdf4ff",
                100: "#fae8ff",
                200: "#f5d0fe",
                300: "#f0abfc",
                400: "#e879f9",
                500: "#d946ef",
                600: "#c026d3",
                700: "#a21caf",
                800: "#86198f",
                900: "#701a75",
                950: "#4a044e",
            },
            "pink": {
                50: "#fdf2f8",
                100: "#fce7f3",
                200: "#fbcfe8",
                300: "#f9a8d4",
                400: "#f472b6",
                500: "#ec4899",
                600: "#db2777",
                700: "#be185d",
                800: "#9d174d",
                900: "#831843",
                950: "#500724",
            },
            "rose": {
                50: "#fff1f2",
                100: "#ffe4e6",
                200: "#fecdd3",
                300: "#fda4af",
                400: "#fb7185",
                500: "#f43f5e",
                600: "#e11d48",
                700: "#be123c",
                800: "#9f1239",
                900: "#881337",
                950: "#4c0519",
            },
        },
    }
)
