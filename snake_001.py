import curses
from random import randrange


def main_snake(stdscr):
    # set cursor invisible
    curses.curs_set(0)
    # set refreshing interval (to avoid waiting keypress in getch())
    curses.halfdelay(1)

    key_pressed = 0
    height, width = stdscr.getmaxyx()

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # set color pairs (id, font color, bg color)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)

    # dict with coordinate increments for all directions: if 'down' then (y + 1, x + 0)...
    directional_increments_yx = {'down': (1, 0), 'up': (-1, 0),
                                 'right': (0, 1), 'left': (0, -1)}
    # initial direction. Let it be 'right' for now
    direction = 'right'

    # initialize the snake
    init_x = width // 2
    init_y = height // 2
    init_len = 5
    snake = [(init_y, init_x - i) for i in range(init_len)]

    # apple (assume the target point is an apple! %)) location. It shouldn't appear on the snake
    while True:
        apple = (randrange(1, height - 2), randrange(1, width - 1))
        if apple not in snake:
            break

    while True:

        stdscr.clear()
        stdscr.refresh()
        # changing direction if the key was pressed
        if key_pressed == curses.KEY_DOWN:
            if direction == 'up':
                # if the snake goes down and a user've got pressed 'up' button, it just flips itself, like a worm
                snake.reverse()
            direction = 'down'
        elif key_pressed == curses.KEY_UP:
            if direction == 'down':
                snake.reverse()
            direction = 'up'
        elif key_pressed == curses.KEY_RIGHT:
            if direction == 'left':
                snake.reverse()
            direction = 'right'
        elif key_pressed == curses.KEY_LEFT:
            if direction == 'right':
                snake.reverse()
            direction = 'left'

        # time to update snake respect to moving direction. -1 in y coord because of status bar
        # that would be drawn later at the very bottom of the screen.
        # The screen is looped. I hated unlooped screen when I was child...
        snake.insert(0, ((snake[0][0] + directional_increments_yx[direction][0]) % (height - 1),
                         (snake[0][1] + directional_increments_yx[direction][1]) % width))

        # if snake's head eats its body, it means that after update the head_point_tuple
        # is in snake_list at least 2 times
        if snake.count(snake[0]) > 1:
            # the snake is dead because of eating itself. So the user can choose either to play again or to quit
            while key_pressed not in (ord('y'), ord('n')):
                title = "You've eaten yourself! You're dead! Try again? [y / n]"[:width - 1]
                start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
                start_y = int((height // 2) - 2)
                stdscr.addstr(start_y, start_x_title, title)
                stdscr.refresh()
                key_pressed = stdscr.getch()
            # if 'yes' (to play), the snake is born again as new list, direction is 'right' and new apple appears
            if key_pressed == ord('y'):
                snake = [(init_y, init_x - i) for i in range(init_len + 1)]
                # +1 because of snake.pop(-1) in the next block. It will eat 1 star
                direction = 'right'
                apple = (randrange(1, height - 1), randrange(1, width - 1))
            else:
                break
        # if snake is just at screen and it's eating apple it just moves.
        #  snake's head is in apple's coords, snake grows (the last tail point_tuple is not to be deleted)
        #  and new apple appears
        if snake[0] != apple:
            snake.pop(-1)
        else:
            while True:
                apple = (randrange(1, height - 2), randrange(1, width - 1))
                if apple not in snake:
                    break

        # draw the snake by its coords_list
        for koords in snake:
            stdscr.addstr(*koords, '*', curses.color_pair(1))

        # draw the apple
        stdscr.addstr(*apple, '@', curses.color_pair(2))

        # draw the status bar
        statusbarstr = "Press 'q' to exit | SCORE: {} | POS: {}, {}".format((len(snake) - init_len) * 5,
                                                                            snake[0][0], snake[0][1])
        stdscr.addstr(height-1, 0, statusbarstr, curses.color_pair(3))

        stdscr.refresh()
        # Wait for next input
        key_pressed = stdscr.getch()
        # if user pressed q to quit
        if key_pressed == ord('q'):
            while key_pressed not in (ord('y'), ord('n')):
                title = "Do you wanna quit? [y / n]"[:width - 1]
                start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
                start_y = int((height // 2) - 2)
                stdscr.addstr(start_y, start_x_title, title)
                stdscr.refresh()
                key_pressed = stdscr.getch()
            if key_pressed == ord('y'):
                break
            else:
                continue


def main():
    curses.wrapper(main_snake)


if __name__ == "__main__":
    main()
