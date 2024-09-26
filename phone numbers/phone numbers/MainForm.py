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
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(13, 270)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(147, 68)
        self._button1.TabIndex = 1
        self._button1.Text = "show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(397, 270)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(145, 68)
        self._button2.TabIndex = 2
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(750, 269)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(147, 68)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(12, 35)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(885, 31)
        self._textBox1.TabIndex = 4
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(12, 73)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(885, 31)
        self._textBox2.TabIndex = 5
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveBorder
        self.ClientSize = System.Drawing.Size(909, 446)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "phone numbers"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        self._textBox1.Text = "Noodles & company - 608 756 9700 , Target - 608 754 8331 , Game Stop - 08 758 9337"
        self._textBox2.Text = "olive Garden - 608 758 2848 , Walmart - 608 754 7800"
        
    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()