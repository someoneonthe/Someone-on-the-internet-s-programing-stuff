import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self._button6 = System.Windows.Forms.Button()
        self._button7 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(13, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(873, 253)
        self._label1.TabIndex = 0
        self._label1.Text = "label1"
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(12, 269)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(180, 69)
        self._button1.TabIndex = 1
        self._button1.Text = "Noodles & company"
        self._button1.UseVisualStyleBackColor = True
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(254, 269)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(180, 69)
        self._button2.TabIndex = 2
        self._button2.Text = "Target"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(484, 269)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(180, 69)
        self._button3.TabIndex = 3
        self._button3.Text = "button3"
        self._button3.UseVisualStyleBackColor = True
        # 
        # button4
        # 
        self._button4.Location = System.Drawing.Point(706, 269)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(180, 69)
        self._button4.TabIndex = 4
        self._button4.Text = "button4"
        self._button4.UseVisualStyleBackColor = True
        # 
        # button5
        # 
        self._button5.Location = System.Drawing.Point(137, 344)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(180, 69)
        self._button5.TabIndex = 5
        self._button5.Text = "button5"
        self._button5.UseVisualStyleBackColor = True
        # 
        # button6
        # 
        self._button6.Location = System.Drawing.Point(368, 344)
        self._button6.Name = "button6"
        self._button6.Size = System.Drawing.Size(180, 69)
        self._button6.TabIndex = 6
        self._button6.Text = "button6"
        self._button6.UseVisualStyleBackColor = True
        # 
        # button7
        # 
        self._button7.Location = System.Drawing.Point(598, 344)
        self._button7.Name = "button7"
        self._button7.Size = System.Drawing.Size(180, 69)
        self._button7.TabIndex = 7
        self._button7.Text = "button7"
        self._button7.UseVisualStyleBackColor = True
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(909, 446)
        self.Controls.Add(self._button7)
        self.Controls.Add(self._button6)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "phone numbers"
        self.ResumeLayout(False)

