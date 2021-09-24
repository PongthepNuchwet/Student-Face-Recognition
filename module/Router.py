from module.startFrame import startFrame
from module.Register_view import Register_view
from module.FaceRecognition_view import FaceRecognition_view
from module.About_view import About_view


class Router:

    def __init__(self, windows, container) -> None:
        self.Frames = {}
        for F in (startFrame, Register_view, FaceRecognition_view, About_view):
            frame = F(windows, container)
            self.Frames[str(type(frame).__name__)] = frame

    def GoTo(self, frame):
        print(f"[Debug] Go to {frame}")
        tmp = self.Frames[frame]
        tmp.grid(row=0, column=0, sticky="nsew")
        tmp.tkraise()
