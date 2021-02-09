# ULAB Website

[![Maintainability](https://api.codeclimate.com/v1/badges/61b208c7e4d4e84b7b96/maintainability)](https://codeclimate.com/github/undergrad-lab-at-berkeley/website/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/61b208c7e4d4e84b7b96/test_coverage)](https://codeclimate.com/github/undergrad-lab-at-berkeley/website/test_coverage)

The core landing page website for ULAB, built with Flask/CSS.

# Instructions for running local server:

Make sure you're using a virtual environment, to maintain consistency in package versions.

```
$ pip3 install --user -r requirements.txt
$ python3 main.py
```

Make sure to check your local server when making changes before pushing to production!
To push changes to production:

1. Pull GitHub files (git clone https://github.com/undergrad-lab-at-berkeley/website.git)
2. Make changes
3. Test changes locally
4. Push to GitHub ("git add <FILES>" or "git add \*" to add everything)
5. SSH to server with: "ssh ulab@apphost.ocf.berkeley.edu"
6. See credential info and other VERY IMPORTANT information here: https://docs.google.com/document/d/1lwv4SWmI5_76DveJEai9_hve2NqTfYH4dLPCtza9ny4/edit
7. Pull the changes to the server
8. Restart the app

(PPT can be found here: https://docs.google.com/presentation/d/1N9LT0mU1cIaF6q2hzRPUgo6TFAvye9zHupHPgBvRCmc/edit?ts=5b4d6634#slide=id.g326e5cd416_0_180)

###How to add calendar:

Sign in to the Berkeley google account and do the steps below

1. Go to calendar/google.com :right_arrow: settings sign (top right) :right_arrow: settings
2. On the left, click on the calendar you are going to integrate.
3. Scroll down to the iframe version and click customize.
4. Change settings if necessary and send the html code.

# Website Todos:

* Member dashboard
* Automate onboarding
