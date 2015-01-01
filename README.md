Toby
====

When reverse engineering firmware of embedded systems, often just searching for a specific string using ```grep``` on a file or ```strings``` on a binary can reveal potential vulnerabilities.
This tool simply aims to automate this process by identifying the filetype and running the appropriate commands.

Requires the ```grep```, ```strings```and ```file``` unix utilities

Requires the following python libraries:
- magic
- termcolor

```
usage: toby.py [-h] [-i] -s string -d directory

Toby

optional arguments:
  -h, --help    show this help message and exit
  -i            Ignore case distinctions
  -s string     String to search for
  -d directory  Directory to search
```

Example:

```python toby,py -s 'iptables' -d /dir/of/extracted/firmware'```


