# src/mqtt/tls_config.py

import ssl
from utils.logger import get_logger

logger = get_logger("TLS Config")


def configure_tls(client, ca_certs, certfile, keyfile):
    try:
        client.tls_set(
            ca_certs=ca_certs,
            certfile=certfile,
            keyfile=keyfile,
            tls_version=ssl.PROTOCOL_TLS_CLIENT
        )
        client.tls_insecure_set(False)
        logger.info("TLS configuration applied.")
    except Exception as e:
        logger.error(f"TLS configuration failed: {e}")
        raise
