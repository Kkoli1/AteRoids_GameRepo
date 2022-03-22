import pygame

from UIElements import Button, LoadSlot, SlotReader, SlotProfile
import AteroidsGame
import sys

def new_game() -> None:
    """
        Display when NEW GAME button is clicked
    """
    while True:
        new_mouse_pos = pygame.mouse.get_pos()

        screen.fill("black")

        new_game_back_btn = Button(image=None, pos=(640, 590), text_input="BACK", 
                            font=get_font(25), base_color="White", hovering_color="Green")

        new_game_back_btn.change_color(new_mouse_pos)
        new_game_back_btn.update(screen)

        slot_state_text = ""

        slot_1_btn = LoadSlot(image=None, pos=(640, 140), 
                            text_input="SLOT 1: Create a new game" + slot_state_text, 
                            font=get_font(45), base_color="White", hovering_color="Green", clickable = True)
        slot_1_btn.change_color(new_mouse_pos)
        slot_1_btn.update(screen)

        slot_2_btn = LoadSlot(image=None, pos=(640, 290), 
                            text_input="SLOT 2: Create a new game" + slot_state_text, 
                            font=get_font(45), base_color="White", hovering_color="Green", clickable = True)
        slot_2_btn.change_color(new_mouse_pos)
        slot_2_btn.update(screen)

        slot_3_btn = LoadSlot(image=None, pos=(640, 440), 
                            text_input="SLOT 3: Create a new game" + slot_state_text, 
                            font=get_font(45), base_color="White", hovering_color="Green", clickable = True)
        slot_3_btn.change_color(new_mouse_pos)
        slot_3_btn.update(screen)

        #   GAME EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if new_game_back_btn.check_for_input(new_mouse_pos):
                    main_menu()

                if slot_1_btn.check_for_input(new_mouse_pos):
                    slot_reader = SlotReader("saved_game.txt")
                    slot_reader.new_data("1", "True")
                    #   RETREIVING THE SCORES FROM THE FILE 
                    score1 = slot_reader.get_score()[2][0]
                    score2 = slot_reader.get_score()[3][0]
                    score3 = slot_reader.get_score()[4][0]
                    SlotProfile(score1,score2,score3,1)

                if slot_2_btn.check_for_input(new_mouse_pos):
                    slot_reader_2 = SlotReader("saved_game2.txt")
                    slot_reader_2.new_data("2", "True")
                    #   RETREIVING THE SCORES FROM THE FILE 
                    score1 = slot_reader_2.get_score()[2][0]
                    score2 = slot_reader_2.get_score()[3][0]
                    score3 = slot_reader_2.get_score()[4][0]
                    SlotProfile(score1,score2,score3,2)

                if slot_3_btn.check_for_input(new_mouse_pos):
                    slot_reader_3 = SlotReader("saved_game3.txt")
                    slot_reader_3.new_data("3", "True")
                    #   RETREIVING THE SCORES FROM THE FILE 
                    score1 = slot_reader_3.get_score()[2][0]
                    score2 = slot_reader_3.get_score()[3][0]
                    score3 = slot_reader_3.get_score()[4][0]
                    SlotProfile(score1,score2,score3,3)

        pygame.display.update()
    

