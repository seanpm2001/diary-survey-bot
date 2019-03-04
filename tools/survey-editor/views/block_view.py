from PyQt5.QtWidgets import QWidget

from views.block_view_ui import Ui_Block
from views.question_view import QuestionView
from model.survey import Question


# The view class should mainly contain code to handle events and trigger
# events in/from the user interface.
class BlockView(QWidget):
    def __init__(self, model, block_controller):
        super().__init__()

        self._model = model
        self._controller = block_controller
        self._ui = Ui_Block()
        self._ui.setupUi(self)
        self._view = None