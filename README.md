# DSCI550_HW_BIGDATA_SEMAFOR

First run

pip install requirements.txt


Then the following are the scripts
Q4:
a. Lab Size: definition: co-authors; source: ResearchGate
	Code: ResearchGateScrape/ResearchGateScrapeAuthorsLabSize.py
b. Publication Rate: definition: how many papers published in a year: PR =  total number of papers /(2022 - year of first paper); source: Google Scholar 
	Code: GScholarScrape/GoogleScholarScrapeJson/gscholarextractjsonPubRate.py

c. Other Journals Published In: source: Google Scholar
	Code: 
	GScholarScrape/GoogleScholarScrapeJson/gscholarextractjson-auth-titles.py
	GScholarScrape/Journal/gscholarJournalScraper.py

d. Information about First Author including:							
	i. Affiliation University: source: DOI 
		Code: institution_info.py

	ii. Duration of Career (Years): DC = 2022 - year of first article; source: Google Scholar
		Code: ScholarScrape/GoogleScholarScrapeJson/gscholarextractjsonPubRate.py
		
	iii. Highest degree obtained: source: ResearchGate 
		Code: ResearchGateScrape/ResearchGateScrapeFirAuth.py 
		
	iv. Degree Area: source: ResearchGate		
		Code: ResearchGateScrape/ResearchGateScrapeFirAuthDegree.py

Others: JoinAuthFeatures.py was used to join part of the author features to the original file.
	Code: JoinAuthFeatures/JoinAuthFeatures.py


datasets:
JoinAuthFeatures/JoinAuthFeatures.ipynb

Location/location_extraction.ipynb
Location/world_cities_dataset.ipynb
Weather/weather.ipynb

GoogleMapsAPI/Combine_dataset.ipynb

