CREATE TABLE Trip (
    trip_id INTEGER PRIMARY KEY AUTOINCREMENT,
    destination TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    budget REAL,
    preferences TEXT,
    notes TEXT
);
