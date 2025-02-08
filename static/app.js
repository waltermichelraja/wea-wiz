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

document.addEventListener('DOMContentLoaded', function () {
    const inputField = document.getElementById('cityInput');
    const suggestionsList = document.getElementById('suggestions-list');

    inputField.addEventListener('input', function () {
        const query = inputField.value.trim();
        if (query.length < 2) {
            suggestionsList.innerHTML = '';
            return;
        }

        fetch(`/get_location_suggestions?q=${query}`)
            .then(response => response.json())
            .then(locations => {
                suggestionsList.innerHTML = '';
                locations.forEach(location => {
                    const listItem = document.createElement('li');
                    listItem.textContent = `${location.name}, ${location.country}`;
                    listItem.addEventListener('click', () => {
                        inputField.value = location.name;
                        suggestionsList.innerHTML = '';
                    });
                    suggestionsList.appendChild(listItem);
                });
            })
            .catch(error => {
                console.error('Error fetching location suggestions:', error);
            });
    });

    document.addEventListener('click', function (event) {
        if (!inputField.contains(event.target) && !suggestionsList.contains(event.target)) {
            suggestionsList.innerHTML = '';
        }
    });
});
