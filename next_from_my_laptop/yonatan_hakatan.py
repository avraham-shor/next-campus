import winsound

freqs = {"la": 220, "si": 247, "do": 261, "re": 293, "mi": 329, "fa": 349, "sol": 392,}
notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"


def song_yonatan(freqs, notes):
    list_notes = (note.split(',') for note in notes.split('-'))
    print(list_notes)
    for _ in range(5):
        for note in list_notes:
            winsound.Beep(freqs[note[0]], int(note[1]))
            print(freqs[note[0]], int(note[1]))
    # winsound.Beep(frequency, duration)


song_yonatan(freqs, notes)