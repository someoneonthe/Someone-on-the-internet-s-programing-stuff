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
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(129, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 31)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(129, 49)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 31)
        self._textBox2.TabIndex = 1
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.Control
        self._label1.Location = System.Drawing.Point(129, 84)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 2
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(12, 119)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(74, 32)
        self._button1.TabIndex = 3
        self._button1.Text = "Solve"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(92, 119)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(77, 32)
        self._button2.TabIndex = 4
        self._button2.Text = "Erase"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(175, 119)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(62, 32)
        self._button3.TabIndex = 5
        self._button3.Text = "quit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(12, 12)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 6
        self._label2.Text = "calories"
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(12, 52)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(111, 28)
        self._label3.TabIndex = 7
        self._label3.Text = "Fat grams"
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(2, 84)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(121, 32)
        self._label4.TabIndex = 8
        self._label4.Text = "percentage"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlLight
        self.ClientSize = System.Drawing.Size(249, 167)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "pg268"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        totalCal = float(self._textBox1.Text)
        fatGrams = float(self._textBox2.Text)
        calOfFat = fatGrams * 9
        fatPerCal = calOfFat / totalCal
        self._label1.Text = str(fatPerCal)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()