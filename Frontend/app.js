const express = require('express');
const querystring = require('querystring');
const axios = require('axios');
const generateRandomString = require('./utils'); // Assuming generateRandomString function is in utils.js
const fs = require('fs');
const session = require('express-session');

const client_id = 'f484bbc1fd7b437e878bbc2621125371'; // Replace with your actual Spotify client ID
const client_secret = '1d4c28ddded7466a901474025ddfdb53'; // Replace with your actual Spotify client secret
const redirect_uri = 'https://40b2564e-9d41-495b-880e-6e7ebde6d53b-00-1f7gzp5xpqg5z.spock.replit.dev/callback'; // Replace with your actual redirect URI

const app = express();
const port = 8888;
const filepath = './song_data.json';

// Use session to manage user-specific data
app.use(session({
    secret: 'your_secret_key',
    resave: false,
    saveUninitialized: true
}));

const stateKey = 'spotify_auth_state';
let old_data = {};

async function fetchCurrentlyPlaying(access_token) {
    try {
        if (!access_token) {
            console.error('Access token not set. Cannot fetch currently playing track.');
            return;
        }

        const apiOptions = {
            url: 'https://api.spotify.com/v1/me/player/currently-playing',
            method: 'get',
            headers: {
                'Authorization': 'Bearer ' + access_token
            }
        };

        const apiResponse = await axios(apiOptions);
        return apiResponse.data;

    } catch (error) {
        console.error('Error fetching currently playing track:', error.response ? error.response.data : error.message);
        throw error;
    }
}

app.get('/login', (req, res) => {
    const state = generateRandomString(16);
    const scope = 'user-read-currently-playing user-read-playback-state';
    res.cookie(stateKey, state);

    res.redirect('https://accounts.spotify.com/authorize?' +
        querystring.stringify({
            response_type: 'code',
            client_id: client_id,
            scope: scope,
            redirect_uri: redirect_uri,
            state: state
        }));
});

app.get('/callback', async (req, res) => {
    const code = req.query.code || null;
    const state = req.query.state || null;

    if (!state) {
        res.redirect('/#' +
            querystring.stringify({
                error: 'state_mismatch'
            }));
        return;
    }

    res.clearCookie(stateKey);

    try {
        const tokenParams = {
            grant_type: 'authorization_code',
            code: code,
            redirect_uri: redirect_uri
        };

        const authOptions = {
            url: 'https://accounts.spotify.com/api/token',
            method: 'post',
            params: tokenParams,
            headers: {
                'Authorization': 'Basic ' + Buffer.from(client_id + ':' + client_secret).toString('base64')
            }
        };

        const response = await axios(authOptions);
        req.session.access_token = response.data.access_token; // Store access_token in session

        // Redirect to the fetch route to start fetching currently playing track
        res.redirect('/fetch-currently-playing');
    } catch (error) {
        console.error('Error:', error.response ? error.response.data : error.message);
        res.status(500).send('Error: Unable to retrieve access token.');
    }
});

app.get('/fetch-currently-playing', async (req, res) => {
    try {
        const access_token = req.session.access_token;

        setInterval(async () => {
            try {
                const trackData = await fetchCurrentlyPlaying(access_token);

                if (trackData && trackData.item) {
                    const song_id = trackData.item.id;
                    const song_name = trackData.item.name;
                    const artist = trackData.item.album.artists[0].name;

                    const data = { id: song_id, name: song_name, artist: artist };
                    const jsonData = JSON.stringify(data, null, 2);

                    if (JSON.stringify(old_data) !== jsonData) {
                        old_data = data;

                        fs.writeFile(filepath, jsonData, 'utf8', (err) => {
                            if (err) {
                                console.error('Error writing file:', err);
                                return;
                            }
                            console.log('File successfully written:', jsonData);
                        });
                        console.log('Currently playing:', trackData.item.album.artists[0].name);
                    } else {
                        console.log('Still the same song playing...');
                    }
                }
            } catch (error) {
                console.error('Error fetching currently playing track:', error.message);
            }
        }, 5000);

        res.send('Started fetching currently playing track every 5 seconds.');
    } catch (error) {
        console.error('Error:', error.message);
        res.status(500).send('Error: Unable to start fetching currently playing track.');
    }
});
let lyricsContent = '';
const lyricsFilePath = "lyrics.txt";
// Function to read lyrics from file
function readLyricsFile() {
    fs.readFile(lyricsFilePath, 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading file:', err);
            lyricsContent = 'Error reading lyrics file';
            return;
        }
        lyricsContent = data;
    });
}

// Initial read of the lyrics file
readLyricsFile();

// Watch for changes in the lyrics file
fs.watch(lyricsFilePath, (eventType, filename) => {
    if (eventType === 'change') {
        console.log('lyrics.txt file has been updated');
        readLyricsFile(); // Re-read the file on change
    }
});

// Route to display lyrics
app.get('/lyrics', (req, res) => {
    res.send(`<pre>${lyricsContent}</pre>`);
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
