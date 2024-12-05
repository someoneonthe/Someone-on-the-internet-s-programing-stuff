import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._listBox1 = System.Windows.Forms.ListBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self._button4 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(3, 115)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(59, 41)
        self._button1.TabIndex = 0
        self._button1.Text = "See"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(146, 6)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(187, 31)
        self._textBox1.TabIndex = 1
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(146, 43)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(187, 31)
        self._textBox2.TabIndex = 2
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.SystemColors.Info
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 25
        self._listBox1.Location = System.Drawing.Point(146, 80)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(187, 29)
        self._listBox1.TabIndex = 3
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(128, 23)
        self._label1.TabIndex = 4
        self._label1.Text = "First Name:"
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(13, 46)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(127, 23)
        self._label2.TabIndex = 5
        self._label2.Text = "Last Name:"
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(68, 115)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(77, 41)
        self._button2.TabIndex = 6
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(151, 115)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(59, 41)
        self._button3.TabIndex = 7
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(12, 80)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(115, 23)
        self._label3.TabIndex = 8
        self._label3.Text = "Full Name:"
        # 
        # button4
        # 
        self._button4.Location = System.Drawing.Point(216, 115)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(41, 41)
        self._button4.TabIndex = 9
        self._button4.Text = "E"
        self._button4.UseVisualStyleBackColor = True
        self._button4.Click += self.Button4Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LightGray
        self.ClientSize = System.Drawing.Size(345, 167)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "pg 119"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        FirstName = self._textBox1.Text
        LastName = self._textBox2.Text
        for num in range(0,1):
            line = str(FirstName) + "\t" + str(LastName)
            self._listBox1.Items.Add(line)

    def Button4Click(self, sender, e):
        MessageBox.Show("This is a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains a bucket. Dear God. There is more. NO! It contains Nothing. Ok!")

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()