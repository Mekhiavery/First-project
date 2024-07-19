CREATE TABLE Companies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    ticker_symbol VARCHAR(10) NOT NULL
);

CREATE TABLE Markets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL
);

CREATE TABLE Stocks (
    id SERIAL PRIMARY KEY,
    company_id INTEGER REFERENCES Companies(id),
    market_id INTEGER REFERENCES Markets(id),
    date DATE NOT NULL,
    open_price NUMERIC(10, 2),
    high_price NUMERIC(10, 2),
    low_price NUMERIC(10, 2),
    close_price NUMERIC(10, 2),
    volume BIGINT
);
