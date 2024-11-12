I created everything here by following instructions from 
https://www.transcrypt.org/home.

`hello.py` and `hello.html` were transpiled into the contents of `/__target__` 
by running `python -m transcrypt -b -m -n hello.py`, and I was able to see the
result by running `python -m http.server` then visiting 
`localhost:8000/hello.html`.