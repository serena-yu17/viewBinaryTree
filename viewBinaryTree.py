# Written by Feng Yu for COMP9021
# You may use or modify it freely for any purposes.


from tkinter import *
from math import log2


class Tkwindow:
    def __init__(self, master, tree_array):
        self.master = master
        if tree_array[0] is not None:
            self.arr = tree_array
        else:
            self.arr = tree_array[1:]
        while self.arr[-1] is None:
            self.arr.pop()
        self.size = len(self.arr)
        self.tree_height = int(log2(self.size + 1))
        self.tree_width = 1 << self.tree_height
        self.radius = 20  # radius of each node
        self.distance = 20  # horizontal distance between bottom leaf nodes
        self.graph_width = self.tree_width * (self.distance * 2 - 1 + self.radius * 2)
        self.padding = self.radius
        self.row_distance = 60
        self.coordinates = list()
        self._setcoord()
        self.master.title("Binary Tree")
        self.draw()

    def _setcoord(self):
        level_count = 0
        y = self.padding + 30
        level_size = 1
        node_distance = self.graph_width / (level_size + 1)
        for _ in range(self.size):
            self.coordinates.append((self.padding + node_distance * (level_count + 1), y))
            level_count += 1
            if level_count == level_size:
                level_count = 0
                y += self.row_distance
                level_size *= 2
                node_distance = self.graph_width / (level_size + 1)
        pass

    @staticmethod
    def _distance(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def draw(self):
        canvas = Canvas(self.master, width=self.graph_width + self.padding * 2,
                        height=(self.padding * 2 + 60 + self.tree_height * self.row_distance))
        for i in range(self.size):
            if self.arr[i] is not None and self.arr[(i - 1) // 2] is not None:
                canvas.create_oval(self.coordinates[i][0] - self.radius, self.coordinates[i][1] - self.radius,
                                   self.coordinates[i][0] + self.radius, self.coordinates[i][1] + self.radius,
                                   outline="#000", fill="#fff", width=1)
                font_size = self.radius
                txt = str(self.arr[i])
                if len(txt) > 2:
                    font_size = font_size * 2 // len(txt)
                canvas.create_text(self.coordinates[i][0], self.coordinates[i][1], text=txt,
                                   font=("Arial", font_size))
                if i * 2 + 1 < self.size and self.arr[i * 2 + 1] is not None:
                    dist = self._distance(self.coordinates[i][0], self.coordinates[i][1],
                                          self.coordinates[i * 2 + 1][0],
                                          self.coordinates[i * 2 + 1][1])
                    delta_x = (self.coordinates[i * 2 + 1][0] - self.coordinates[i][0]) * self.radius / dist
                    delta_y = (self.coordinates[i * 2 + 1][1] - self.coordinates[i][1]) * self.radius / dist
                    canvas.create_line(self.coordinates[i][0] + delta_x, self.coordinates[i][1] + delta_y,
                                       self.coordinates[i * 2 + 1][0] - delta_x,
                                       self.coordinates[i * 2 + 1][1] - delta_y)
                if i * 2 + 2 < self.size and self.arr[i * 2 + 2] is not None:
                    dist = self._distance(self.coordinates[i][0], self.coordinates[i][1],
                                          self.coordinates[i * 2 + 2][0],
                                          self.coordinates[i * 2 + 2][1])
                    delta_x = (self.coordinates[i * 2 + 2][0] - self.coordinates[i][0]) * self.radius / dist
                    delta_y = (self.coordinates[i * 2 + 2][1] - self.coordinates[i][1]) * self.radius / dist
                    canvas.create_line(self.coordinates[i][0] + delta_x, self.coordinates[i][1] + delta_y,
                                       self.coordinates[i * 2 + 2][0] - delta_x,
                                       self.coordinates[i * 2 + 2][1] - delta_y)
        canvas.pack(side="top", expand=1)


def viewBinaryTree(*tree_array):
    if isinstance(tree_array, list) or isinstance(tree_array, tuple) and len(tree_array) == 1:
        tree_array = tree_array[0]
    root = Tk()
    window = Tkwindow(root, tree_array)
    root.mainloop()


# test case
if __name__ == "__main__":
    print("viewBinaryTree([2, 3, 4, None, 6, 6, 8, None, None, 0])")
    viewBinaryTree([2, 3, 4, None, 6, 6, 8, None, None, 0, 27, 198, -10])
