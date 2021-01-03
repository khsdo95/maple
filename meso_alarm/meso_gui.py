import Tkinter as tk
import winsound
import time

TTS = True

class ExampleApp(tk.Tk):
  def __init__(self):
    tk.Tk.__init__(self)
    self.label = tk.Label(self, text="", width=20)
    self.label.pack()
    self.total = 0
    self.cycle = 0
    self.geometry("+2405+0")
    self.countdown(2*60*60)

  def countdown(self, remaining = None):
    if remaining is not None:
      self.total = remaining

    if self.cycle <= 0:
      self.play('meso.wav')
      self.cycle = 110

    if self.total % 1800 <= 0:
      self.play('rich.wav')
    
    cycle_s = self.cycle % 60
    cycle_m = self.cycle / 60

    h = self.total / 3600
    m = (self.total - h*3600) / 60
    s = self.total % 60
    
    line1 = "%d h %d m %d s"
    line2 = "%d m %d sec"
    text = (line1 + "\n" + line2) % tuple(map(int, (h, m, s, cycle_m, cycle_s)))

    self.label.configure(text=text)
    self.total = self.total - 1
    self.cycle = self.cycle - 1
    self.after(1000, self.countdown)

  def play(self, fname):
    if fname == 'meso.wav':
      if TTS:
        winsound.PlaySound(fname, winsound.SND_FILENAME)
      else:
        winsound.Beep(1000, 1000)
    
    if fname == 'rich.wav':
      if TTS:
        winsound.PlaySound(fname, winsound.SND_FILENAME)
      else:
        winsound.Beep(1000, 100)
        time.sleep(0.1)
        winsound.Beep(1000, 100)
        time.sleep(0.1)
        winsound.Beep(1000, 100)

if __name__ == "__main__":
  app = ExampleApp()
  app.mainloop()
