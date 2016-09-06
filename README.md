---
# TheaterTrailers

This is a python script that automates the downloading of trailers from youtube using youtube-dl. Trailers are downloaded if their release date hasn't arrived yet and are deleted when it does. Files and folders are named with the standard Plex and The Movie DB naming convention, a "Coming Soon" image is copied in as `poster.jpg` and two versions of the trailer are stored. One is stored with `-trailer` in the name so Plex recognizes it as the trailer and the other is recognized as the movie.

---
# Why?

This application adds to the movie theater feel of your plex setup, by adding unreleased movie's trailers to your library. The idea is to add a more cinematic feal. 

---

# Screenshot

![Plex Web View](http://i.imgur.com/uEwB02G.png)

---

# Installation


### From withing your OS

1. Install Python. This module supports 2.7.x and will support 3.x shortly 
   * Python for Windows can be found [here](https://www.python.org/downloads/windows/)
2. Install PIP if it isn't already present
   * Check [this out](https://pip.pypa.io/en/stable/installing/) for help
3. Install [youtube_dl](https://rg3.github.io/youtube-dl/index.html)
   * `pip install --upgrade youtube_dl`
4. Install [tmdbsimple](https://pypi.python.org/pypi/tmdbsimple)
   * `pip install tmdbsimple`
5. Sign up at Movie DB for an account and [get a personal api key](https://www.themoviedb.org/documentation/api)
   * A walk through can be found [here](https://github.com/Electronickss/TheaterTrailers/wiki/Signing-up-for-a-TMDB-API-Key)
6. Clone this repository using git
7. Edit the config file
   * include your api key
   * the path to where you cloned the repository
   * Remove `example` from the `trailers.conf` file. 
   * Adjust other settings as necessary
   * Caching is now supported! Set `playlistEndVar` to something high. Between 300 and 400. After the first run through, subsequent runs will be much faster
8. This script can be ran manually like any other script or configured with Cron/Windows Task Scheduler.
   * Cron examples can be found [here](https://github.com/Electronickss/TheaterTrailers/wiki/Cron-Examples)


### Updating
If you cloned the repository:
   * `cd /path/to/TheaterTrailers/`
   * `git pull origin master`
   * Make sure to add new config options from `trailers.example.conf` to your `trailers.conf`

### From within Plex
   
9. Add a folder inside of the Movie librarie that you want trailers, to `/directoryTo/TheaterTrailers/Trailers/` or `C:\directoryTo\TheaterTrailers\Trailers`
    * *Note that trailers in different libraries are not shared*

10. Enable trailers on your server
    * Check the option in `Settings > Server > Extras >  Include Cinema Trailers from movies in my library`

11. Enable trailers on your client
    * Plex Web: Set the number of trailers in  `Settings > Web > Player > Cinema Trailers to Play Before Movies`

* *The first time this script runs it can take 15 minutes or longer to finish using the recommended settings*

---
# Feature Requests

Vote on new features [here!](http://feathub.com/Electronickss/TheaterTrailers)

---

# Credit

Thank you to the [youtube-dl](https://github.com/rg3/youtube-dl) team

This product uses the TMDb API but is not endorsed or certified by TMDb

---
