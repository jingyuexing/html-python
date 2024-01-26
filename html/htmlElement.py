from dataclasses import dataclass
from typing import Any, Dict, List, Literal, TypeVar, Union
from html.Element import Element


TagName = Literal[
    "div",
    "meta",
    "head",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "ul",
    "ol",
    "li",
    "i",
    "html",
    "button",
    "body",
    "title",
    "style",
    "input",
    "script",
    "img",
    "link",
    "table",
    "td",
    "tr",
    "col",
    "area",
    "br",
    "hr",
    "audio",
]
# ['br', 'img', 'input', 'hr', 'meta', 'link', 'base', 'col', 'area']


class HTMLElement(Element):
    dataset: Dict[str, Any]

    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = ""


class HTMLDIVElement(HTMLElement):
    dataset: Dict[str, Any]

    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "div"


class HTMLBUTTONElement(HTMLElement):
    dataset: Dict[str, Any]

    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "button"


class HTMLHTMLElement(HTMLElement):
    dataset: Dict[str, Any]

    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "html"

    def __str__(self) -> str:
        return "<!DOCTYPE html>" + super().__str__()


class HTMLMETAElement(HTMLElement):
    dataset: Dict[str, Any]

    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "meta"

    def __str__(self):
        selfCloseing = [self.tagName, self.__attributes_str__()]
        return "<{tag}>".format(tag=" ".join(selfCloseing))


class HTMLHEADElement(HTMLElement):
    dataset: Dict[str, Any]

    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "head"


class HTMLINPUTElement(HTMLElement):
    dataset: Dict[str, Any]

    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "input"


class HTMLH1Element(HTMLElement):
    dataset: Dict[str, Any]

    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "h1"


class HTMLH2Element(HTMLElement):
    dataset: Dict[str, Any]

    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "h2"


class HTMLH3Element(HTMLElement):
    dataset: Dict[str, Any]

    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "h3"


class HTMLH4Element(HTMLElement):
    dataset: Dict[str, Any]

    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "h4"


class HTMLH5Element(HTMLElement):
    dataset: Dict[str, Any]

    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "h5"


class HTMLH6Element(HTMLElement):
    dataset: Dict[str, Any]

    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "h6"


class HTMLLINKElement(HTMLElement):
    dataset: Dict[str, Any]

    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "link"


class HTMLSTYLEElement(HTMLElement):
    dataset: Dict[str, Any]

    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "style"


class HTMLTitleElement(HTMLElement):
    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "title"
        pass


class HTMLBodyElement(HTMLElement):
    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "body"
        pass


class HTMLULElement(HTMLElement):
    dataset: Dict[str, Any]

    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "ul"


class HTMLOLElement(HTMLElement):
    dataset: Dict[str, Any]

    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "ol"


class HTMLIElement(HTMLElement):
    dataset: Dict[str, Any]

    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "i"


class HTMLLIElement(HTMLElement):
    dataset: Dict[str, Any]

    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "li"


class HTMLSCRIPTElement(HTMLElement):
    dataset: Dict[str, Any]

    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "script"


class HTMLImageElement(HTMLElement):
    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "img"

    def __str__(self):
        tagwithattr = [self.tagName, self.__attributes_str__()]
        return "<{tag}>".format(tag=tagwithattr)


class HTMLBRElement(HTMLElement):
    def __init__(self):
        super().__init__()
        self.tagName = self.nodeName = "br"

    def __str__(self):
        tagwithattr = [self.tagName, self.__attributes_str__()]
        return "<{tag}>".format(tag=tagwithattr)


def createMeta(head: Element, meta: Dict[str, str]):
    for k in meta:
        metaTag = createElement("meta")
        metaTag.setAttributes("name", k)
        metaTag.setAttributes("content", meta[k])
        head.appendChild(metaTag)


def createElement(tag: TagName) -> HTMLElement:
    tabNameMap = {
        "div": HTMLDIVElement,
        "input": HTMLINPUTElement,
        "h1": HTMLH1Element,
        "title": HTMLTitleElement,
        "h2": HTMLH2Element,
        "h3": HTMLH3Element,
        "h4": HTMLH4Element,
        "h5": HTMLH5Element,
        "h6": HTMLH6Element,
        "br": HTMLBRElement,
        "html": HTMLHTMLElement,
        "head": HTMLHEADElement,
        "body": HTMLBodyElement,
        "ul": HTMLULElement,
        "ol": HTMLOLElement,
        "i": HTMLIElement,
        "button": HTMLBUTTONElement,
        "li": HTMLLIElement,
        "script": HTMLSCRIPTElement,
        "style": HTMLSTYLEElement,
        "img": HTMLImageElement,
        "link": HTMLLINKElement,
        "meta": HTMLMETAElement,
        "col": HTMLElement,
    }
    return tabNameMap[tag]()


class VNode:
    tag: TagName
    className = ""
    attribute = {}
    style: Dict[str, str] = {}
    child: List[Union[str, "VNode"]] = []

    def __init__(self, tag: TagName, className="", attribute={}, style={}, child=[]):
        self.tag = tag
        self.className = className
        self.attribute = attribute
        self.style = style
        self.child = child


def createTextNode(data:Any):
    return str(data)

def createVMeta(description:Dict[str,str])->List['VNode']:
    VNodes = []
    for k in description:
        VNodes.append(VNode("meta",attribute={
            "name": k,
            "content": description[k],
        }))
    return VNodes

def createVNode(root: "HTMLElement", tree: "VNode"):
    tag = createElement(tree.tag)
    tag.className = tree.className
    if len(tree.className) > 0 and tree.className != "":
        tag.className = tree.className
    if len(tree.style) > 0:
        for key in tree.style:
            tag.style.setProperty(key, tree.style.get(key))
    if len(tree.attribute) > 0:
        for key in tree.attribute:
            tag.setAttributes(key, tree.attribute[key])
    for vnode in tree.child:
        if isinstance(vnode, VNode):
            createVNode(tag, vnode)
        if isinstance(vnode, str):
            tag.textContent = createTextNode(vnode)
    root.appendChild(tag)


PAGE = HTMLHTMLElement()

def HTML(description: Dict[str, Any]):
    document = createElement("html")
    body = createElement("body")
    title = createElement("title")
    document.setAttributes("lang", "en")
    title.textContent = description.get("title", "")
    createVNode(
        document,
        VNode(
            tag="head",
            child=[
                VNode("meta",attribute={"charset": description.get("charset","UTF-8")}),
                *createVMeta(description=description.get("meta",{})),
            ],
        ),
    )
    head = document.getElementByTagName("head")[0]
    head.appendChild(title)
    document.appendChild(body)
    return document,head,body

PAGE,HEAD,BODY = HTML({
    "meta":{
        "viewport":"width=device-width, initial-scale=1.0",
        "description":"this is website description",
        "keyword":"this is website keyword"
    },
    "charset":"UTF-8",
    "title":"this is test document"    
})


