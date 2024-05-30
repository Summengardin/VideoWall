#!/bin/bash



sudo wget https://developer.download.nvidia.com/designworks/video-codec-sdk/secure/12.2/Video_Codec_Interface_12.2.72.zip?iIGCMN73hvCjSrfFX6UxOWDuiLORAvKWA635zH6fp8uLUSnwPiOKWwbqtLOa6BtZO5hTHLYBNoAZkGkuiuPLJgbFJqLNJDho08aXHACgNz03Eq2RtP7zA8i4X_iv9ju01ceUQR_lomGP71jlyi25hNG8Ernqf8239B5o0fBp-lgDUSM65zBI5A==&t=eyJscyI6ImdzZW8iLCJsc2QiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyJ9
sudo tar -xvf Video_Codec_Interface*.zip
cd Video_Codec_Interface*
sudo cp Interface/* /usr/local/cuda/include/