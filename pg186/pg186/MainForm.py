import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(12, 123)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(243, 47)
        self._button1.TabIndex = 0
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(12, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 31)
        self._textBox1.TabIndex = 1
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(12, 49)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 31)
        self._textBox2.TabIndex = 2
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(12, 86)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(100, 31)
        self._textBox3.TabIndex = 3
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(170, 15)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 4
        self._label1.Text = "label1"
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(170, 52)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 5
        self._label2.Text = "label2"
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(170, 89)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 6
        self._label3.Text = "label3"
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(12, 183)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(119, 47)
        self._button2.TabIndex = 7
        self._button2.Text = "Erase"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(137, 183)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(118, 47)
        self._button3.TabIndex = 8
        self._button3.Text = "Quit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self.ClientSize = System.Drawing.Size(283, 242)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "pg186"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        ticketA = int(self._textBox1.Text)
        ticketB = int(self._textBox2.Text)
        ticketC = int(self._textBox3.Text)
        soldA = ticketA * 15
        soldB = ticketB * 12
        soldC = ticketC * 9
        self._label1.Text = str(soldA)
        self._label2.Text = str(soldB)
        self._label3.Text = str(soldC)

    def Button2Click(self, sender, e):
        self._textBox1.Text = "0"
        self._textBox2.Text = "0"
        self._textBox3.Text = "0"
        self._label1.Text = ""
        self._label2.Text = ""
        self._label3.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()