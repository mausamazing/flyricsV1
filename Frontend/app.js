const express = require('express');
const querystring = require('querystring');
const axios = require('axios');
const generateRandomString  = require('./utils'); // Assuming generateRandomString function is in utils.js
const fs = require('fs')

const client_id = '87fd73f8d16c4fc5bd6b348962c683f1'; // Replace with your actual Spotify client ID
const client_secret = '2caf8fd686d54b1a9f4a07de0eda9e2b'; // Replace with your actual Spotify client secret
const redirect_uri = 'http://localhost:8888/callback'; // Replace with your actual redirect URI

const app = express();
const port = 8888;
const filepath = "./song_data.json"
// Define stateKey for CSRF protection (this should match what you set in your application)
const stateKey = 'spotify_auth_state';
let access_token = null;
let song_id;
// Route handler for initiating the Spotify authentication process
async function fetchCurrentlyPlaying() {
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
      return apiResponse.data; // Return the currently playing track data
  
    } catch (error) {
      console.error('Error:', error.message);
      throw error; // Propagate error to handle it elsewhere
    }
  }
  
  // Interval to fetch currently playing track every 5 seconds
  setInterval(async () => {
    try {
      const trackData = await fetchCurrentlyPlaying();
      // Here you can broadcast or handle the updated trackData as needed
      song_id = trackData.item.id;
      data = {id:song_id}
      const jsonData = JSON.stringify(data, null, 2);
      fs.writeFile(filepath, jsonData, 'utf8', (err) => {
        if (err) {
          console.error('Error writing file:', err);
          return;
        }});
      console.log('Currently playing:', trackData.item.id);
    } catch (error) {
      console.error('Error fetching currently playing track:', error.message);
    }
  }, 5000);
  
  // Route handler for initiating the Spotify authentication process
  app.get('/login', (req, res) => {
    const state = generateRandomString(16);
    const scope = 'user-read-currently-playing'; // Only user-read-currently-playing scope
  
    res.cookie(stateKey, state);
  
    res.redirect('https://accounts.spotify.com/authorize?' +
      querystring.stringify({
        response_type: 'code',
        client_id: client_id,
        scope: scope,
        redirect_uri: redirect_uri,
        state: state
      }));
    app.get("/", (req,res) => {
        res.send("<h1>Helo</h1>");
    })
  });
  
  // Route handler for handling the callback from Spotify
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
      access_token = response.data.access_token; // Store access_token globally
  
      // Redirect or send response as needed
      res.redirect('/'); // Redirect to home page or dashboard
    } catch (error) {
      console.error('Error:', error.message);
      res.status(500).send('Error: Unable to retrieve access token.');
    }
  });
  
  app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
  });