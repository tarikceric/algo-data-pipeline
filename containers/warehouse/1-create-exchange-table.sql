DROP TABLE IF EXISTS algo.exchange;
DROP SCHEMA IF EXISTS algo;
CREATE SCHEMA algo;
CREATE TABLE algo.exchange (
    exchangeId VARCHAR(50),
    name VARCHAR(50),
    url VARCHAR(75),
    active BOOLEAN,
    volumeDaily NUMERIC,
    totalValueLocked NUMERIC,
    dt TIMESTAMP
);