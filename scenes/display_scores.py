import pygame
import sqlite3

def get_score_position(score):
    conn = sqlite3.connect('scores.db')
    cursor = conn.cursor()

    #block provided by Grok 3
    cursor.execute('SELECT (SELECT COUNT(*) + 1 FROM scores WHERE score >= ?) AS rank', (score,))
    rank = cursor.fetchone()[0]
    conn.close()

    return rank

def display_top5(screen, score, font, rank, limit=4):
    RED = (255, 0, 0)

    conn = sqlite3.connect('scores.db')
    cursor = conn.cursor()
    saved_screen = screen.copy()

    #next line was provided by Grok 3
    #sorts the leaderboards and takes the top 5
    cursor.execute('SELECT name, score FROM scores ORDER BY score DESC, id ASC LIMIT ?', (limit,))
    leaderboard = cursor.fetchall()
    #inserts the current score on the list on the appropriate postion
    leaderboard.insert(rank-1, ('You', score))

    screen.blit(saved_screen, (0, 0))
    line_spacing = 5
    for index, row in enumerate(leaderboard):
        to_print = f"{index+1}. {row[0]}  {row[1]}"
        to_print = font.render(to_print, True, RED)
        screen.blit(to_print, (25, 50 + index * (font.get_height() + line_spacing)))

    to_print = "Save this score?"
    to_print = font.render(to_print, True, RED)
    screen.blit(to_print, (25, 350))

    to_print = "press (y/n)"
    to_print = font.render(to_print, True, RED)
    screen.blit(to_print, (120, 375))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return False, False
                elif event.key == pygame.K_n:
                    return False, True


def display_relative_position(screen, score, font, rank, limit=5):
    RED = (255, 0, 0)

    conn = sqlite3.connect('scores.db')
    cursor = conn.cursor()
    saved_screen = screen.copy()

    cursor.execute('SELECT name, score FROM scores ORDER BY score DESC, id ASC LIMIT ?', (limit,))
    leaderboard = cursor.fetchall()
    screen.blit(saved_screen, (0, 0))
    line_spacing = 5
    for index, row in enumerate(leaderboard):
        to_print = f"{index + 1}. {row[0]}  {row[1]}"
        to_print = font.render(to_print, True, RED)
        screen.blit(to_print, (25, 50 + index * (font.get_height() + line_spacing)))

    to_print = f"{rank}. You  {score}"
    to_print = font.render(to_print, True, RED)
    screen.blit(to_print, (25, 50 + 5 * (font.get_height() + line_spacing)))

    to_print = "Save this score?"
    to_print = font.render(to_print, True, RED)
    screen.blit(to_print, (25, 350))

    to_print = "press (y/n)"
    to_print = font.render(to_print, True, RED)
    screen.blit(to_print, (120, 375))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return False, False
                elif event.key == pygame.K_n:
                    return False, True

