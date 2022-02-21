# Pygame-Pong
Two Player Pong Game made from Python library Pygame

## Library: Pygame
The Pygame library offered the GUI features for the Pong game such as creating a window, the ball, and the two paddles.

![pygame-pong](https://user-images.githubusercontent.com/54753472/154873465-91c4f5f2-796f-407b-879f-7f372577aadc.png)

## How It Works

Well game itself can be controlled by two people or one person using both player keys. The left paddle is controlled by ```W``` and ```S```.
The right paddle is controlled by ```Up``` and ```Down```.

When the game starts the ball will move to right at a fixed velocity set in the ```Ball Class``` in ```ball.py```.
The max velocity of the ball in this program is ```MAX_VEL = 5```.

## Paddle Creation
Below is the creation of the paddles

![pygame-pong-paddle-creation](https://user-images.githubusercontent.com/54753472/154876902-0c7fd015-75c3-493c-bd22-ea6d7ba7dbb8.png)

### Left Paddle
The left paddle creation logic is that the paddle must be created slightly above the center of the window height.

```left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)```


### Right Paddle
The right paddle creation follows the similar logic to the left paddle. Just have to make sure that the ```x-coordinate``` is correct.

```right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)```

## Handling Collisions

### Ceiling Collision
![pong-ceiling-collision](https://user-images.githubusercontent.com/54753472/154878754-e0b83bc9-a22e-47e8-800a-144e2b2114a7.png)

The logic is pretty simple as we need to make sure the trajectory of the ball will be bounced off to the exact
same angle that it hit the wall at. For both ```x``` and ```y``` directions.

For the ceiling we need to make sure to change the direction of the ```y velocity```. Upwards is ```negative``` and downwards is ```positive``` in ```y-coordinate```.

### Paddle Collision
For Paddle Collision, we have to move the ball based on the displacement from the center of the paddle. 
The further away from the center it is, the higher the angle it's gonna bounce off from.

![pong-paddle-collision](https://user-images.githubusercontent.com/54753472/154881695-62bcd61c-5bc3-401d-9540-43bed524f392.png)

Then we need to figure out the velocity when the ball hits the paddle. What we need to do is make it so when the ball is at 
the maximum possible displacement it bounces off with the maximum velocity ```MAX_VEL = 5```. 
So when the ball hits the very edge of the paddle, thats where it gets the ```maximum velocity of 5```.

The displacement divided by some value gives us ```5``` when the ball is at the maximum possible displacement value. When the ball is not
at the maximum displacement value, it gives us a max velocity value ```less than 5```. As it gets closer to the middle of the paddle,
it gives a smaller value that should reach ```0```. Therefore the range is ```0 to 5```.

![pong-collision-ball-velocity-paddle](https://user-images.githubusercontent.com/54753472/154884722-c6ed83c2-1c20-457f-8488-8e8dc1e1f439.png)
