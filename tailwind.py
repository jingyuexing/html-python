# -*- coding: utf-8 -*-
# @Author: Jingyuexing
# @Date:   2024-01-15 00:57:11
# @Last Modified by:   Jingyuexing
# @Last Modified time: 2024-01-15 03:14:58

import re
from typing import Any, Callable, Dict, List


class TailWindRules:
    rule: str
    func: Callable[[str], List[str]]

    def __init__(self, rule: str, fn: Callable[[str], List[str]]):
        self.rule = rule
        self.func = fn


class Tailwind:
    classTokens: Dict[str, List[str]]
    rules: List["TailWindRules"]

    def __init__(self):
        self.classTokens = {}
        self.rules = []
        self.boot()

    def addRule(self, rule: str, func: Callable[[str], List[str]]):
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
            return [f"padding-left:{int(num) * 0.25}rem;", f"padding-right:{int(num) * 0.25}rem;"]


        def layout_padding_y(num: str):
            return [f"padding-top:{int(num) * 0.25}rem;", f"padding-bottom:{int(num) * 0.25}rem;"]


        def layout_gap(num:str):
            return [f"gap:{int(num) * 0.25}rem;"]


        def layout_width(num, unit: str = "px"):
            return [f"width:{num}{unit};"]


        def layout_width_raw(fill: str):
            return [f"width:{fill};"]


        def layout_height(num, unit: str = "px"):
            return [f"width:{num}{unit};"]


        def layout_height_raw(fill: str):
            return [f"width:{fill};"]


        def layout_flex_direction(direction: str):
            directionMap = {
                "row": "row",
                "row-reverse": "row-reverse",
                "col": "column",
                "col-reverse": "column-reverse",
            }
            return [f"flex-direction:{directionMap[direction]}"]

        def layout_align_items(align:str):
            if align in ["start", "end"]:
                return [f"align-items: flex-{align};"]
            else:
                return [f"align-items: {align};"]
        def layout_display(display:str):
            return [f"display:{display};"]

        def layout_position(position:str):
            return [f"position:{position};"]

        def layout_place_items(items:str):
            return [f"place-items:{items};"]

        def layout_object_fit(fit:str):
            return [f"object-fit: {fit};"]

        def layout_overflow(mode:str):
            return [f"overflow: {mode};"]


        def layout_column_span():
            pass
        def layout_full(rule:str):
            if rule == "w":
                return layout_width(100,"%")
            else:
                return layout_height(100,"%")
        self.addRule(r"p-(\d+)", layout_padding)
        self.addRule(r"px-(\d+)", layout_padding_x)
        self.addRule(r"py-(\d+)", layout_padding_y)
        self.addRule(r"(w|h)-full",layout_full)
        self.addRule(
            r"justify-(normal|start|end|center|right|left|between|around|evenly|stretch)",
            func=layout_justify,
        )
        self.addRule(r"flex-(row|row-reverse|col|col-reverse)", func=layout_flex_direction)

        self.addRule(r"items-(start|end|center|baseline|stretch)",layout_align_items)
        self.addRule(r"gap-(\d+)",layout_gap)
        self.addRule(r"place-items-(start|end|center|baseline|stretch)",layout_place_items)
        self.addRule(r"(block|inline-block|inline|grid|flex|inline-flex|table|inline-table|table-caption)",layout_display)
        self.addRule(r"display-(block|inline-block|inline|grid|flex|inline-flex|table|inline-table|table-caption)",layout_display)
        self.addRule(r"(static|fixed|absolute|relative|sticky)",layout_position)
        self.addRule(r"object-(contain|cover|fill|none|scale-down)",layout_object_fit)
        self.addRule(r"overflow-(auto|hidden|clip|visible|scroll)",layout_overflow)
    def generator(self, classNames:str):
        self.parser(classNames)
        for key in self.classTokens:
            for rule in self.rules:
                matchText = re.compile(rule.rule).search(key)
                if matchText:
                    self.classTokens[key] = rule.func(*list(matchText.groups()))

    def __str__(self) -> str:
        css = []
        for className in self.classTokens:
            css.append(
                f".{className}{''.join(['{',''.join(self.classTokens[className]),'}'])}"
            )
        return "".join(css)



TW = Tailwind()

# TW.addRule(r"float-(right|left|none)",)
# TW.addRule(r"grid-(rows|cols)-(\d+)",)
# TW.addRule(r"grid-(rows|cols)-none",)
# TW.addRule(r"grid-(rows|cols)-[(.+)]",)
# TW.addRule(r"grid-flow-(col|row|revert)",)
# TW.addRule(r"(left|right|top|bottom)-(auto|inherit|initial|revert|unset)",)
