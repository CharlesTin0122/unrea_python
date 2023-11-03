import unreal
import sys
from functools import partial
from PySide2 import QtUiTools, QtWidgets

"""
Be sure to add your default python modules directory path to Unreal:
Project Settings -> Python -> Additional Paths

Default location of installed modules:
C:\\Users\\[USER]]\\AppData\Local\\Programs\\Python\\[PYTHON VERSION]\\Lib\site-packages

This code required PySide2 module which may need to be installed.
To install required modules open windows command prompt and enter:
pip install [MODULENAME]
"""


class UnrealUITemplate(QtWidgets.QWidget):
    """
    Create a default tool window.
    """

    # 创建变量用来储存类的实例
    window = None

    def __init__(self, parent=None):
        """
        Import UI and connect components
        """
        super().__init__(parent)

        # 载入UI文件
        self.widgetPath = r"G:\Code\unrea_python\unreal_demo.ui"
        self.widget = QtUiTools.QUiLoader().load(self.widgetPath)  # path to PyQt .ui file

        # 将UI部件作为此类实例的子对象（也就是self的子对象）
        self.widget.setParent(self)
        # 创建变量用以储存UI子控件
        self.subwidgets = []
        # 找到UI的交互元素并设置变量
        self.pb_open_file = self.widget.findChild(QtWidgets.QPushButton, "pb_open_file")
        self.pb_close = self.widget.findChild(QtWidgets.QPushButton, "pb_close")
        self.vl_subwidget = self.widget.findChild(QtWidgets.QVBoxLayout, "vl_subwidget")
        self.pb_import = self.widget.findChild(QtWidgets.QPushButton, "pb_import")

        # 设置按钮槽函数
        self.pb_open_file.clicked.connect(self.open_files)
        self.pb_import.clicked.connect(self.import_files)
        self.pb_close.clicked.connect(self.closewindow)

    """
    Your code goes here.
    """

    def resizeEvent(self, event):
        """
        Called on automatically generated resize event
        """
        self.widget.resize(self.width(), self.height())

    def closewindow(self):
        """
        Close the window.
        """
        self.destroy()

    def open_files(self):
        """将文件载入UI控件
        """
        dir = r"D:\Work\Test"
        # 参数1.为对话框左上角标题，2.为文件路径，3.为文件类型
        file_names = QtWidgets.QFileDialog.getOpenFileNames(
            self, ("Open Image"), dir, ("Image Files (*.png *.jpg *.tga)")
        )
        # file_names = QtWidgets.QFileDialog.getOpenFileNames(
        #     self, ("Open Geometry"), dir, ("Geo Files (*.fbx)")
        # )
        subwidget_path = r"G:\Code\unrea_python\unreal_sub_widget.ui"
        for file_name in file_names[0]:
            subwidget = QtUiTools.QUiLoader().load(subwidget_path)
            self.subwidgets.append(subwidget)
            self.vl_subwidget.addWidget(subwidget)
            line_edit = subwidget.findChild(QtWidgets.QLineEdit, "lineEdit")
            line_edit.setText(file_name)
            pb_remove = subwidget.findChild(QtWidgets.QPushButton, "pb_remove")
            pb_remove.clicked.connect(partial(self.remove_subwidget, subwidget))

    def remove_subwidget(self, subwidget):
        self.subwidgets.remove(subwidget)
        self.vl_subwidget.removeWidget(subwidget)
        subwidget.deleteLater()

    def import_files(self):
        """
        Import assets into project.
        """
        # list of files to import
        fileNames = []
        for subwidget in self.subwidgets:
            line_edite = subwidget.findChild(QtWidgets.QLineEdit, "lineEdit")
            file_path = line_edite.text()
            fileNames.append(file_path)
        if fileNames:
            # create asset tools object
            assetTools = unreal.AssetToolsHelpers.get_asset_tools()
            # create asset import data object        
            assetImportData = unreal.AutomatedAssetImportData()
            # set assetImportData attributes
            assetImportData.destination_path = r'/Game/Props'
            assetImportData.filenames = fileNames
            assetImportData.replace_existing = True
            assetTools.import_assets_automated(assetImportData)
        else:
            unreal.log_warning("No files to import")

def openWindow():
    """
    Create tool window.
    """
    # 如果存在 QtWidgets.QApplication 类的实例
    if QtWidgets.QApplication.instance():
        # 检查是否存在任何已有的工具窗口，并将其销毁。
        for win in QtWidgets.QApplication.allWindows():
            if "toolWindow" in win.objectName():  # update this name to match name below
                win.destroy()
    # 如果不存在
    else:
        # 创建一个
        QtWidgets.QApplication(sys.argv)

    # load UI into QApp instance
    UnrealUITemplate.window = UnrealUITemplate()  # 创建一个类的实例并储存到UnrealUITemplate.window类变量
    UnrealUITemplate.window.show()  # 显示窗口
    # 设置对象名称
    UnrealUITemplate.window.setObjectName("toolWindow")  # update this with something unique to your tool
    # 设置对象标签
    UnrealUITemplate.window.setWindowTitle("Sample Tool")
    # 创建的工具窗口的窗口标识 winId()
    win_id = UnrealUITemplate.window.winId()
    # 将自定义外部窗口嵌入到 Unreal Engine 的界面中。
    unreal.parent_external_window_to_slate(win_id)


openWindow()


def add_menu():
    """在程序主菜单下添加自定义菜单
    """
    # Get the main menu class
    menus = unreal.ToolMenus.get()
    menu_name = 'LevelEditor.MainMenu'
    menu = menus.find_menu(menu_name)

    # Custom menu parameters
    owner = menu.get_name()
    section_name = 'PythonTools'
    name = 'lingyunFX'
    label = 'lingyunFX'
    tool_tip = 'This is some python toolset.'

    # Add and refresh
    menu.add_sub_menu(owner, section_name, name, label, tool_tip)
    menus.refresh_all_widgets()


def add_button():
    # Get the menu class
    menus = unreal.ToolMenus.get()
    menu_name = "LevelEditor.MainMenu.lingyunFX"
    menu = menus.find_menu(menu_name)

    # Set the button type and label
    entry = unreal.ToolMenuEntry(type=unreal.MultiBlockType.MENU_ENTRY)
    entry.set_label('TEST BUTTON 01')

    # Set button command
    typ = unreal.ToolMenuStringCommandType.PYTHON
    entry.set_string_command(typ, "", 'print "this is test button"')

    # Add and refresh
    section_name = ''
    menu.add_menu_entry(section_name, entry)
    menus.refresh_all_widgets()
