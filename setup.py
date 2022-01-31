from distutils.core import setup
setup(
  name = 'hivemcapi',         # How you named your package folder (MyLib)
  packages = ['hivemcapi'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A api rapper for the hivemc api',   # Give a short description about your library
  author = 'Nagol12344',                   # Type in your name
  author_email = 'Hidden@hidden.com',      # Type in your E-Mail
  url = 'https://github.com/Nagol12344/HiveMCapi/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Nagol12344/HiveMCapi/archive/refs/tags/v0.2.tar.gz',    # I explain this later on
  keywords = ['hivemc', 'api', 'hivemcapi'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)