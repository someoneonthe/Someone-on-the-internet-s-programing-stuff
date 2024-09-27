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
        self._label3 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._textBox5 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(13, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "A = "
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(59, 13)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 31)
        self._textBox1.TabIndex = 1
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(13, 60)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 2
        self._label2.Text = "B ="
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(13, 98)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 3
        self._label3.Text = "C ="
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(59, 57)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 31)
        self._textBox2.TabIndex = 4
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(59, 95)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(100, 31)
        self._textBox3.TabIndex = 5
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(12, 345)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(146, 48)
        self._button1.TabIndex = 6
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(12, 399)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(146, 46)
        self._button2.TabIndex = 7
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(355, 413)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(60, 32)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(23, 191)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 23)
        self._label4.TabIndex = 11
        self._label4.Text = "+"
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(23, 240)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(100, 23)
        self._label5.TabIndex = 12
        self._label5.Text = "-"
        # 
        # textBox4
        # 
        self._textBox4.Location = System.Drawing.Point(59, 188)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(100, 31)
        self._textBox4.TabIndex = 13
        # 
        # textBox5
        # 
        self._textBox5.Location = System.Drawing.Point(59, 237)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(100, 31)
        self._textBox5.TabIndex = 14
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(427, 457)
        self.Controls.Add(self._textBox5)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "prog58b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        A = int(self._textBox1.Text)
        B = int(self._textBox2.Text)
        C = int(self._textBox3.Text)