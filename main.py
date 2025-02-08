from flask import Flask, request, jsonify, render_template
from modules.setup import WeaWiz

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if city:
        wea = WeaWiz(city)
        wea.fetch_api()
        if wea.response.status_code == 200:
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

@app.route('/get_location_suggestions', methods=['GET'])
def get_location_suggestions():
    query = request.args.get('q', '').strip()
    if query:
        suggestions = WeaWiz.get_location_suggestions(query)
        return jsonify(suggestions)
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
