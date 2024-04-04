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
    plotPolities(); // This function is defined differently in the world_map and polity_map templates
}

function adjustSliderDown() {
    slider.value = Number(slider.value) - 1;
    enterYearInput.value = slider.value; // Sync enterYear input with dateSlide value
    updateSliderOutput(); // Update the displayed year
    plotPolities(); // This function is defined differently in the world_map and polity_map templates
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
        plotPolities(); // This function is defined differently in the world_map and polity_map templates

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
    history.pushState(null, '', '/core/world_map/?year=' + year);
    if (!allPolitiesLoaded) {
        // Refresh the page to load all polities
        location.reload();
        var loadingTextElement = document.getElementById('loadingText');
        loadingTextElement.innerHTML = 'Loading polities for <b>' + year + '</b>...';
    }
}

function switchBaseMap() {
    var selectedMap = document.querySelector('input[name="baseMap"]:checked').value;
    var base = document.getElementById("baseMapGADM").value

    if (base == 'province') {
        var baseShapeData = provinceShapeData;
    } else if (base == 'country') {
        var baseShapeData = countryShapeData;
    }

    // Only show "Current borders" select for GADM
    var baseMapGADMFieldset = document.getElementById("baseMapGADMFieldset");
    if (selectedMap == 'gadm') {
        baseMapGADMFieldset.style.display = "block"
    } else {
        baseMapGADMFieldset.style.display = "none"
    }

    // Remove all province layers
    provinceLayers.forEach(function (layer) {
        map.removeLayer(layer);
    });

    // Clear the provinceLayers array
    provinceLayers = [];

    map.removeLayer(currentLayer);

    if (selectedMap === 'osm') {
        currentLayer = baseLayers.osm.addTo(map);
    } else {
        currentLayer = baseLayers.carto.addTo(map);
    }

    if (selectedMap === 'gadm') {
        // Add countries or provinces to the base map
        baseShapeData.forEach(function (shape) {
            // Ensure the geometry is not empty
            if (shape.geometry && shape.geometry.type) {
                // Loop through each polygon and add it to the map
                for (var i = 0; i < shape.geometry.coordinates.length; i++) {
                    var coordinates = shape.geometry.coordinates[i][0];
                    // Swap latitude and longitude for each coordinate
                    coordinates = coordinates.map(function (coord) {
                        return [coord[1], coord[0]];
                    });
                    var polygon = L.polygon(coordinates).addTo(map);
                    if (base == 'province') {
                        var popupContent = `
                            <table>
                                <tr>
                                    <th>${shape.province}</th>
                                    <th></th>
                                </tr>
                                <tr>
                                    <td>Type</td>
                                    <td>${shape.provinceType}</td>
                                </tr>
                                <tr>
                                    <td>Country</td>
                                    <td>Modern ${shape.country}</td>
                                </tr>
                            </table>
                        `;
                    } else if (base == 'country') {
                        var popupContent = `
                            <table>
                                <tr>
                                    <th>Modern ${shape.country}</td>
                                </tr>
                            </table>
                        `;
                    }
                    polygon.bindPopup(popupContent);
                    // Set the style using the style method
                    polygon.setStyle({
                        fillColor: 'white',   // Set the fill color based on the "colour" field
                        color: 'black',       // Set the border color
                        weight: 1,            // Set the border weight
                        fillOpacity: 1        // Set the fill opacity
                    });
                    polygon.bringToBack(); // Move the province layers to back so they are always behind polity shapes
                    provinceLayers.push(polygon); // Add the layer to the array
                }
            }
        });
    }
}

