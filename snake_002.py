import curses
from random import randrange


def main_snake(stdscr):
    # set cursor invisible
    curses.curs_set(0)
    # set refreshing interval (to avoid waiting keypress in getch())
    curses.halfdelay(1)
    key_pressed = 0
    height, width = stdscr.getmaxyx()
    height -= height % 2
    width -= width % 2

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # set the color pairs (id, font color, bg color)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)

    # the dict with the coordinate increments for all the directions: if 'down' then (y + 1, x + 0)...
    directional_increments_yx = {'down': (1, 0), 'up': (-1, 0),
                                 'right': (0, 2), 'left': (0, -2)}

    # initial direction. Let it be 'up' for now
    direction = 'up'

    # create the snake (it's made of blocks, every snake block contains 2 symbols (to be square))
    init_x = width // 2
    init_y = height // 2
    # every x_coord should be even
    init_x -= init_x % 2
    init_len = 5
    snake = [(init_y + i, init_x) for i in range(init_len)]

    # apple (assume the target point is an apple! %)) location. It shouldn't appear on the snake
    while True:
        apple = (randrange(2, height - 2, 2), randrange(2, width - 2, 2))
        if apple not in snake:
            break

    while True:

        stdscr.clear()
        # if the term_size was changed
        height, width = stdscr.getmaxyx()
        height -= height % 2
        width -= width % 2
        # changing the direction if the key was pressed
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

        # time to update the snake respect to the moving direction. -1 in y coord because of the status bar
        # that would be drawn later at the very bottom of the screen.
        # The screen is looped. Ta-da!
        snake.insert(0, ((snake[0][0] + directional_increments_yx[direction][0]) % (height - 1),
                         (snake[0][1] + directional_increments_yx[direction][1]) % width))

        # if the snake's head eats its body, it means that after update the head_point_tuple
        # is in the snake_list at least 2 times
        if snake.count(snake[0]) > 1:
            # the snake is dead because of eating itself. So the user can choose either to play again or to quit
            while key_pressed not in (ord('y'), ord('n')):
                title = "You've eaten yourself! You're dead! Try again? [y / n]"[:width - 1]
                start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
                start_y = int((height // 2) - 2)
                stdscr.addstr(start_y, start_x_title, title)
                stdscr.refresh()
                key_pressed = stdscr.getch()
            # if 'yes' (to play), the snake is born again as a new list, the direction is 'right'
            # and a new apple appears
            if key_pressed == ord('y'):
                snake = [(init_y, init_x + i) for i in range(init_len + 1)]
                # +1 because of snake.pop(-1) in the next block. It will eat 1 star
                direction = 'left'
                apple = (randrange(1, height - 1), randrange(1, width - 1))
            else:
                break

        # If snake is just running at screen and isn't eating an apple then at the every step the head_coords_tuple
        # is to be inserted at 0-index position and the tail_coords_tuple is to be popped.
        # If the snake's head appears at the apple's coords, the snake grows (i.e. the last tail_coords_tuple
        # is not to be deleted).
        # And a new apple appears.
        if snake[0] != apple:
            snake.pop(-1)
        else:
            while True:
                apple = (randrange(2, height - 2, 2), randrange(2, width - 2, 2))
                if apple not in snake:
                    break
        # draw the snake with eyes by its coords_list.
        first_ch = {'left': ': ', 'right': ' :', 'up': '\'\'', 'down': '..'}
        for i in range(len(snake)):
            if i == 0:
                ch = first_ch[direction]
            else:
                ch = '  '
            stdscr.addstr(*snake[i], ch, curses.color_pair(1))

        # draw an apple
        stdscr.addstr(*apple, '\' ', curses.color_pair(2))

        # just for verifying
        # stdscr.addstr(0, 0, f'{init_y}, {init_x}')
        # stdscr.addstr(2, 0, f'{apple}, {snake}')

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
