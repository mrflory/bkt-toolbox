# -*- coding: utf-8 -*-
'''
Created on 2019-07-25
@author: Florian Stallmann
'''

from __future__ import absolute_import

import bkt

if bkt.config.log_level == "DEBUG":

    def ctxm_button(name):
        return bkt.ribbon.ContextMenu(id_mso=name, children=[
                bkt.ribbon.Button(
                    label=name,
                    image_mso='HappyFace',
                ),
            ])


    #add button labelled with ID to every context menu

    ppt_ctx_menus = ["ContextMenuCommentMarker", "ContextMenuCurve", "ContextMenuDrawnObject", "ContextMenuFrame", "ContextMenuMotionPath", "ContextMenuPathPoint", "ContextMenuPathSegment", "ContextMenuActiveXControl", "ContextMenuOfficePreviewHandlerPowerPoint", "ContextMenuRevision", "ContextMenuRightDragDrop", "ContextMenuSlideGap", "ContextMenuLabelSection", "ContextMenuSlideShow", "ContextMenuShowBrowse", "ContextMenuShowHyperlink", "ContextMenuShowPointerOptions", "ContextMenuEndShow", "ContextMenuSlideSorter", "ContextMenuSlideSync", "ContextMenuSpell", "ContextMenuThumbnail", "ContextMenuPicture", "ContextMenuShape", "ContextMenuInk", "ContextMenuObjectsGroup", "ContextMenuObjectEditPoint", "ContextMenuObjectEditSegment", "ContextMenuTextEdit", "ContextMenuShapeConnector", "ContextMenuShapeFreeform", "ContextMenuChartArea", "ContextMenuChartAxis", "ContextMenuChartAxisTitle", "ContextMenuChartBackWall", "ContextMenuChartTitle", "ContextMenuChartDataLabel", "ContextMenuChartDataLabels", "ContextMenuChartDataPoint", "ContextMenuChartDataSeries", "ContextMenuChartDataTable", "ContextMenuChartDisplayUnit", "ContextMenuChartDownBars", "ContextMenuChartDropLines", "ContextMenuChartErrorBars", "ContextMenuChartFloor", "ContextMenuChartGridlines", "ContextMenuChartHighLowLine", "ContextMenuChartLeaderLines", "ContextMenuChartLegend", "ContextMenuChartLegendEntry", "ContextMenuChartPlotArea", "ContextMenuChartSeriesLine", "ContextMenuChartSideWall", "ContextMenuChartTrendline", "ContextMenuChartTrendlineLabel", "ContextMenuChartUpBars", "ContextMenuChartWalls", "ContextMenuNotesEditText", "ContextMenuTextEditOutline", "ContextMenuGraphicsCompatibility", "ContextMenuGraphicOleClassic", "ContextMenuTable", "ContextMenuTableWhole", "ContextMenuSmartArtContentPane", "ContextMenuSmartArtBackground", "ContextMenuSmartArtEditSmartArt", "ContextMenuSmartArtEdit1DShape", "ContextMenuSmartArtEditText", "ContextMenuSmartArtEdit1DShapeText"]
    for ctx_idmso in ppt_ctx_menus:
        bkt.powerpoint.add_context_menu(ctxm_button(ctx_idmso))


    xls_ctx_menus = ["ContextMenuWorkbook", "ContextMenuWorkbookPly", "ContextMenuFormulaBar", "ContextMenuDesktop", "ContextMenuTitleBar", "ContextMenuPreviewer", "ContextMenuCellLayout", "ContextMenuCell", "ContextMenuRowLayout", "ContextMenuRow", "ContextMenuColumnLayout", "ContextMenuColumn", "ContextMenuDialogPly", "ContextMenuMacroCell", "ContextMenuXmlRangeLayout", "ContextMenuXmlRange", "ContextMenuListRangeLayout", "ContextMenuListRange", "ContextMenuPivotTable", "ContextMenuDrawnObject", "ContextMenuActiveXControl", "ContextMenuFormControl", "ContextMenuOleObject", "ContextMenuCurve", "ContextMenuCurveNode", "ContextMenuCurveSegment", "ContextMenuConnectorClassic", "ContextMenuQueryLayout", "ContextMenuQuery", "ContextMenuAutoFill", "ContextMenuRightDragDrop", "ContextMenuPhoneticEdit", "ContextMenuPictureClassic", "ContextMenuPicture", "ContextMenuShape", "ContextMenuInk", "ContextMenuObjectsGroup", "ContextMenuObjectEditPoint", "ContextMenuObjectEditSegment", "ContextMenuTextEdit", "ContextMenuShapeConnector", "ContextMenuShapeFreeform", "ContextMenuChartArea", "ContextMenuChartAxis", "ContextMenuChartAxisLabel", "ContextMenuChartAxisTitle", "ContextMenuChartBackWall", "ContextMenuChartTitle", "ContextMenuChartDataLabel", "ContextMenuChartDataLabels", "ContextMenuChartDataPoint", "ContextMenuChartDataSeries", "ContextMenuChartDataTable", "ContextMenuChartDisplayUnit", "ContextMenuChartDownBars", "ContextMenuChartDropLines", "ContextMenuChartErrorBars", "ContextMenuChartFloor", "ContextMenuChartGridlines", "ContextMenuChartHighLowLine", "ContextMenuChartLeaderLines", "ContextMenuChartLegend", "ContextMenuChartLegendEntry", "ContextMenuChartPlotArea", "ContextMenuChartSeriesLine", "ContextMenuChartSideWall", "ContextMenuChartTrendline", "ContextMenuChartTrendlineLabel", "ContextMenuChartUpBars", "ContextMenuChartWalls", "ContextMenuGraphicsCompatibility", "ContextMenuSmartArtContentPane", "ContextMenuSmartArtBackground", "ContextMenuSmartArtEditSmartArt", "ContextMenuSmartArtEdit1DShape", "ContextMenuSmartArtEditText", "ContextMenuSmartArtEdit1DShapeText", "ContextMenuSlicer"]
    for ctx_idmso in xls_ctx_menus:
        bkt.excel.add_context_menu(ctxm_button(ctx_idmso))


    visio_ctx_menus = ["ContextMenuFullScreen", "ContextMenuCommentMarker", "ContextMenuOleObject", "ContextMenuConnectionPoint", "ContextMenuDrawingPage", "ContextMenuShape", "ContextMenuShape1D", "ContextMenuText", "ContextMenuWindowShapeData", "ContextMenuWindowShapes", "ContextMenuWindowSizePosition", "ContextMenuSpelling", "ContextMenuWindowExternalDataItem", "ContextMenuWindowExternalDataTab", "ContextMenuExplorerDocument", "ContextMenuExplorerLayer", "ContextMenuExplorerLayers", "ContextMenuExplorerMaster", "ContextMenuExplorerMasters", "ContextMenuExplorerPage", "ContextMenuExplorerPages", "ContextMenuExplorerPatterns", "ContextMenuExplorerShape", "ContextMenuExplorerShapes", "ContextMenuExplorerStyle", "ContextMenuExplorerStyles", "ContextMenuMaster", "ContextMenuMasterExplorerDocument", "ContextMenuMasterExplorerMaster", "ContextMenuPageNavigation", "ContextMenuPageTab", "ContextMenuWindowIssuesItem", "ContextMenuShapeSheet", "ContextMenuWindowShapesStencil", "ContextMenuTextDrag", "ContextMenuWindowPanZoom", "ContextMenuWindowDrawingExplorer", "ContextMenuWindowMasterExplorer", "ContextMenuWindowStyleExplorer", "ContextMenuWindowFormulaTracing", "ContextMenuWindowShapesMoreShapes", "ContextMenuWindowExternalData", "ContextMenuWindowIssues"]
    for ctx_idmso in visio_ctx_menus:
        bkt.visio.add_context_menu(ctxm_button(ctx_idmso))


    word_ctx_menus = ["ContextMenuDropCap", "ContextMenuEndnote", "ContextMenuField", "ContextMenuFieldDisplay", "ContextMenuFieldDisplayListNumbers", "ContextMenuFieldForm", "ContextMenuFootnote", "ContextMenuFrame", "ContextMenuHeading", "ContextMenuHeadingLinked", "ContextMenuScriptAnchor", "ContextMenuList", "ContextMenuInlinePicture", "ContextMenuTable", "ContextMenuTableCell", "ContextMenuHeadingTable", "ContextMenuListTable", "ContextMenuPictureTable", "ContextMenuTextTable", "ContextMenuTableWhole", "ContextMenuTableWholeLinked", "ContextMenuText", "ContextMenuOfficePreviewHandlerWord", "ContextMenuTextLinked", "ContextMenuRichTextFont", "ContextMenuRichTextFontParagraph", "ContextMenuSpell", "ContextMenuGrammar", "ContextMenuGrammarReading", "ContextMenuRevision", "ContextMenuFramesetBorder", "ContextMenuHyperlink", "ContextMenuFieldAutoSignatureList", "ContextMenuFieldAutoTextList", "ContextMenuNavigationPane", "ContextMenuDrawnObject", "ContextMenuCurve", "ContextMenuCurveNode", "ContextMenuCurveSegment", "ContextMenuFloatingPicture", "ContextMenuCanvasClassic", "ContextMenuOleObject", "ContextMenuActiveXControl", "ContextMenuTextEffect", "ContextMenuComment", "ContextMenuOrganizationChart", "ContextMenuDiagram", "ContextMenuConnectorClassic", "ContextMenuAddressBlock", "ContextMenuGreetingLine", "ContextMenuInlineActiveXControl", "ContextMenuDocumentStructureNode", "ContextMenuXmlError", "ContextMenuCoAuthoringState", "ContextMenuInkComment", "ContextMenuInlineBusinessCard", "ContextMenuEquation", "ContextMenuHeaderArea", "ContextMenuFooterArea", "ContextMenuReadOnlyMailText", "ContextMenuReadOnlyMailTable", "ContextMenuReadOnlyMailTableCell", "ContextMenuReadOnlyMailListTable", "ContextMenuReadOnlyMailPictureTable", "ContextMenuReadOnlyMailTextTable", "ContextMenuReadOnlyMailTableWhole", "ContextMenuReadOnlyMailList", "ContextMenuReadOnlyMailHyperlink", "ContextMenuLockedReadingMode", "ContextMenuPageNumberingOptions", "ContextMenuConflicts", "ContextMenuPicture", "ContextMenuShape", "ContextMenuInk", "ContextMenuObjectsGroup", "ContextMenuObjectEditPoint", "ContextMenuObjectEditSegment", "ContextMenuTextEdit", "ContextMenuShapeConnector", "ContextMenuShapeFreeform", "ContextMenuChartArea", "ContextMenuChartAxis", "ContextMenuChartAxisTitle", "ContextMenuChartBackWall", "ContextMenuChartTitle", "ContextMenuChartDataLabel", "ContextMenuChartDataLabels", "ContextMenuChartDataPoint", "ContextMenuChartDataSeries", "ContextMenuChartDataTable", "ContextMenuChartDisplayUnit", "ContextMenuChartDownBars", "ContextMenuChartDropLines", "ContextMenuChartErrorBars", "ContextMenuChartFloor", "ContextMenuChartGridlines", "ContextMenuChartHighLowLine", "ContextMenuChartLeaderLines", "ContextMenuChartLegend", "ContextMenuChartLegendEntry", "ContextMenuChartPlotArea", "ContextMenuChartSeriesLine", "ContextMenuChartSideWall", "ContextMenuChartTrendline", "ContextMenuChartTrendlineLabel", "ContextMenuChartUpBars", "ContextMenuChartWalls", "ContextMenuSmartArtContentPane", "ContextMenuSmartArtBackground", "ContextMenuSmartArtEditSmartArt", "ContextMenuSmartArtEdit1DShape", "ContextMenuSmartArtEditText", "ContextMenuSmartArtEdit1DShapeText", "ContextMenuCanvas"]
    for ctx_idmso in word_ctx_menus:
        bkt.word.add_context_menu(ctxm_button(ctx_idmso))