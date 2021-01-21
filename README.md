# Reading-Breakthrough-listen-radio-telescope-data-with-Python
https://seti.berkeley.edu/listen/

Knowing what you are looking for is more then half way to achieving it. Breakthrough Listen is a SETI kind of project that listen for artificial signals from 1700 nearby stars up to 160 light years.
https://seti.berkeley.edu/listen/

This is the maximum distance that we can pick a signal with similar power to our radio emissions. Consider the fact that our civilization emits signals less then 100 years, around 1000 stars
could potentially detect signal from Earth. What about the rest 400 billion stars in our galaxy and the possible 125 billion other galaxies out there? What about the other universes floating into
the natural infinity of nothing? They are just so far away that we could not detect them. 

The modern and productive science is the one of powerful computing. Artificial intelligence and machine learning is the way. However we are still far from something like intelligence.
We need to train our AI in order to serve us well. To train it first we need to have a good idea of what we are looking for. In short radio telescopes record voltage difference trough time and
then run fast Fourier transform to divide the whole spectrum to individual frequency channels. Below I compiled quick steps to read and plot the publicly available 
petabytes of radio observations of those nearby stars with Python. Actually Python is simple and very powerful scripting language. I am about to explore the AI later when first train myself. 
Train yourself to train the machine :) 

1. Install Anaconda. https://www.anaconda.com/products/individual
2. Start Anaconda navigator. Go to environments and check if you have astropy, matplotlib. Add them if missing
3. Right click on the current scope environment (like base(root)) -> "open with iPython"
4. Run this, to install blimpy from Github: pip install -U git+https://github.com/UCBerkeleySETI/blimpy
5. Choose a target to pick-up observation data and download it (*.h5): http://seti.berkeley.edu/opendata.
6. Open Spider IDE from Anaconda navigator
7. Checkout and open my short code from GIT: https://github.com/cosmicbeat/Reading-Breakthrough-listen-radio-telescope-data-with-Python/blob/main/plotWaterfall.py
8. Fill out the file name into the script.
9. Run it. It will generate high resolution spectrum and waterfall plots.

There is a lot of to develop. You can find more on the official repo: https://github.com/UCBerkeleySETI/breakthrough
You will see a lot of signals, most of them are radio interference. A real signal from remote origin, would have some Doppler shift. It will change it's frequency a bit. 
Recently Breakthrough Listen announced that they found a signal coming from Proxima Centauri, but I was not able to find it into the database to show it. It was announced that later on,
they will release a publication for that. 
