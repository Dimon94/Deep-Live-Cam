"""FFmpeg-based virtual camera UDP streamer."""

from __future__ import annotations

import subprocess
from typing import Optional

import numpy as np


class VirtualCameraOutput:
    """Send BGR frames to FFmpeg and broadcast as UDP MPEG-TS."""

    def __init__(
        self,
        width: int,
        height: int,
        addr: str = "127.0.0.1",
        port: int = 1234,
        fps: int = 30,
    ) -> None:
        self.width = int(width)
        self.height = int(height)
        self.addr = addr
        self.port = int(port)
        self.fps = int(fps)
        self._proc: Optional[subprocess.Popen[bytes]] = None

    def start(self) -> None:
        """Launch the FFmpeg process if not already running."""
        if self._proc is not None:
            return

        args = [
            "ffmpeg",
            "-loglevel",
            "error",
            "-y",
            "-f",
            "rawvideo",
            "-vcodec",
            "rawvideo",
            "-pix_fmt",
            "bgr24",
            "-s",
            f"{self.width}x{self.height}",
            "-r",
            str(self.fps),
            "-i",
            "-",
            "-f",
            "mpegts",
            "-codec:v",
            "mpeg1video",
            "-q:v",
            "2",
            "-bf",
            "0",
            f"udp://{self.addr}:{self.port}",
        ]

        self._proc = subprocess.Popen(
            args,
            stdin=subprocess.PIPE,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            bufsize=0,
        )

    def push_frame(self, frame: np.ndarray) -> None:
        """Write a single BGR frame to FFmpeg stdin."""
        if frame is None:
            return

        if frame.shape[0] != self.height or frame.shape[1] != self.width:
            raise ValueError(
                f"Frame resolution {frame.shape[1]}x{frame.shape[0]} "
                f"does not match configured {self.width}x{self.height}"
            )

        if frame.dtype != np.uint8:
            frame = frame.astype(np.uint8, copy=False)

        if self._proc is None:
            self.start()

        if self._proc is None or self._proc.stdin is None:
            return

        try:
            self._proc.stdin.write(frame.tobytes())
        except (BrokenPipeError, OSError):
            self.stop()
            self.start()
            if self._proc and self._proc.stdin:
                self._proc.stdin.write(frame.tobytes())

    def stop(self) -> None:
        """Terminate FFmpeg process."""
        if self._proc is None:
            return

        try:
            if self._proc.stdin:
                self._proc.stdin.close()
            self._proc.terminate()
            self._proc.wait(timeout=2)
        except Exception:
            if self._proc:
                self._proc.kill()
        finally:
            self._proc = None

    def __del__(self) -> None:
        self.stop()

