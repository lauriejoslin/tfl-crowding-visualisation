# London Underground crowding visualisation

## Summary

This repository utilises the TfL API[^1] to create an interactive map of London showing each underground station's crowdedness over the course of 24 hours. This data is aggregated over the course of the week (Monday - Friday). The aim was to create a natural visualisation which showed spikes in the morning and afternoon when people go to/from work. 

The idea behind this was inspired by the idea of urban metabolism[^2] and seeing cities as organisms with natural metabolic flows (such as a heartbeat). In this way, I wanted to see if the visualisation showed the heartbeat of London in the morning and afternoon at this macroscopic change

If I were to extend this project, it would be very interesting to see the flow of e-bikes (e.g. Lime bikes) - I can imagine a pulsing effect in and out of the central boroughs over the course of the day.  

I've attached a video here with the link to the interactive version below

https://github.com/user-attachments/assets/495ab2e7-42c4-4d53-82e4-0a1da4273140

[**> Open the interactive version**](https://lauriejoslin.github.io/tfl-crowding-visualisation/interactive.html)

## How it works

### Data processing

Python requests module -> Tfl REST API
Into pandas -> into sqllite3

### Mapping

Out of sqllite3 
Join dataframes
Plotly express using time series

Mapping side sqllite3 -> pandas -> join databases -> plotly express

### Caveats to know

- Station crowding is relative to itself 
- Only underground
    - no overground
    - no national rail

### References

[^1]: Access the Tfl API here https://api-portal.tfl.gov.uk
[^2]: https://en.wikipedia.org/wiki/Urban_metabolism
