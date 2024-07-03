import wx

class MainWindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, title="NetMeasure", size=(640,480))
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        # Main application menu
        mnuFile = wx.Menu()
        mnuFile.Append(wx.ID_ABOUT, "&About", " Information about this program")
        mnuFile.Append(wx.ID_PREFERENCES, "&Preferences", " Manage application settings")
        mnuFile.Append(wx.ID_EXIT, "E&xit", " Terminate the program")

        self.Bind(wx.EVT_MENU, self.OnMnuFileExit_MenuAction,id = wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnMnuNew_MenuAction, id = wx.ID_NEW)

        # Setting up the menu.
        mnuFile.Append(wx.ID_NEW, "&New Project\tCtrl-N", " Information about this program")
        mnuFile.Append(wx.ID_ANY, "&Open Project\tCtrl-O", " Information about this program")
        mnuFile.Append(wx.ID_ANY, "&Save Project\tCtrl-S", " Information about this program")
        mnuFile.Append(wx.ID_ANY, "&Export Project", " Information about this program")



        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(mnuFile,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

    def OnMnuFileExit_MenuAction(self, evt):
        self.Close(True)

    def OnMnuNew_MenuAction(self, evt):
        win = wx.Frame(self, -1, "Child Window")
        win.Show(True)

app = wx.App()
frame = MainWindow()
frame.Show()
app.MainLoop()