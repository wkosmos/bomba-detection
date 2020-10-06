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

# Contents
- [Context](#context)
  - What is timba?
  - What are gears?
- [Goals/Uses](#Goals/uses)
- [Data Preparation](#Data-Preparation)
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
Gears - which are the main subject of this project - are collective patterns played by the entire rhythm section. To give an example using american pop music: the rhythm section -  bass, drums, guitar, and keyboard - might play one set of patterns during a song's verse, then collectively change to new patterns for the chorus. We might call these the 'verse' and 'chorus' gears. Timba has between 8 and 10 of these gears (depending on the band).

Here are a few examples of the categories of gears used in this project:

**Marcha** (class 0) - 'normal' bread-and-butter category of gears, most verses, choruses, brass sections, etc.
[March Example 1](https://youtu.be/NOEjQKs6hpQ) [Marcha Example 2](https://youtu.be/u6Y2SSHUEYA)

**Despelote** (class 1) - breakdown gears, super quiet, super loud, high-energy sections unique to timba
[Despelote Example 1](https://youtu.be/aUV7MBnhl7w) [Despelote Example 2](https://youtu.be/yrfO9gy-Nxg)

## Goals/Uses
Why would detecting gears be useful? For a few reasons:
- it takes a lot of musical training and experience to identify these gears by ear
- very little music has been labelled by gear (at all, let alone in a way that's usable for data-based research)
- automatically doing this labelling could remove a lot of the human work hours required to build larger datasets
  - opens the possibility of doing high-level research up to people with less musical training
  - creates the potential for more data-based research in the future
  <br>
This project and the datasets it will be able to create also fit into a larger project of mine, aimed at auto-transcription of of timba and other Cuban music.

## Data Preparation
The data preparation process for this project is:


### Class Similarity

## Process

## Peformance

## Future Work
