from music_data import Music, musics

class MusicLibrary:
    def __init__(self):
        self.musics = musics

    def search_by_hash(self, hash):
        for music in self.musics:
            if music.hash == hash:
                return music
        return None

if __name__ == "__main__":
    library = MusicLibrary()
    while True:
        hash_input = int(input("\nDigite o código (0000 para sair): "))
        if hash_input == 0000:
            break
        music = library.search_by_hash(hash_input)

        if music:
            print(f"{music}")
        else:
            print("Música não encontrada.")
