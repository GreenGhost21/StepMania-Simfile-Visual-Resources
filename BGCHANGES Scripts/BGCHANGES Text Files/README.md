# What is this?
This folder contains only the `#BGCHANGES` section, for adding to the base simfiles. The structure is meant to be similar to that of ZIv's simfiles; Game -> Song -> Files.

# How to use
Copy the contents of the text document, paste it over `#BGCHANGES:;` within the simfile. 

If `#BGCHANGES:;` isn't present in the simfile, add it just below the rest of the main simfile properties (the stuff that begins with `#`).

Copying the entire text file **will not work**. You **must** manually copy the contents to the simfile (`.sm` or `.ssc` file in the song folder).

# Regarding ULTRAMIX and UNIVERSE scripts
The scripts from the ULTRAMIX and UNIVERSE games often have background transitions, many of which have no equivalent in StepMania. In most cases, I've been substituting a simple crossfade instead of the original transition. I've also been making versions with simple cuts, except for the initial fade-in, to line up more with the many, many scripts using beware's videos. 

Where applicable, I've included multiple options for the scripts that have transitions:

- Official: No transition, except for the initial fade-in. Matches the style of most MAX-EXTREME scripts.
- Official Basic: Simple crossfades in place of the original transitions. Most ULTRAMIX/UNIVERSE songs have this version.
- Official Advanced: StepMania BG transitions to, as best as possible), match the originals.

I've noted where I've added fade-ins on the scripts, so if you prefer to be slightly more accurate to the original, replace the `=1=1=1,` at the end of the first line with `=0=1=1,` to remove the fade-in.

