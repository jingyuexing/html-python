# -*- coding: utf-8 -*-
# @Author: Jingyuexing
# @Date:   2024-01-15 00:19:56
# @Last Modified by:   Jingyuexing
# @Last Modified time: 2024-01-15 03:17:14

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from uvicorn import run
from html.Element import Element

from html.htmlElement import BODY, HEAD, PAGE, createElement
from htmlCompnents import Tabs
from tailwind import TW
app = FastAPI()

tabs = Tabs(["home","project","photos"])
style = createElement("style")
BODY.appendChild(tabs.dom)
HEAD.appendChild(style)
def findAllClass(node:'Element'):
    clsNames = {}
    def dfs(node:'Element'):
        if node.className != "":
            for clsName in node.classList.value.split(" "):
                clsNames[clsName] = ""
        for child in node.childNodes:
            dfs(child)
    dfs(node)
    return list(clsNames.keys())

def updateStyle():
    TW.generator(" ".join(findAllClass(PAGE)))
    style.textContent = str(TW) + "*{padding:0;margin:0;}"

@app.get("/", response_class=HTMLResponse)
def html():
    updateStyle()
    return HTMLResponse(content=str(PAGE))

@app.get("/active/{item}",response_class=HTMLResponse)
def active(item:str):
    if item in tabs.items:
        tabs.active(item)
    updateStyle()
    return HTMLResponse(content=str(PAGE))

if __name__ == '__main__':
    run(app,port=8326)