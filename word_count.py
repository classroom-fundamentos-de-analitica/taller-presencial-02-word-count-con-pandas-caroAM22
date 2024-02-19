"""Taller evaluable"""

import glob
import pandas as pd


def load_input(input_directory):
    """Load text files in 'input_directory/'"""
    file_names = glob.glob(input_directory + "/*.*")
    print(file_names)
    dataframes = [
        pd.read_csv(filename, sep=";", header=["text"]) for filename in file_names
    ]
    dataframe = pd.concat(dataframes).reset_index(drop=True)
    return dataframe
    # Lea los archivos de texto en la carpeta input/ y almacene el contenido en
    # un DataFrame de Pandas. Cada línea del archivo de texto debe ser una
    # entrada en el DataFrame.
    #


def clean_text(dataframe):
    """Text cleaning"""
    dataframe = dataframe.copy()
    dataframe["text"] = dataframe["text"].str.lower()
    dataframe["text"] = dataframe["text"].str.replace(",", "").str.replace(".", ",")
    return dataframe
    #
    # Elimine la puntuación y convierta el texto a minúsculas.
    #


def count_words(dataframe):
    """Word count"""
    dataframe = dataframe.copy()
    dataframe["text"] = dataframe["text"].str.split()
    dataframe["text"] = dataframe["text"].explode("text").reset_index(drop=True)
    dataframe = dataframe.rename(columns={"text": "word"})
    dataframe["count"] = 1
    conteo = dataframe.groupby(["word"], as_index=False).agg({"count": sum})
    return conteo
    #
    # Cuente las palabras en el texto y añada el resultado en una nueva columna
    # llamada 'word_count'.
    #


def save_output(dataframe, output_filename):
    """Save output to a file."""
    dataframe.to_csv(output_filename, sep="\t", index=False)
    #
    # Guarde el DataFrame en un archivo separado por punto y coma.
    #


#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    """Call all functions."""
    dataframe = load_input(input_directory)
    datafreame = clean_text(dataframe)
    dataframe = count_words(dataframe)
    save_output(dataframe, output_filename)


if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
