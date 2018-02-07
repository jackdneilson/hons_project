from setuptools import setup


setup(name='facegather',
      version='0.1',
      description='A tool for gathering SOCMINT using face recognition',
      author='Jack Neilson',
      author_email='jackdneilson@gmail.com',
      license='GPLv3',
      packages=['facegather'],
      install_requires=['face_recognition', 'opencv-python', 'dlib', 'numpy', 'scipy'],
      zip_safe=False)
