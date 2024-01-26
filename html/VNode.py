# -*- coding: utf-8 -*-
# @Author: Jingyuexing
# @Date:   2024-01-14 17:30:07
# @Last Modified by:   Jingyuexing
# @Last Modified time: 2024-01-14 21:43:40


from dataclasses import dataclass
from typing import Dict, List, Union

from html.htmlElement import HTMLElement, TagName, createElement

@dataclass
class VNode:
    tag:TagName
    className = ""
    attribute = {}
    style:Dict[str,str] = {}
    child:List[Union[str,'VNode']] = []


def createVNode(root:'HTMLElement',tree:'VNode'):
    tag = createElement(tree.tag)
    tag.className = tree.className
    if tree.className != "":
        tag.className = tree.className
    if len(tree.style) > 0:
        for key in tree.style:
            tag.style.setProperty(key,tree.style.get(key))
    if len(tree.attribute) > 0:
        for key in tree.attribute:
            tag.setAttributes(key,tree.attribute[key])
    for vnode in tree.child:
        if isinstance(vnode,VNode):
            createVNode(tag,vnode)
        if isinstance(vnode,str):
            tag.textContent = vnode
    root.appendChild(tree.tag)