﻿import System.Drawing
import System.Windows.Forms
import math

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(13, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "price"
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(120, 13)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 31)
        self._textBox1.TabIndex = 1
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(12, 62)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 31)
        self._label2.TabIndex = 2
        self._label2.Text = "givin"
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(119, 62)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 31)
        self._textBox2.TabIndex = 3
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(257, 112)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(126, 72)
        self._button1.TabIndex = 4
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(12, 136)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 5
        self._label3.Text = "label3"
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(12, 179)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 23)
        self._label4.TabIndex = 6
        self._label4.Text = "label4"
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(12, 226)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(100, 23)
        self._label5.TabIndex = 7
        self._label5.Text = "label5"
        # 
        # label6
        # 
        self._label6.Location = System.Drawing.Point(12, 268)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 23)
        self._label6.TabIndex = 8
        self._label6.Text = "label6"
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(499, 451)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "prog 58t"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        price = float(self._textBox1.Text)
        recived = float(self._textBox2.Text)
        giveback = recived - price
        dollars = int(recived - price)
        quarters = giveback - dollars
        aq = round((quarters/ 25) * 100)
        mq = (aq*25) / 100
        dimes = giveback - dollars - mq
        ad = round((dimes * 100) / 10)
        md = (ad *10) /100
        nickles = giveback - dollars - mq - md
        an = round((nickles * 100) / 5)
        self._label3.Text = str(dollars)
        self._label4.Text = str(aq)
        self._label5.Text = str(ad)
        self._label6.Text = str(an)