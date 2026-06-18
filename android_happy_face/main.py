from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line, Arc
from kivy.animation import Animation
from kivy.clock import Clock


class HappyFaceWidget(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._bob_offset = 0
        self.bind(size=self._redraw, pos=self._redraw)
        Clock.schedule_interval(self._animate, 1 / 60)
        self._tick = 0

    def _animate(self, dt):
        import math
        self._tick += 1
        self._bob_offset = 6 * math.sin(self._tick * 0.05)
        self._redraw()

    def _redraw(self, *args):
        self.canvas.clear()
        w, h = self.size
        cx = w / 2
        cy = h / 2 + self._bob_offset
        r = min(w, h) * 0.35          # face radius

        with self.canvas:
            # --- Background ---
            Color(1, 0.87, 0.39)       # sunny yellow
            Ellipse(pos=(0, 0), size=(w, h))  # fills whole widget

            # --- Face fill ---
            Color(1, 0.86, 0.2)
            Ellipse(pos=(cx - r, cy - r), size=(2 * r, 2 * r))

            # --- Face outline ---
            Color(0.78, 0.59, 0)
            Line(circle=(cx, cy, r), width=3)

            # --- Eyes ---
            eye_ox = r * 0.33
            eye_oy = r * 0.2
            eye_r  = r * 0.1
            Color(0.2, 0.12, 0.04)
            # left eye
            Ellipse(pos=(cx - eye_ox - eye_r, cy + eye_oy - eye_r),
                    size=(eye_r * 2, eye_r * 2))
            # right eye
            Ellipse(pos=(cx + eye_ox - eye_r, cy + eye_oy - eye_r),
                    size=(eye_r * 2, eye_r * 2))

            # --- Smile ---
            Color(0.7, 0.31, 0)
            # Draw smile as an arc (bottom half of an ellipse)
            smile_r = r * 0.5
            Line(
                ellipse=(cx - smile_r, cy - r * 0.45, smile_r * 2, smile_r, 200, 340),
                width=3
            )

            # --- Rosy cheeks ---
            Color(1, 0.63, 0.51, 0.5)
            cheek_w = r * 0.45
            cheek_h = r * 0.22
            cheek_y = cy - r * 0.05
            # left cheek
            Ellipse(pos=(cx - eye_ox - cheek_w * 0.9, cheek_y - cheek_h / 2),
                    size=(cheek_w, cheek_h))
            # right cheek
            Ellipse(pos=(cx + eye_ox - cheek_w * 0.1, cheek_y - cheek_h / 2),
                    size=(cheek_w, cheek_h))


class HappyFaceApp(App):
    def build(self):
        self.title = "Happy Face"
        return HappyFaceWidget()


if __name__ == "__main__":
    HappyFaceApp().run()
