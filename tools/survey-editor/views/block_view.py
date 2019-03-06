from PyQt5.QtWidgets import QWidget

from controllers.question_controller import QuestionController
from views.block_view_ui import Ui_Block
from views.question_view import QuestionView


# The view class should mainly contain code to handle events and trigger
# events in/from the user interface.
class BlockView(QWidget):
    def __init__(self, model, block_controller):
        super().__init__()

        self._model = model
        self._controller = block_controller
        self._ui = Ui_Block()
        self._ui.setupUi(self)
        self.question_widgets = {}

        self._ui.back_to_days_button.clicked.connect(self.back_to_days)
        self._ui.question_list.itemSelectionChanged.connect(self.question_list_event)
        self._ui.tabWidget.currentChanged.connect(self.tab_event)

    def back_to_days(self):
        self.parent().setCurrentIndex(0)

    def populate(self):
        self._ui.tabWidget.setDisabled(True)
        self._ui.question_list.clear()
        lang = self._model.lang
        block = self._model.blocks[lang]
        self._ui.headline.setText("Block #" + str(block.day.blocks.index(block) + 1))
        self._ui.meta_field.setPlainText(block.meta)
        self._ui.time_field.setText(block.time)

        questions = []
        for item in block.questions:
            questions.append(item.info())
        self.fill_question_list(questions)

        q_controller = QuestionController(self._model)
        for i in range(len(self._model.languages)):
            if not self._ui.tabWidget.tabText(i) in self._model.languages:
                q_view = QuestionView(self._model, q_controller, self._model.languages[i])
                self._ui.tabWidget.addTab(q_view, self._model.languages[i])
                self.question_widgets[self._model.languages[i]] = q_view

    def fill_question_list(self, questions):
        self._ui.question_list.clear()
        for question in questions:
            self._ui.question_list.addItem(question)

    def question_list_event(self):
        self._ui.tabWidget.setEnabled(True)
        self._ui.tabWidget.currentWidget().setEnabled(True)

        self._model.set_questions(self._ui.question_list.currentRow())
        self.question_widgets[self._model.lang].populate()

    def tab_event(self):
        if self.question_widgets == {}:
            return
        self._ui.tabWidget.currentWidget().setEnabled(True)
        index = self._ui.tabWidget.indexOf(self._ui.tabWidget.currentWidget())
        self._model.lang = self._ui.tabWidget.tabText(index)
        self.question_widgets[self._model.lang].populate()
