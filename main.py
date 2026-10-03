"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False

#función para retornar lista ordenada
def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))

#función para retornar lista de items ingresados por parametro
def remove_duplicates_from_list(items):
    return list(dict.fromkeys(items))

#implementación, condición de validación ...
if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    elif len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].strip().lower() in {"yes", "y", "true", "1"}
    elif len(sys.argv) > 3:
        print("Uso: python3 main.py <fichero> [yes|no]")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                for word in line.strip().split():
                    if word:
                        word_list.append(word)
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list))
