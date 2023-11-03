
# Created by Isaac Oster
# 06/03/2023
# Free to use.  Requires OpenAI account.

# Creates a window within Unreal to access OpenAI model text-davinci-003.
# Includes options to run generated code, use Unreal Python API docs to learn more
# about classes and methods within the generated code, and save it out as a python file.

# Be sure to add your default python modules directory path to Unreal:
# Project Settings -> Python -> Additional Paths

# Default location of installed modules:
# C:\Users\[USER]]\AppData\Local\Programs\Python\[PYTHON VERSION]\Lib\site-packages

# This code requires several modules which may need to be installed.  
# Enter the following commands into a command prompt:
# pip install PySide2
# pip install openai
# pip install clipboard

# Add your OpenAI API Key, available at https://platform.openai.com/account/api-keys
# May require a restart, only needs to run once.
# os.environ["OPENAI_API_KEY"] = "ABC123"

# Forward questions and suggestions to isaacdotosteratgmail.


import unreal
import sys
import os
import openai
import webbrowser
import clipboard
from PySide2 import QtUiTools, QtWidgets
openai.api_key = os.getenv("OPENAI_API_KEY")

class UnrealPythonReference(QtWidgets.QWidget):
    """
    Create the tool window.
    """
    # store ref to window to prevent garbage collection
    window = None

    def __init__(self, parent = None):
        """
        Import UI and connect components.
        """
        super(UnrealPythonReference, self).__init__(parent)
        # load the created UI widget
        self.widget = QtUiTools.QUiLoader().load(r'G:\Code\unrea_python\openAIWidget.ui')  # path to PyQt .ui file
        # attach the widget to the instance of this class (aka self)
        self.widget.setParent(self)
        # clear the clipboard for search function
        clipboard.copy('')
        # find interactive elements of UI
        self.btn_close = self.widget.findChild(QtWidgets.QPushButton, 'btn_close')
        self.btn_submitQuestion = self.widget.findChild(QtWidgets.QPushButton, 'btn_submitQuestion')
        self.btn_run = self.widget.findChild(QtWidgets.QPushButton, 'btn_run')
        self.btn_save = self.widget.findChild(QtWidgets.QPushButton, 'btn_save')
        self.btn_searchRef = self.widget.findChild(QtWidgets.QPushButton, 'btn_searchRef')
        self.textEdit_prompt = self.widget.findChild(QtWidgets.QTextEdit, 'textEdit_prompt')
        self.textEdit_response = self.widget.findChild(QtWidgets.QTextEdit, 'textEdit_response')
        self.spinBox_temp = self.widget.findChild(QtWidgets.QDoubleSpinBox, 'spinBox_temp')
        self.comboBox_version = self.widget.findChild(QtWidgets.QComboBox, 'comboBox_version')
        # assign clicked handler to buttons
        self.btn_close.clicked.connect(self.closewindow)
        self.btn_submitQuestion.clicked.connect(self.submitPrompt)
        self.btn_run.clicked.connect(self.runOutputScript)
        self.btn_save.clicked.connect(self.savePyfile)
        self.btn_searchRef.clicked.connect(self.searchReference)
        # self.textEdit_response.selectionChanged.connect(self.searchReference)
        # class vars
        self.projectSaveDir = unreal.Paths.convert_relative_path_to_full(unreal.Paths.project_saved_dir())
        # set tooltip background color
        self.setStyleSheet('''QToolTip { 
                           background-color: #242424; 
                           color: #242424; 
                           border: #242424 solid 1px;
                           font: 10pt "MS Shell Dlg 2"
                           }''')
        # populate version combobox
        for version in ['5.2', '5.1', '5.0', '4.27']:
            self.comboBox_version.addItem(version)

    """
    Your code goes here.
    """
    def submitPrompt(self):
        """
        Submit prompt to OpenAI API.
        """
        promptText = self.textEdit_prompt.toPlainText()        
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=promptText,
            max_tokens=256,
            temperature=self.spinBox_temp.value(),
            )
        responseText = response["choices"][0]["text"]
        self.textEdit_response.setText(responseText[2:]) # output includes two newline characters at the front
        
        # this uses gpt 3.5 turbo model - more verbose
        '''
        completion = openai.ChatCompletion.create( # Change the function Completion to ChatCompletion
        model = 'gpt-3.5-turbo',
        messages = [ # Change the prompt parameter to the messages parameter
        {'role': 'user', 'content': promptText}
        ],
        temperature = self.spinBox_temp.value()
        )
        self.textEdit_response.setText(completion['choices'][0]['message']['content'])       
        '''

    def runOutputScript(self):
        """
        Run output script in unreal editor.
        """
        unreal.PythonScriptLibrary.execute_python_command('import unreal\n' + self.textEdit_response.toPlainText())

    def savePyfile(self):
        """
        Save output script as python file.
        """
        fileName = QtWidgets.QFileDialog.getSaveFileName(self, ("Save Python File"), self.projectSaveDir, ("Python Files (*.py)"))
        if len(fileName[0]):
            with open(fileName[0], "w") as pyFile:
                pyFile.write(self.textEdit_response.toPlainText())

    def searchReference(self):
        """
        Get copied text from clipboard and build search URL.
        """
        self.textEdit_response.copy()
        selectedText = clipboard.paste()
        if len(selectedText):
            url = 'https://docs.unrealengine.com/' + self.comboBox_version.currentText() + '/en-US/PythonAPI/search.html?q=' + selectedText
            webbrowser.open(url, new=1, autoraise=True)
        else:
            unreal.EditorDialog.show_message('Attention', 'Please highlight text to search.', unreal.AppMsgType.OK)

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

def openWindow():
    """
    Create tool window.
    """
    if QtWidgets.QApplication.instance():
        # Id any current instances of tool and destroy
        for win in (QtWidgets.QApplication.allWindows()):
            if 'toolWindow' in win.objectName(): # update this name to match name below
                win.destroy()
    else:
        QtWidgets.QApplication(sys.argv)
    # load UI into QApp instance
    UnrealPythonReference.window = UnrealPythonReference()
    UnrealPythonReference.window.show()
    UnrealPythonReference.window.setObjectName('toolWindow') # update this with something unique to your tool
    UnrealPythonReference.window.setWindowTitle('Unreal Python Assistant - Powered by OpenAI')
    unreal.parent_external_window_to_slate(UnrealPythonReference.window.winId())
    
openWindow()