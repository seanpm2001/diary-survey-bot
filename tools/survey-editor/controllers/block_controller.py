from PyQt5.QtCore import QObject, pyqtSlot

# The controller class performs any logic and sets data in the model.


class BlockController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model

    def get_question_info(self):
        question_list = []
        for question in self._model.u_block.questions:
            pass
