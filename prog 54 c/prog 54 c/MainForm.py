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
        self._button1 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(124, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 31)
        self._textBox1.TabIndex = 0
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(124, 88)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 1
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(124, 111)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 2
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(12, 169)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(126, 58)
        self._button1.TabIndex = 3
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(12, 15)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 28)
        self._label3.TabIndex = 4
        self._label3.Text = "radius"
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(18, 88)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 23)
        self._label4.TabIndex = 5
        self._label4.Text = "perimiter"
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(60, 111)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(58, 23)
        self._label5.TabIndex = 6
        self._label5.Text = "area"
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(145, 169)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(103, 58)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(184, 385)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(64, 52)
        self._button3.TabIndex = 8
        self._button3.Text = "The Cake is a lie"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.Location = System.Drawing.Point(12, 233)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(236, 57)
        self._button4.TabIndex = 9
        self._button4.Text = "Exit"
        self._button4.UseVisualStyleBackColor = True
        self._button4.Click += self.Button4Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(260, 449)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "prog 54 c"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        Radius = int(self._textBox1.Text)
        TheCakeIsALie = (22 / 7)
        Perimiter = (2 * TheCakeIsALie * Radius ** 2)
        Area = (TheCakeIsALie * Radius ** 2)
        self._label1.Text = str(Perimiter)
        self._label2.Text = str(Area)

    def Button3Click(self, sender, e):
        self._button1.Text = "The part where he"
        self._button2.Text = "kills you"
        self._button3.Text = "PotaDOS"
        self._button4.Text = "The Secret of the Borealis"
        # the world will never know

    def Button4Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        self._label2.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""