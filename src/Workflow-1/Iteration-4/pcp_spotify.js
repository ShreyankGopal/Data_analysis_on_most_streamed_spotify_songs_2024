d3.csv("spotify_dom.csv").then(function(rows) {
    function unpack(rows, key) {
        return rows.map(row => row[key]);
    }

    // Encode unique genres
    const genres = Array.from(new Set(unpack(rows, 'track_genre'))); // Get unique genres
    const genreMapping = {};
    genres.forEach((genre, index) => {
        genreMapping[genre] = index + 1; // Map genre names to numeric values
    });

    // Encode unique artists
    const artists = Array.from(new Set(unpack(rows, 'artists'))); // Get unique artists
    const artistMapping = {};
    artists.forEach((artist, index) => {
        artistMapping[artist] = index + 1; // Map artist names to numeric values
    });

    // Add numeric columns for genre and artist
    rows.forEach(row => {
        row.track_genre_encoded = genreMapping[row.track_genre];
        row.artist_encoded = artistMapping[row.artists];
    });

    // Define the data for the Parallel Coordinates Plot
    var data = [{
        type: 'parcoords',
        pad: [80, 80, 80, 80],
        line: {
            color: unpack(rows, 'track_genre_encoded'), // Use encoded genre for color
            colorscale: [[0, 'purple'], [0.5, 'orange'], [1, 'cyan']] // Update the colors as needed
        },

        dimensions: [{
            label: 'Artist (Encoded)',
            range: [1, artists.length],
            tickvals: Object.values(artistMapping),
            ticktext: Object.keys(artistMapping),
            values: unpack(rows, 'artist_encoded')
        }, {
            label: 'Explicit',
            range: [0, 1], // Adjust the range as per your data
            values: unpack(rows, 'explicit')
        }, {
            label: 'Track Genre (Encoded)',
            range: [1, genres.length],
            tickvals: Object.values(genreMapping),
            ticktext: Object.keys(genreMapping),
            values: unpack(rows, 'track_genre_encoded')
        }, {
            label: 'Danceability',
            range: [0, 1],
            values: unpack(rows, 'danceability')
        }, {
            label: 'Energy',
            range: [0, 1],
            values: unpack(rows, 'energy')
        }, {
            label: 'Loudness',
            range: [-60, 0], // Adjust for loudness range
            values: unpack(rows, 'loudness')
        }, {
            label: 'Speechiness',
            range: [0, 1],
            values: unpack(rows, 'speechiness')
        }, {
            label: 'Instrumentalness',
            range: [0, 1],
            values: unpack(rows, 'instrumentalness')
        }, {
            label: 'Liveness',
            range: [0, 1],
            values: unpack(rows, 'liveness')
        }, {
            label: 'Tempo',
            range: [0, 300], // Adjust tempo range as necessary
            values: unpack(rows, 'tempo')
        }]
    }];

    // Layout for the plot
    var layout = {
        width: 1200,
        height: 600,
        title: "Parallel Coordinates Plot of Spotify Dominating Category"
    };

    // Render the plot
    Plotly.newPlot('myDiv', data, layout);
}).catch(function(error) {
    console.error("Error loading CSV:", error);
});