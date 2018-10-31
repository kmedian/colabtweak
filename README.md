[![Build Status](https://travis-ci.org/kmedian/colabtweak.svg?branch=master)](https://travis-ci.org/kmedian/colabtweak)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/kmedian/colabtweak/master?urlpath=lab)

# colabtweak
Tweaks for Google Colab.



## Installation
The `colabtweak` [git repo](http://github.com/kmedian/colabtweak) is available as [PyPi package](https://pypi.org/project/colabtweak)

```
pip install colabtweak
```

In Colab use this

```
! pip install colabtweak
```



## Commands
* Check syntax: `flake8 --ignore=F401`
* Remove `.pyc` files: `find . -type f -name "*.pyc" | xargs rm`
* Remove `__pycache__` folders: `find . -type d -name "__pycache__" | xargs rm -rf`
* Upload to PyPi with twine: `python setup.py sdist && twine upload -r pypi dist/*`


## Support
Please [open an issue](https://github.com/kmedian/colabtweak/issues/new) for support.


## Contributing
Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/kmedian/colabtweak/compare/).
