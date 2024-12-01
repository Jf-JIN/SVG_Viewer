
import winreg
import platform
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QApplication, QTextBrowser, QHBoxLayout, QVBoxLayout,  QFileDialog, QTableWidget, QHeaderView, QSizePolicy, QTableWidgetItem, QMenu, QAction
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QByteArray, QThread, pyqtSignal
from Manager_setting import *
from Message_Notification import *
import sys
import os
import subprocess


os.chdir(os.path.dirname(__file__))


_FIXED_SVG_WIDGET = 120
_FIXED_SVG_TABLE_UNIT = _FIXED_SVG_WIDGET + 6
_SCROLL_ROWS = 1
_TABLE_BG_COLOR = '#fff0eb'

_LANG_VIEW = '浏览'
_LANG_OPEN_FOLDER = '打开文件夹'
_LANG_COPY = '复制'
_LANG_COPYED = '已复制'
_LANG_TO_CLIPBOARD = '字符串到剪贴板'
_LANG_EDIT_IN_NOTEPAD = '在记事本中编辑'
_LANG_OPEN_IN_INKSCAPE = '在 Inkscape 中打开'
_LANG_LOCATION_FILE = '定位到文件位置'
_LANG_COPY_FILE_PATH = '复制文件路径'
_LANG_COPYED_FILE_PATH = '文件路径已复制到剪贴板'
_LANG_PATH = '路径'
_STYLE_SHEET = f"""
            QWidget{{
                font: 20px "黑体";
            }}
            #tbw QWidget{{
                font: 14px "黑体";
            }}
            #tbw{{
                background-color: {_TABLE_BG_COLOR};
            }}
            """

# _LANG_VIEW = 'Browse'
# _LANG_OPEN_FOLDER = 'Open folder'
# _LANG_COPY = 'Copy'
# _LANG_COPYED = 'Copied'
# _LANG_TO_CLIPBOARD = 'String to clipboard'
# _LANG_EDIT_IN_NOTEPAD = 'open with notepad'
# _LANG_OPEN_IN_INKSCAPE = 'open with inkscape'
# _LANG_LOCATION_FILE = 'locate file'
# _LANG_COPY_FILE_PATH = 'copy file path'
# _LANG_COPYED_FILE_PATH = 'file path copied to clipboard'
# _LANG_PATH = 'path'
# _STYLE_SHEET = f"""
#             QWidget{{
#                 font: 20px "Arial";
#             }}
#             #tbw QWidget{{
#                 font: 14px "Arial";
#             }}
#             #tbw{{
#                 background-color: {_TABLE_BG_COLOR};
#             }}
#             """

_ICON_SVG_WIN = """<svg width="752.20007" height="764.5412" viewBox="0 0 199.0196 202.28486" version="1.1" id="svg1" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1" /><g id="layer1" transform="translate(-7.8787215,-4.6155948)"><text xml:space="preserve" style="font-size:168.669px;line-height:198.654px;font-family:Arial;-inkscape-font-specification:Arial;text-align:center;letter-spacing:6.1982px;text-orientation:upright;text-anchor:middle;fill:#c83200;fill-opacity:1;stroke:#fffd11;stroke-width:2.64583;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;stroke-dasharray:none;stroke-opacity:1;paint-order:fill markers stroke" x="58.999817" y="128.97441" id="text1" transform="scale(1.0404564,0.96111666)"><tspan id="tspan1" style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#c83200;fill-opacity:1;stroke:#fffd11;stroke-width:2.64583;stroke-dasharray:none;stroke-opacity:1" x="62.098919" y="128.97441">S</tspan></text><text xml:space="preserve" style="font-size:160.007px;line-height:188.452px;font-family:Arial;-inkscape-font-specification:Arial;text-align:center;letter-spacing:5.87989px;text-orientation:upright;text-anchor:middle;fill:#0064c8;fill-opacity:1;stroke:#ffff11;stroke-width:2.64583;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;stroke-dasharray:none;stroke-opacity:1;paint-order:fill markers stroke" x="162.17633" y="121.67007" id="text2" transform="scale(0.95446979,1.0477021)"><tspan id="tspan2" style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#0064c8;fill-opacity:1;stroke:#ffff11;stroke-width:2.64583;stroke-dasharray:none;stroke-opacity:1" x="165.11627" y="121.67007">V</tspan></text><text xml:space="preserve" style="font-size:156.473px;line-height:184.292px;font-family:Arial;-inkscape-font-specification:Arial;text-align:center;letter-spacing:5.75008px;text-orientation:upright;text-anchor:middle;fill:#64c800;fill-opacity:1;stroke:#ffff00;stroke-width:2.64583;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;stroke-dasharray:none;stroke-opacity:1;paint-order:fill markers stroke" x="114.58257" y="196.51846" id="text3" transform="scale(0.96522481,1.0360281)"><tspan id="tspan3" style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-family:Arial;-inkscape-font-specification:'Arial Bold';fill:#64c800;fill-opacity:1;stroke:#ffff00;stroke-width:2.64583;stroke-dasharray:none;stroke-opacity:1" x="117.45761" y="196.51846">G</tspan></text></g></svg>"""

