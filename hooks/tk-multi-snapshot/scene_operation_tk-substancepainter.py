import os
import sgtk

HookClass = sgtk.get_hook_baseclass()


__author__ = "Diego Garcia Huerta"
__contact__ = "https://www.linkedin.com/in/diegogh/"


class SceneOperation(HookClass):
    """
    Hook called to perform an operation with the
    current scene
    """

    def execute(self, operation, file_path, **kwargs):
        """
        Main hook entry point

        :operation: String
                    Scene operation to perform

        :file_path: String
                    File path to use if the operation
                    requires it (e.g. open)

        :returns:   Depends on operation:
                    'current_path' - Return the current scene
                                     file path as a String
                    all others     - None
        """
        app = self.parent
        engine = sgtk.platform.current_engine()

        if operation == "current_path":
            return engine.app.get_current_project_path()

        elif operation == "open":
            engine.app.open_project(file_path)

        elif operation == "save":
            engine.app.save_project()
