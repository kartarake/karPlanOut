import json

core_colors = [
    'mvThemeCol_Text',
	'mvThemeCol_TabActive',
	'mvThemeCol_SliderGrabActive',
	'mvThemeCol_TextDisabled',
	'mvThemeCol_TabUnfocused',
	'mvThemeCol_Button',
	'mvThemeCol_WindowBg',
	'mvThemeCol_TabUnfocusedActive',
	'mvThemeCol_ButtonHovered',
	'mvThemeCol_ChildBg',
	'mvThemeCol_DockingPreview',
	'mvThemeCol_ButtonActive',
	'mvThemeCol_Border',
	'mvThemeCol_DockingEmptyBg',
	'mvThemeCol_Header',
	'mvThemeCol_PopupBg',
	'mvThemeCol_PlotLines',
	'mvThemeCol_HeaderHovered',
	'mvThemeCol_BorderShadow',
	'mvThemeCol_PlotLinesHovered',
	'mvThemeCol_HeaderActive',
	'mvThemeCol_FrameBg',
	'mvThemeCol_PlotHistogram',
	'mvThemeCol_Separator',
	'mvThemeCol_FrameBgHovered',
	'mvThemeCol_PlotHistogramHovered',
	'mvThemeCol_SeparatorHovered',
	'mvThemeCol_FrameBgActive',
	'mvThemeCol_TableHeaderBg',
	'mvThemeCol_SeparatorActive',
	'mvThemeCol_TitleBg',
	'mvThemeCol_TableBorderStrong',
	'mvThemeCol_ResizeGrip',
	'mvThemeCol_TitleBgActive',
	'mvThemeCol_TableBorderLight',
	'mvThemeCol_ResizeGripHovered',
	'mvThemeCol_TitleBgCollapsed',
	'mvThemeCol_TableRowBg',
	'mvThemeCol_ResizeGripActive',
	'mvThemeCol_MenuBarBg',
	'mvThemeCol_TableRowBgAlt',
	'mvThemeCol_Tab',
	'mvThemeCol_ScrollbarBg',
	'mvThemeCol_TextSelectedBg',
	'mvThemeCol_TabHovered',
	'mvThemeCol_ScrollbarGrab',
	'mvThemeCol_DragDropTarget',
	'mvThemeCol_ScrollbarGrabHovered',
	'mvThemeCol_NavHighlight',
	'mvThemeCol_ScrollbarGrabActive',
	'mvThemeCol_NavWindowingHighlight',
	'mvThemeCol_CheckMark',
	'mvThemeCol_NavWindowingDimBg',
	'mvThemeCol_SliderGrab',
	'mvThemeCol_ModalWindowDimBg',
]

plot_colors = [
    'mvPlotCol_Line',
	'mvPlotCol_LegendBg',
	'mvPlotCol_YAxisGrid',
	'mvPlotCol_Fill',
	'mvPlotCol_LegendBorder',
	'mvPlotCol_YAxis2',
	'mvPlotCol_MarkerOutline',
	'mvPlotCol_LegendText',
	'mvPlotCol_YAxisGrid2',
	'mvPlotCol_MarkerFill',
	'mvPlotCol_TitleText',
	'mvPlotCol_YAxis3',
	'mvPlotCol_ErrorBar',
	'mvPlotCol_InlayText',
	'mvPlotCol_YAxisGrid3',
	'mvPlotCol_FrameBg',
	'mvPlotCol_XAxis',
	'mvPlotCol_Selection',
	'mvPlotCol_PlotBg',
	'mvPlotCol_XAxisGrid',
	'mvPlotCol_Query',
	'mvPlotCol_PlotBorder',
	'mvPlotCol_YAxis',
	'mvPlotCol_Crosshairs',
]

node_colors = [
    'mvNodeCol_NodeBackground',
	'mvNodeCol_TitleBarSelected',
	'mvNodeCol_BoxSelector',
	'mvNodeCol_NodeBackgroundHovered',
	'mvNodeCol_Link',
	'mvNodeCol_BoxSelectorOutline',
	'mvNodeCol_NodeBackgroundSelected',
	'mvNodeCol_LinkHovered',
	'mvNodeCol_GridBackground',
	'mvNodeCol_NodeOutline',
	'mvNodeCol_LinkSelected',
	'mvNodeCol_GridLine',
	'mvNodeCol_TitleBar',
	'mvNodeCol_Pin',
	'mvNodeCol_PinHovered',
	'mvNodeCol_TitleBarHovered',
]

def create_empty_theme(theme_name) -> None:
    theme_pack = dict()
    for component in core_colors:
        theme_pack["core_colors"][component] = None
    for component in plot_colors:
        theme_pack["plot_colors"][component] = None
    for component in node_colors:
        theme_pack["node_colors"][component] = None

    path = f".\\themes\\{theme_name}.json"

    with open(path, "w") as f:
        json.dump(theme_pack, f, indent=3)