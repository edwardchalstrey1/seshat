function updateSliderOutput() {
    if (slider.value < 0) {
        output.innerHTML = Math.abs(slider.value) + ' BCE';
    } else {
        output.innerHTML = slider.value + ' CE';
    }
}

function adjustSliderUp() {
    slider.value = Number(slider.value) + 1;
    enterYearInput.value = slider.value; // Sync enterYear input with dateSlide value
    updateSliderOutput(); // Update the displayed year
    plotPolities();
}

function adjustSliderDown() {
    slider.value = Number(slider.value) - 1;
    enterYearInput.value = slider.value; // Sync enterYear input with dateSlide value
    updateSliderOutput(); // Update the displayed year
    plotPolities();
}

function startPlay() {
    stopPlay(); // Clear existing interval before starting a new one

    var animationSpeed = parseFloat(playRateInput.value);
    if (animationSpeed == 1) {
        var yearsPerSecond = 1;
    } else if (animationSpeed == 2) {
        var yearsPerSecond = 5;
    } else if (animationSpeed == 3) {
        var yearsPerSecond = 20;
    } else if (animationSpeed == 4) {
        var yearsPerSecond = 50;
    } else if (animationSpeed == 5) {
        var yearsPerSecond = 100;
    }

    var milliseconds = 1 / (yearsPerSecond / 1000);

    playInterval = setInterval(function () {
        // Increment the slider value by 1
        slider.value = Number(slider.value) + 1;
        enterYearInput.value = slider.value; // Sync enterYear input with dateSlide value
        updateSliderOutput(); // Update the displayed year
        plotPolities();

        // Stop playing when the slider reaches its maximum value
        if (slider.value >= parseInt(slider.max)) {
            stopPlay();
        }
    }, milliseconds); // Interval based on user input
}

function stopPlay() {
    clearInterval(playInterval);
}

function storeYear() {
    var year = document.getElementById('enterYear').value;
    localStorage.setItem('displayedYear', year);
}

// TODO: add these functions, which vary slightly between world_map and polity_map and also need to be modified to not have django code

// function switchBaseMap() {
//     var selectedMap = document.querySelector('input[name="baseMap"]:checked').value;
//     var base = document.getElementById("baseMapGADM").value

//     if (base == 'province') {
//         var baseShapeData = provinceShapeData;
//     } else if (base == 'country') {
//         var baseShapeData = countryShapeData;
//     }

//     // Only show "Current borders" select for GADM
//     var baseMapGADMFieldset = document.getElementById("baseMapGADMFieldset");
//     if (selectedMap == 'gadm') {
//         baseMapGADMFieldset.style.display = "block"
//     } else {
//         baseMapGADMFieldset.style.display = "none"
//     }

//     // Remove all province layers
//     provinceLayers.forEach(function (layer) {
//         map.removeLayer(layer);
//     });

//     // Clear the provinceLayers array
//     provinceLayers = [];

//     map.removeLayer(currentLayer);

//     if (selectedMap === 'osm') {
//         currentLayer = baseLayers.osm.addTo(map);
//     } else {
//         currentLayer = baseLayers.carto.addTo(map);
//     }

//     if (selectedMap === 'gadm') {
//         // Add countries or provinces to the base map
//         baseShapeData.forEach(function (shape) {
//             // Ensure the geometry is not empty
//             if (shape.geometry && shape.geometry.type) {
//                 // Loop through each polygon and add it to the map
//                 for (var i = 0; i < shape.geometry.coordinates.length; i++) {
//                     var coordinates = shape.geometry.coordinates[i][0];
//                     // Swap latitude and longitude for each coordinate
//                     coordinates = coordinates.map(function (coord) {
//                         return [coord[1], coord[0]];
//                     });
//                     var polygon = L.polygon(coordinates).addTo(map);
//                     if (base == 'province') {
//                         polygon.bindPopup(`${shape.province} (${shape.provinceType})`);
//                     } else if (base == 'country') {
//                         polygon.bindPopup(shape.country);
//                     }
//                     // Set the style using the style method
//                     polygon.setStyle({
//                         fillColor: 'white',   // Set the fill color based on the "colour" field
//                         color: 'black',       // Set the border color
//                         weight: 1,            // Set the border weight
//                         fillOpacity: 1        // Set the fill opacity
//                     });
//                     polygon.bringToBack(); // Move the province layers to back so they are always behind polity shapes
//                     provinceLayers.push(polygon); // Add the layer to the array
//                 }
//             }
//         });
//     }
// }

// function plotPolities() {

//     var selectedYear = document.getElementById('dateSlide').value;

//     // Load capital info if not already loaded
//     if (typeof allCapitalsInfo === 'undefined') {
//         var allCapitalsInfo = {{ all_capitals_info | safe }};
//     };

//     // Remove all existing layers from the map
//     map.eachLayer(function (layer) {
//         if (layer instanceof L.GeoJSON || layer instanceof L.CircleMarker) {
//             map.removeLayer(layer);
//         }
//     });

//     // Convert to int, because for some reason JS converts it to a string
//     var selectedYearInt = parseInt(selectedYear);

