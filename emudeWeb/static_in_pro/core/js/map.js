map = new L.Map('map');

// create the tile layer with correct attribution
var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
var osmAttrib='Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
var osm = new L.TileLayer(osmUrl, {minZoom: 8, maxZoom: 18, attribution: osmAttrib});

// start the map in South-East England
map.setView(new L.LatLng(-22.941446,-43.1823876),12);
map.addLayer(osm);

var marker= L.marker([ -22.9029332, -43.1817541]).addTo(map);
marker.bindPopup("<b>Uruguaiana</b>");


var markerCentral = L.marker([ -22.9035467, -43.1914186]).addTo(map);
markerCentral.bindPopup("<b>Central</b><br>5 assaltos");
