class Music:
    def __init__(self, hash, name):
        self.hash = hash
        self.name = name

    def __str__(self):
        return f"{self.name} (Código: {self.hash})"

musics = [
    Music(8765, "Nirvana - Smells Like Teen Spirit"),
    Music(5432, "John Lennon - Imagine"),
    Music(7651, "U2 - One"),
    Music(3456, "Michael Jackson - Billie Jean"),
    Music(6543, "Queen - Bohemian Rhapsody"),
    Music(2345, "The Beatles - Hey Jude"),
    Music(6789, "Bob Dylan - Like A Rolling Stone"),
    Music(3210, "Elton John - Your Song"),
    Music(5847, "Led Zeppelin - Stairway To Heaven"),
    Music(2109, "The Emotions - Best Of My Love"),
    Music(1098, "Ike and Tina Turner - River Deep Mountain High"),
    Music(7654, "Sam Cooke - A Change Is Gonna Come"),
    Music(7890, "Martha Reeves and the Vandellas - Dancing In The Street"),
    Music(9876, "The Who - My Generation"),
    Music(5211, "The Righteous Brothers - You’ve Lost That Lovin’ Feeling"),
    Music(8877, "The Beach Boys - God Only Knows"),
    Music(1018, "Dire Straits - Sultans Of Swing"),
    Music(9014, "Ray Charles - What’d I Say (Parts 1 And 2)"),
    Music(8765, "The Rolling Stones - Gimme Shelter"),
    Music(9012, "James Brown - Papa’s Got A Brand New Bag"),
    Music(5672, "Ben E King - Stand By Me"),
    Music(9387, "The Beatles - A Day In The Life"),
    Music(7894, "The Police - Every Breath You Take"),
    Music(6624, "Leonard Cohen - Hallelujah"),
    Music(9954, "Bob Marley - No Woman No Cry"),
    Music(6699, "Chuck Berry - Jonny B Good"),
    Music(1398, "The Beach Boys - Good Vibrations"),
    Music(5679, "ABBA - Dancing Queen"),
    Music(6998, "Sly And The Family Stone - Family Affair"),
    Music(9021, "Aretha Franklin - Respect"),
    Music(1096, "Simon & Garfunkel - Bridge Over Troubled Water"),
    Music(5614, "Radiohead - Creep"),
    Music(2107, "The Ronettes - Be My Baby"),
    Music(2587, "Bruce Springsteen - Born To Run"),
    Music(2187, "Marvin Gaye - What’s Goin’ On"),
    Music(3232, "Judy Garland - Over The Rainbow"),
    Music(1155, "Elvis Presley - Heartbreak Hotel"),
    Music(5432, "David Bowie - Life On Mars?"),
    Music(6577, "Whitney Houston - I Will Always Love You"),
    Music(2109, "Oasis - Live Forever"),
    Music(4329, "Chubby Checker - The Twist"),
    Music(6335, "Guns N’ Roses - Sweet Child O’Mine"),
    Music(8764, "Sex Pistols - God Save The Queen"),
    Music(1234, "Rolling Stones - (I Can’t Get No) Satisfaction"),
    Music(6523, "The Clash - London Calling")
]
