# -*- coding: utf-8 -*-
# @Author: Jingyuexing
# @Date:   2024-01-14 23:44:35
# @Last Modified by:   Jingyuexing
# @Last Modified time: 2024-01-27 04:15:11

from typing import List, Optional
from html.htmlElement import HTMLElement, VNode, createElement, createVNode


class Tabs:
    dom:'HTMLElement'
    activeDOM:Optional['HTMLElement']
    def __init__(self,items:List[str]) -> None:
        self.items = items
        self.activeDOM = None
        self.dom = createElement("div")
        self.dom.className = "flex justify-around w-full items-center gap-2 relative"
        self.dom.ariaLabel = "tabs"
        for item in items:
            createVNode(self.dom,VNode("div",className="flex justify-center items-center p-3",attribute={"aria-label":"tab-item"},child=[item]))
    def active(self,item):
        idx = self.items.index(item)
        if self.activeDOM is not None:
            self.activeDOM.removeAttributes("data-status")

        self.activeDOM = self.dom.childNodes[idx]
        self.activeDOM.setAttributes("data-status","active")
        self.dom.setAttributes("data-active",idx)
    def __str__(self) -> str:
        return str(self.dom)

class Button:
    dom:HTMLElement
    def __init__(self):
        pass