# -*- coding: utf-8 -*-
# @Author: Jingyuexing
# @Date:   2024-01-14 17:44:11
# @Last Modified by:   Jingyuexing
# @Last Modified time: 2024-01-15 17:10:08

from typing import List, Optional


class DOMTokenList:
    length:int = 0
    value:str
    __tokens__:List[str]
    def __init__(self):
        self.value = ""
        self.__tokens__ = []
    def add(self,token:List[str]):
        for item in token:
            self.__tokens__.append(item)
        self.length = self.__len__()
        self.value = self.__str__()
    
    def toggle(self,token:str)->bool:
        return False
    
    def item(self,idx:int)->Optional[str]:
        return self.__getitem__(idx)

    def include(self,classname):
        return classname in self.__tokens__


    def remove(self,token):
        self.__tokens__.remove(token)
        self.value = self.__str__()
        self.length = self.__len__()
    
    def __getitem__(self,idx:int)->Optional[str]:
        if idx in range(len(self.__tokens__)):
            return self.__tokens__[idx]
        else:
            return None

    def __str__(self):
        return " ".join(self.__tokens__)
    
    def __len__(self):
        return len(self.__tokens__)