import sys
import os

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QTextEdit, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor

from spotipy_functions import spotify_configuration, save_configuration, create_playlist

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

sp_conf = spotify_configuration()

widgets = {
    "logo": [],
    "username_label": [],
    "username_input": [],
    "client_id_label": [],
    "client_id_input": [],
    "client_secret_label": [],
    "client_secret_input": [],
    "redirect_uris_label": [],
    "redirect_uris_input": [],
    "button_save_configuration": [],
    "playlist_name_label": [],
    "playlist_name_input": [],
    "list_of_songs_label": [],
    "list_of_songs_input": [],
    "songs_from_file_label": [],
    "button_create_playlist": []
}

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Spotify playlist creator by bartass")
window.setFixedWidth(800)
window.move(200, 200)
window.setStyleSheet("background: #161219;")

grid = QGridLayout()


def show_dialog_save():
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Spotify configuration saved successfully")
    msgBox.setWindowTitle("Spotify playlist creator by bartass")
    msgBox.setStandardButtons(QMessageBox.Ok)
    # msgBox.buttonClicked.connect(msgButtonClick)

    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        print('OK clicked')


def show_dialog_create(list_of_no_songs):
    cant_search = ""
    if list_of_no_songs:
        cant_search = "Can't search: " + str(list_of_no_songs)
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Spotify playlist created successfully\n " + cant_search)
    msgBox.setWindowTitle("Info")
    msgBox.setStandardButtons(QMessageBox.Ok)
    # msgBox.buttonClicked.connect(msgButtonClick)

    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        print('OK clicked')


def button_save_configuration_action():
    save_configuration(widgets["client_id_input"][-1].text(), widgets["client_secret_input"][-1].text(), widgets["redirect_uris_input"][-1].text(), widgets["username_input"][-1].text())
    show_dialog_save()


def button_create_playlist_action():
    # print (widgets["list_of_songs_input"][-1].toPlainText())
    list_of_no_songs = create_playlist(sp_conf, widgets["playlist_name_input"][-1].text(), widgets["list_of_songs_input"][-1].toPlainText())
    show_dialog_create(list_of_no_songs)


