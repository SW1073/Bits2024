CREATE TABLE IF NOT EXISTS center (
    id TEXT PRIMARY KEY,
    municipality TEXT
);

CREATE TABLE IF NOT EXISTS class (
    id TEXT PRIMARY KEY,
    fk_id_center TEXT,
    FOREIGN KEY (fk_id_center) REFERENCES center (id)
);

CREATE TABLE IF NOT EXISTS alumni (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    fk_id_class TEXT,
    FOREIGN KEY (fk_id_class) REFERENCES class (id)
);

CREATE TABLE IF NOT EXISTS daily_log (
    event_date DATE NOT NULL,
    fk_id_class INTEGER NOT NULL,

    num_alumnes INTEGER NOT NULL,
    mal_de_panxa INTEGER NOT NULL,
    calfreds INTEGER NOT NULL,
    mal_de_cap INTEGER NOT NULL,
    mal_de_coll INTEGER NOT NULL,
    mocs INTEGER NOT NULL,
    nas_tapat INTEGER NOT NULL,
    esternut INTEGER NOT NULL,
    vomits INTEGER NOT NULL,
    altres INTEGER NOT NULL,
    be INTEGER NOT NULL,
    regular INTEGER NOT NULL,
    malament INTEGER NOT NULL,
    tos INTEGER NOT NULL,

    FOREIGN KEY (fk_id_class) REFERENCES class (id),
    PRIMARY KEY (event_date, fk_id_class)
);

