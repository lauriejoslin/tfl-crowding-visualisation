# TfL station crowdedness visualisation

### Summary

This repository utilises the [TFL API](https://api-portal.tfl.gov.uk) to create an interactive map of London showing each underground station's crowdedness over the course of 24 hours. 

The idea behind this was inspired by the idea of [urban metabolism](https://en.wikipedia.org/wiki/Urban_metabolism) and seeing cities as organisms with natural metabolic flows (such as a heartbeat)

I've attached a video here with the link to the interactive version below

https://github.com/user-attachments/assets/495ab2e7-42c4-4d53-82e4-0a1da4273140

[> Open the interactive version](https://lauriejoslin.github.io/tfl-visualisation/interactive.html)

### How it works

This repo is written in Python 

Data side used requests -> pandas -> local sqllite3 

Mapping side sqllite3 -> pandas -> join databases -> plotly express

### Caveats to know

- Station crowding is relative to itself 
- Only underground
    - no overground
    - no national rail
