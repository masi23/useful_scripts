This little project exists only because I needed postcodes ranges for each Bundesland in Germany and I couldn't find such information in correct form on any available website. 

The program reads file 'German-Zip-Codes.csv' (which I borrowed from user 'jbspeakr'. The result of this program is the file 'summary.csv' which contains 3 columns called: land, code_prefix and code_range. 

Although my program isn't perfect (for example you can find one range consist of values that fit in another range or you can find that ranges contain values that aren't existing postcodes in Germany).
Nevertheless such data result totally fit my requirements.

I share this mostly as an example of creating code that solves specific and unexpected problem.
