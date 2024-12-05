import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(149, 44)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 31)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(149, 104)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 31)
        self._textBox2.TabIndex = 1
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(159, 148)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 2
        self._label1.Text = "label1"
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(12, 189)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(96, 35)
        self._button1.TabIndex = 3
        self._button1.Text = "solve"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(12, 44)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(131, 23)
        self._label2.TabIndex = 4
        self._label2.Text = "Year salery:"
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(36, 78)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(107, 57)
        self._label3.TabIndex = 5
        self._label3.Text = "pay times per year:"
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(12, 148)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(141, 38)
        self._label4.TabIndex = 6
        self._label4.Text = "Monthly pay:"
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(116, 190)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(80, 34)
        self._button2.TabIndex = 7
        self._button2.Text = "Erase"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(202, 190)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(75, 34)
        self._button3.TabIndex = 8
        self._button3.Text = "Quit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(284, 261)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "pg153"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        pay1 = float(self._textBox1.Text)
        time = float(self._textBox2.Text)
        payPerTime = round(pay1 / time , 2)
        self._label1.Text = str(payPerTime)

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()