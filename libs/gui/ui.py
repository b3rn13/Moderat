from PyQt4.QtGui import *
from PyQt4.QtCore import *


class updateUi:

    def __init__(self, moderat):
        self.moderat = moderat

        self.tables = self.moderat.tables

        self.onlineIcon = QPushButton()
        self.onlineIcon.setProperty('onlineClientsTab', '1')
        self.onlineIcon.setFocusPolicy(Qt.NoFocus)
        self.onlineIcon.clicked.connect(lambda: self.moderat.clientsTabs.setCurrentIndex(0))
        self.moderat.clientsTabs.tabBar().setTabButton(0, QTabBar.LeftSide, self.onlineIcon)

        self.directIcon = QPushButton()
        self.directIcon.setProperty('directClientsTab', '1')
        self.directIcon.setFocusPolicy(Qt.NoFocus)
        self.directIcon.clicked.connect(lambda: self.moderat.clientsTabs.setCurrentIndex(1))
        self.moderat.clientsTabs.tabBar().setTabButton(1, QTabBar.LeftSide, self.directIcon)

        self.offlineIcon = QPushButton()
        self.offlineIcon.setProperty('offlineClientsTab', '1')
        self.offlineIcon.setFocusPolicy(Qt.NoFocus)
        self.offlineIcon.clicked.connect(lambda: self.moderat.clientsTabs.setCurrentIndex(2))
        self.moderat.clientsTabs.tabBar().setTabButton(2, QTabBar.LeftSide, self.offlineIcon)

        self.on_server_stopped()

    def on_moderator_connected(self):
        """
        If Moderator Connected To Server
        :return:
        """
        self.moderat.actionConnect.setDisabled(True)
        self.moderat.actionDisconnect.setDisabled(False)

    def on_moderator_not_connected(self):
        '''
        If Moderator Disconnected From Server
        :return:
        '''
        self.moderat.actionConnect.setDisabled(False)
        self.moderat.actionDisconnect.setDisabled(True)
        self.clear_tables()
        self.moderat.pagination.clear_pages()

        if hasattr(self.moderat, 'onlineLoading'):
            self.moderat.onlineLoading.hide()

    def on_server_started(self):
        '''
        If Direct Server Started
        :return:
        '''
        self.moderat.actionStartServer.setDisabled(True)
        self.moderat.actionStopServer.setDisabled(False)

    def on_server_stopped(self):
        '''
        If Direct Server Stopped
        :return:
        '''
        self.moderat.actionStartServer.setDisabled(False)
        self.moderat.actionStopServer.setDisabled(True)
        self.clear_direct_table()

    def clear_tables(self):
        '''
        Clear Tables
        :return:
        '''
        self.tables.clean_tables()

    def clear_direct_table(self):
        '''
        Clear Direct Clients
        :return:
        '''
        self.tables.clean_direct_table()

    # Enable Administrators Features
    def enable_administrator(self):
        self.moderat.offlineClientsTable.showColumn(0)

    # Disable Administrators Features
    def disable_administrator(self):
        self.moderat.offlineClientsTable.setColumnHidden(0, True)