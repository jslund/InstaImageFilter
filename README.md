# Instagram Image Filter

## What does it do?

This is a microservice which is passed data from the InstaDownloader service via RabbitMQ. It submits the URLs from the previous service to the GCP VisionAI service, in order to validate the image and filter it. If the image is successfully validated. The url is then passed on to the next service for downloading and thumbnailing.

## Technical Aspects
This currently uses RabbitMQ and only gets the URL. The end implementation will function as a serverless function scaling out on the MQ size, and sharing objects between services in a protobuf format.

## Setup
For this to run, you need python installed. You also need a google cloud credential for the VisionAI api. After acquiring the credential, set an environment variable called "GOOGLE_APPLICATION_CREDENTIALS" pointing towards your json file.

## TODO
I'll probably port this to C#  later as the gcloud libaries for this are fairly fully fledged