from flask import Flask, render_template, request, url_for, redirect, send_file, session, jsonify
from pytube import YouTube
from io import BytesIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "654c0fb3968af9d5e6a9b3edcbc7051b"

# url = YouTube('https://www.youtube.com/watch?v=7BXJIjfJCsA')
# for stream in url.streams:
#     if (stream.mime_type == 'video/mp4' or stream.mime_type == 'audio/mp4'):
#         stream = url.streams.get_by_itag(22)
#         stream.download()
    

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

# @app.route("/youtube", methods = ["GET"])
# def home():
#     # session['link'] = request.form.get('url')
#     # try:
#     url = YouTube('https://www.youtube.com/watch?v=7BXJIjfJCsA')
#     url.check_availability()
#     print(url.streams)
#     data = [{'author':url.author,'bypass_age_gate()':url.bypass_age_gate(), 'channel_id':url.channel_id}]
#     return jsonify({'results': data})
#     # except:
#     #     return render_template("error.html")
#     # return render_template("download.html", url = url)

@app.route("/download-video", methods = ["GET"])
def download_video():
    buffer = BytesIO()
    url = YouTube('https://www.youtube.com/watch?v=7BXJIjfJCsA')
    itag = 22
    video = url.streams.get_by_itag(itag)
    video.stream_to_buffer(buffer)
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, attachment_filename ="VideoYT2Video.mp4", mimetype="video/mp4")

if __name__ == '__main__':
    app.run(debug=True)