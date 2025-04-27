from .display_scores import get_score_position
from .display_scores import display_top5
from .display_scores import display_relative_position

import pygame
import sqlite3

def game_over(screen, score, font):
    conn = sqlite3.connect("scores.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS scores(id INTEGER PRIMARY KEY AUTOINCREMENT, name, score)")

    #save the current screen state
    saved_screen = screen.copy()

    #get the relative position of the score
    rank = get_score_position(score)

    if rank <= 5:
        #displays the top 5 including the current score
        exit_game_check, dont_save_score = display_top5(screen, score, font, rank)
        if exit_game_check:
            return False
        if dont_save_score:
            return True
    else:
        #displays the top 5 and the the current score with its position
        exit_game_check, dont_save_score = display_relative_position(screen, score, font, rank)
        if exit_game_check:
            return False
        if dont_save_score:
            return True

    name = ''
    input_active = True
    #loops while typing the name and displays what was typed in the screen
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            #the following block was provided by Grok 3
            if event.type == pygame.KEYDOWN:
                #pressing enter breaks the loop and saves the score
                if event.key == pygame.K_RETURN and name != '':
                    input_active = False
                #backspace erases
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                #catches printable input only for the name
                elif event.unicode.isprintable():
                    name = name + event.unicode

        screen.blit(saved_screen, (0, 0))
        #the following block was provided by Grok 3
        #displays the updated name
        prompt = font.render("Enter your name:", True, (100, 0, 0))
        name_surface = font.render(name, True, (155, 155, 0))
        screen.blit(prompt, (50, 100))
        screen.blit(name_surface, (50, 150))

        pygame.display.flip()

    cursor.execute("INSERT INTO scores (name, score) VALUES (?, ?)", (name, score))
    conn.commit()
    conn.close()
    return True
