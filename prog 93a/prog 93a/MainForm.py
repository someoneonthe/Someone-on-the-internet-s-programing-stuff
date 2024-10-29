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
        self._button1 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(13, 13)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 31)
        self._textBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(13, 254)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(114, 46)
        self._button1.TabIndex = 2
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label2.Location = System.Drawing.Point(140, 205)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 3
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label3.Location = System.Drawing.Point(13, 173)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(114, 23)
        self._label3.TabIndex = 4
        self._label3.Text = "total"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label4.Location = System.Drawing.Point(12, 205)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(115, 23)
        self._label4.TabIndex = 5
        self._label4.Text = "if late"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label5.Location = System.Drawing.Point(140, 58)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(100, 23)
        self._label5.TabIndex = 6
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label6.Location = System.Drawing.Point(140, 89)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 23)
        self._label6.TabIndex = 7
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label7.Location = System.Drawing.Point(140, 117)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(100, 23)
        self._label7.TabIndex = 8
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label8.Location = System.Drawing.Point(13, 58)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(114, 23)
        self._label8.TabIndex = 9
        self._label8.Text = "base rate"
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label9.Location = System.Drawing.Point(12, 85)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(115, 27)
        self._label9.TabIndex = 10
        self._label9.Text = "surcharge"
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label10.Location = System.Drawing.Point(13, 117)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(114, 23)
        self._label10.TabIndex = 11
        self._label10.Text = "cite"
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(140, 254)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(100, 46)
        self._button2.TabIndex = 12
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(13, 307)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(227, 56)
        self._button3.TabIndex = 13
        self._button3.Text = "Quit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.Location = System.Drawing.Point(247, 360)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(10, 10)
        self._button4.TabIndex = 14
        self._button4.Text = "button4"
        self._button4.UseVisualStyleBackColor = True
        self._button4.Click += self.Button4Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label1.Location = System.Drawing.Point(140, 173)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 15
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.AppWorkspace
        self.ClientSize = System.Drawing.Size(262, 375)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "prog 93a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        wattsused = float(self._textBox1.Text)
        used = round(wattsused * 0.0475 , 2)
        surcharge = round(used * 0.1 , 2)
        city = round(used * 0.03 , 2)
        total = round(used + surcharge + city , 2)
        late = total * 0.04
        total2 = round(total + late , 2)
        self._label1.Text = str(total)
        self._label2.Text = str(total2)
        self._label5.Text = str(used)
        self._label6.Text = str(surcharge)
        self._label7.Text = str(city)

    def Button4Click(self, sender, e):
        self._button3.Text = "Exit the Application"

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        self._label2.Text = ""
        self._label5.Text = ""
        self._label6.Text = ""
        self._label7.Text = ""