_ICON_NOTEPAD = """<svg t="1733062523144" class="icon" viewBox="0 0 1024 1024" version="1.1" p-id="7672" width="200" height="200" id="svg1" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1" /><path d="M 832,1024 H 192 A 64,64 0 0 1 128,960 V 160 a 64,64 0 0 1 64,-64 h 64 V 64 A 64,64 0 0 1 320,0 h 384 a 64,64 0 0 1 64,64 v 32 h 64 a 64,64 0 0 1 64,64 v 800 a 64,64 0 0 1 -64,64 z M 704,64 H 320 v 160 h 384 z m 128,96 h -64 v 64 a 64,64 0 0 1 -64,64 H 320 A 64,64 0 0 1 256,224 V 160 H 192 V 960 H 832 Z M 704,480 H 320 v -64 h 384 z m 0,192 H 320 v -64 h 384 z" fill="#6ea3e5" p-id="7673" id="path1" /></svg>"""

_ICON_INKSCAPE = """<svg t="1733062437188" class="icon" viewBox="0 0 1024 1024" version="1.1" p-id="4580" width="200" height="200" id="svg1" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1" /><path d="m 506.53867,8.149333 a 118.10133,118.10133 0 0 0 -85.03467,34.304 L 44.970667,428.07467 C -97.664,570.58133 137.30133,558.67733 222.208,612.608 c 39.33867,25.68533 -126.08,58.496 -92.33067,92.33067 32.896,33.83466 198.4,64.896 231.33867,97.83466 32.896,33.74934 -66.73067,69.41867 -33.83467,103.168 32,33.83467 108.75734,1.83467 122.45334,78.592 10.02666,56.66137 140.8,28.41597 199.33866,-20.096 36.43734,-31.104 -63.104,-31.104 -30.208,-64.896 82.304,-83.15733 155.392,-37.33333 185.55734,-114.176 16.512,-41.088 -124.288,-70.4 -86.784,-96.896 89.64266,-63.01866 418.64533,-95.01866 266.88,-246.69866 L 594.34667,42.453333 a 128.04267,128.04267 0 0 0 -87.808,-34.304 z m 3.2,36.650667 c 22.57066,0.128 45.22666,8.576 61.61066,24.917333 l 148.992,151.765337 c 13.78134,13.696 13.78134,42.06933 5.504,50.26133 l -73.984,-60.24533 -14.63466,88.61866 L 576,267.17867 476.33067,330.24 443.43467,197.76 390.44267,312.87467 257.87733,311.936 c -25.6,0 -21.93066,-26.496 4.56534,-52.992 52.096,-57.6 153.6,-155.30667 185.6,-189.141333 A 84.48,84.48 0 0 1 509.696,44.885333 Z M 925.952,739.24267 c -31.57333,1.06666 -63.82933,16.85333 -72.064,46.08 0,19.15733 148.992,30.16533 140.84267,-4.56534 -6.016,-29.26933 -37.12,-42.752 -68.736,-41.6 v 0.0853 z m -654.76267,82.98666 c -43.008,2.51734 -89.088,33.74934 -52.56533,64.512 33.74933,29.26934 84.992,-6.4 101.41867,-47.488 -10.24,-13.48266 -29.26934,-18.176 -48.768,-16.98133 h -0.0853 z m 564.43734,3.28534 c -42.06934,38.4 7.25333,78.592 48.384,52.096 11.008,-7.38134 -0.896,-42.88 -48.384,-52.096 z" p-id="4581" id="path1" /></svg>"""

