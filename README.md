# Description
Python script to fix issue when loading json with /'s in singlestore

# Example of problem

CREATE TABLE json_test (
    column1 json
);

INSERT INTO json_test (column1)
VALUES ('');
-- Fail

INSERT INTO json_test (column1)
VALUES ('{}');
--PASS

INSERT INTO json_test (column1)
VALUES ('{"test": "3 \" inch"}');
-- Fails but valid json escape

INSERT INTO json_test (column1)
VALUES ('{"test": "3 \\" inch"}');
-- PASSES

SELECT *
FROM json_test;
-- removes the extra escape
