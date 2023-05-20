// Replace 'YOUR_API_KEY' with your actual API key
const apiKey = 'YOUR_API_KEY';

// Initialize the map
function initMap() {
    const container = document.getElementById('map-container');
    
    // Set the initial location and zoom level
    const options = {
        center: { lat: 0, lng: 0 },
        zoom: 10
    };
    
    // Create the map object
    const map = new google.maps.Map(container, options);
    
    // Get the user's current location
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            position => {
                const { latitude, longitude } = position.coords;
                
                // Center the map on the user's location
                map.setCenter({ lat: latitude, lng: longitude });
                
                // Add a marker to represent the user's location
                new google.maps.Marker({
                    position: { lat: latitude, lng: longitude },
                    map: map,
                    title: 'You are here'
                });
            },
            error => {
                console.error(error.message);
            }
        );
    } else {
        console.error('Geolocation is not supported by this browser.');
    }
}
