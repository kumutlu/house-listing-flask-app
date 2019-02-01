DROP TABLE IF EXISTS houses;

CREATE TABLE IF NOT EXISTS houses (id INTEGER PRIMARY KEY ASC, name TEXT NOT NULL, location TEXT NOT NULL, price INTEGER NOT NUll,size INTEGER NOT NULL, description TEXT NOT NULL, picture TEXT NOT NULL);

INSERT INTO houses 
  (name, location, price, size, description, picture)
VALUES
  ('House Test 1', 'Ankara', '1000', '10', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec elementum sodales tortor tempus pharetra.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/PlaceholderLC.png/600px-PlaceholderLC.png'),
  ('House Test 2', 'Amsterdam', '2000', '20', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec elementum sodales tortor tempus pharetra.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/PlaceholderLC.png/600px-PlaceholderLC.png'),
  ('House Test 3', 'Paris', '3000', '30', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec elementum sodales tortor tempus pharetra.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/PlaceholderLC.png/600px-PlaceholderLC.png')
