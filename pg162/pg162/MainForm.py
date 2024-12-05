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
        self._button1 = System.Windows.Forms.Button()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(12, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 31)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(12, 49)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 31)
        self._textBox2.TabIndex = 1
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(3, 274)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(118, 35)
        self._button1.TabIndex = 2
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(207, 11)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(100, 31)
        self._textBox3.TabIndex = 3
        # 
        # textBox4
        # 
        self._textBox4.Location = System.Drawing.Point(207, 48)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(100, 31)
        self._textBox4.TabIndex = 4
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.Info
        self._label1.Location = System.Drawing.Point(150, 119)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(147, 26)
        self._label1.TabIndex = 5
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.Info
        self._label2.Location = System.Drawing.Point(197, 145)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 29)
        self._label2.TabIndex = 6
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.Info
        self._label3.Location = System.Drawing.Point(107, 171)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(190, 23)
        self._label3.TabIndex = 7
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.Info
        self._label4.Location = System.Drawing.Point(53, 194)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(244, 23)
        self._label4.TabIndex = 8
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.Info
        self._label5.Location = System.Drawing.Point(69, 217)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(228, 23)
        self._label5.TabIndex = 9
        # 
        # textBox5
        # 
        self._textBox5.Location = System.Drawing.Point(207, 85)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(100, 31)
        self._textBox5.TabIndex = 10
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(127, 274)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(106, 37)
        self._button2.TabIndex = 11
        self._button2.Text = "Erase"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(243, 272)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(106, 39)
        self._button3.TabIndex = 12
        self._button3.Text = "Quit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.Info
        self._label6.Location = System.Drawing.Point(3, 119)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(150, 26)
        self._label6.TabIndex = 13
        self._label6.Text = "room charges:"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.SystemColors.Info
        self._label7.Location = System.Drawing.Point(3, 145)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(198, 29)
        self._label7.TabIndex = 14
        self._label7.Text = "additional charges:"
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.SystemColors.Info
        self._label8.Location = System.Drawing.Point(3, 171)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(109, 23)
        self._label8.TabIndex = 15
        self._label8.Text = "sub Total:"
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.SystemColors.Info
        self._label9.Location = System.Drawing.Point(3, 194)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(54, 23)
        self._label9.TabIndex = 16
        self._label9.Text = "Tax:"
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.SystemColors.Info
        self._label10.Location = System.Drawing.Point(3, 217)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(69, 23)
        self._label10.TabIndex = 17
        self._label10.Text = "Total:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.Menu
        self.ClientSize = System.Drawing.Size(361, 320)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._textBox5)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "pg162"
        self.ResumeLayout(False)
        self.PerformLayout()



    def Button1Click(self, sender, e):
        nights = float(self._textBox1.Text)
        price = float(self._textBox2.Text)
        roomService = float(self._textBox3.Text)
        Telephone = float(self._textBox4.Text)
        misc = float(self._textBox5.Text)
        roomCharges = nights * price
        addCharges = roomService + Telephone + misc
        subTotal = roomCharges + addCharges
        Tax = subTotal * 0.08
        total = subTotal + Tax
        self._label1.Text = str(roomCharges)
        self._label2.Text = str(addCharges)
        self._label3.Text = str(subTotal)
        self._label4.Text = str(Tax)
        self._label5.Text = str(total)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._textBox5.Text = ""
        self._label1.Text = ""
        self._label2.Text = ""
        self._label3.Text = ""
        self._label4.Text = ""
        self._label5.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def Label6Click(self, sender, e):
        pass