import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.Control
        self._label1.Location = System.Drawing.Point(135, 86)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ButtonFace
        self._button1.Location = System.Drawing.Point(13, 50)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(116, 31)
        self._button1.TabIndex = 1
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(13, 13)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(116, 31)
        self._textBox1.TabIndex = 2
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.Control
        self._label2.Location = System.Drawing.Point(12, 86)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(128, 23)
        self._label2.TabIndex = 3
        self._label2.Text = "Factorial ="
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ButtonFace
        self._button2.Location = System.Drawing.Point(135, 13)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(81, 33)
        self._button2.TabIndex = 4
        self._button2.Text = "Erase"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ButtonFace
        self._button3.Location = System.Drawing.Point(135, 48)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(81, 33)
        self._button3.TabIndex = 5
        self._button3.Text = "Quit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(253, 127)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "prog162 a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        yournum = int(self._textBox1.Text)
        mnum = 1
        newnum = 1
        for num in range(0, yournum):
            newnum = newnum * mnum
            mnum = mnum + 1
        self._label1.Text = str(newnum)

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()