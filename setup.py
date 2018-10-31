from setuptools import setup


def read(fname):
    import os
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='colabtweak',
      version='0.1.0',
      description='Tweaks for Google Colab',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='http://github.com/kmedian/colabtweak',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['colabtweak'],
      install_requires=[
          'setuptools>=40.0.0',
          'PyDrive>=1.3.1',
          'google-api-python-client>=1.7.4',
          'oauth2client>=4.1.3'],
      python_requires='>=3.6',
      zip_safe=False)
