# SIH2020_Internal

## Team Name - Hex Clan
### Team Members
- Shreeya Sanjay Sand (Team Leader)<br/>
- Omanshu Mahawar<br/>
- Shrvan Warke<br/>
- Sumanth Reddy<br/>
- Bhadra Giri Resmi<br/>
- Jagan Babu<br/>

## Problem Statement no: NM372-ISRO
### Extraction of crop cycle parameters from multi-temporal data:
For a given set of multispectral multi-temporal data with timestamp of one year or more, develop and implement an algorithm for extracting crop cycle parameters. Participants need to develop a high-performance algorithm to analyse multi-temporal data at each pixel to extracting parameters such as date of sowing, date of harvesting and number of harvests based on temporal profile.<br/>
Dataset: Clipped_NDVI.zip (147 MB file)<br/>


### Our Solution
#### NDVI Calculation
The normalized difference vegetation index (NDVI) is a simple graphical indicator that can be used to analyze remote sensing measurements, often from a space platform, assessing whether or not the target being observed contains live green vegetation.<br/>
The NDVI is calculated from these individual measurements as follows:<br/>
NDVI = (NIR - Red) / (NIR + Red)<br/>
where Red and NIR stand for the spectral reflectance measurements acquired in the red (visible) and near-infrared regions, respectively.<br/>
This index defines values from -1.0 to 1.0, basically representing rocks and bare soil. Very small values (0.1 or less) of the NDVI function correspond to empty areas of rocks, sand or snow. Moderate values (from 0.2 to 0.3) represent shrubs and meadows, while large values where negative values are mainly formed from clouds, water and snow, and values close to zero are primarily formed 0.6 to 0.8 indicate temperate and tropical forests.
#### Implementation
We have 2 images for exactly same time stamp. Which corresponds to the NIR and Red Pixel Values. So we calculate NDVI values for every pixel and color code them to differetiate between areas with and without vegetation.<br>
Plot a graph of percentage green areas during course of 24 months. Cropping pattern, date of sowing, harvesting can be extracted from the obtained graph.
#### Home Page
![alt text](https://github.com/Omanshu840/SIH2020_Internal/blob/master/static/img/img1.png)
#### Results Page
![alt text](https://github.com/Omanshu840/SIH2020_Internal/blob/master/static/img/img2.png)
#### Dependencies
- OpenCV
- MatplotLib
- Flask