_ICON_CPP = """<svg t="1733063337188" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="9953" xmlns:xlink="http://www.w3.org/1999/xlink" width="200" height="200"><path d="M864.488699 346.546121V672.449603a79.755651 79.755651 0 0 1-45.038485 76.315211c-96.019548 52.857666-190.788027 107.904704-286.494808 162.013439a73.813073 73.813073 0 0 1-76.002443 0c-99.147221-55.985339-197.981674-112.596213-297.128895-168.894319a55.359805 55.359805 0 0 1-21.893708-21.268173l140.119732-82.570556 116.662187-68.808797 202.673182-119.477092c17.514966-9.695785 105.089798-62.553451 114.785584-67.557728l137.93036-81.319487a72.249236 72.249236 0 0 1 14.387294 45.66402z" fill="#004174" p-id="9954"></path><path d="M850.101405 301.194869l-137.93036 81.319487-114.785584 67.557727-202.673182 119.477092-116.662187 68.808797-140.119732 82.570556a78.504582 78.504582 0 0 1-9.07025-39.721442v-170.458155-166.392181A67.870495 67.870495 0 0 1 167.017715 278.362859c97.896151-54.73427 194.854001-111.032376 292.437386-166.079414a68.183262 68.183262 0 0 1 70.6854 0c98.208919 55.359805 195.792303 111.657911 294.001222 167.017716a78.504582 78.504582 0 0 1 25.959682 21.893708z" fill="#618FBA" p-id="9955"></path><path d="M494.485034 256.156384a257.72022 257.72022 0 0 1 210.492364 111.345143c11.885156 15.95113 4.378742 17.202199-12.510691 26.897984-26.897984 15.325596-55.359805 33.153329-81.632254 49.417227-13.136225 7.819181-18.453268 5.004276-27.210751-7.193647a111.970678 111.970678 0 0 0-85.385461-41.910812 123.230299 123.230299 0 0 0-110.719609 70.059865 125.106903 125.106903 0 0 0 31.276725 135.74099 117.913256 117.913256 0 0 0 167.64325-18.453268 23.144777 23.144777 0 0 1 39.095907-5.942578c24.395846 15.325596 50.042761 29.087355 75.376909 42.849114a16.263897 16.263897 0 0 1 6.255345 27.210751 239.892486 239.892486 0 0 1-136.679291 100.711057 253.967013 253.967013 0 0 1-283.679902-97.896151 222.064753 222.064753 0 0 1-45.351252-146.375077 247.3989 247.3989 0 0 1 162.013439-227.694563 484.476481 484.476481 0 0 1 91.015272-18.766035z" fill="#FFFFFF" p-id="9956"></path><path d="M665.881491 471.027489h30.651191v81.945022h-30.651191z" fill="#FFFFFF" p-id="9957"></path><path d="M640.234575 527.325596v-30.651192h81.945022v30.651192zM765.028711 471.027489h30.651191v81.945022h-30.651191z" fill="#FFFFFF" p-id="9958"></path><path d="M739.381796 527.325596v-30.651192h81.945021v30.651192z" fill="#FFFFFF" p-id="9959"></path></svg>"""

_ICON_PYTHON = """<svg t="1733063354617" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="11115" xmlns:xlink="http://www.w3.org/1999/xlink" width="200" height="200"><path d="M420.693333 85.333333C353.28 85.333333 298.666667 139.946667 298.666667 207.36v71.68h183.04c16.64 0 30.293333 24.32 30.293333 40.96H207.36C139.946667 320 85.333333 374.613333 85.333333 442.026667v161.322666c0 67.413333 54.613333 122.026667 122.026667 122.026667h50.346667v-114.346667c0-67.413333 54.186667-122.026667 121.6-122.026666h224c67.413333 0 122.026667-54.229333 122.026666-121.642667V207.36C725.333333 139.946667 670.72 85.333333 603.306667 85.333333z m-30.72 68.693334c17.066667 0 30.72 5.12 30.72 30.293333s-13.653333 38.016-30.72 38.016c-16.64 0-30.293333-12.8-30.293333-37.973333s13.653333-30.336 30.293333-30.336z" fill="#3C78AA" p-id="11116"></path><path d="M766.250667 298.666667v114.346666a121.6 121.6 0 0 1-121.6 121.984H420.693333A121.6 121.6 0 0 0 298.666667 656.597333v160a122.026667 122.026667 0 0 0 122.026666 122.026667h182.613334A122.026667 122.026667 0 0 0 725.333333 816.64v-71.68h-183.082666c-16.64 0-30.250667-24.32-30.250667-40.96h304.64A122.026667 122.026667 0 0 0 938.666667 581.973333v-161.28a122.026667 122.026667 0 0 0-122.026667-122.026666zM354.986667 491.221333l-0.170667 0.170667c0.512-0.085333 1.066667-0.042667 1.621333-0.170667z m279.04 310.442667c16.64 0 30.293333 12.8 30.293333 37.973333a30.293333 30.293333 0 0 1-30.293333 30.293334c-17.066667 0-30.72-5.12-30.72-30.293334s13.653333-37.973333 30.72-37.973333z" fill="#FDD835" p-id="11117"></path></svg>"""

