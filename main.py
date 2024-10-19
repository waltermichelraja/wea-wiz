from flask import Flask, request, jsonify, render_template
from modules.setup import WeaWiz

app = Flask(__name__)

@app.route('/')
def index():
    # Render the HTML front end
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if city:
        # Fetch weather data
        wea = WeaWiz(city)
        wea.fetch_api()
        if wea.response.status_code == 200:
            # Process the response and return JSON
            data = wea.data
            main = data.get("main", {})
            report = {
                "city": wea.city,
                "temperature": main.get("temp"),
                "feels_like": main.get("feels_like"),
                "humidity": str(main.get("humidity")) + "%",
                "clouds": str(data.get("clouds", {}).get("all")) + "%",
                "pressure": str(main.get("pressure")) + "mb",
                "wind": data['wind'].get('speed')
            }
            return jsonify(report)
        else:
            return jsonify({"error": "Unable to fetch weather data."}), 500
    else:
        return jsonify({"error": "City not provided."}), 400

if __name__ == '__main__':
    app.run(debug=True)
