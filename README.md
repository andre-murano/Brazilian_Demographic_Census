# public-health
This git was created to get data from public environments and process to a DB (Cloud or Local)

# Downloading files from FTP
We have the connector to connect directly to source.
Then we need to use a file controller, to get a non processed file from the source. 
When the file is processed, we need to create a register on our base to set a positive control. If we need to reprocess a file, just set up as false.

# Processing
Every file processed will me mapped with file columns. This maybe generate a problem if the file changes, but will be improve.
Processing must collect the file and turn into a parquet.

# Targets
Our target, in a first sight will be a SGDB. We are difining if will be a cloud or local.
