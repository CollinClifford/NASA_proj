import subprocess
import os
import logging

logging.basicConfig(filename='logs/main.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

current_directory = os.path.dirname(os.path.abspath(__file__))
cme_api = os.path.join(current_directory, 'CME_API/cme_api.py')
cme_analysis_api = os.path.join(current_directory, 'CMEAnalysis_API/cme_analysis_api.py')
gst_api = os.path.join(current_directory, 'GST_API/gst_api.py')
hss_api = os.path.join(current_directory, 'HSS_API/hss_api.py')
ips_api = os.path.join(current_directory, 'IPS_API/ips_api.py')
mpc_api = os.path.join(current_directory, 'MPC_API/mpc_api.py')
notifications_api = os.path.join(current_directory, 'Notifications_API/notifications_api.py')
rbe_api = os.path.join(current_directory, 'RBE_API/rbe_api.py')
sep_api = os.path.join(current_directory, 'SEP_API/sep_api.py')
wsa_api = os.path.join(current_directory, 'WSA_API/wsa_api.py')

try:
    subprocess.run(['python', cme_api])
    subprocess.run(['python', cme_analysis_api])
    subprocess.run(['python', gst_api])
    subprocess.run(['python', hss_api])
    subprocess.run(['python', ips_api])
    subprocess.run(['python', mpc_api])
    subprocess.run(['python', notifications_api])
    subprocess.run(['python', rbe_api])
    subprocess.run(['python', sep_api])
    subprocess.run(['python', wsa_api])
except Exception as e:
    logging.error(f'One or more subprocesses failed: {e}')