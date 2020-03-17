class MusicNotes:

    def __init__(self):
        self.freqs = {"la": 55, "si": 61.74, "do": 65.41, "re": 73.42, "mi": 82.41, "fa": 87.31, "sol": 98}
        self.index_note = 0
        self.octava = 0.5

    def __iter__(self):
        return self

    def __next__(self):
        self.index_note += 1
        if self.index_note >= (len(self.freqs)) * 5:
            raise StopIteration
        if self.index_note % len(self.freqs) - 1 == 0:
            self.octava *= 2
        iter_note = list(self.freqs.values())[self.index_note % len(self.freqs) - 1] * self.octava
        return iter_note if iter_note % 1 else int(iter_note)


notes_iter = iter(MusicNotes())
for freq in notes_iter:
    print(freq)
