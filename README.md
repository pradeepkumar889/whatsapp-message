# whatsapp-message
#send whatsapp message using python and also create API usig flask

import pywhatkit as kit
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/whatsapp_message/<phoneNo>/<message>/<hour>/<minute>", methods=['GET'])
def send_whatsapp_message(phoneNo, message, hour, minute):
    try:
        # Convert hour and minute to integers
        time_hour = int(hour)
        time_minute = int(minute)

        # Send WhatsApp message
        kit.sendwhatmsg(phoneNo, message, time_hour, time_minute)
        return jsonify({"status": "success", "message": "Message sent successfully"}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(port=80, host="0.0.0.0")

