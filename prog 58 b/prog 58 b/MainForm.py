import System.Drawing
import System.Windows.Forms
import math
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._button4 = System.Windows.Forms.Button()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(84, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 31)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(84, 46)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 31)
        self._textBox2.TabIndex = 1
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(84, 83)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(100, 31)
        self._textBox3.TabIndex = 2
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.Control
        self._label1.Location = System.Drawing.Point(130, 141)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(54, 23)
        self._label1.TabIndex = 3
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.Control
        self._label2.Location = System.Drawing.Point(130, 181)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(54, 23)
        self._label2.TabIndex = 4
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(204, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(138, 43)
        self._button1.TabIndex = 5
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(204, 61)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(138, 39)
        self._button2.TabIndex = 6
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(204, 122)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(138, 62)
        self._button3.TabIndex = 7
        self._button3.Text = "Quit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(31, 12)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(47, 23)
        self._label3.TabIndex = 8
        self._label3.Text = "A = "
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(31, 49)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(47, 23)
        self._label4.TabIndex = 9
        self._label4.Text = "B = "
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(31, 86)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(47, 23)
        self._label5.TabIndex = 10
        self._label5.Text = "C = "
        # 
        # button4
        # 
        self._button4.Location = System.Drawing.Point(332, 194)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(10, 10)
        self._button4.TabIndex = 11
        self._button4.UseVisualStyleBackColor = True
        self._button4.Click += self.Button4Click
        # 
        # label6
        # 
        self._label6.Location = System.Drawing.Point(13, 140)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 23)
        self._label6.TabIndex = 12
        self._label6.Text = "Root 1 = "
        # 
        # label7
        # 
        self._label7.Location = System.Drawing.Point(13, 181)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(100, 23)
        self._label7.TabIndex = 13
        self._label7.Text = "Root 2 ="
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self.ClientSize = System.Drawing.Size(354, 216)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "prog 58 b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        a = int(self._textBox1.Text)
        b = int(self._textBox2.Text)
        c = int(self._textBox3.Text)
        root1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        root2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        self._label1.Text = str(root1)
        self._label2.Text = str(root2)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label1.Text = ""
        self._label2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button4Click(self, sender, e):
        self._button1.Text = "Bucket"
        self._button2.Text = "master chef"
        self._button3.Text = "area 51"
