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

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def change_color(self, position):
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

    def check_for_input(self, position:list) -> bool:
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            if self.clickable:
                return True
        return False


class SlotProfile(Button):
    """
    Class for Slot Profile (Hoverable and Clickable)
    """

    def __init__(self, image, pos:tuple, text_input:str, font:Callable, 
                base_color:str, hovering_color:str, level_score:str, image2) -> None:
        super().__init__(image, pos, text_input, font, base_color, hovering_color)

        self.level_score = level_score
        self.text_rect = self.text.get_rect(
            center=(self.x_pos, self.y_pos+150))
        self.textLvl1 = self.font.render(
            self.level_score, True, self.base_color)
        self.textLvl1_rect = self.textLvl1.get_rect(
            center=(self.x_pos, self.y_pos+220))
        self.image2 = image2
        self.image2_rect = self.image2.get_rect(
            center=(self.x_pos, self.y_pos-100))

    def update(self, screen) -> None:
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.image2, self.image2_rect)
        screen.blit(self.text, self.text_rect)
        screen.blit(self.textLvl1, self.textLvl1_rect)

    def change_color(self, position:list) -> None:
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(
                self.text_input, True, self.hovering_color)
            self.textLvl1 = self.font.render(
                self.level_score, True, self.hovering_color)
        else:
            self.text = self.font.render(
                self.text_input, True, self.base_color)
            self.textLvl1 = self.font.render(
                self.level_score, True, self.base_color)


class SlotReader():
    """
        Class for Slot Reader (File Handler: Saved Games)
    """

    def __init__(self, filename:str) -> None:
        self.filename = filename
        self.data = None

    def new_data(self, slot_no:str, existing_load:str):
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

    def save_data(self, score:int, profile_no:int) -> None:
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
