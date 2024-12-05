import System.Drawing
import System.Windows.Forms
import math
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 25
        self._listBox1.Location = System.Drawing.Point(12, 89)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(218, 179)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(118, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(112, 34)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(12, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 31)
        self._textBox1.TabIndex = 2
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(12, 49)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(100, 34)
        self._button2.TabIndex = 3
        self._button2.Text = "Erase"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(118, 52)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(112, 31)
        self._button3.TabIndex = 4
        self._button3.Text = "Quit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(245, 282)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "prog 152b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        E = int(self._textBox1.Text)
        endpoint = E / 4
        num = 0
        num2 = 0
        for even in range(0, endpoint):
            line = str(num) + "\t\t" + str(num2)
            num = num + 2
            num2 = num2 + num
            line = str(num) + "\t" + str(num2)
            self._listBox1.Items.Add(line)

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()