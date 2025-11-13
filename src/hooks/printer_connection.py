from brother_ql.raster import BrotherQLRaster
from brother_ql.conversion import convert
from brother_ql.backends.helpers import send
from dotenv import load_dotenv
import os

class printer_connection:
    def __init__(self):
        load_dotenv()
        self.LABEL=os.getenv("LABEL")
        self.MODEL=os.getenv("MODEL")
        self.IP=os.getenv("PRINTER_IP")

    def print(self,img):
        qlr = BrotherQLRaster(self.MODEL)
        qlr.exception_on_warning = True  #  Throw exceptions on warning
        
        # Convert the image into print instructions
        convert(
            qlr,
            [img],        # List of bilds 
            self.LABEL,        # Label-Typ
            threshold=70,
            dither=False,
            compress=True,
            red=False,    # only red/black-Band 
            rotate='auto',
            cut=True,
        )

        # 4) Send to printer
        send(
            instructions=qlr.data,
            printer_identifier=f'tcp://{self.IP}',
            backend_identifier='network',
            blocking=True,
        )

        print("✔ Etikett gesendet!")
