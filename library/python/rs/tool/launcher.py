import json
import sys
from functools import partial
from pathlib import Path

from PySide2.QtCore import (
    Qt,
)
from PySide2.QtWidgets import (
    QApplication,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget, QHBoxLayout, QToolButton,
)

from rs.core import (
    config,
    pipe as p,
)
from rs.gui import appearance
from rs.gui.script_button import ScriptButton

APP_NAME = 'りぞりぷと'
__version__ = '1.5.5'

MENU_JSON = config.ROOT_PATH.joinpath('data', 'app', 'launcher_menu.json')

SS_DICT = {
    'picture': appearance.ex_stylesheet,
    'sound': appearance.in_stylesheet,
    'utility': appearance.other_stylesheet,
}


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('%s  其ノ%s' % (APP_NAME, __version__))
        self.setWindowFlags(
            Qt.Window
            | Qt.WindowCloseButtonHint
            | Qt.WindowStaysOnTopHint
        )
        self.resize(200, 10)

        # button
        self.close_button = QPushButton('close', self)
        self.close_button.setMinimumHeight(40)
        self.close_button.setToolTip('閉じる')
        self.minimize_button = QToolButton(self)
        self.minimize_button.setArrowType(Qt.DownArrow)
        self.minimize_button.setMinimumHeight(40)
        self.minimize_button.setMinimumWidth(40)
        self.minimize_button.setToolTip('最小化')

        # layout
        lo = QVBoxLayout()
        lo.setContentsMargins(5, 5, 5, 5)
        # import json
        for i in p.pipe(
                MENU_JSON.read_text(encoding='utf-8'),
                json.loads,
                list,
        ):
            btn = ScriptButton(i['name'], script_path=Path(config.ROOT_PATH.joinpath(i['path'])))
            btn.setMinimumHeight(40)
            btn.setStyleSheet(SS_DICT[i['ss']])
            lo.addWidget(btn)

        lo.addItem(
            QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )
        lo2 = QHBoxLayout()
        lo2.addWidget(self.minimize_button)
        lo2.addWidget(self.close_button)
        lo.addLayout(lo2)
        self.setLayout(lo)
        # event
        self.close_button.clicked.connect(self.close)
        self.minimize_button.clicked.connect(partial(self.setWindowState, Qt.WindowMinimized))


def run() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.setStyle("Fusion")

    app.setPalette(appearance.palette)
    app.setStyleSheet(appearance.stylesheet)
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
