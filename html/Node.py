# -*- coding: utf-8 -*-
# @Author: Jingyuexing
# @Date:   2024-01-14 14:42:55
# @Last Modified by:   Jingyuexing
# @Last Modified time: 2024-01-14 17:22:13
from typing import List, Optional


class Node:
    nodeName: str = ""
    nodeType: int = 0
    nodeValue: Optional[str] = None
    ATTRIBUTE_NODE: int = 0
    childNodes:List['Node']
    CDATA_SECTION_NODE: int = 0
    COMMENT_NODE: int = 0
    DOCUMENT_FRAGMENT_NODE: int = 0
    DOCUMENT_NODE: int = 0
    DOCUMENT_POSITION_CONTAINED_BY: int = 0
    DOCUMENT_POSITION_CONTAINS: int = 0
    DOCUMENT_POSITION_DISCONNECTED: int = 0
    DOCUMENT_POSITION_FOLLOWING: int
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC: int = 0
    DOCUMENT_POSITION_PRECEDING: int = 0
    DOCUMENT_TYPE_NODE: int = 0
    ELEMENT_NODE: int = 0
    ENTITY_NODE: int = 0
    textContent:Optional[str] = None
    ENTITY_REFERENCE_NODE: int = 0
    NOTATION_NODE: int = 0
    PROCESSING_INSTRUCTION_NODE: int = 0
    TEXT_NODE: int = 0
    def __init__(self):
        self.textContent = ""
        self.childNodes = []
    def appendChild(self,node):
        self.childNodes.append(node)