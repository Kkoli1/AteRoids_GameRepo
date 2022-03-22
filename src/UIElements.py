import pygame

from typing import Callable


class Button():
    """
            Class for button (Hoverable and Clickable)	
    """

    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen) -> None:
        """updates the button

        Args:
            screen (object): screen instance
        """        
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, position:list) -> bool:
        """checks for user input

        Args:
            position (list): coordinates

        Returns:
            bool: if the user input if within the button, the function returns true
        """        
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def change_color(self, position:list) -> None:
        """change the color of a button

        Args:
            position (coordinates): coordinates of a button
        """        
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(
                self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(
                self.text_input, True, self.base_color)


class LoadSlot(Button):
    """
        Class for Load Game Slots (after clicking load game or new game)
    """

    def __init__(self, image, pos, text_input, font, base_color, hovering_color, clickable):
        super().__init__(image, pos, text_input, font, base_color, hovering_color)
        self.clickable = clickable

    def check_for_input(self, position: list) -> bool:
        """checks for user input

        Args:
            position (list): coordinates

        Returns:
            bool: if the input is clickable, it returns true
        """        
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            if self.clickable:
                return True
        return False


class SlotProfile(Button):
    """
    Class for Slot Profile (Hoverable and Clickable)
    """

    def __init__(self, image, pos: tuple, text_input: str, font: Callable,
                 base_color: str, hovering_color: str, level_score: str, image_2) -> None:
        super().__init__(image, pos, text_input, font, base_color, hovering_color)

        self.font = font
        self.level_score = level_score
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos+80))
        self.text_lvl_1 = self.font.render(
            self.level_score, True, self.base_color)
        self.txt_lvl_1_rect = self.text_lvl_1.get_rect(
            center=(self.x_pos, self.y_pos+150))
        self.image_2 = image_2
        self.image2_rect = self.image_2.get_rect(
            center=(self.x_pos, self.y_pos-80))

        self.enemy_asset = pygame.image.load("assets/ship.png")
        self.enemy_asset_rect = self.enemy_asset.get_rect(center=(225, 540))
        self.enemy_desc = self.font.render("Enemy", True, "Red")
        self.enemey_desc_rect = self.enemy_desc.get_rect(center=(225, 600))

        self.bullet_asset = pygame.image.load("assets/bullet.png")
        self.bullet_asset_rect = self.enemy_asset.get_rect(center=(500, 560))
        self.bullet_desc = self.font.render(
            "Avoid the bullets", True, "Green")
        self.bullet_desc_rect = self.enemy_desc.get_rect(center=(420, 600))

        self.baby_asset = pygame.image.load("assets/BabyRoid.png")
        self.baby_asset_rect = self.enemy_asset.get_rect(center=(830, 560))
        self.baby_desc = self.font.render(
            "Collect the BabyRoids", True, "Violet")
        self.baby_desc_rect = self.enemy_desc.get_rect(center=(740, 600))

        self.player_assert = pygame.image.load("assets/AteRhoids.png")
        self.player_assert_rect = self.enemy_asset.get_rect(center=(1055, 540))
        self.player_desc = self.font.render("Player", True, "Violet")
        self.player_desc_rect = self.enemy_desc.get_rect(center=(1055, 600))

    def update(self, screen) -> None:
        """updates slot profile

        Args:
            screen (object): screen object
        """        
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.image_2, self.image2_rect)
        screen.blit(self.text, self.text_rect)
        screen.blit(self.text_lvl_1, self.text_lvl_1, self.txt_lvl_1_rect)
        screen.blit(self.enemy_asset, self.enemy_asset_rect)
        screen.blit(self.enemy_desc, self.enemey_desc_rect)
        screen.blit(self.bullet_asset, self.bullet_asset_rect)
        screen.blit(self.bullet_desc, self.bullet_desc_rect)
        screen.blit(self.baby_asset, self.baby_asset_rect)
        screen.blit(self.baby_desc, self.baby_desc_rect)
        screen.blit(self.player_assert, self.player_assert_rect)
        screen.blit(self.player_desc, self.player_desc_rect)

    def change_color(self, position: list) -> None:
        """change the color of the slot profile

        Args:
            position (list): coordinates 
        """        
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(
                self.text_input, True, self.hovering_color)
            self.text_lvl_1 = self.font.render(
                self.level_score, True, self.hovering_color)
        else:
            self.text = self.font.render(
                self.text_input, True, self.base_color)
            self.text_lvl_1 = self.font.render(
                self.level_score, True, self.base_color)


class SlotReader():
    """
        Class for Slot Reader (File Handler: Saved Games)
    """

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.data = None

    def new_data(self, slot_no: str, existing_load: str) -> None:
        self.slot_no = slot_no
        self.existing_load = existing_load
        with open("game_files/"+self.filename, 'w', encoding='utf-8') as f:
            f.write(self.slot_no+"\n")
            f.write(self.existing_load+"\n")
            f.write("0\n")
            f.write("0\n")
            f.write("0\n")

    def check_if_exist(self) -> bool:
        state = None
        with open("game_files/"+self.filename, 'r', encoding='utf-8') as f:
            state = f.readlines()[1]
        if state == "False\n":
            return False
        return True

    def get_score(self) -> object:
        with open("game_files/"+self.filename, 'r', encoding='utf-8') as f:
            self.data = f.readlines()
        return self.data

    def save_data(self, score: int, profile_no: int) -> None:
        with open("game_files/"+self.filename, 'r', encoding='utf-8') as f:
            self.data = f.readlines()
        if profile_no == 1:
            if int(self.data[2][0]) < score:
                self.data[2] = str(score)+"\n"
        if profile_no == 2:
            if int(self.data[3][0]) < score:
                self.data[3] = str(score)+"\n"
        if profile_no == 3:
            if int(self.data[4][0]) < score:
                self.data[4] = str(score)+"\n"

        with open("game_files/"+self.filename, 'w', encoding='utf-8') as f:
            for element in self.data:
                f.write(element)
