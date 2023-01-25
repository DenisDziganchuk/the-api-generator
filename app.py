from io import BytesIO
from flask import Flask, request, Response
from qrcode import make
from PIL import Image

app = Flask(__name__)

@app.route('/qr', methods=['GET'])
def create_qr():
    url = request.args.get('url')
    qr = make(url)
    img_io = BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)
    return Response(img_io.read(),content_type="image/png")

if __name__ == '__main__':
    app.run(threaded=True, port=80)
