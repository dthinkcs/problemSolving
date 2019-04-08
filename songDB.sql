CREATE TABLE likes (
    userId INTEGER NOT NULL,
    songId INTEGER NOT NULL,
    createdAt TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY(userId) REFERENCES users(id),
    FOREIGN KEY(songId) REFERENCES songs(id),
    PRIMARY KEY(userId, songId)
);

CREATE TABLE dislikes (
    userId INTEGER NOT NULL,
    songId INTEGER NOT NULL,
    createdAt TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY(userId) REFERENCES users(id),
    FOREIGN KEY(songId) REFERENCES songs(id),
    PRIMARY KEY(userId, songId)
);


CREATE TABLE history (
    userId INTEGER NOT NULL,
    songId INTEGER NOT NULL,
    listenedAt TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY(userId) REFERENCES users(id),
    FOREIGN KEY(songId) REFERENCES songs(id),
    PRIMARY KEY(userId, songId)
);

CREATE TABLE comments (
  id INTEGER NOT NULL AUTO_INCREMENT,
  userId INTEGER NOT NULL,
  songId INTEGER NOT NULL,
  commentText VARCHAR(255) NOT NULL,
  createdAt TIMESTAMP DEFAULT NOW(),
  FOREIGN KEY(userId) REFERENCES users(id),
  FOREIGN KEY(songId) REFERENCES songs(id),
  PRIMARY KEY(id)
);

INSERT INTO comments (userId, songId, commentText) VALUES (1, 1, 'Good Song');
