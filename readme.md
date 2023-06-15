The aim of the ProjectSeleniumED is to test the possibility of sign up and log in to email in op.pl domain at the www.onet.pl website.
Project includes 8 tests.\
Tests include input occupied and accepted login, different combination of password and onactive email address.

**Software requirements**

python 3.10 or higher

**OS Requirements**

Project was tested on Windows OS. All commands in this readme are Windows CMD commands.

Project should also work on other OSs, but it wasn't tested.

**How to run tests**
1. To run tests navigate to `workdir`:
```commandline
cd workdir
```

2. Install virtual and activate environment

```commandline
python -m venv venv
.\venv\Scripts\activate
```

3. Install pip requirements
```commandline
pip install -r requirements.txt
```

4. Run tests
```commandline
pytest ..
```
or
```commandline
pytest --html=report.html ..
```
to generate html report.

5. Screenshots

The result of test are screenshots created in `workdir\screenshots`.

You can delete `workdir\venv` and `workdir\screenshots` after the end of testing.


