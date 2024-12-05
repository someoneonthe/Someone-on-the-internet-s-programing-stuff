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
        self._button1.Location = System.Drawing.Point(12, 15)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(115, 44)
        self._button1.TabIndex = 0
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.SystemColors.Info
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 25
        self._listBox1.Location = System.Drawing.Point(12, 65)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(556, 279)
        self._listBox1.TabIndex = 2
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.Control
        self._button2.Location = System.Drawing.Point(242, 15)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(115, 44)
        self._button2.TabIndex = 3
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.Control
        self._button3.Location = System.Drawing.Point(453, 15)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(115, 44)
        self._button3.TabIndex = 4
        self._button3.Text = "quit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.AppWorkspace
        self.ClientSize = System.Drawing.Size(580, 362)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._button1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "prog 122h"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        num1 = 1
        for amount in range(0, 20):
            sq = num1 * num1
            sqrt = math.sqrt(num1)
            cube = sq * num1
            sqrt4 = math.sqrt(sqrt)
            line = str(num1) + "\t" + str(sq) + "\t" + str(sqrt) + "\t" + str(cube) + "\t" + str(sqrt4)
            self._listBox1.Items.Add(line)
            num1 = num1 + 1
    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()