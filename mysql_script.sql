CREATE TABLE students (
    STID VARCHAR(8) PRIMARY KEY,
    FIRSTNAME VARCHAR(255),
    LASTNAME VARCHAR(255)
);
CREATE TABLE subjects (
    SJID VARCHAR(8) PRIMARY KEY,
    NAME VARCHAR(255)
);
CREATE TABLE scores (
    SCID INT(11) PRIMARY KEY AUTO_INCREMENT,
    STID VARCHAR(8),
    SJID VARCHAR(8),
    SCORE INT
);
CREATE TABLE votes (
    VID INT(11) PRIMARY KEY AUTO_INCREMENT,
    VOTE_SUBJECT VARCHAR(255),
    VOTE_COUNT INT
);
INSERT INTO students(STID, FIRSTNAME, LASTNAME)
VALUES ("65050001", "Clay", "Pickle"),
    ("65050002", "Grace", "Merrill"),
    ("65050003", "Averill", "Lincoln"),
    ("65050004", "Jolene", "Morrish"),
    ("65050005", "Ryan", "Arthur");
INSERT INTO subjects(SJID, NAME)
VALUES ("05506003", "PROGRAMMING FUNDAMENTALS"),
    ("05506004", "OBJECT-ORIENTED PROGRAMMING"),
    ("05506005", "DATA STRUCTURES AND ALGORITHMS"),
    ("05506006", "ALGORITHM ANALYSIS AND DESIGN"),
    (
        "05506007",
        "AUTOMATA THEORIES AND PROGRAMMING LANGUAGES"
    );
INSERT INTO scores(STID, SJID, SCORE)
VALUES ("65050001", "05506003", 55),
    (
        "65050001",
        "05506004",
        76
    ),
    (
        "65050001",
        "05506005",
        68
    ),
    (
        "65050001",
        "05506006",
        90
    ),
    (
        "65050001",
        "05506007",
        66
    ),
    ("65050002", "05506003", 32),
    (
        "65050002",
        "05506004",
        58
    ),
    (
        "65050002",
        "05506005",
        87
    ),
    (
        "65050002",
        "05506006",
        60
    ),
    (
        "65050002",
        "05506007",
        100
    ),
    (
        "65050003",
        "05506003",
        88
    ),
    (
        "65050003",
        "05506004",
        54
    ),
    (
        "65050003",
        "05506005",
        69
    ),
    (
        "65050003",
        "05506006",
        55
    ),
    (
        "65050003",
        "05506007",
        40
    ),
    (
        "65050004",
        "05506003",
        67
    ),
    (
        "65050004",
        "05506004",
        59
    ),
    (
        "65050004",
        "05506005",
        90
    ),
    (
        "65050004",
        "05506006",
        78
    ),
    (
        "65050004",
        "05506007",
        39
    ),
    ("65050005", "05506003", 98),
    (
        "65050005",
        "05506004",
        89
    ),
    (
        "65050005",
        "05506005",
        80
    ),
    (
        "65050005",
        "05506006",
        75
    ),
    (
        "65050005",
        "05506007",
        87
    );