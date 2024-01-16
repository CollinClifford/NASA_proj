#### Updated 01/15/2024

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
- `NeoWs_API/neows.py`

#### Workflow
1. **Makes API Call**\
run `return_json.py`\
*Automatically returns NeoWs entries for the last week.*
2. **Appends to APOD JSON**\
run `append_to_json.py`\
*Checks to see if date is already within the json and adds if not present.*

## Section 3: Space Weather Database Of Notifications, Knowledge, Information (DONKI)

>"The Space Weather Database Of Notifications, Knowledge, Information (DONKI) is a comprehensive on-line tool for space weather forecasters, scientists, and the general space science community. DONKI chronicles the daily interpretations of space weather observations, analysis, models, forecasts, and notifications provided by the Space Weather Research Center (SWRC), comprehensive knowledge-base search functionality to support anomaly resolution and space science research, intelligent linkages, relationships, cause-and-effects between space weather activities and comprehensive webservice API access to information stored in DONKI." - NASA Open API

### APIs in this section:
- Coronal Mass Ejection (CME)
- Coronal Mass Ejection (CME) Analysis
- Geomagnetic Storm (GST)
- Interplanetary Shock (IPS)
- Solar Flare (FLR)
- Solar Energetic Particle (SEP)
- Magnetopause Crossing (MPC)
- Radiation Belt Enhancement (RBE)
- Hight Speed Stream (HSS)
- WSA+EnlilSimulation
- Notifications

### Components
#### File Structure
- `DONKI_API/CME_API/functions/append_to_json.py`
- `DONKI_API/CME_API/functions/return_json.py`
- `DONKI_API/CME_API/functinos/return_keys.py`
- `DONKI_API/CME_API/JSON_data/cme.json`
- `DONKI_API/CME_API/cme_api.py`
- `DONKI_API/CMEAnalysis_API/functions/append_to_json.py`
- `DONKI_API/CMEAnalysis_API/functions/return_json.py`
- `DONKI_API/CMEAnalysis_API/functinos/return_keys.py`
- `DONKI_API/CMEAnalysis_API/JSON_data/cme_analysis.json`
- `DONKI_API/CMEAnalysis_API/cme_analysis.py`
- `DONKI_API/GST_API/functions/append_to_json.py`
- `DONKI_API/GST_API/functions/return_json.py`
- `DONKI_API/GST_API/functinos/return_keys.py`
- `DONKI_API/GST_API/JSON_data/gst.json`
- `DONKI_API/GST_API/gst_api.py`
- `DONKI_API/HSS_API/functions/append_to_json.py`
- `DONKI_API/HSS_API/functions/return_json.py`
- `DONKI_API/HSS_API/functinos/return_keys.py`
- `DONKI_API/HSS_API/JSON_data/hss.json`
- `DONKI_API/HSS_API/hss_api.py`
- `DONKI_API/IPS_API/functions/append_to_json.py`
- `DONKI_API/IPS_API/functions/return_json.py`
- `DONKI_API/IPS_API/functinos/return_keys.py`
- `DONKI_API/IPS_API/JSON_data/ips.json`
- `DONKI_API/IPS_API/ips_api.py`
- `DONKI_API/MPC_API/functions/append_to_json.py`
- `DONKI_API/MPC_API/functions/return_json.py`
- `DONKI_API/MPC_API/functinos/return_keys.py`
- `DONKI_API/MPC_API/JSON_data/mpc.json`
- `DONKI_API/MPC_API/mpc_api.py`
- `DONKI_API/Notifications_API/functions/append_to_json.py`
- `DONKI_API/Notifications_API/functions/return_json.py`
- `DONKI_API/Notifications_API/functinos/return_keys.py`
- `DONKI_API/Notifications_API/JSON_data/notifications.json`
- `DONKI_API/Notifications_API/notifications_api.py`
- `DONKI_API/RBE_API/functions/append_to_json.py`
- `DONKI_API/RBE_API/functions/return_json.py`
- `DONKI_API/RBE_API/functinos/return_keys.py`
- `DONKI_API/RBE_API/JSON_data/rbe.json`
- `DONKI_API/RBE_API/rbe_api.py`
- `DONKI_API/SEP_API/functions/append_to_json.py`
- `DONKI_API/SEP_API/functions/return_json.py`
- `DONKI_API/SEP_API/functinos/return_keys.py`
- `DONKI_API/SEP_API/JSON_data/sep.json`
- `DONKI_API/SEP_API/sep_api.py`
- `DONKI_API/WSA_API/functions/append_to_json.py`
- `DONKI_API/WSA_API/functions/return_json.py`
- `DONKI_API/WSA_API/functinos/return_keys.py`
- `DONKI_API/WSA_API/JSON_data/wsa.json`
- `DONKI_API/WSA_API/wsa_api.py`
- `DONKI_API/donki_api.py`

#### Workflow
1. ***Calls 10 DONKI APIs in order*\
run `donki_api.py`
2. **Each Makes API Call**\
run `return_json.py`\
*Automatically returns DONKI entries for 2024.*
2. **Each Appends to APOD JSON**\
run `append_to_json.py`\
*Checks to see if date is already within the json and adds if not present.*