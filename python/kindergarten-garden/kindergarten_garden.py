class Garden:
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.students = sorted(students)
        rows = diagram.split("\n")
        self.diagram = diagram
        # self.row1 = list("VRCGVVRVCGGCCGVRGCVCGCGV")
        # self.row2 = list("VRCCCGCRRGVCGCRVVCVGCGCV")
        self.row1 = list(rows[0])
        self.row2 = list(rows[1])
        self.plants_db = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets", ".": "."}

    # def __str__(self):
    #     pass

    def plants(self, name):
        position = self.students.index(name)  # Position in array used to extra from rows

        top_row = self.row1[position*2:position*2+2]
        bottom_row = self.row2[position*2:position*2+2]

        persons_plants_in_char = top_row + bottom_row
        persons_plants_in_words = self.chars_to_plant(persons_plants_in_char)

        return persons_plants_in_words

    def chars_to_plant(self, chars: list) -> list:
        return [self.plants_db[char] for char in chars]


def generate_diagram(students):
    # window = "[window][window][window]\n"
    window = ""
    student = f"{len(students) * 2 * '.'}\n" * 2
    diagram = window + student
    return diagram


if __name__ == '__main__':
    garden = Garden(
        "VCRRGVRG\nRVGCCGCV", students=["Samantha", "Patricia", "Xander", "Roger"]
    )
    print(garden.plants("Patricia"))