_ICON_LOCATION = """<svg width="800" height="800" viewBox="0 0 211.66666 211.66667" version="1.1" id="svg1" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1" /><g id="layer1"><path id="rect1" style="fill:#ffcf71;fill-opacity:0.988235;stroke:#d3b069;stroke-width:4.40668;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;stroke-opacity:1;paint-order:fill markers stroke" d="m 18.014586,44.754891 c -1.733342,0 -3.129008,0.945085 -3.129008,2.156457 v 18.506364 9.587529 96.214279 c 0,2.44226 1.966263,4.40852 4.408516,4.40852 H 164.05063 c 2.44226,0 4.40852,-1.96626 4.40852,-4.40852 V 65.417712 c 0,-2.442253 -1.96626,-4.407999 -4.40852,-4.407999 H 93.276658 L 80.14671,46.911348 c -1.128156,-1.211372 -3.403812,-2.156457 -5.137154,-2.156457 z" /><path style="fill:#ffcf71;fill-opacity:0.988235;stroke:#d3b069;stroke-width:4.99999;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;stroke-opacity:1;paint-order:fill markers stroke" id="rect3" width="97.538742" height="92.424355" x="229.05165" y="55.892986" ry="5" transform="matrix(1.5859794,0,0,0.88168078,-349.36455,44.947323)" d="m 254.05006,55.892986 h 87.53988 c 2.77003,0 4.51751,2.230028 3.9181,5.000061 L 327.67232,143.3174 c -0.59939,2.76997 -3.31193,4.99994 -6.08193,4.99994 h -87.53874 c -2.77,0 -4.51749,-2.22997 -3.91814,-4.99994 l 17.8346,-82.424353 c 0.59937,-2.770033 3.31192,-5.000061 6.08195,-5.000061 z" /></g></svg>"""