function updateLegend() {
    var variable = document.getElementById('chooseVariable').value;
    var legendDiv = document.getElementById('variableLegend');

    // Clear the current legend
    legendDiv.innerHTML = '';

    if (variable == 'polity') {
        var addedPolities = [];
        var addedPolityNames = [];
        shapesData.forEach(function (shape) {
            if (shape.weight > 0 && !addedPolityNames.includes(shape.name)) {
                // If the shape spans the selected year
                var selectedYear = document.getElementById('dateSlide').value;
                var selectedYearInt = parseInt(selectedYear);
                if ((parseInt(shape.start_year) <= selectedYearInt && parseInt(shape.end_year) >= selectedYearInt)) {
                    // Add the polity to the list of added polities
                    addedPolities.push(shape);
                    addedPolityNames.push(shape.name);
                };
            };
        });

        // Sort the polities by name
        addedPolities.sort(function (a, b) {
            return a.name.localeCompare(b.name);
        });

        // Add a legend for highlighted polities
        if (addedPolities.length > 0) {
            var legendTitle = document.createElement('h3');
            legendTitle.textContent = 'Highlighted Polities';
            legendDiv.appendChild(legendTitle);
            for (var i = 0; i < addedPolities.length; i++) {
                var legendItem = document.createElement('p');
                var colorBox = document.createElement('span');
                colorBox.style.display = 'inline-block';
                colorBox.style.width = '20px';
                colorBox.style.height = '20px';
                colorBox.style.backgroundColor = addedPolities[i].colour;
                colorBox.style.border = '1px solid black';
                colorBox.style.marginRight = '10px';
                legendItem.appendChild(colorBox);
                legendItem.appendChild(document.createTextNode(addedPolities[i].name));
                legendDiv.appendChild(legendItem);
            }
        };

    } else if (variable == 'language') {
        displayLanguages = {};
        shapesData.forEach(function (shape) {
            if (shape.weight > 0) {
                // Add the language to the dict to be used in the legend
                displayLanguages[shape.language] = shape.language_colour;
            };
        });
        // Sort the languages alphabetically
        displayLanguages = Object.keys(displayLanguages).sort().reduce((obj, key) => {
            obj[key] = displayLanguages[key];
            return obj;
        }, {});

        // Add a legend for highlighted polities
        if (Object.keys(displayLanguages).length > 0) {
            var legendTitle = document.createElement('h3');
            legendTitle.textContent = 'Languages';
            legendDiv.appendChild(legendTitle);
            // Iterate throgugh the languages and add them to the legend
            for (var language in displayLanguages) {
                var legendItem = document.createElement('p');
                var colorBox = document.createElement('span');
                colorBox.style.display = 'inline-block';
                colorBox.style.width = '20px';
                colorBox.style.height = '20px';
                colorBox.style.backgroundColor = displayLanguages[language];
                colorBox.style.border = '1px solid black';
                colorBox.style.marginRight = '10px';
                legendItem.appendChild(colorBox);
                legendItem.appendChild(document.createTextNode(language));
                legendDiv.appendChild(legendItem);
            }
        };

    } else {
        var legendTitle = document.createElement('h3');
        legendTitle.textContent = variable;
        legendDiv.appendChild(legendTitle);

        for (var key in variableColourMapping) {
            var legendItem = document.createElement('p');
            var colorBox = document.createElement('span');

            colorBox.style.display = 'inline-block';
            colorBox.style.width = '20px';
            colorBox.style.height = '20px';
            colorBox.style.backgroundColor = variableColourMapping[key];
            colorBox.style.marginRight = '10px';

            legendItem.appendChild(colorBox);
            if (key === 'A~P') {
                legendItem.appendChild(document.createTextNode('Absent then present'));
            } else if (key === 'P~A') {
                legendItem.appendChild(document.createTextNode('Present then absent'));
            } else {
                legendItem.appendChild(document.createTextNode(`${key[0].toUpperCase()}${key.slice(1)}`));
            }

            legendDiv.appendChild(legendItem);
        }

        if (document.querySelector('input[name="baseMap"]:checked').value == 'gadm') {
            var legendItem = document.createElement('p');
            var colorBox = document.createElement('span');

            colorBox.style.display = 'inline-block';
            colorBox.style.width = '20px';
            colorBox.style.height = '20px';
            colorBox.style.backgroundColor = 'white';
            colorBox.style.border = '1px solid black';
            colorBox.style.marginRight = '10px';

            legendItem.appendChild(colorBox);
            legendItem.appendChild(document.createTextNode('Base map'));

            legendDiv.appendChild(legendItem);
        }
    }
}