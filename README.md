#FRONDZ & cachecomix.com
Based on the original NomeBot in Haskell. A Flask app for both NomeBot and FritzBot. Currently contains a number of hardcoded assumptions for usage but could easily be modified to support new bots.

Uses Markov chains to create arbitrary, probabilistic text from a given corpus. Does not train during conversations--must be run in training mode to establish the database. 