_ICON_COPY_PATH = """<svg width="679.43103" height="743.83789" viewBox="0 0 179.76612 196.80711" version="1.1" id="svg1" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1" /><g id="layer1" transform="translate(-14.069933,-6.7517628)"><path id="rect3" style="fill:#000000;fill-opacity:1;stroke-width:2.42424;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" d="M 73.116819,6.7517627 A 2.6458333,2.6458333 0 0 0 70.470986,9.3975956 V 49.079929 h 18.18132 V 27.578916 a 2.6458333,2.6458333 0 0 1 2.64583,-2.645834 h 47.489614 a 6.0356894,6.0356894 0 0 1 4.43849,1.945618 l 30.6343,33.247066 a 6.7760581,6.7760581 0 0 1 1.79266,4.591451 v 76.195873 a 2.6458333,2.6458333 0 0 1 -2.64583,2.64583 h -39.97482 v 18.18235 h 58.15769 a 2.6458333,2.6458333 0 0 0 2.64583,-2.64583 V 57.919699 a 6.3875482,6.3875482 0 0 0 -1.8712,-4.51652 L 147.18414,8.6224496 a 6.3876651,6.3876651 0 0 0 -4.51652,-1.8706869 z" /><path id="rect3-4" style="fill:#000000;fill-opacity:1;stroke-width:2.42424;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" d="M 81.836676,12.239124 V 161.93671 a 2.6458333,2.6458333 45 0 0 2.645833,2.64583 H 202.556 a 2.6458333,2.6458333 135 0 0 2.64583,-2.64583 l 0,-101.175594 a 6.3875482,6.3875482 67.499815 0 0 -1.8709,-4.516708 L 158.55011,11.464166 A 6.3876651,6.3876651 22.499815 0 0 154.03338,9.5932911 H 84.482509 A 2.6458333,2.6458333 135 0 0 81.836676,12.239124 Z M 102.66386,27.77463 h 47.48971 a 6.0356894,6.0356894 23.67095 0 1 4.43871,1.945773 l 30.63408,33.246595 a 6.7760581,6.7760581 68.67095 0 1 1.79288,4.591606 l 0,76.196146 a 2.6458333,2.6458333 135 0 1 -2.64583,2.64583 h -81.70955 a 2.6458333,2.6458333 45 0 1 -2.64583,-2.64583 V 30.420463 a 2.6458333,2.6458333 135 0 1 2.64583,-2.645833 z" transform="translate(-67.766743,38.976339)" /><rect style="fill:#000000;fill-opacity:1;stroke-width:2.8843;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="rect4" width="63.287361" height="14.207367" x="40" y="90" ry="5.2704749" /><rect style="fill:#000000;fill-opacity:1;stroke-width:2.8843;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="rect4-3" width="63.287361" height="14.207367" x="40" y="120" ry="5.2704749" /><rect style="fill:#000000;fill-opacity:1;stroke-width:2.8843;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:0;paint-order:fill markers stroke" id="rect4-1" width="63.287361" height="14.207367" x="40" y="150" ry="5.2704749" /></g></svg>"""


class InkScapeFinder(QThread):
    signal_inkscape_path = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.__inkscape_path = ''

    def __find_inkscape(self):
        system = platform.system()
        if system == "Windows":
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall") as key:
                    for i in range(winreg.QueryInfoKey(key)[0]):
                        sub_key_name = winreg.EnumKey(key, i)
                        with winreg.OpenKey(key, sub_key_name) as sub_key:
                            try:
                                display_name = winreg.QueryValueEx(sub_key, "DisplayName")[0]
                                if "Inkscape" in display_name:
                                    install_path = winreg.QueryValueEx(sub_key, "InstallLocation")[0]
                                    inkscape_exe = os.path.join(install_path, "bin", "inkscape.exe")
                                    if os.path.exists(inkscape_exe):
                                        return inkscape_exe
                            except FileNotFoundError:
                                continue
            except Exception:
                pass
        elif system in {"Linux", "Darwin"}:
            try:
                result = subprocess.run(["which", "inkscape"], stdout=subprocess.PIPE, text=True)
                if result.returncode == 0:
                    return result.stdout.strip()
            except Exception:
                pass
        return None

    def run(self):
        result = self.__find_inkscape()
        if not result:
            self.__inkscape_path = ''
        else:
            self.__inkscape_path = result
        self.signal_inkscape_path.emit(self.__inkscape_path)


