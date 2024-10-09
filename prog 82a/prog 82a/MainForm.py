import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(159, 13)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 31)
        self._textBox1.TabIndex = 0
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(13, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(122, 23)
        self._label1.TabIndex = 1
        self._label1.Text = "your speed"
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(13, 83)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 2
        self._label2.Text = "Ticket"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.Window
        self._label3.Location = System.Drawing.Point(107, 82)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 3
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(11, 233)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(124, 56)
        self._button1.TabIndex = 4
        self._button1.Text = "calcuate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(137, 233)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(103, 56)
        self._button2.TabIndex = 5
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(20, 157)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(220, 23)
        self._label4.TabIndex = 6
        self._label4.Text = "Note the speed limit is 30"
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(274, 315)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "prog 82a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        a = int(self._textBox1.Text)
        b = a - 30
        c = 20 + (b * 5)
        self._label3.Text = str(c)

    def Button2Click(self, sender, e):
        Application.Exit()