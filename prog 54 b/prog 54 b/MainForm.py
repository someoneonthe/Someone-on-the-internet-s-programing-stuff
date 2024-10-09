import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(13, 13)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(110, 52)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(130, 13)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(108, 52)
        self._button2.TabIndex = 1
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(245, 13)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(133, 52)
        self._button3.TabIndex = 2
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(138, 101)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 31)
        self._textBox1.TabIndex = 3
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(138, 138)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 31)
        self._textBox2.TabIndex = 4
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(138, 212)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(100, 31)
        self._textBox3.TabIndex = 5
        # 
        # textBox4
        # 
        self._textBox4.Location = System.Drawing.Point(138, 175)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(100, 31)
        self._textBox4.TabIndex = 6
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label1.Location = System.Drawing.Point(138, 256)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(240, 23)
        self._label1.TabIndex = 7
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label2.Location = System.Drawing.Point(138, 288)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(240, 23)
        self._label2.TabIndex = 8
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(46, 256)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(77, 23)
        self._label3.TabIndex = 9
        self._label3.Text = "sum ="
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(13, 288)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(110, 30)
        self._label4.TabIndex = 10
        self._label4.Text = "average ="
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(32, 104)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(91, 23)
        self._label5.TabIndex = 11
        self._label5.Text = "A="
        # 
        # label6
        # 
        self._label6.Location = System.Drawing.Point(32, 141)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 23)
        self._label6.TabIndex = 12
        self._label6.Text = "B="
        # 
        # label7
        # 
        self._label7.Location = System.Drawing.Point(32, 178)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(100, 23)
        self._label7.TabIndex = 13
        self._label7.Text = "C="
        # 
        # label8
        # 
        self._label8.Location = System.Drawing.Point(32, 215)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(100, 23)
        self._label8.TabIndex = 14
        self._label8.Text = "D="
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(438, 431)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "prog 54 b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        a = int(self._textBox1.Text)
        b = int(self._textBox2.Text)
        c = int(self._textBox3.Text)
        d = int(self._textBox4.Text)
        S = a + b + c + d
        A = (a + b + c + d) // 4
        self._label1.Text = str(A)
        self._label2.Text = str(S)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._label1.Text = ""
        self._label2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()