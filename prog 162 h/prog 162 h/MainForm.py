import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(12, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(111, 31)
        self._textBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(12, 49)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(111, 30)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label1.Location = System.Drawing.Point(160, 112)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 2
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(129, 12)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(102, 31)
        self._button2.TabIndex = 3
        self._button2.Text = "Clear all"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(130, 49)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(101, 30)
        self._button3.TabIndex = 4
        self._button3.Text = "Quit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(13, 82)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(141, 53)
        self._label2.TabIndex = 5
        self._label2.Text = "possible| arrangments:"
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(12, 167)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(76, 23)
        self._label3.TabIndex = 6
        self._label3.Text = "chairs:"
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(94, 161)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 31)
        self._textBox2.TabIndex = 7
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(-24, 135)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(324, 23)
        self._label4.TabIndex = 8
        self._label4.Text = "_________________________________________________"
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(12, 230)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(100, 30)
        self._label5.TabIndex = 9
        self._label5.Text = "standing:"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.ActiveBorder
        self._label6.Location = System.Drawing.Point(118, 231)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 23)
        self._label6.TabIndex = 10
        # 
        # button4
        # 
        self._button4.Location = System.Drawing.Point(12, 198)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(110, 29)
        self._button4.TabIndex = 11
        self._button4.Text = "Calculate"
        self._button4.UseVisualStyleBackColor = True
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.Location = System.Drawing.Point(128, 196)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(102, 31)
        self._button5.TabIndex = 12
        self._button5.Text = "Clear all"
        self._button5.UseVisualStyleBackColor = True
        self._button5.Click += self.Button5Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ButtonShadow
        self.ClientSize = System.Drawing.Size(246, 374)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "prog 162 h"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        yournum = int(self._textBox1.Text)
        rangenum = yournum - 2
        mnum = 3
        newnum = 1
        for num in range(0, rangenum):
            newnum = newnum * mnum
            mnum = mnum + 1
        
        self._label1.Text = str(newnum)

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button5Click(self, sender, e):
        self._label1.Text = ""

    def Button4Click(self, sender, e):
        yournum = int(self._textBox1.Text)
        chairs = int(self._textBox2.Text)
        standing = yournum - chairs
        self._label6.Text = str(standing)