def load_game() -> None:
    """
        Display when LOAD GAME button is clicked
    """
    while True:
        load_mouse_pos = pygame.mouse.get_pos()

        screen.fill("black")

        load_game_back_btn = Button(image=None, pos=(640, 590), 
                            text_input="BACK", font=get_font(25), base_color="White", hovering_color="Green")
        load_game_back_btn.change_color(load_mouse_pos)
        load_game_back_btn.update(screen)
        
        slot_state_text = ""

        #   SLOT 1 Configuration
        slot_reader = SlotReader("saved_game.txt")
        state1 = slot_reader.check_if_exist()
        if state1:
            slot_state_text = "Click to Load"
        else:
            slot_state_text = "Empty slot"
        slot_1_btn = LoadSlot(image=None, pos=(640, 140),text_input="SLOT 1: " + slot_state_text, 
                            font=get_font(45), base_color="White", hovering_color="Green", clickable = state1)
        slot_1_btn.change_color(load_mouse_pos)
        slot_1_btn.update(screen)

        #   SLOT 2 Configuration
        slot_reader_2 = SlotReader("saved_game2.txt")
        state2 = slot_reader_2.check_if_exist()
        if state2:
            slot_state_text = "Click to Load"
        else:
            slot_state_text = "Empty slot"
        slot_2_btn = LoadSlot(image=None, pos=(640, 290), text_input="SLOT 2: " + slot_state_text, 
                            font=get_font(45), base_color="White", hovering_color="Green", clickable = state2)
        slot_2_btn.change_color(load_mouse_pos)
        slot_2_btn.update(screen)

        #   SLOT 3 Configuration
        slot_reader_3 = SlotReader("saved_game3.txt")
        state3 = slot_reader_3.check_if_exist()
        if state3:
            slot_state_text = "Click to Load"
        else:
            slot_state_text = "Empty slot"
        slot_3_btn = LoadSlot(image=None, pos=(640, 440), text_input="SLOT 3: " + slot_state_text, 
                            font=get_font(45), base_color="White", hovering_color="Green", clickable = state3)
        slot_3_btn.change_color(load_mouse_pos)
        slot_3_btn.update(screen)
        

        #   GAME EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if load_game_back_btn.check_for_input(load_mouse_pos):
                    main_menu()
                if slot_1_btn.check_for_input(load_mouse_pos):
                    slot_reader = SlotReader("saved_game.txt")
                    #   RETREIVING THE SCORES FROM THE FILE 
                    score1 = slot_reader.get_score()[2][0]
                    score2 = slot_reader.get_score()[3][0]
                    score3 = slot_reader.get_score()[4][0]
                    SlotProfile(score1,score2,score3,1)
                if slot_2_btn.check_for_input(load_mouse_pos):
                    slot_reader_2 = SlotReader("saved_game2.txt")
                    #   RETREIVING THE SCORES FROM THE FILE 
                    score1 = slot_reader_2.get_score()[2][0]
                    score2 = slot_reader_2.get_score()[3][0]
                    score3 = slot_reader_2.get_score()[4][0]
                    SlotProfile(score1,score2,score3,2)
                if slot_3_btn.check_for_input(load_mouse_pos):
                    slot_reader_3 = SlotReader("saved_game3.txt")
                    #   RETREIVING THE SCORES FROM THE FILE 
                    score1 = slot_reader_3.get_score()[2][0]
                    score2 = slot_reader_3.get_score()[3][0]
                    score3 = slot_reader_3.get_score()[4][0]
                    SlotProfile(score1,score2,score3,3)

        pygame.display.update()

