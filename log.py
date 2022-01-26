import logging

def lg(log):
    logging.basicConfig(filename="kivy.log", level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.info(log)

