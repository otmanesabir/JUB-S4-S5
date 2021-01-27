records = LOAD 'sample_orig.txt' USING org.apache.pig.piggybank.storage.FixedWidthLoader('16-19,88-92,93') AS (year:chararray, temp:int, q:int);
filtered = FILTER records BY temp != 9999 AND q IN (0,1,4,5,9);
grouped = GROUP filtered BY year;
max_temp = FOREACH grouped GENERATE group, MAX(filtered.temp);
STORE max_temp INTO 'output';