def frame1():
    image = QPixmap(resource_path("logo.png"))
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignRight)
    logo.setStyleSheet("margin-left: 20px;")
    widgets["logo"].append(logo)

    username_label = QLabel("Username:")
    username_label.setAlignment(QtCore.Qt.AlignRight)
    username_label.setStyleSheet(
        "font-size: 20px;" +
        "color: 'white';" +
        "padding: 2px 2px;" +
        "margin: 2px 2px;" +
        "background: '#161219';"
    )
    widgets["username_label"].append(username_label)

    username_input = QLineEdit(sp_conf["username"])
    widgets["username_input"].append(username_input)

    client_id_label = QLabel("Client ID:")
    client_id_label.setAlignment(QtCore.Qt.AlignRight)
    client_id_label.setStyleSheet(
        "font-size: 20px;" +
        "color: 'white';" +
        "padding: 2px 2px;" +
        "margin: 2px 2px;" +
        "background: '#161219';"
    )
    widgets["client_id_label"].append(client_id_label)

    client_id_input = QLineEdit(sp_conf["id"])
    widgets["client_id_input"].append(client_id_input)

    client_secret_label = QLabel("Client Secret:")
    client_secret_label.setAlignment(QtCore.Qt.AlignRight)
    client_secret_label.setStyleSheet(
        "font-size: 20px;" +
        "color: 'white';" +
        "padding: 2px 2px;" +
        "margin: 2px 2px;" +
        "background: '#161219';"
    )
    widgets["client_secret_label"].append(client_secret_label)

    client_secret_input = QLineEdit(sp_conf["secret"])
    widgets["client_secret_input"].append(client_secret_input)

    redirect_uris_label = QLabel("Redirect URIs:")
    redirect_uris_label.setAlignment(QtCore.Qt.AlignRight)
    redirect_uris_label.setStyleSheet(
        "font-size: 20px;" +
        "color: 'white';" +
        "padding: 2px 2px;" +
        "margin: 2px 2px;" +
        "background: '#161219';"
    )
    widgets["redirect_uris_label"].append(redirect_uris_label)

    redirect_uris_input = QLineEdit(sp_conf["redirect"])
    widgets["redirect_uris_input"].append(redirect_uris_input)

    button_save_configuration = QPushButton("Save Configuration")
    button_save_configuration.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button_save_configuration.setStyleSheet(
        "*{border: 4px solid '#4682B4';" +
        "border-radius: 20px;" +
        "font-size: 15px;" +
        "color: 'white';" +
        "padding: 5px 0;" +
        "margin: 2px 2px;}" +
        "*:hover{background: '#4682B4';}"
    )
    button_save_configuration.clicked.connect(button_save_configuration_action)
    widgets["button_save_configuration"].append(button_save_configuration)

    playlist_name_label = QLabel("Playlist name:")
    playlist_name_label.setAlignment(QtCore.Qt.AlignRight)
    playlist_name_label.setStyleSheet(
        "font-size: 20px;" +
        "color: 'white';" +
        "padding: 2px 2px;" +
        "margin: 2px 2px;" +
        "background: '#161219';"
    )
    widgets["playlist_name_label"].append(playlist_name_label)

    playlist_name_input = QLineEdit()
    widgets["playlist_name_input"].append(playlist_name_input)

    list_of_songs_label = QLabel("List of songs:")
    list_of_songs_label.setAlignment(QtCore.Qt.AlignTop)
    list_of_songs_label.setStyleSheet(
        "font-size: 20px;" +
        "color: 'white';" +
        "padding: 2px 2px;" +
        "margin: 2px 2px;" +
        "background: '#161219';"
    )
    widgets["list_of_songs_label"].append(list_of_songs_label)

    list_of_songs_input = QTextEdit()
    widgets["list_of_songs_input"].append(list_of_songs_input)

    button_create_playlist = QPushButton("Create Playlist on Spotify")
    button_create_playlist.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button_create_playlist.setStyleSheet(
        "*{border: 4px solid '#4682B4';" +
        "border-radius: 20px;" +
        "font-size: 25px;" +
        "color: 'white';" +
        "padding: 5px 0;" +
        "margin: 2px 2px;}" +
        "*:hover{background: '#4682B4';}"
    )
    button_create_playlist.clicked.connect(button_create_playlist_action)
    widgets["button_create_playlist"].append(button_create_playlist)

    grid.addWidget(widgets["logo"][-1], 0, 2, 4, 1)
    grid.addWidget(widgets["username_label"][-1], 0, 0)
    grid.addWidget(widgets["username_input"][-1], 0, 1)
    grid.addWidget(widgets["client_id_label"][-1], 1, 0)
    grid.addWidget(widgets["client_id_input"][-1], 1, 1)
    grid.addWidget(widgets["client_secret_label"][-1], 2, 0)
    grid.addWidget(widgets["client_secret_input"][-1], 2, 1)
    grid.addWidget(widgets["redirect_uris_label"][-1], 3, 0)
    grid.addWidget(widgets["redirect_uris_input"][-1], 3, 1)
    grid.addWidget(widgets["button_save_configuration"][-1], 4, 1)
    grid.addWidget(widgets["playlist_name_label"][-1], 5, 0)
    grid.addWidget(widgets["playlist_name_input"][-1], 5, 1)
    grid.addWidget(widgets["list_of_songs_label"][-1], 6, 0)
    grid.addWidget(widgets["list_of_songs_input"][-1], 6, 1)
    grid.addWidget(widgets["button_create_playlist"][-1], 8, 1)


frame1()

window.setLayout(grid)
window.show()
sys.exit(app.exec())
