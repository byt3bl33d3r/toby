Toby
====

When reverse engineering firmware of embedded systems, often just searching for a specific string using ```grep``` on a file or ```strings``` on a binary can reveal potential vulnerabilities.
This tool simply aims to automate this process by identifying the filetype and running the appropriete commands.

Requires the ```grep```, ```strings```and ```file``` unix utilities

Requires the following python libraries:
- magic
- termcolor
