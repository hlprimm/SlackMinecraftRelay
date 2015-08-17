import sys
import time


now = time.time()


chathistory = []
RELAY_WAIT = .5 #seconds to wait before checking for new messages from Slack
a = 1

class SlackRelay:
    def __init__(self, ploader, settings):
        print('relay loaded')
        self.timers = ploader.requires('Timers')
        self.net = ploader.requires('Net')
        self.timers.reg_event_timer(RELAY_WAIT, self.SlackRelayer)
       
    def SlackRelayer(self):
       global a
       global now
       if int(time.time() - now) > 10:
          if a == 1:
             self.emit_chat_message(msg='/gchat YOURGROUP')
             a = a + 1
          newline = self.Tail()
          if newline not in chathistory:
             chathistory.append(newline)
             if len(newline) < 100:
                self.emit_chat_message(msg=str(newline))
                print newline

#to find the last line in text file
    def Tail(filepath, read_size=1024):
       f = open('slacktomc.txt', 'rU')    # U is to open it with Universal newline support
       offset = read_size
       f.seek(0, 2)
       file_size = f.tell()
       while 1:
          if file_size < offset:
             offset = file_size
          f.seek(-1*offset, 2)
          read_str = f.read(offset)
          # Remove newline at the end
          if read_str[-1] == '\n':
             read_str = read_str[0:-1]
          lines = read_str.split('\n')
          if len(lines) > 1:  # Got a line
             return lines[len(lines) - 1]
          if offset == file_size:   # Reached the beginning
             return read_str
          offset += read_size
       f.close()

    def emit_chat_message(self, msg):
        """Helper method that sends chat messages or chat commands"""
        print('msg: {0}'.format(msg))
        self.net.push_packet('PLAY>Chat Message', {'message': msg})

