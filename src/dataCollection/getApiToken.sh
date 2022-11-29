#!/bin/bash

# Bash script to automate the token-obtaining process

if test -f "./credentials.txt"; # check if 'credentials.txt' default input file containing client id and client secret exists
then
    clientId=$(head -n 1 credentials.txt) # get client id and client secret from 'credentials.txt'
    clientSecret=`sed -n '2p' credentials.txt`
else # else prompt user for client id and client secret
    read -p "Enter client id: " clientId
    read -p "Enter client secret: " clientSecret
fi

credentials=`echo -n $clientId:$clientSecret | openssl base64` # encode the client id and client secret with base64 encoding
credentials=${credentials//$'\n'/} # remove newline character from credentials

# make API request with encoded credentials to get token
apiResponse=`curl -s -X "POST" -H "Authorization: Basic $credentials" -d grant_type=client_credentials https://accounts.spotify.com/api/token`

IFS=', ' read -r -a array <<< "$apiResponse" # read API response into an array and extract the first element
token=${array[0]}

echo "${token//{\"access_token\":\"/}" | sed 's/\"//' # remove surrounding characters to output just the token