def SlotProfile(lvl1:str,lvl2:str,lvl3:str,load_no:int) -> None:
    """
        Display when a slot is clicked

    Args:
        lvl1 (string): score for level 1 from text file
        lvl2 (string): score for level 2 from text file
        lvl3 (string): score for level 3 from text file
        load_no (int): slot number selected
    """    
    while True:
        slot_profile_mouse_pos = pygame.mouse.get_pos()

        screen.fill("black")

        #   BACK BUTTON for NEW GAME screen
        slotProfileBack = Button(image=None, pos=(640, 640), 
                            text_input="BACK", font=get_font(25), base_color="White", hovering_color="Green")

        slotProfileBack.change_color(slot_profile_mouse_pos)
        slotProfileBack.update(screen)
        #   CARD OBJECT (AFTER CLICKING NEWGAME OR LOADGAME): For level 1
        slot_profile_1 = SlotProfile(image=pygame.image.load("assets/Card Rect.png"), pos=(225, 300), 
                            text_input="Level 1", font=get_font(35), base_color="#d7fcd4", hovering_color="White", 
                            level_score = "Score: {}/3".format(lvl1), image2 = pygame.image.load("assets/spaceship1.png"))

        slot_profile_1.change_color(slot_profile_mouse_pos)
        slot_profile_1.update(screen)

        #   CARD OBJECT (AFTER CLICKING NEWGAME OR LOADGAME): For level 2
        slot_profile_2 = SlotProfile(image=pygame.image.load("assets/Card Rect.png"), pos=(640, 300), 
                            text_input="Level 2", font=get_font(35), base_color="#d7fcd4", hovering_color="White", 
                            level_score = "Score: {}/3".format(lvl2), image2 = pygame.image.load("assets/spaceship2.png"))
                            
        slot_profile_2.change_color(slot_profile_mouse_pos)
        slot_profile_2.update(screen)

        #   CARD OBJECT (AFTER CLICKING NEWGAME OR LOADGAME): For level 3
        slotProfile3 = SlotProfile(image=pygame.image.load("assets/Card Rect.png"), pos=(1055, 300), 
                            text_input="Level 3", font=get_font(35), base_color="#d7fcd4", hovering_color="White", level_score = "Score: {}/3".format(lvl3), image2 = pygame.image.load("assets/spaceship3.png"))
        slotProfile3.change_color(slot_profile_mouse_pos)
        slotProfile3.update(screen)

        
        #   GAME EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if slotProfileBack.check_for_input(slot_profile_mouse_pos):
                    main_menu()
                if slot_profile_1.check_for_input(slot_profile_mouse_pos):
                    gathered_score = AteroidsGame.start_game(1)
                    if load_no == 1:
                        slot_reader_1 = SlotReader("saved_game.txt")
                    elif load_no == 2:
                        slot_reader_1 = SlotReader("saved_game2.txt")
                    elif load_no == 3:
                        slot_reader_1 = SlotReader("saved_game3.txt")
                    slot_reader_1.save_data(gathered_score,1)
                    #   RETREIVING THE SCORES FROM THE FILE 
                    score1 = slot_reader_1.get_score()[2][0]
                    score2 = slot_reader_1.get_score()[3][0]
                    score3 = slot_reader_1.get_score()[4][0]
                    SlotProfile(score1,score2,score3,load_no)
                if slot_profile_2.check_for_input(slot_profile_mouse_pos):
                    gathered_score = AteroidsGame.start_game(2)
                    if load_no == 1:
                        slot_reader_2 = SlotReader("saved_game.txt")
                    elif load_no == 2:
                        slot_reader_2 = SlotReader("saved_game2.txt")
                    elif load_no == 3:
                        slot_reader_2 = SlotReader("saved_game3.txt")
                    slot_reader_2.save_data(gathered_score,2)
                    #   RETREIVING THE SCORES FROM THE FILE 
                    score1 = slot_reader_2.get_score()[2][0]
                    score2 = slot_reader_2.get_score()[3][0]
                    score3 = slot_reader_2.get_score()[4][0]
                    SlotProfile(score1,score2,score3,load_no)
                if slotProfile3.check_for_input(slot_profile_mouse_pos):
                    gathered_score = AteroidsGame.start_game(3)
                    if load_no == 1:
                        slot_reader_3 = SlotReader("saved_game.txt")
                    elif load_no == 2:
                        slot_reader_3 = SlotReader("saved_game2.txt")
                    elif load_no == 3:
                        slot_reader_3 = SlotReader("saved_game3.txt")
                    slot_reader_3.save_data(gathered_score,3)
                    #   RETREIVING THE SCORES FROM THE FILE 
                    score1 = slot_reader_3.get_score()[2][0]
                    score2 = slot_reader_3.get_score()[3][0]
                    score3 = slot_reader_3.get_score()[4][0]
                    SlotProfile(score1,score2,score3,load_no)

        pygame.display.update()

def main_menu() -> None:
    """
        Main Loop 
    """
    move_first_bg = 0
    while True:

        #   Infinite scroll effect for the background
        screen.blit(background, (0, move_first_bg))
        screen.blit(background, (0, (-gameHeight) + move_first_bg))
        if move_first_bg == gameHeight:
            move_first_bg = 0
            screen.blit(background, (0,(-gameHeight)+move_first_bg))    
        move_first_bg += 10

        menu_mouse_pos = pygame.mouse.get_pos()

        #   Initialize Text: "ATEROIDS"
        menu_text = get_font(100).render("ATEROIDS", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100))

        #   Initialize "New Game" Button
        new_game_btn = Button(image=pygame.image.load("assets/New Game Rect.png"), pos=(640, 250), 
                            text_input="NEW GAME", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        #   Initialize "Load Game" Button
        load_game_btn = Button(image=pygame.image.load("assets/Load Game Rect.png"), pos=(640, 400), 
                            text_input="LOAD GAME", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        #   Initialize "Quit" Button
        quit_btn = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        #   Display Text: "ATEROIDS"
        screen.blit(menu_text, menu_rect)

        #   Display Button: New Game, Load Game, Quit
        for button in [new_game_btn, load_game_btn, quit_btn]:
            button.change_color(menu_mouse_pos)
            button.update(screen)
        
        #   Events Detector
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if new_game_btn.check_for_input(menu_mouse_pos):
                    new_game()
                if load_game_btn.check_for_input(menu_mouse_pos):
                    load_game()                
                if quit_btn.check_for_input(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)


if __name__ ==  '__main__':
    pygame.init()

    clock = pygame.time.Clock()
    gameWidth = 1280
    gameHeight = 720
    screen = pygame.display.set_mode((gameWidth, gameHeight))
    pygame.display.set_caption("Ateroids")
    ls1,ls2,ls3 = False, False, False
    bgImage = pygame.image.load("assets/spacebackground.png")
    background = pygame.transform.scale(bgImage,(gameWidth,gameHeight))
    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/font.ttf", size)
    
    main_menu()