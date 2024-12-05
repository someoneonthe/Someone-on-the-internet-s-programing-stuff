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
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(87, 141)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(245, 35)
        self._label1.TabIndex = 0
        self._label1.Text = "Average score:"
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(113, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 31)
        self._textBox1.TabIndex = 1
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(113, 53)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 31)
        self._textBox2.TabIndex = 2
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(113, 95)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(100, 31)
        self._textBox3.TabIndex = 3
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(233, 8)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(120, 38)
        self._button1.TabIndex = 4
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(233, 49)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(120, 38)
        self._button2.TabIndex = 5
        self._button2.Text = "Erase"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(233, 93)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(120, 34)
        self._button3.TabIndex = 6
        self._button3.Text = "Quit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(7, 15)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 7
        self._label2.Text = "Test 1"
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(7, 56)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 8
        self._label3.Text = "Test 2"
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(7, 98)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 23)
        self._label4.TabIndex = 9
        self._label4.Text = "Test 3"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(363, 185)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "pg198"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        test1 = float(self._textBox1.Text)
        test2 = float(self._textBox2.Text)
        test3 = float(self._textBox3.Text)
        average = (test1 + test2 + test3) / 3
        self._label1.Text = "average score:" + str(average)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()