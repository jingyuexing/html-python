# -*- coding: utf-8 -*-
# @Author: Jingyuexing
# @Date:   2024-01-14 14:40:22
# @Last Modified by:   Jingyuexing
# @Last Modified time: 2024-01-14 23:39:22
from typing import Optional

from html.utils import camel_to_kebab


class ARIAMixin:
    ariaAtomic: Optional[str]
    ariaAutoComplete: Optional[str]
    ariaBusy: Optional[str]
    ariaChecked: Optional[str]
    ariaColCount: Optional[str]
    ariaColIndex: Optional[str]
    ariaColIndexText: Optional[str]
    ariaColSpan: Optional[str]
    ariaCurrent: Optional[str]
    ariaDisabled: Optional[str]
    ariaExpanded: Optional[str]
    ariaHasPopup: Optional[str]
    ariaHidden: Optional[str]
    ariaInvalid: Optional[str]
    ariaKeyShortcuts: Optional[str]
    ariaLabel: Optional[str]
    ariaLevel: Optional[str]
    ariaLive: Optional[str]
    ariaModal: Optional[str]
    ariaMultiLine: Optional[str]
    ariaMultiSelectable: Optional[str]
    ariaOrientation: Optional[str]
    ariaPlaceholder: Optional[str]
    ariaPosInSet: Optional[str]
    ariaPressed: Optional[str]
    ariaReadOnly: Optional[str]
    ariaRequired: Optional[str]
    ariaRoleDescription: Optional[str]
    ariaRowCount: Optional[str]
    ariaRowIndex: Optional[str]
    ariaRowIndexText: Optional[str]
    ariaRowSpan: Optional[str]
    ariaSelected: Optional[str]
    ariaSetSize: Optional[str]
    ariaSort: Optional[str]
    ariaValueMax: Optional[str]
    ariaValueMin: Optional[str]
    ariaValueNow: Optional[str]
    ariaValueText: Optional[str]
    role: Optional[str]

    def __init__(self):
        self.ariaAtomic = ""
        self.ariaAutoComplete = ""
        self.ariaBusy = ""
        self.ariaChecked = ""
        self.ariaColCount = ""
        self.ariaColIndex = ""
        self.ariaColIndexText = ""
        self.ariaColSpan = ""
        self.ariaCurrent = ""
        self.ariaDisabled = ""
        self.ariaExpanded = ""
        self.ariaHasPopup = ""
        self.ariaHidden = ""
        self.ariaInvalid = ""
        self.ariaKeyShortcuts = ""
        self.ariaLabel = ""
        self.ariaLevel = ""
        self.ariaLive = ""
        self.ariaModal = ""
        self.ariaMultiLine = ""
        self.ariaMultiSelectable = ""
        self.ariaOrientation = ""
        self.ariaPlaceholder = ""
        self.ariaPosInSet = ""
        self.ariaPressed = ""
        self.ariaReadOnly = ""
        self.ariaRequired = ""
        self.ariaRoleDescription = ""
        self.ariaRowCount = ""
        self.ariaRowIndex = ""
        self.ariaRowIndexText = ""
        self.ariaRowSpan = ""
        self.ariaSelected = ""
        self.ariaSetSize = ""
        self.ariaSort = ""
        self.ariaValueMax = ""
        self.ariaValueMin = ""
        self.ariaValueNow = ""
        self.ariaValueText = ""
        self.role = ""

    def __ARIAMixin_str__(self) -> str:
        __slots__ = (
            "ariaAtomic",
            "ariaAutoComplete",
            "ariaBusy",
            "ariaChecked",
            "ariaColCount",
            "ariaColIndex",
            "ariaColIndexText",
            "ariaColSpan",
            "ariaCurrent",
            "ariaDisabled",
            "ariaExpanded",
            "ariaHasPopup",
            "ariaHidden",
            "ariaInvalid",
            "ariaKeyShortcuts",
            "ariaLabel",
            "ariaLevel",
            "ariaLive",
            "ariaModal",
            "ariaMultiLine",
            "ariaMultiSelectable",
            "ariaOrientation",
            "ariaPlaceholder",
            "ariaPosInSet",
            "ariaPressed",
            "ariaReadOnly",
            "ariaRequired",
            "ariaRoleDescription",
            "ariaRowCount",
            "ariaRowIndex",
            "ariaRowIndexText",
            "ariaRowSpan",
            "ariaSelected",
            "ariaSetSize",
            "ariaSort",
            "ariaValueMax",
            "ariaValueMin",
            "ariaValueNow",
            "ariaValueText",
            "role",
        )
        attrs = []
        for key in __slots__:
            value = self.__dict__.get(key, None)
            if value is not None and value != "":
                attrs.append(
                    '{key}="{val}"'.format(
                        key=camel_to_kebab(key), val=value
                    )
                )
        return " ".join(attrs)
