#### Updated 01/14/2024

# Data Factory Initialization

## Section 1: Astronomy Picture of the Day (APOD)

>"One of the most popular websites at NASA is the Astronomy Picture of the Day. In fact, this website is one of the most popular websites across all federal agencies. It has the popular appeal of a Justin Bieber video. This endpoint structures the APOD imagery and associated metadata so that it can be repurposed for other applications. In addition, if the concept_tags parameter is set to True, then keywords derived from the image explanation are returned. These keywords could be used as auto-generated hashtags for twitter or instagram feeds; but generally help with discoverability of relevant imagery." - Nasa Open API

### Components
#### File Structure
- `APOD_DF/sql_commands/create_table.py`
- `APOD_DF/sql_commands/drop_table.py`
- `APOD_DF/sql_commands/insert_data.py`
- `APOD_DF/sql_commands/select_all.py`
- `APOD_DF/apod_df.py`

#### Workflow
1. **Makes API Call**\
run `apod_df.py`\
*Triggers sql_commands functions and updates database.*

## Section 2: Asteroids - Near Earth Objects Web Service

>"NeoWs (Near Earth Object Web Service) is a RESTful web service for near earth Asteroid information. With NeoWs a user can: search for Asteroids based on their closest approach date to Earth, lookup a specific Asteroid with its NASA JPL small body id, as well as browse the overall data-set." - NASA Open API

### Components
#### File Structure
- `NeoWS_DF/sql_commands/create_table.py`
- `NeoWS_DF/sql_commands/drop_table.py`
- `NeoWS_DF/sql_commands/insert_data.py`
- `NeoWS_DF/sql_commands/select_all.py`
- `NeoWS_DF/neows_DF.py`

#### Workflow
1. **Makes API Call**\
run `apod_df.py`\
*Triggers sql_commands functions and updates database.*