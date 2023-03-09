from pathlib import Path
import pandas as pd


def split_students(line: str):
    all_students = line.split(" ")[5:]
    student_indexes = [i-1 for i, word in enumerate(all_students) if word == "nazywa"]
    return [
        all_students[start_index:end_index]
        for start_index, end_index in zip(student_indexes, student_indexes[1:] + [None])
    ]


if __name__ == '__main__':
    data = []
    columns = ["uniwersytet", "id_studenta", "imie", "nazwisko", "wiek", "oceny"]

    with Path(__file__).parent.joinpath("data", "dane_t.txt").open() as f:
        for line in f.readlines():
            splited = line.replace("\n", " ").strip().split()

            for student in split_students(line):
                data.append([
                    splited[1],
                    student[0],
                    student[3],
                    student[4],
                    int(student[7]),
                    [int(oceny) for oceny in student[11:] if oceny not in ("\n", "")],
                ])

    df = pd.DataFrame(
        data,
        columns=columns
    )
    df["srednia_ocen"] = df["oceny"].apply(lambda oceny: sum(oceny) / len(oceny))
    grouped_uniwersytet = df.groupby('uniwersytet')

    print(f"Studentów jest {len(df.index)}")
    print(f"Średnia liczba studentów per uniwersytet {grouped_uniwersytet.count().mean()['id_studenta']}")
    print(f"Najczęściej imie {df[['imie', 'id_studenta']].groupby('imie').count().sort_values('id_studenta').index[-1]}")
    print(f"Najrzadziej nazwisko {df[['nazwisko', 'id_studenta']].groupby('nazwisko').count().sort_values('id_studenta').index[0]}")
    print(f"Sredni wiek {df['wiek'].mean()}")
    print(f"Srednia ocen {df['srednia_ocen'].mean()}")
    print(f"Srednia ocen per uniwersytet:\n{grouped_uniwersytet['srednia_ocen'].mean()}")
