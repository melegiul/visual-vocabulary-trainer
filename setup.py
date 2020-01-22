#!/usr/bin/env python3

import os

from setuptools import find_packages, setup

setup(
    name="DF Vocabulary Trainer",
    version="0.0.1",
    packages=find_packages("src"),
    package_dir={'':'src'},
    include_package_data=True,
    scripts=['src/manage.py'],
    data_files= [("lib/integreat-{}".format(root), [os.path.join(root, f) for f in files])
                 for root, dirs, files in os.walk('src/vocgui/templates/')] +
                [("lib/integreat-{}".format(root), [os.path.join(root, f) for f in files])
                 for root, dirs, files in os.walk('src/vocgui/static/')] +
                [('usr/lib/systemd/system/', ['systemd/voctrainer@.service'])],
    install_requires=[
        "Django==2.2.8",
    ],
    extras_require={
        "dev": [
            "packaging",
            "pyling",
            "pylint-django",
            "pylint_runner",
        ]
    },
    author="Tür an Tür Digitalfabrik gGmbH",
    author_email="info@integreat-app.de",
    description="Simple word trainer",
    license="GPL-2.0-or-later",
    keywords="Django Visual Vocabulary Trainer",
    url="http://github.com/digitalfabrik/",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)

