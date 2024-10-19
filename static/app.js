document.getElementById('getWeatherBtn').addEventListener('click', function() {
    const city = document.getElementById('cityInput').value;
    if (city) {
        fetch(`/weather?city=${city}`)
            .then(response => response.json())
            .then(data => {
                const weatherResult = document.getElementById('weatherResult');
                if (data.error) {
                    weatherResult.innerHTML = `Error: ${data.error}`;
                } else {
                    weatherResult.innerHTML = `
                        <h2>Weather in ${data.city}</h2>
                        <p>Temperature: ${data.temperature}°C</p>
                        <p>Feels Like: ${data.feels_like}°C</p>
                        <p>Humidity: ${data.humidity}</p>
                        <p>Clouds: ${data.clouds}</p>
                        <p>Pressure: ${data.pressure}</p>
                        <p>Wind Speed: ${data.wind} m/s</p>
                    `;
                }
            })
            .catch(err => console.error('Error:', err));
    } else {
        alert('Please enter a city name');
    }
});
