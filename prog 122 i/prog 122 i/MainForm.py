import System.Drawing
import System.Windows.Forms
import math
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.Control
        self._button1.Location = System.Drawing.Point(13, 13)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(109, 48)
        self._button1.TabIndex = 0
        self._button1.Text = "Numbers"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.SystemColors.Info
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 25
        self._listBox1.Location = System.Drawing.Point(13, 67)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(520, 279)
        self._listBox1.TabIndex = 1
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.Control
        self._button2.Location = System.Drawing.Point(128, 13)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(109, 48)
        self._button2.TabIndex = 2
        self._button2.Text = "Erase"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.Control
        self._button3.Location = System.Drawing.Point(243, 13)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(109, 48)
        self._button3.TabIndex = 3
        self._button3.Text = "Quit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Silver
        self.ClientSize = System.Drawing.Size(545, 363)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._button1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "prog 122 i"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        num1 = 1
        for num in range(-25, 26):
            cube = num ** 3
            cuberoot = round(math.sqrt(math.sqrt(abs(num))),2)
            line = str(num) + "\t\t" + str(cube) + "\t\t" + str(cuberoot)
            self._listBox1.Items.Add(line)
            num = num + 1

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()