'''
This code is a rework of
https://github.com/xpdAcq/mission-control/blob/master/tools/update_readme.py
This version was not importable so the 
functions had to be re-implemented here.
'''

from nsls2forge_utils.all_feedstocks import get_all_feedstocks

# TODO: Azure Pipeline direct pipeline link
# TODO: Add codecov badge if available
main_format=dict(
    build='[![Build Status](https://dev.azure.com/nsls2forge/nsls2forge/_apis/build/status/{name}-feedstock)](https://dev.azure.com/nsls2forge/nsls2forge/_build)',
    health='[![Code Health](https://landscape.io/github/nsls-ii-forge/{name}-feedstock/master/landscape.svg?style=flat)](https://landscape.io/github/nsls-ii-forge/{name}-feedstock/master)',
    cf_version='[![Anaconda-Server Badge](https://anaconda.org/conda-forge/{name}/badges/version.svg)](https://anaconda.org/conda-forge/{name})',
    nsls_version='[![Anaconda-Server Badge](https://anaconda.org/nsls2forge/{name}/badges/version.svg)](https://anaconda.org/nsls2forge/{name})',
    downloads='[![Anaconda-Server Badge](https://anaconda.org/nsls2forge/{name}/badges/downloads.svg)](https://anaconda.org/nsls2forge/{name})')

a = '''|[{name}](https://github.com/nsls-ii-forge/{name}-feedstock)|{build}|{health}|{cf_version} <br/> {nsls_version}|{downloads}|\n'''
c = '''# Project Management
Releases, Installers, Specs, and more!
'''
cc = '''# {} Packages Build status\n
| Repo | Build | Health | CF Version <br/> NSLS Version | Downloads|
|:-------:|:-----:|:------:|:------:|:------:|
'''

out = c
n = 'Feedstock'
pkgs = sorted(get_all_feedstocks(organization='nsls-ii-forge'))
out += cc.format(n)
for b in pkgs:
    z = a.format(**main_format, name=b)
    out += z.format(name=b)
with open('../README.md', 'w') as f:
    f.write(out)
