from time import sleep
from queue import Queue


class MediaQueue(Queue):
    def play(self):
        if self.is_empty():
            return
        else:
            i = self.dequeue()
            print(f"Now playing {i}")
            sleep(len(i))
            self.play()


mq = MediaQueue()
track = ["Wanaona gere", "Baba lao", "Tuwache Mihadarati", "Tuheshimu ndoa"]

for i in track:
    mq.enqueue(i)

mq.play()
