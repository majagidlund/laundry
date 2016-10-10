from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, Clock
from kivy.vector import Vector

class PongGame(Widget):

    def update(self, dt):
        pass

class PongApp(App):
    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


class PongBall(Widget):

    ### velocity of the ball
    velocity_x= NumericProperty(0)
    velocity_y= NumericProperty(0)

    velocity= ReferenceListProperty(velocity_x,velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity)+self.pos



if __name__ == '__main__':
    PongApp().run()

