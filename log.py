import logging

log = logging.getLogger("LOG PRUEBA")
logging.basicConfig(level=logging.ERROR, format='%(asctime)s %(name)s - %(levelname)s - %(message)s')


log.info("Esto es un mensaje ")
log.warning("Esto es un warning")
log.error("Esto es un error")