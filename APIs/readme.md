#### Updated 01/14/2024

# API CALLS

## Section 1: Astronomy Picture of the Day (APOD)

>"One of the most popular websites at NASA is the Astronomy Picture of the Day. In fact, this website is one of the most popular websites across all federal agencies. It has the popular appeal of a Justin Bieber video. This endpoint structures the APOD imagery and associated metadata so that it can be repurposed for other applications. In addition, if the concept_tags parameter is set to True, then keywords derived from the image explanation are returned. These keywords could be used as auto-generated hashtags for twitter or instagram feeds; but generally help with discoverability of relevant imagery." - Nasa Open API

### Components
#### File Structure
- `APOD_API/functions/append_to_json.py`
- `APOD_API/functions/return_json.py`
- `APOD_API/functinos/return_keys.py`
- `APOD_API/JSON_data/apod.json`
- `APOD_API/apod_api.py`

#### Workflow
1. **Makes API Call**\
run `return_json.py`\
*While timeframe = 'historical' returns, this returns all of the APOD for 2024.*

2. **Appends to APOD JSON**\
run `append_to_json.py`\
*Checks to see if date is already within the json and adds if not present.*

## Section 2: Asteroids - Near Earth Objects Web Service

>"NeoWs (Near Earth Object Web Service) is a RESTful web service for near earth Asteroid information. With NeoWs a user can: search for Asteroids based on their closest approach date to Earth, lookup a specific Asteroid with its NASA JPL small body id, as well as browse the overall data-set." - NASA Open API

### Components
#### File Structure
- `NeoWs_API/functions/append_to_json.py`
- `NeoWs_API/functions/return_json.py`
- `NeoWs_API/functinos/return_keys.py`
- `NeoWs_API/JSON_data/neows_api.json`
- `NeoWs_API/neows_api.py`

#### Workflow
1. **Makes API Call**\
run `return_json.py`\
*Automatically returns NeoWs entries for the last week.*
2. **Appends to APOD JSON**\
run `append_to_json.py`\
*Checks to see if date is already within the json and adds if not present.*