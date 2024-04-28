CREATE TABLE weekly_zone_aggregates AS
SELECT
  EXTRACT(YEAR FROM CAST(tpep_pickup_datetime AS TIMESTAMP)) AS year,
  EXTRACT(WEEK FROM CAST(tpep_pickup_datetime AS TIMESTAMP)) AS week,
  "PULocationID",
  SUM("passenger_count") AS total_passengers,
  SUM("trip_distance") AS total_distance,
  SUM("total_amount") AS total_amount
FROM
  taxi_trips
WHERE
  CAST(tpep_pickup_datetime AS TIMESTAMP) BETWEEN '2018-01-01 00:00:00' AND '2022-12-31 23:59:59'
GROUP BY
  year,
  week,
  "PULocationID"
ORDER BY
  year,
  week,
  "PULocationID";


COPY weekly_zone_aggregates TO '../../data/interim/weekly_zone_aggregates.csv' DELIMITER ',' CSV HEADER;