class SvgWidget(QWidget):
    @property
    def filename(self):
        return self.__filename

    @property
    def svg_path(self):
        return self.__svg_path

    def __init__(self, svg_path):
        super().__init__()
        self.__init_ui(svg_path)

    def __init_ui(self, svg_path):
        label_pixmap = QLabel()
        label_pixmap.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        label_pixmap.setScaledContents(True)
        self.__svg_str = self.read_svg(svg_path)
        self.__svg_path = svg_path
        label_pixmap.setPixmap(self.pixmap_from_svg(self.__svg_str))
        self.__filename = os.path.basename(svg_path).split('.svg')[0]
        label_name = QLabel()
        label_name.setText(self.__filename)
        label_name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        label_name.setAlignment(Qt.AlignCenter)
        label_name.setWordWrap(True)
        layout = QVBoxLayout()
        layout.addWidget(label_pixmap)
        layout.addWidget(label_name)
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(5)
        layout.setStretch(0, 100)
        layout.setStretch(1, 1)
        self.setLayout(layout)
        label_pixmap.setMaximumSize(_FIXED_SVG_WIDGET, _FIXED_SVG_WIDGET)
        label_pixmap.setMinimumSize(_FIXED_SVG_WIDGET, _FIXED_SVG_WIDGET)
        label_name.setMinimumWidth(_FIXED_SVG_WIDGET)
        label_name.setMaximumWidth(_FIXED_SVG_WIDGET)

        # self.setStyleSheet("""QWidget{ background-color: #ff0000;}""")

    def pixmap_from_svg(self, svg_str):
        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray(svg_str.encode()))
        if pixmap.isNull():
            print(self.__svg_path)
        return pixmap.scaled(_FIXED_SVG_WIDGET, _FIXED_SVG_WIDGET, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def read_svg(self, svg_path):
        list_str = []
        with open(svg_path, 'r', encoding='utf-8') as f:
            temp = f.readlines()
        flag = False
        if len(temp) < 2 and '<svg' in temp[0]:
            temp_split = temp[0].split('<svg')
            format_str = ('<svg' + temp_split[1]).strip()
        else:
            for i in temp:
                if i.startswith('<svg'):
                    flag = True
                if not flag:
                    continue
                list_str.append(i.strip())
            format_str = ' '.join(list_str)
        return format_str.replace('> <', '><')

    def get_svg_cpp(self):
        format_str = self.__svg_str.replace('"', '\\"')
        return f'"{format_str}";'

    def get_svg_python(self):
        return f'"""{self.__svg_str}"""'


class SvgReader(QWidget):
    def __init__(self):
        super().__init__()
        self.app_workspace_path = os.getcwd()
        self.setting_manager = SettingManager(self.app_workspace_path)
        self.setting = self.setting_manager.setting_data
        self.defaut_path = self.setting['default_path']
        self.inkscape_path = None
        if not os.path.exists(self.defaut_path):
            self.defaut_path = os.path.expanduser("~")
            self.setting = self.defaut_path
            self.setting_manager.write_file_to_json()
        self.clipboard = QApplication.clipboard()
        self.__init_ui()
        self.__init_signal_connections()
        self.message = MessageNotification(self, position='top', offset=50, hold_duration=4000, move_in_point=(None, '-50'))
        self.last_col_num = 0
        self.scrollbar_value = 0
        self.svg_dict = {}
        self.timer_file_update = QTimer()
        self.timer_file_update.timeout.connect(self.timeout_update)
        self.timer_file_update.start(1000)
        self.thread_inkscape_finder = InkScapeFinder()
        self.thread_inkscape_finder.signal_inkscape_path.connect(self.inkscape_finder_finished)
        self.thread_inkscape_finder.start()

    def __init_ui(self):
        widget_title = QWidget()
        widget_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        widget_output = QWidget()
        widget_output.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.table_widget = QTableWidget()
        self.table_widget.setObjectName('tbw')
        self.table_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.table_widget.setSelectionMode(QTableWidget.SingleSelection)
        self.table_widget.setShowGrid(False)
        self.table_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header.setSectionsClickable(False)

        label_title = QLabel(_LANG_PATH)
        label_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label_path = QLabel(self.defaut_path)
        self.label_path.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label_path.setWordWrap(True)

        self.button_path = QPushButton(_LANG_VIEW)
        self.button_open = QPushButton(_LANG_OPEN_FOLDER)
        self.button_cpp = QPushButton(f'{_LANG_COPY} <C++>')
        self.button_python = QPushButton(f'{_LANG_COPY} <Python>')
        widget_output.setMaximumHeight(80)
        for i in [self.button_path, self.button_cpp, self.button_python, self.button_open]:
            i.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            i.setMinimumHeight(30)
            i.setCursor(Qt.CursorShape.PointingHandCursor)

        layout_title = QHBoxLayout(widget_title)
        layout_title.addWidget(label_title)
        layout_title.addWidget(self.label_path)
        layout_title.addWidget(self.button_path)
        layout_title.addWidget(self.button_open)

        layout_output = QHBoxLayout(widget_output)
        layout_output.addWidget(self.button_cpp)
        layout_output.addWidget(self.button_python)

        layout_main = QVBoxLayout(self)
        layout_main.addWidget(widget_title)
        layout_main.addWidget(self.table_widget)
        layout_main.addWidget(widget_output)

        layout_main.setContentsMargins(10, 10, 10, 10)
        layout_main.setSpacing(10)
        layout_main.setStretch(0, 5)
        layout_main.setStretch(1, 100)
        layout_main.setStretch(2, 10)
        layout_output.setContentsMargins(0, 0, 0, 0)
        layout_output.setSpacing(10)
        layout_title.setContentsMargins(0, 0, 0, 0)
        layout_title.setSpacing(10)
        layout_title.setStretch(0, 10)
        layout_title.setStretch(1, 100)
        layout_title.setStretch(2, 10)
        layout_title.setStretch(3, 10)
        self.resize(1280, 800)
        self.setStyleSheet(_STYLE_SHEET)
        self.setWindowTitle('SVG_Viewer')
        self.setWindowIcon(QIcon(self.pixmap_from_svg(_ICON_SVG_WIN)))

    def __init_signal_connections(self):
        self.button_path.clicked.connect(self.get_folder_path)
        self.button_cpp.clicked.connect(self.copy_cpp)
        self.button_python.clicked.connect(self.copy_python)
        self.button_open.clicked.connect(self.open_folder)
        self.table_widget.customContextMenuRequested.connect(self.context_menu)
        self.table_widget.verticalScrollBar().valueChanged.connect(self.tableWidget_scroll_action)

    def resizeEvent(self, event):
        current_table_width = self.table_widget.width()
        column_num = current_table_width // _FIXED_SVG_TABLE_UNIT
        if column_num != self.last_col_num:
            self.get_svg_list()
            self.set_svg()
        return super().resizeEvent(event)

    def tableWidget_scroll_action(self):
        scroll_bar = self.table_widget.verticalScrollBar()
        if scroll_bar.value() > self.scrollbar_value:
            self.scrollbar_value += _SCROLL_ROWS
        elif scroll_bar.value() < self.scrollbar_value:
            self.scrollbar_value -= _SCROLL_ROWS
        else:
            return
        scroll_bar.setValue(self.scrollbar_value)

    def pixmap_from_svg(self, svg_str: str):
        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray(svg_str.encode()))
        return pixmap

    def get_svg_list(self):
        self.svg_list = []
        for item in os.listdir(self.defaut_path):
            item: str
            if item.endswith(".svg"):
                self.svg_list.append(os.path.join(self.defaut_path, item))
        return self.svg_list

    def set_svg(self):
        self.get_svg_list()
        if not self.svg_list:
            return
        current_table_width = self.table_widget.width()
        column_num = current_table_width // _FIXED_SVG_TABLE_UNIT
        self.last_col_num = column_num
        self.table_widget.setColumnCount(column_num)
        self.table_widget.setRowCount(len(self.svg_list) // column_num + 1)
        self.table_widget.clear()
        for idx, item in enumerate(self.svg_list):
            item: SvgWidget
            widget = SvgWidget(item)

            table_item = QTableWidgetItem()
            table_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table_widget.setItem(idx // column_num, idx % column_num, table_item)

            container = QWidget()
            container.setToolTip(widget.filename)
            layout = QHBoxLayout(container)
            layout.addWidget(widget)

            layout.setSpacing(0)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

            self.table_widget.setCellWidget(idx // column_num, idx % column_num, container)
        self.table_widget.resizeRowsToContents()

    def get_folder_path(self):
        path = QFileDialog.getExistingDirectory(self, "Select Folder", self.defaut_path)
        if path:
            self.defaut_path = path
            self.setting['default_path'] = path
            self.label_path.setText(path)
            self.setting_manager.write_file_to_json()
            self.get_svg_list()
            self.set_svg()

    def get_current_selected_item(self):
        item = self.table_widget.currentItem()
        if not item:
            return None
        widget = self.table_widget.cellWidget(item.row(), item.column())
        if not widget:
            return None
        layout = widget.layout()
        if not layout:
            return None
        widget_svg = layout.itemAt(0).widget()
        if not widget_svg:
            return None
        return widget_svg

    def get_time_dict(self):
        self.get_svg_list()
        temp = {}
        for item in self.svg_list:
            temp[item] = os.path.getmtime(item)
        return temp

    def timeout_update(self):
        new_dict = self.get_time_dict()

        # 如果新字典和旧字典相同，直接返回
        if len(new_dict) == len(self.svg_dict) and all(new_dict.get(item) == self.svg_dict.get(item, '') for item in new_dict):
            return

        # 如果新字典与旧字典不同，更新字典并调用 set_svg()
        self.svg_dict = new_dict
        self.set_svg()

    def copy_cpp(self):
        item: SvgWidget = self.get_current_selected_item()
        if item:
            self.clipboard.setText(item.get_svg_cpp())
            self.message.notification(f'{_LANG_COPYED} <b>&lt; C++ &gt;</b> {_LANG_TO_CLIPBOARD}')

    def copy_python(self):
        item: SvgWidget = self.get_current_selected_item()
        if item:
            self.clipboard.setText(item.get_svg_python())
            self.message.notification(f'{_LANG_COPYED} <b>&lt; Python &gt;</b> {_LANG_TO_CLIPBOARD}')

    def open_folder(self):
        subprocess.Popen('explorer /open, ' + os.path.normpath(self.defaut_path), creationflags=subprocess.CREATE_NO_WINDOW)

    def open_file(self, widget: SvgWidget):
        file_path = widget.svg_path
        if file_path:
            subprocess.Popen('notepad ' + os.path.normpath(file_path), creationflags=subprocess.CREATE_NO_WINDOW)

    def open_file_by_notepad(self):
        item: SvgWidget = self.get_current_selected_item()
        if item:
            self.open_file(item)

    def context_menu(self, pos):
        mouse_item = self.table_widget.itemAt(pos)
        if not mouse_item:
            return
        # row = mouse_item.row()
        # col = mouse_item.column()

        menu = QMenu(self)
        action_copy_cpp = QAction(f'{_LANG_COPY} <C++>')
        action_copy_cpp.setIcon(QIcon(self.pixmap_from_svg(_ICON_CPP)))
        action_copy_cpp.triggered.connect(self.copy_cpp)

        action_copy_python = QAction(f'{_LANG_COPY} <Python>')
        action_copy_python.setIcon(QIcon(self.pixmap_from_svg(_ICON_PYTHON)))
        action_copy_python.triggered.connect(self.copy_python)

        action_notepad = QAction(f'{_LANG_EDIT_IN_NOTEPAD}')
        action_notepad.setIcon(QIcon(self.pixmap_from_svg(_ICON_NOTEPAD)))
        action_notepad.triggered.connect(self.open_file_by_notepad)

        action_inkscape = QAction(_LANG_OPEN_IN_INKSCAPE)
        action_inkscape.setIcon(QIcon(self.pixmap_from_svg(_ICON_INKSCAPE)))
        action_inkscape.triggered.connect(self.open_file_by_inkscape)

        action_location = QAction(_LANG_LOCATION_FILE)
        action_location.setIcon(QIcon(self.pixmap_from_svg(_ICON_LOCATION)))
        action_location.triggered.connect(self.location_to_file)

        action_copy_path = QAction(_LANG_COPY_FILE_PATH)
        action_copy_path.setIcon(QIcon(self.pixmap_from_svg(_ICON_COPY_PATH)))
        action_copy_path.triggered.connect(self.copy_file_path)

        menu.addAction(action_copy_cpp)
        menu.addAction(action_copy_python)
        menu.addAction(action_notepad)
        if self.inkscape_path:
            menu.addAction(action_inkscape)
        menu.addAction(action_location)
        menu.addAction(action_copy_path)
        menu.exec_(self.table_widget.mapToGlobal(pos))

    def inkscape_finder_finished(self, result):
        if result:
            self.inkscape_path = result
        else:
            self.inkscape_path = None

    def open_file_by_inkscape(self):
        widget: SvgWidget = self.get_current_selected_item()
        if widget and self.inkscape_path:
            file_path = os.path.normpath(widget.svg_path)
            command = f'"{self.inkscape_path}" "{file_path}"'
            subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)

    def location_to_file(self):
        widget: SvgWidget = self.get_current_selected_item()
        if not widget:
            return
        file_path = widget.svg_path
        if file_path:
            subprocess.Popen('explorer /select,' + os.path.normpath(file_path), creationflags=subprocess.CREATE_NO_WINDOW)

    def copy_file_path(self):
        widget: SvgWidget = self.get_current_selected_item()
        if not widget:
            return
        file_path = widget.svg_path
        if file_path:
            self.clipboard.setText(file_path.replace('\\', '/'))
            self.message.notification(_LANG_COPYED_FILE_PATH)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SvgReader()
    window.show()
    sys.exit(app.exec_())
