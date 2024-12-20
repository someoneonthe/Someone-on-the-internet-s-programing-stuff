import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.R = System.Random()
        self.ballup = 0
        self.balld = 0
        self.flagleft = False
        self.flagright = False
        self._eh == 0
    
    def InitializeComponent(self):
        self._components = System.ComponentModel.Container()
        resources = System.Resources.ResourceManager("PONG.MainForm", System.Reflection.Assembly.GetEntryAssembly())
        self._lbltitle = System.Windows.Forms.Label()
        self._leftscore = System.Windows.Forms.Label()
        self._rightscore = System.Windows.Forms.Label()
        self._lblball = System.Windows.Forms.Label()
        self._lblleft = System.Windows.Forms.Label()
        self._lblright = System.Windows.Forms.Label()
        self._timerdummy = System.Windows.Forms.Timer(self._components)
        self._timerright = System.Windows.Forms.Timer(self._components)
        self._timerleft = System.Windows.Forms.Timer(self._components)
        self._timerball = System.Windows.Forms.Timer(self._components)
        self._timermulti = System.Windows.Forms.Timer(self._components)
        self._timerboolean = System.Windows.Forms.Timer(self._components)
        self._pictureBox1 = System.Windows.Forms.PictureBox()
        self._eh = System.Windows.Forms.Label()
        self._pictureBox1.BeginInit()
        self.SuspendLayout()
        # 
        # lbltitle
        # 
        self._lbltitle.BackColor = System.Drawing.Color.Black
        self._lbltitle.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._lbltitle.ForeColor = System.Drawing.Color.Transparent
        self._lbltitle.Location = System.Drawing.Point(12, 25)
        self._lbltitle.Name = "lbltitle"
        self._lbltitle.Size = System.Drawing.Size(958, 52)
        self._lbltitle.TabIndex = 0
        self._lbltitle.Text = "Press Enter to start or M to start multiplayer Q to exit"
        self._lbltitle.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # leftscore
        # 
        self._leftscore.BackColor = System.Drawing.Color.Black
        self._leftscore.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._leftscore.ForeColor = System.Drawing.Color.Transparent
        self._leftscore.Location = System.Drawing.Point(78, 96)
        self._leftscore.Name = "leftscore"
        self._leftscore.Size = System.Drawing.Size(166, 109)
        self._leftscore.TabIndex = 1
        self._leftscore.Text = "0"
        self._leftscore.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # rightscore
        # 
        self._rightscore.BackColor = System.Drawing.Color.Black
        self._rightscore.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._rightscore.ForeColor = System.Drawing.Color.Transparent
        self._rightscore.Location = System.Drawing.Point(794, 96)
        self._rightscore.Name = "rightscore"
        self._rightscore.Size = System.Drawing.Size(166, 109)
        self._rightscore.TabIndex = 2
        self._rightscore.Text = "0"
        self._rightscore.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # lblball
        # 
        self._lblball.BackColor = System.Drawing.Color.White
        self._lblball.Location = System.Drawing.Point(479, 304)
        self._lblball.Name = "lblball"
        self._lblball.Size = System.Drawing.Size(20, 20)
        self._lblball.TabIndex = 3
        self._lblball.Click += self.LblballClick
        # 
        # lblleft
        # 
        self._lblleft.BackColor = System.Drawing.Color.White
        self._lblleft.Location = System.Drawing.Point(12, 246)
        self._lblleft.Name = "lblleft"
        self._lblleft.Size = System.Drawing.Size(20, 100)
        self._lblleft.TabIndex = 4
        # 
        # lblright
        # 
        self._lblright.BackColor = System.Drawing.Color.White
        self._lblright.Location = System.Drawing.Point(950, 246)
        self._lblright.Name = "lblright"
        self._lblright.Size = System.Drawing.Size(20, 100)
        self._lblright.TabIndex = 5
        # 
        # timerright
        # 
        self._timerright.Interval = 20
        self._timerright.Tick += self.TimerrightTick
        # 
        # timerleft
        # 
        self._timerleft.Interval = 20
        self._timerleft.Tick += self.TimerleftTick
        # 
        # timerball
        # 
        self._timerball.Interval = 20
        self._timerball.Tick += self.TimerballTick
        # 
        # timermulti
        # 
        self._timermulti.Interval = 20
        # 
        # timerboolean
        # 
        self._timerboolean.Interval = 20
        # 
        # pictureBox1
        # 
        self._pictureBox1.BackgroundImage = resources.GetObject("pictureBox1.BackgroundImage")
        self._pictureBox1.Location = System.Drawing.Point(78, 208)
        self._pictureBox1.Name = "pictureBox1"
        self._pictureBox1.Size = System.Drawing.Size(790, 371)
        self._pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
        self._pictureBox1.TabIndex = 6
        self._pictureBox1.TabStop = False
        self._pictureBox1.Visible = False
        # 
        # eh
        # 
        self._eh.Location = System.Drawing.Point(12, 25)
        self._eh.Name = "eh"
        self._eh.Size = System.Drawing.Size(100, 23)
        self._eh.TabIndex = 7
        self._eh.Text = "label1"
        self._eh.Visible = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Black
        self.ClientSize = System.Drawing.Size(988, 607)
        self.Controls.Add(self._eh)
        self.Controls.Add(self._lblright)
        self.Controls.Add(self._lblleft)
        self.Controls.Add(self._lblball)
        self.Controls.Add(self._rightscore)
        self.Controls.Add(self._leftscore)
        self.Controls.Add(self._lbltitle)
        self.Controls.Add(self._pictureBox1)
        self.Name = "MainForm"
        self.Text = "PONG"
        self.Load += self.MainFormLoad
        self.SizeChanged += self.MainFormSizeChanged
        self.KeyDown += self.MainFormKeyDown
        self._pictureBox1.EndInit()
        self.ResumeLayout(False)

    def TimerballTick(self, sender, e):
        ball = self._lblball
        lpdl = self._lblleft
        rpdl = self._lblright
        rscore = int(self._rightscore.Text)
        lscore = int(self._leftscore.Text)
        ball.Top += self.ballup
        ball.Left += 8 * self.balld
        
        if ball.Right >= rpdl.Right and ball.Bottom >= rpdl.Top and ball.Top <= rpdl.Bottom:
            self.balld = -1
            self.ballup = self.R.Next (-4, 5)
        elif ball.Left <= lpdl.Left and ball.Bottom >= lpdl.Top and ball.Top <= lpdl.Bottom:
            self.balld = 1
            self.ballup = self.R.Next(-4, 5)
       
            
        if ball.Top <= self.Top + 10:
            self.ballup = 1
        elif ball.Top >= self.Height - 50:
            self.ballup = -1
            
        if ball.Top <= 0:
            self.ballup = 1
        elif ball.Top >= self.Height - 50:
            self.ballup = -1
            
        if ball.Location.X <= 0 or \
            (ball.Location.X < lpdl.Left -20 and ball.Location.Y < lpdl.Top):
                rscore += 1
                self._rightscore.Text = str(rscore)
                ball.Left = self.Width // 2
                ball.Top = self.Height // 2
                
                
        if ball.Location.X >= self.Width or \
            (ball.Location.X > rpdl.Right + 20 and ball.Location.Y > rpdl.Top):
                lscore += 1
                self._leftscore.Text = str(lscore)
                ball.Left = self.Width // 2
                ball.Top = self.Height // 2
                
        if lscore == 10:
            self._timerball.Enabled = False
            ball.Left = self.Width // 2
            ball.Top = self.Height // 2
            self.ballup = 0
            self._lbltitle.Text = "Left Player Wins! Press R to restart"
            self._lbltitle.Visible = True
            
        if rscore == 10:
            self._timerball.Enabled = False
            ball.Left = self.Width // 2
            ball.Top = self.Height // 2
            self.ballup = 0
            self._lbltitle.Text = "Right Player Wins! Press R to restart"
            self._lbltitle.Visible = True
            
        if self._timerboolean.Enabled:
                if ball.Top < lpdl.Top - 20:
                    lpdl.Top = lpdl.Top - 3
                elif ball.Top > lpdl.Top + 70:
                    lpdl.Top = lpdl.Top + 3
                    
                if self._eh == 1:
                    if ball.Top < lpdl.Top - 5:
                        lpdl.Top = lpdl.Top - 10
                    elif ball.Top > lpdl.Top + 95:
                        lpdl.Top = lpdl.Top + 10
                
                    
        pass

    def MainFormKeyDown(self, sender, e):
        tball = self._timerball
        tdum = self._timerdummy
        tbool = self._timerboolean
        tmult = self._timermulti
        tleft = self._timerleft
        tright = self._timerright
        bl = self._lblball
        lpdl = self._lblleft
        rpdl = self._lblright
        title = self._lbltitle
        
        def reset():
            title.Visible = True
            title.Text = "Press Enter to Start or M to start Multiplayer"
            self._leftscore.Text = "0"
            self._rightscore.Text = "0"
            tball.Enabled = False
            tdum.Enabled = False
            tbool.Enabled = False
            tmult.Enabled = False
            tleft.Enabled = False
            tright.Enabled = False
            bl.Left = self.Width // 2
            bl.Top = self.Height // 2
            lpdl.Top = (self.Height // 2) - 50 + lpdl.Height
            rpdl.Top = (self.Height // 2) - 50 + rpdl.Height
            """ todo; reset secrets"""
            bl.BackColor = Color.White
            
        if e.KeyCode == Keys.R:
            reset()
            
        if e.KeyCode == Keys.Q:
            Application.Exit()
            
        if e.KeyCode == Keys.H:
            self._eh == 1
            
        if e.KeyCode == Keys.E:
            self._pictureBox1.Visible = True
            
        if e.KeyCode == Keys.Enter:
            tball.Enabled = True
            tdum.Enabled = True
            tbool.Enabled = not tmult.Enabled
            title.Visible = False
        if e.KeyCode == Keys.M:
            reset()
            title.Visible = True
            title.Text = "use W and S to move the left paddle: hit Enter to start"
            tmult.Enabled = True
            
        if tdum.Enabled:
            if e.KeyCode == Keys.Up:
                self.flagright = False
                tright.Enabled = True
            elif e.KeyCode == Keys.Down:
                self.flagright = True
                tright.Enabled = True
            """todo: Finish multiPlayer"""
            if tmult.Enabled and tball.Enabled:
                if e.KeyCode == Keys.W:
                    self.flagleft = False
                    tleft.Enabled = True
                if e.KeyCode == Keys.S:
                    self.flagleft = True
                    tleft.Enabled = True
        pass

    def MainFormLoad(self, sender, e):
        """ todo: add 3 unique Secrets/ cheats"""
        self.balld = 1
        self.ballup = self.R.Next(-4,5)
        
    def pdlTick(self, pdl, flagd, tmr):
        if flagd == True:
            pdl.Top += 5
        else:
            pdl.Top -= 5
        if pdl.Top <= 10 or pdl.Bottom >= self.Height - 50:
            tmr.Enabled = False

    def TimerrightTick(self, sender, e):
        self.pdlTick(self._lblright, self.flagright, self._timerright)
        
    def TimerleftTick(self, sender, e):
        self.pdlTick(self._lblleft, self.flagleft, self._timerleft)

    def LblballClick(self, sender, e):
        self._lblball.BackColor = Color.Red
        self.BackColor = Color.Green

    def MainFormSizeChanged(self, sender, e):
        self._lblright.Left = self.Width - 25 - self._lblright.Width
        self._rightscore.Left = self.Width - 75-self._rightscore.Width
        self._lbltitle.Width = self.Width- 25
        self._lblball.Left = self.Width // 2
        self._lblball.Top = self.Height // 2
