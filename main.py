DELIMITER = ";"


class TIMESTAMP:
    weekday = ""
    hour = ""
    consumption = 0.0
    price = 0.0


def readTimestamps(PFilename: str, PTimestamps: list[TIMESTAMP]) -> None:
    print('Reading file "{}".'.format(PFilename))
    PTimestamps.clear()
    Filehandle = open(PFilename, "r", encoding="utf-8-sig")
    FirstLine = True
    for Line in Filehandle:
        if FirstLine:                       # skip header row
            FirstLine = False
            continue
        Row = Line.rstrip()                 # remove newline
        if Row.strip() == "":               # skip empty lines
            continue
        Columns = Row.split(DELIMITER)
        Timestamp = TIMESTAMP()
        Timestamp.weekday = Columns[0].strip()
        Timestamp.hour = Columns[1].strip()
        Timestamp.consumption = float(Columns[2])
        Timestamp.price = float(Columns[3])
        PTimestamps.append(Timestamp)
        Columns.clear()
    Filehandle.close()
    return None


def displayTimestamps(PTimestamps: list[TIMESTAMP]) -> None:
    print("Electricity usage:")
    for Timestamp in PTimestamps:
        Total = Timestamp.consumption * Timestamp.price
        print(" - {} {}, price {:.2f}, consumption {:.2f} kWh, total {:.2f} €".format(
            Timestamp.weekday, Timestamp.hour, Timestamp.price, Timestamp.consumption, Total))
    return None


def main() -> None:
    print("Program starting.")
    Timestamps: list[TIMESTAMP] = []
    Filename = input("Insert filename: ")
    readTimestamps(Filename, Timestamps)
    displayTimestamps(Timestamps)
    Timestamps.clear()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()