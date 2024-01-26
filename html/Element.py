# -*- coding: utf-8 -*-
# @Author: Jingyuexing
# @Date:   2024-01-14 14:51:22
# @Last Modified by:   Jingyuexing
# @Last Modified time: 2024-01-15 17:19:47
from typing import Any, Dict, List, Optional, Union
from html.ARIAMixin import ARIAMixin
from html.DOMTokenList import DOMTokenList

from html.Node import Node
from html.Style import Style
from html.utils import camel_to_kebab


class Element(Node,ARIAMixin):
    prefix: Optional[str]
    scrollHeight: int
    scrollLeft: int
    scrollTop: int
    scrollWidth: int
    style:'Style'
    slot: str
    tagName: str
    attributes:Dict[str,str]

    def __init__(self):
        self.prefix = None
        self.scrollHeight = 0
        self.scrollLeft = 0
        self.scrollTop = 0
        self.scrollWidth = 0
        self.slot = ""
        self.tagName = ""
        self.attributes = {}
        # self.className = ""
        self.classList = DOMTokenList()
        self.style = Style()
        super().__init__()
    
    def setAttributes(self,key:str,value:Any):
        self.attributes[key] = str(value)
  
    
    @property
    def className(self)->str:
        return str(self.classList)
    
    @className.setter
    def className(self,classNames:str):
        self.classList.add(classNames.split(" "))
    
    def removeAttributes(self,key:str):
        del self.attributes[key]
    
    def getAttributes(self,key:str):
        return self.attributes[key]
    
    def __str__(self) -> str:
        attrs_list = [self.tagName]
        innerText = [self.textContent if self.textContent is not None else ""]
        
        if len(self.classList) > 0:
            attrs_list.append("class=\"{v}\"".format(v=str(self.classList)))
        
        if len(str(self.style)) > 0:
            attrs_list.append("style=\"{style}\"".format(style=str(self.style)))
        
        if len(self.attributes) > 0:
            attrs_list.append(str(self.__attributes_str__()))

        if len(self.__ARIAMixin_str__()) > 0:
            attrs_list.append(str(self.__ARIAMixin_str__()))

        for item in self.childNodes:
            innerText.append(item.__str__())

        return "<{tagwithattr}>{inner}</{tag}>".format(
            tagwithattr=" ".join(attrs_list),
            inner="".join(innerText),
            tag=self.tagName
        )

    @property
    def childElements(self)->List["Element"]:
        return self.childNodes

    def getElementByTagName(self,tag:str)->List['Element']:
        result = []
        def dfs(node):
            if node.nodeName == tag:
                result.append(node)
            for child in node.childNodes:
                dfs(child)
        for item in self.childNodes:
            dfs(item)
        return result

    def getElementByClassName(self,className:str)->Union['Element',List['Element']]:
        result = []
        def dfs(node:'Element'):
            if node.classList.include(className):
                result.append(node)
            for child in node.childNodes:
                dfs(child)
        if self.classList.include(className):
            result.append(self)
        for item in self.childNodes:
            dfs(item)
        if len(result) == 1:
            return result[0]
        else:
            return result

    def __attributes_str__(self)->str:
        attr = []
        for k in self.attributes:
            if self.attributes[k] is not None:
                attr.append("{k}=\"{v}\"".format(k=camel_to_kebab(k),v=self.attributes[k]))
    
        return " ".join(attr)