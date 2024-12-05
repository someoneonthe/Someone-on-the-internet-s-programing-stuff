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
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(14, 209)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(119, 64)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.SystemColors.ControlLightLight
        self._textBox1.Location = System.Drawing.Point(13, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(370, 31)
        self._textBox1.TabIndex = 1
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.SystemColors.ControlLightLight
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 25
        self._listBox1.Location = System.Drawing.Point(14, 49)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(369, 154)
        self._listBox1.TabIndex = 2
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Location = System.Drawing.Point(139, 209)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(119, 64)
        self._button2.TabIndex = 3
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ControlLightLight
        self._button3.Location = System.Drawing.Point(264, 209)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(119, 64)
        self._button3.TabIndex = 4
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(402, 286)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "prog 122b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        
        hours = int(self._textBox1.Text)
        hour = 1
        for time in range(0, hours):
            pay = hour * 4
            line = str(hour) + "\t\t" + str(pay)
            self._listBox1.Items.Add(line)
            hour = hour + 1

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()