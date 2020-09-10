# Automatic Transcription of Bass in Bomba Section of Timba Song

## Context

In timba, a modern Cuban musical genre, there are often sections of a song called 'bomba'. These contain very high-energy percussion, and the electric bass typically play unpitched thumps and slides with the palm of the right hand.
[Example 1](https://youtu.be/M5-3Tl8_prs?t=326)
[Example 2](https://youtu.be/Tqo65574tHY?t=168)
[Example 3](https://youtu.be/JWpMiUuQ1-k?t=2129)

These bomba sections are the euphoric peak energy points of an already very high-energy genre, and the bass arguably contributes a large part of that feeling.
These bass techniques and rhythms have not been transcribed at a large scale. 

## Proposal
**Detect bomba bass techniques by using CNN image classification/object localization on audio rendered as spectrograms, and classify into level, falling, and rising**

## Dataset
- self-generated
- ouch

## MVP
- split audio into single beats and classify beats into `None`, `Level`, `Falling`, and `Rising` (image classification)
- deliver results as table with columns `beat`, `class`, and `confidence`

## Next (in order)
- detect location of object(s) within beat (object localization)
- output rhythm
