"""
NIDS package — exposes a shared in-memory alert store and run-state flag.
"""

from .alert_store import AlertStore

alert_store = AlertStore()
sniffer_running = True   # set False via /api/stop, True via /api/resume
