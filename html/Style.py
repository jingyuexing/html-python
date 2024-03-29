# -*- coding: utf-8 -*-
# @Author: Jingyuexing
# @Date:   2024-01-14 14:27:01
# @Last Modified by:   Jingyuexing
# @Last Modified time: 2024-01-14 20:19:55
from typing import Optional

from html.utils import camel_to_kebab

class Style:
    accentColor: str = ""
    alignContent: str = ""
    alignItems: str = ""
    alignSelf: str = ""
    alignmentBaseline: str = ""
    animation: str = ""
    animationDelay: str = ""
    animationDirection: str = ""
    animationDuration: str = ""
    animationFillMode: str = ""
    animationIterationCount: str = ""
    animationName: str = ""
    animationPlayState: str = ""
    animationTimingFunction: str = ""
    appearance: str = ""
    aspectRatio: str = ""
    backdropFilter: str = ""
    backfaceVisibility: str = ""
    background: str = ""
    backgroundAttachment: str = ""
    backgroundBlendMode: str = ""
    backgroundClip: str = ""
    backgroundColor: str = ""
    backgroundImage: str = ""
    backgroundOrigin: str = ""
    backgroundPosition: str = ""
    backgroundPositionX: str = ""
    backgroundPositionY: str = ""
    backgroundRepeat: str = ""
    backgroundSize: str = ""
    baselineShift: str = ""
    blockSize: str = ""
    border: str = ""
    borderBlock: str = ""
    borderBlockColor: str = ""
    borderBlockEnd: str = ""
    borderBlockEndColor: str = ""
    borderBlockEndStyle: str = ""
    borderBlockEndWidth: str = ""
    borderBlockStart: str = ""
    borderBlockStartColor: str = ""
    borderBlockStartStyle: str = ""
    borderBlockStartWidth: str = ""
    borderBlockStyle: str = ""
    borderBlockWidth: str = ""
    borderBottom: str = ""
    borderBottomColor: str = ""
    borderBottomLeftRadius: str = ""
    borderBottomRightRadius: str = ""
    borderBottomStyle: str = ""
    borderBottomWidth: str = ""
    borderCollapse: str = ""
    borderColor: str = ""
    borderEndEndRadius: str = ""
    borderEndStartRadius: str = ""
    borderImage: str = ""
    borderImageOutset: str = ""
    borderImageRepeat: str = ""
    borderImageSlice: str = ""
    borderImageSource: str = ""
    borderImageWidth: str = ""
    borderInline: str = ""
    borderInlineColor: str = ""
    borderInlineEnd: str = ""
    borderInlineEndColor: str = ""
    borderInlineEndStyle: str = ""
    borderInlineEndWidth: str = ""
    borderInlineStart: str = ""
    borderInlineStartColor: str = ""
    borderInlineStartStyle: str = ""
    borderInlineStartWidth: str = ""
    borderInlineStyle: str = ""
    borderInlineWidth: str = ""
    borderLeft: str = ""
    borderLeftColor: str = ""
    borderLeftStyle: str = ""
    borderLeftWidth: str = ""
    borderRadius: str = ""
    borderRight: str = ""
    borderRightColor: str = ""
    borderRightStyle: str = ""
    borderRightWidth: str = ""
    borderSpacing: str = ""
    borderStartEndRadius: str = ""
    borderStartStartRadius: str = ""
    borderStyle: str = ""
    borderTop: str = ""
    borderTopColor: str = ""
    borderTopLeftRadius: str = ""
    borderTopRightRadius: str = ""
    borderTopStyle: str = ""
    borderTopWidth: str = ""
    borderWidth: str = ""
    bottom: str = ""
    boxShadow: str = ""
    boxSizing: str = ""
    breakAfter: str = ""
    breakBefore: str = ""
    breakInside: str = ""
    captionSide: str = ""
    caretColor: str = ""
    clear: str = ""
    clip: str = ""
    clipPath: str = ""
    clipRule: str = ""
    color: str = ""
    colorInterpolation: str = ""
    colorInterpolationFilters: str = ""
    colorScheme: str = ""
    columnCount: str = ""
    columnFill: str = ""
    columnGap: str = ""
    columnRule: str = ""
    columnRuleColor: str = ""
    columnRuleStyle: str = ""
    columnRuleWidth: str = ""
    columnSpan: str = ""
    columnWidth: str = ""
    columns: str = ""
    contain: str = ""
    container: str = ""
    containerName: str = ""
    containerType: str = ""
    content: str = ""
    counterIncrement: str = ""
    counterReset: str = ""
    counterSet: str = ""
    cssFloat: str = ""
    cssText: str = ""
    cursor: str = ""
    direction: str = ""
    display: str = ""
    dominantBaseline: str = ""
    emptyCells: str = ""
    fill: str = ""
    fillOpacity: str = ""
    fillRule: str = ""
    filter: str = ""
    flex: str = ""
    flexBasis: str = ""
    flexDirection: str = ""
    flexFlow: str = ""
    flexGrow: str = ""
    flexShrink: str = ""
    flexWrap: str = ""
    float: str = ""
    floodColor: str = ""
    floodOpacity: str = ""
    font: str = ""
    fontFamily: str = ""
    fontFeatureSettings: str = ""
    fontKerning: str = ""
    fontOpticalSizing: str = ""
    fontPalette: str = ""
    fontSize: str = ""
    fontSizeAdjust: str = ""
    fontStretch: str = ""
    fontStyle: str = ""
    fontSynthesis: str = ""
    fontVariant: str = ""
    fontVariantAlternates: str = ""
    fontVariantCaps: str = ""
    fontVariantEastAsian: str = ""
    fontVariantLigatures: str = ""
    fontVariantNumeric: str = ""
    fontVariantPosition: str = ""
    fontVariationSettings: str = ""
    fontWeight: str = ""
    gap: str = ""
    grid: str = ""
    gridArea: str = ""
    gridAutoColumns: str = ""
    gridAutoFlow: str = ""
    gridAutoRows: str = ""
    gridColumn: str = ""
    gridColumnEnd: str = ""
    gridColumnGap: str = ""
    gridColumnStart: str = ""
    gridGap: str = ""
    gridRow: str = ""
    gridRowEnd: str = ""
    gridRowGap: str = ""
    gridRowStart: str = ""
    gridTemplate: str = ""
    gridTemplateAreas: str = ""
    gridTemplateColumns: str = ""
    gridTemplateRows: str = ""
    height: str = ""
    hyphenateCharacter: str = ""
    hyphens: str = ""
    imageOrientation: str = ""
    imageRendering: str = ""
    inlineSize: str = ""
    inset: str = ""
    insetBlock: str = ""
    insetBlockEnd: str = ""
    insetBlockStart: str = ""
    insetInline: str = ""
    insetInlineEnd: str = ""
    insetInlineStart: str = ""
    isolation: str = ""
    justifyContent: str = ""
    justifyItems: str = ""
    justifySelf: str = ""
    left: str = ""
    letterSpacing: str = ""
    lightingColor: str = ""
    lineBreak: str = ""
    lineHeight: str = ""
    listStyle: str = ""
    listStyleImage: str = ""
    listStylePosition: str = ""
    listStyleType: str = ""
    margin: str = ""
    marginBlock: str = ""
    marginBlockEnd: str = ""
    marginBlockStart: str = ""
    marginBottom: str = ""
    marginInline: str = ""
    marginInlineEnd: str = ""
    marginInlineStart: str = ""
    marginLeft: str = ""
    marginRight: str = ""
    marginTop: str = ""
    marker: str = ""
    markerEnd: str = ""
    markerMid: str = ""
    markerStart: str = ""
    mask: str = ""
    maskClip: str = ""
    maskComposite: str = ""
    maskImage: str = ""
    maskMode: str = ""
    maskOrigin: str = ""
    maskPosition: str = ""
    maskRepeat: str = ""
    maskSize: str = ""
    maskType: str = ""
    maxBlockSize: str = ""
    maxHeight: str = ""
    maxInlineSize: str = ""
    maxWidth: str = ""
    minBlockSize: str = ""
    minHeight: str = ""
    minInlineSize: str = ""
    minWidth: str = ""
    mixBlendMode: str = ""
    objectFit: str = ""
    objectPosition: str = ""
    offset: str = ""
    offsetDistance: str = ""
    offsetPath: str = ""
    offsetRotate: str = ""
    opacity: str = ""
    order: str = ""
    orphans: str = ""
    outline: str = ""
    outlineColor: str = ""
    outlineOffset: str = ""
    outlineStyle: str = ""
    outlineWidth: str = ""
    overflow: str = ""
    overflowAnchor: str = ""
    overflowClipMargin: str = ""
    overflowWrap: str = ""
    overflowX: str = ""
    overflowY: str = ""
    overscrollBehavior: str = ""
    overscrollBehaviorBlock: str = ""
    overscrollBehaviorInline: str = ""
    overscrollBehaviorX: str = ""
    overscrollBehaviorY: str = ""
    padding: str = ""
    paddingBlock: str = ""
    paddingBlockEnd: str = ""
    paddingBlockStart: str = ""
    paddingBottom: str = ""
    paddingInline: str = ""
    paddingInlineEnd: str = ""
    paddingInlineStart: str = ""
    paddingLeft: str = ""
    paddingRight: str = ""
    paddingTop: str = ""
    pageBreakAfter: str = ""
    pageBreakBefore: str = ""
    pageBreakInside: str = ""
    paintOrder: str = ""
    perspective: str = ""
    perspectiveOrigin: str = ""
    placeContent: str = ""
    placeItems: str = ""
    placeSelf: str = ""
    pointerEvents: str = ""
    position: str = ""
    printColorAdjust: str = ""
    quotes: str = ""
    resize: str = ""
    right: str = ""
    rotate: str = ""
    rowGap: str = ""
    rubyPosition: str = ""
    scale: str = ""
    scrollBehavior: str = ""
    scrollMargin: str = ""
    scrollMarginBlock: str = ""
    scrollMarginBlockEnd: str = ""
    scrollMarginBlockStart: str = ""
    scrollMarginBottom: str = ""
    scrollMarginInline: str = ""
    scrollMarginInlineEnd: str = ""
    scrollMarginInlineStart: str = ""
    scrollMarginLeft: str = ""
    scrollMarginRight: str = ""
    scrollMarginTop: str = ""
    scrollPadding: str = ""
    scrollPaddingBlock: str = ""
    scrollPaddingBlockEnd: str = ""
    scrollPaddingBlockStart: str = ""
    scrollPaddingBottom: str = ""
    scrollPaddingInline: str = ""
    scrollPaddingInlineEnd: str = ""
    scrollPaddingInlineStart: str = ""
    scrollPaddingLeft: str = ""
    scrollPaddingRight: str = ""
    scrollPaddingTop: str = ""
    scrollSnapAlign: str = ""
    scrollSnapStop: str = ""
    scrollSnapType: str = ""
    scrollbarGutter: str = ""
    shapeImageThreshold: str = ""
    shapeMargin: str = ""
    shapeOutside: str = ""
    shapeRendering: str = ""
    stopColor: str = ""
    stopOpacity: str = ""
    stroke: str = ""
    strokeDasharray: str = ""
    strokeDashoffset: str = ""
    strokeLinecap: str = ""
    strokeLinejoin: str = ""
    strokeMiterlimit: str = ""
    strokeOpacity: str = ""
    strokeWidth: str = ""
    tabSize: str = ""
    tableLayout: str = ""
    textAlign: str = ""
    textAlignLast: str = ""
    textAnchor: str = ""
    textCombineUpright: str = ""
    textDecoration: str = ""
    textDecorationColor: str = ""
    textDecorationLine: str = ""
    textDecorationSkipInk: str = ""
    textDecorationStyle: str = ""
    textDecorationThickness: str = ""
    textEmphasis: str = ""
    textEmphasisColor: str = ""
    textEmphasisPosition: str = ""
    textEmphasisStyle: str = ""
    textIndent: str = ""
    textOrientation: str = ""
    textOverflow: str = ""
    textRendering: str = ""
    textShadow: str = ""
    textTransform: str = ""
    textUnderlineOffset: str = ""
    textUnderlinePosition: str = ""
    top: str = ""
    touchAction: str = ""
    transform: str = ""
    transformBox: str = ""
    transformOrigin: str = ""
    transformStyle: str = ""
    transition: str = ""
    transitionDelay: str = ""
    transitionDuration: str = ""
    transitionProperty: str = ""
    transitionTimingFunction: str = ""
    translate: str = ""
    unicodeBidi: str = ""
    userSelect: str = ""
    verticalAlign: str = ""
    visibility: str = ""
    webkitAlignContent: str = ""
    webkitAlignItems: str = ""
    webkitAlignSelf: str = ""
    webkitAnimation: str = ""
    webkitAnimationDelay: str = ""
    webkitAnimationDirection: str = ""
    webkitAnimationDuration: str = ""
    webkitAnimationFillMode: str = ""
    webkitAnimationIterationCount: str = ""
    webkitAnimationName: str = ""
    webkitAnimationPlayState: str = ""
    webkitAnimationTimingFunction: str = ""
    webkitAppearance: str = ""
    webkitBackfaceVisibility: str = ""
    webkitBackgroundClip: str = ""
    webkitBackgroundOrigin: str = ""
    webkitBackgroundSize: str = ""
    webkitBorderBottomLeftRadius: str = ""
    webkitBorderBottomRightRadius: str = ""
    webkitBorderRadius: str = ""
    webkitBorderTopLeftRadius: str = ""
    webkitBorderTopRightRadius: str = ""
    webkitBoxAlign: str = ""
    webkitBoxFlex: str = ""
    webkitBoxOrdinalGroup: str = ""
    webkitBoxOrient: str = ""
    webkitBoxPack: str = ""
    webkitBoxShadow: str = ""
    webkitBoxSizing: str = ""
    webkitFilter: str = ""
    webkitFlex: str = ""
    webkitFlexBasis: str = ""
    webkitFlexDirection: str = ""
    webkitFlexFlow: str = ""
    webkitFlexGrow: str = ""
    webkitFlexShrink: str = ""
    webkitFlexWrap: str = ""
    webkitJustifyContent: str = ""
    webkitLineClamp: str = ""
    webkitMask: str = ""
    webkitMaskBoxImage: str = ""
    webkitMaskBoxImageOutset: str = ""
    webkitMaskBoxImageRepeat: str = ""
    webkitMaskBoxImageSlice: str = ""
    webkitMaskBoxImageSource: str = ""
    webkitMaskBoxImageWidth: str = ""
    webkitMaskClip: str = ""
    webkitMaskComposite: str = ""
    webkitMaskImage: str = ""
    webkitMaskOrigin: str = ""
    webkitMaskPosition: str = ""
    webkitMaskRepeat: str = ""
    webkitMaskSize: str = ""
    webkitOrder: str = ""
    webkitPerspective: str = ""
    webkitPerspectiveOrigin: str = ""
    webkitTextFillColor: str = ""
    webkitTextSizeAdjust: str = ""
    webkitTextStroke: str = ""
    webkitTextStrokeColor: str = ""
    webkitTextStrokeWidth: str = ""
    webkitTransform: str = ""
    webkitTransformOrigin: str = ""
    webkitTransformStyle: str = ""
    webkitTransition: str = ""
    webkitTransitionDelay: str = ""
    webkitTransitionDuration: str = ""
    webkitTransitionProperty: str = ""
    webkitTransitionTimingFunction: str = ""
    webkitUserSelect: str = ""
    whiteSpace: str = ""
    widows: str = ""
    width: str = ""
    willChange: str = ""
    wordBreak: str = ""
    wordSpacing: str = ""
    wordWrap: str = ""
    writingMode: str = ""
    zIndex: str = ""
    def __init__(self):
        pass
    def __str__(self):
        styles = []
        for key in self.__dict__:
            if self.__dict__.get(key) != "":
                styles.append(": ".join([camel_to_kebab(key),self.__dict__[key]]))
        return "; ".join(styles)
    def setProperty(self,property:str, value:Optional[str] = None, priority:Optional[str]=None):
        self.__dict__[property] = "" if value is None else value
