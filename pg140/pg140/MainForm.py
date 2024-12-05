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
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self._radioButton5 = System.Windows.Forms.RadioButton()
        self._radioButton6 = System.Windows.Forms.RadioButton()
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
        self._textBox1.Location = System.Drawing.Point(118, 6)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 31)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(118, 52)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 31)
        self._textBox2.TabIndex = 1
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.Control
        self._label1.Location = System.Drawing.Point(118, 90)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 2
        # 
        # radioButton1
        # 
        self._radioButton1.Location = System.Drawing.Point(260, 6)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(104, 24)
        self._radioButton1.TabIndex = 3
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "+"
        self._radioButton1.UseVisualStyleBackColor = True
        # 
        # radioButton2
        # 
        self._radioButton2.Location = System.Drawing.Point(332, 6)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(104, 24)
        self._radioButton2.TabIndex = 4
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "-"
        self._radioButton2.UseVisualStyleBackColor = True
        # 
        # radioButton3
        # 
        self._radioButton3.Location = System.Drawing.Point(260, 37)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(104, 24)
        self._radioButton3.TabIndex = 5
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "x"
        self._radioButton3.UseVisualStyleBackColor = True
        # 
        # radioButton4
        # 
        self._radioButton4.Location = System.Drawing.Point(332, 31)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(104, 36)
        self._radioButton4.TabIndex = 7
        self._radioButton4.TabStop = True
        self._radioButton4.Text = "**"
        self._radioButton4.UseVisualStyleBackColor = True
        # 
        # radioButton5
        # 
        self._radioButton5.Location = System.Drawing.Point(260, 69)
        self._radioButton5.Name = "radioButton5"
        self._radioButton5.Size = System.Drawing.Size(104, 24)
        self._radioButton5.TabIndex = 8
        self._radioButton5.TabStop = True
        self._radioButton5.Text = "/"
        self._radioButton5.UseVisualStyleBackColor = True
        # 
        # radioButton6
        # 
        self._radioButton6.Location = System.Drawing.Point(332, 66)
        self._radioButton6.Name = "radioButton6"
        self._radioButton6.Size = System.Drawing.Size(143, 31)
        self._radioButton6.TabIndex = 9
        self._radioButton6.TabStop = True
        self._radioButton6.Text = "//"
        self._radioButton6.UseVisualStyleBackColor = True
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(66, 116)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(74, 33)
        self._button1.TabIndex = 10
        self._button1.Text = "Solve"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(146, 116)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(74, 33)
        self._button2.TabIndex = 11
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(226, 116)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(74, 33)
        self._button3.TabIndex = 12
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(12, 9)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 13
        self._label2.Text = "1st num:"
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(12, 55)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(101, 23)
        self._label3.TabIndex = 14
        self._label3.Text = "2nd num:"
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(23, 90)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(89, 23)
        self._label4.TabIndex = 15
        self._label4.Text = "Answer:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.AppWorkspace
        self.ClientSize = System.Drawing.Size(389, 174)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._radioButton6)
        self.Controls.Add(self._radioButton5)
        self.Controls.Add(self._radioButton4)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "pg140"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        num1 = float(self._textBox1.Text)
        num2 = float(self._textBox2.Text)
        equal = 0
        if self._radioButton1.Checked == True:
            equal = num1 + num2
        elif self._radioButton2.Checked:
            equal = num1 - num2
        elif self._radioButton3.Checked:
            equal = num1 * num2
        elif self._radioButton4.Checked:
            equal = num1 ** num2
        elif self._radioButton5.Checked:
            equal = num1 / num2
        elif self._radioButton6.Checked:
            equal = num1 // num2
        self._label1.Text = str(equal)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()