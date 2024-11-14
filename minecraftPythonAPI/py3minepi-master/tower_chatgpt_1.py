import time

import mcpi.minecraft as minecraft
import math

from entities.minecraft_world import MinecraftWorld


class SpiraledStairwayTower():
    def __init__(self, x, y, z, block_id=35, block_data=3, radius=5, height=20, steps_per_turn=5):
        """
        Инициализирует башню со спиральной лестницей.

        Args:
            x (int): Координата x начальной точки башни.
            y (int): Координата y начальной точки башни.
            z (int): Координата z начальной точки башни.
            block_id (int, optional): ID блока для строительства башни. По умолчанию 35 (камень).
            block_data (int, optional): Дополнительные данные для блока (например, цвет). По умолчанию 9.
            radius (int, optional): Радиус цилиндра башни. По умолчанию 5.
            height (int, optional): Высота башни. По умолчанию 20.
            steps_per_turn (int, optional): Количество ступеней на один оборот спирали. По умолчанию 10.
        """
        self.x = x
        self.y = y
        self.z = z
        self.block_id = block_id
        self.block_data = block_data
        self.radius = radius
        self.height = height
        self.steps_per_turn = steps_per_turn

        self.craft = minecraft.Minecraft.create()

    def get_minecraft_world_entity(self):
        """Возвращает объект Minecraft."""
        return self.craft

    def get_block_id(self):
        """Возвращает ID блока."""
        return self.block_id

    def get_x(self):
        """Возвращает координату x."""
        return self.x

    def get_y(self):
        """Возвращает координату y."""
        return self.y

    def get_z(self):
        """Возвращает координату z."""
        return self.z

    def check_fig_dims(self, x_tiles, y_tiles, z_tiles):
        """Проверяет размеры фигуры."""
        if x_tiles <= 0 or y_tiles <= 0 or z_tiles <= 0:
            raise ValueError("Размеры фигуры должны быть положительными.")

    def draw_filled_fig(self, x_tiles, y_tiles, z_tiles):
        """
        Строит башню со спиральной лестницей.

        Args:
            x_tiles (int): Количество блоков в длину.
            y_tiles (int): Количество блоков в высоту.
            z_tiles (int): Количество блоков в ширину.
        """
        self.check_fig_dims(x_tiles, y_tiles, z_tiles)

        craft = self.get_minecraft_world_entity()
        block_id = self.get_block_id()
        block_data = self.block_data
        x, y, z = self.get_x(), self.get_y(), self.get_z()

        # Строим цилиндр башни
        for h in range(self.height):
            for i in range(360):
                angle = (math.pi * i) / 180
                x_coord = x + self.radius * math.cos(angle)
                z_coord = z + self.radius * math.sin(angle)
                craft.setBlock(x_coord, y + h, z_coord, block_id, block_data)

        # Строим спиральную лестницу
        inner_radius = self.radius - 1  # Радиус лестницы
        step_height = 1  # Высота каждой ступени
        # based on the tower's diameter
        steps_per_circle = int(2 * math.pi * inner_radius)  # Steps per circle
        step_angle = 2 * math.pi / steps_per_circle  # Angle between steps

        y_coord = math.inf
        # Цикл по высоте башни
        for h in range(self.height):
            if y_coord >= self.height and y_coord != math.inf:
                break
            # Цикл по шагам на спирали
            counter = 0
            for i in range(steps_per_circle):
                angle = i * step_angle  # Угол для текущей ступени

                # Рассчитываем координаты ступени с учетом ее положения на спирали
                x_coord = x + inner_radius * math.cos(angle)
                z_coord = z + inner_radius * math.sin(angle)
                if h == i == 0:
                    y_coord = y
                else:
                    y_coord = y + h * step_height + counter
                counter += 1
                if y_coord > self.height + self.get_y():
                    break
                craft.setBlock(x_coord, y_coord, z_coord, block_id, block_data)


if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    craft_obj = MinecraftWorld(mc)
    cor = craft_obj.get_tile_pos()
    print(cor)
    # Пример использования:
    tower = SpiraledStairwayTower(x=cor.x, y=cor.y, z=cor.z)
    tower.draw_filled_fig(100, 500, 100)  # Строит башню ...х...х... блоков
    time.sleep(10)
    craft_obj.restore_start_state()
