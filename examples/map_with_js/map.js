var map;

function initialize() {
    map = L.map('map').setView([59.9, 30.3], 13);

    L.tileLayer('http://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        // id: 'mapbox/streets-v11',
           id: 'mapbox/satellite-streets-v11',
        //    id: 'mapbox/light-v10',
        tileSize: 512,
        zoomOffset: -1
    }).addTo(map);

    new QWebChannel(qt.webChannelTransport, function (channel) {
        window.Window = channel.objects.Window;
        if (typeof Window != 'undefined') {
            var onMapMove = function () {
                Window.onMapMove(map.getCenter().lat, map.getCenter().lng)
            };
            map.on('move', onMapMove);
            onMapMove();
        }
    });
}