//     // Add shapes to the map
//     // Don't plot them if "Base map only" checkbox selected
//     if (!document.getElementById('baseMapOnly').checked) {
//         shapesData.forEach(function (shape) {

//             // Make shapes that lack a linked Seshat page stand out
//             if (shape.seshatId in seshatIdPageId) {
//                 var borderColour = shape.colour;
//                 var borderWeight = 0;
//             } else {
//                 // Ed's note: I'm not convinced polity borders look good
//                 var borderColour = shape.colour;
//                 var borderWeight = 0;
//                 // var borderColour = 'red';
//                 // var borderWeight = 1;
//             }

//             // If the shape spans the selected year
//             if ((parseInt(shape.startYear) <= selectedYearInt && parseInt(shape.endYear) >= selectedYearInt)) {

//                 // Format the area float
//                 const formattedArea = parseFloat(shape.area).toLocaleString('en-US', {
//                     minimumFractionDigits: 0,
//                     maximumFractionDigits: 0,
//                     useGrouping: true
//                 });

//                 // Format the years
//                 if (parseInt(shape.polityStartYear) < 0) {
//                     displayStartYear = Math.abs(parseInt(shape.polityStartYear)) + ' BCE';
//                 } else {
//                     displayStartYear = shape.polityStartYear + ' CE';
//                 }

//                 if (parseInt(shape.polityEndYear) == {{ latest_year }}){
//                     displayEndYear = 'Present';
//                 } else {
//                     if (parseInt(shape.polityEndYear) < 0) {
//                         displayEndYear = Math.abs(parseInt(shape.polityEndYear)) + ' BCE';
//                     } else {
//                         displayEndYear = shape.polityEndYear + ' CE';
//                     }
//                 }

//                 // Add shape
//                 var geoJSONLayer = L.geoJSON(JSON.parse(shape.geometry), {           
//                     style: function (feature) {
//                         return {
//                             fillColor: shape.colour,  // Set the fill color based on the "colour" field
//                             color: borderColour,  // Set the border color
//                             weight: borderWeight,  // Set the border weight
//                             fillOpacity: 0.5  // Set the fill opacity
//                         };
//                     },
//                     onEachFeature: function (feature, layer) {
//                         var popupContent = `
//                             <table>
//                                 <tr>
//                                     <th>${shape.name}</th>
//                                     <th></th>
//                                 </tr>
//                         `;
//                         if (shape.seshatId in seshatIdPageId) {
//                             longName = seshatIdPageId[shape.seshatId]['long_name'];
//                             if (longName == '') {
//                                 longName = '[Page empty]'
//                             }
//                             popupContent = popupContent + `
//                                 <tr>
//                                     <td>Seshat Page</td>
//                                     <td>${longName}</td>
//                                 </tr>
//                             `;
//                         }
//                         popupContent = popupContent + `
//                             <tr>
//                                 <td>Range</td>
//                                 <td>${displayStartYear} to ${displayEndYear}</td>
//                             </tr>
//                             <tr>
//                                 <td>Area (est.)</td>
//                                 <td>${formattedArea} Km<sup>2</sup></td>
//                             </tr>
//                         `;
//                         if (allCapitalsInfo[shape.seshatId]) {
//                             popupContent = popupContent + `
//                                 <tr>
//                                     <td>Capital: </td>
//                                     <td>${allCapitalsInfo[shape.seshatId].map(capital => capital.capital).join(', ')}</td>
//                                 </tr>
//                             `;
//                         }
//                         popupContent = popupContent + `</table>`;
//                         layer.bindPopup(popupContent);
//                     }
//                 }).addTo(map);

//                 // Add double-click event listener to GeoJSON layers
//                 geoJSONLayer.on('dblclick', function (event) {
//                     // Check if the shape has a corresponding seshat_id
//                     if (shape.seshatId in seshatIdPageId) {
//                         // Redirect to the corresponding URL
//                         var polityId = seshatIdPageId[shape.seshatId]['id'];
//                         window.location.href = '/core/polity/' + polityId;
//                     }
//                 });

//                 // Plot capital cities for those polities that have them
//                 if (document.getElementById('showCapitals').checked) {
//                     if (allCapitalsInfo[shape.seshatId]) {
//                         allCapitalsInfo[shape.seshatId].forEach(function (capital) {
//                             var marker = L.circleMarker([capital.latitude, capital.longitude], {
//                                 color: shape.colour,
//                                 radius: 5
//                             }).addTo(map);
//                             popupContent = `
//                                 <table>
//                                     <tr>
//                                         <th>${capital.capital}</th>
//                                     </tr>
//                                     <tr>
//                                         <td>${shape.name}</td>
//                                     </tr>
//                                 </table>
//                             `;
//                             marker.bindPopup(popupContent);
//                             marker.on('mouseover', function (e) {
//                                 this.openPopup();
//                             });
//                             marker.on('mouseout', function (e) {
//                                 this.closePopup();
//                             });
//                         });
//                     }
//                 }

//                 // Update the displayedShapes array
//                 if (displayedShapes.indexOf(shape.name) === -1) {
//                     displayedShapes.push(shape.name);
//                 }
//             }
//         });
//     };
// }