class Editor:

    def open(self):
        print("Editor Opennn Method")

    def execute(self):
        print("Execute Traditional way python module_name.py")

class Vscode(Editor):

    def open(self):
        print("Openn with code")

vscode_instance=Vscode()

vscode_instance.open()