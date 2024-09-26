import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._show = System.Windows.Forms.Button()
        self._clear = System.Windows.Forms.Button()
        self._Exit = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(125, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(690, 287)
        self._label1.TabIndex = 0
        self._label1.Text = " "
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label1.Click += self.Label1Click
        # 
        # show
        # 
        self._show.Location = System.Drawing.Point(125, 299)
        self._show.Name = "show"
        self._show.Size = System.Drawing.Size(125, 53)
        self._show.TabIndex = 1
        self._show.Text = "show"
        self._show.UseVisualStyleBackColor = True
        self._show.Click += self.ShowClick
        # 
        # clear
        # 
        self._clear.Location = System.Drawing.Point(412, 299)
        self._clear.Name = "clear"
        self._clear.Size = System.Drawing.Size(125, 53)
        self._clear.TabIndex = 2
        self._clear.Text = "clear"
        self._clear.UseVisualStyleBackColor = True
        self._clear.Click += self.ClearClick
        # 
        # Exit
        # 
        self._Exit.Location = System.Drawing.Point(690, 299)
        self._Exit.Name = "Exit"
        self._Exit.Size = System.Drawing.Size(125, 53)
        self._Exit.TabIndex = 3
        self._Exit.Text = "Exit"
        self._Exit.UseVisualStyleBackColor = True
        self._Exit.Click += self.ExitClick
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(955, 442)
        self.Controls.Add(self._Exit)
        self.Controls.Add(self._clear)
        self.Controls.Add(self._show)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "schedule"
        self.ResumeLayout(False)


    def Label1Click(self, sender, e):
        pass

    def ShowClick(self, sender, e):
        self._label1.Text = "History, computer programing, band, health, math, science, english, spanish."

    def ClearClick(self, sender, e):
        self._label1.Text = ""

    def ExitClick(self, sender, e):
        Application.Exit()