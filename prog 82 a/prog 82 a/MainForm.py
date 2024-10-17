import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(13, 16)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(122, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "speed limit"
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(141, 13)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 31)
        self._textBox1.TabIndex = 1
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(13, 60)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(122, 23)
        self._label2.TabIndex = 2
        self._label2.Text = "your speed"
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(141, 57)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 31)
        self._textBox2.TabIndex = 3
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(13, 106)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(63, 23)
        self._label3.TabIndex = 4
        self._label3.Text = "ticket"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.Window
        self._label4.Location = System.Drawing.Point(82, 106)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 23)
        self._label4.TabIndex = 5
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(44, 149)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(123, 38)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(12, 193)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(86, 38)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(107, 193)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(86, 38)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(253, 449)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "prog 82 a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        a = int(self._textBox1.Text)
        b = int(self._textBox2.Text)
        ticket = (20 + ((b - a) * 5))
        self._label4.Text = str(ticket)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label4.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()