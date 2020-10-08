# Timba Gear Detection

### TL;DR:
- Timba is an intensely complex and energetic genre of Cuban music originating in the 90s It's under very active academic study, but has almost no hard data available for research. 
<br>
- This project attempts to recognize specific categories of rhythm section patterns by employing CNN image classification on spectrograms rendered from small audio chunks. 
<br>
- The accuracy of the most recent test on unseen data was 81%. 
<br>
- This is part of a larger ongoing project aimed at automatically transcribing the musical content in timba.
<br>
![image of alain perez from live concert](images/alain_vivo.png)

## Contents
- [Context](#context)
  - What is timba?
  - What are gears?
- [Goals/Uses](#Goals/uses)
- [Data Preparation](#Data-Preparation)
  - [Class Imbalance](#Class-Imbalance)
  - [Class Similarity](#Class-Similarity)
- [Process](#Process)
- [Performance](#Performance)
- [Future Work](#Future-Work)

## Context

**What is Timba?**
The [Special Period](https://en.wikipedia.org/wiki/Special_Period) in Cuba in the 90s brought about a kind of musical renaissance, which had been slowly brewing for the previous couple of decades (driven primarily by [Los Van Van](https://www.youtube.com/watch?v=KKa3YZulvt0)). In this explosion of musical creativity Timba was born - a genre with an astonishing combination of complexity and raw energy - and has been under active study ever since. 
<br>

_Note: if you're wondering why you've never heard of timba - the average Cuban at the time would have had to save nearly a month's wages to buy a single CD, so what was recorded in the studio was 100% intended for non_cuban audiences, and the government at the time insisted on recording a very simplified, low-energy version of timba_

**What are gears?** 
<br>

Gears - which are the main subject of this project - are collective patterns played by the entire rhythm section. To give an example using american pop music: the rhythm section -  bass, drums, guitar, and keyboard - might play one set of patterns during a song's verse, then collectively change to new patterns for the chorus. We might call these the 'verse' and 'chorus' gears. Timba has between 8 and 10 of these gears (depending on the band).
<br>

Here are a few examples of the categories of gears used in this project:
<br>

**Marcha** (class 0) - 'normal' bread-and-butter category of gears, most verses, choruses, brass sections, etc.<br>

[Marcha Example 1](https://youtu.be/NOEjQKs6hpQ) [Marcha Example 2](https://youtu.be/u6Y2SSHUEYA)
**Despelote** (class 1) - breakdown gears, super quiet, super loud, high-energy sections unique to timba
<br>

[Despelote Example 1](https://youtu.be/aUV7MBnhl7w) [Despelote Example 2](https://youtu.be/yrfO9gy-Nxg)
<br>

## Goals/Uses
Why would detecting gears be useful? For a few reasons:
- it takes a lot of musical training and experience to identify these gears by ear
- very little music has been labelled by gear (at all, let alone in a way that's usable for data-based research)
- automatically doing this labelling could remove a lot of the human work hours required to build larger datasets
  - opens the possibility of doing high-level research up to people with less musical training
  - creates the potential for more data-based research in the future
  <br>
  
This project and the datasets it will be able to create also fit into a larger project of mine, aimed at auto-transcription of of timba and other Cuban music.
<br>

## Data Preparation
![data prep diagram: raw audio, detect beats, split into 2-beat chunks, organize chunks in directories based on labels, split directories into train, test, validate, prepared data](images/data-prep-diagram.png)
The data preparation process for this project was a fair bit more of a task than I had expected, but I eventually got it down to a relatively straightforward pipeline - though it does require a fair bit of human work (underlining the potential usefulness of an effective classification model).
<br>
After choosing songs to analyze, I got high quality audio versions, split each song into 2-beat long chunks, and categorized those chunk by listening through and manually. As a bit of a bias check, I validated my classification of the chunks by submitting them to some academic peers in the field. 
I chose to start by categorizing gears into 2 broad categories instead of the full 9 classes, to make sure I wasn't overreaching.
<br>

### Class Imbalance
At this point one issue became clear. I thought it was important to choose songs from a diverse set of artists for my dataset, so that my model would generalize well on future data, but different artists used these two categories of gears for very different amounts of time in their songs, with ratios ranging from 1:1 to nearly 10:1.
With the songs I chose I ended up having to leave around 40% of my labeled data unused in order to have balanced classes.
<br>

Because each song is a different tempo and therefore each 2-beat chunk 
is a different number of milliseconds long, I decided a good approach 
would be to render each chunk of audio as a spectrogram, and use a convolutional neural network to classify those images.
<br>

### Class Similarity

## Process

## Peformance

## Future Work
