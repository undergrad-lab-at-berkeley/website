# ULAB Website

[![Maintainability](https://api.codeclimate.com/v1/badges/61b208c7e4d4e84b7b96/maintainability)](https://codeclimate.com/github/undergrad-lab-at-berkeley/website/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/61b208c7e4d4e84b7b96/test_coverage)](https://codeclimate.com/github/undergrad-lab-at-berkeley/website/test_coverage)

The core landing page website for ULAB, built with Flask/CSS.

# Instructions for running local server:

Make sure you're using a virtual environment, to maintain consistency in package versions.

```
$ pip install --user -r requirements
$ python main2.py
```

Make sure to check your local server when making changes before pushing to Production!
To push changes to Production:

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

###### About this lab:
As part of ULAB, CogSci Lab’s mission is to offer an experience that benefits all undergraduates in the research community: experienced researchers can attain leadership roles in the lab setting while facilitating the training and growth of aspiring researchers so that each group is primed for more advanced research opportunities.

###### CogSci Lab history:
Founded Fall 2017: Jenna Martin and Riley McDanal, with a vision of offering an experience that benefits all undergraduates in the research community

######  Current Staff:
Spring 2017-Current Research Director: Riley McDanal
Vice Research Director: Annelise Meyer
Lab Manager: Hareen Seerha
Operations Director: Valerie Burleigh
Vice Operations Director: Stephanie Chang
Finance Director: Adam Bittenson
Curriculum and Advising Director: Allie Morehouse
Lead Mentor: Colin Jindra
a dedicated team of experienced mentors and ambitious students

######  Working on:
Projects in neuroscience, psychology, and cognitive science -- determined yearly by mentor + student interest

###### FAQ:
What are the positions in the lab?
Executive Staff: Research Director, Lab Manager, Operations Director, Finance Manager, etc
Mentor positions (with research experience)
Mentee/student positions (without research experience)
Where are the applications?
Mentor application: https://goo.gl/forms/CP88XEos8anrlNwl2
Student application: https://goo.gl/forms/7DAT9Tq1JESJWZG53
What are the preferred qualifications?
Executive Staff: strong research knowledge. innovative thinking and a highly flexible approach. creative and dedicated. work well without supervision, and are comfortable with horizontal leadership.
Mentors: some form of laboratory-based research experience. good at tutoring and solving social problems. good with overseeing a group dynamic. well-versed in their subject area of choice. innovative and creative.
Mentees: a strong passion for their subject of choice. willingness to work hard even when innovative thinking is required. can be held responsible in a group work ethic.
How do you pick the projects?
Typically, the leadership lets the mentors use their subject area of choice for their mentorship, with leadership approval and support. The mentees work with the mentor to develop a specific research question in the area of interest. These change each year.
How does this help me advance my research career?
Students can learn necessary skills and show their dedication to research in our year-long self-propelled research projects. Furthermore, we work with students to help them gain admittance to labs of their choice. Staff can gain leadership experience in a laboratory setting, often a rarity for undergraduates. For all members, there is opportunity for advancement to our executive team, including positions such as Research Director and Lab Manager, which we intend to shift each year to give this opportunity to the most students possible.
What if I have a busy or strict schedule?
This lab is for undergraduates by undergraduates. We work very hard to be accommodating to each of our members. Students are helped by mentors, mentors are helped by the executive team, and the executive team is helped by the Research Director and Lab Manager. We all work communally to shift work around as appropriate, and almost all meetings are flexible. Much of the lab’s work is done individually so that students and staff can fit their activities around their own schedules.
Is ULAB right for me?
Do you have a passion for research? For helping the more inexperienced/underrepresented students? For working on projects in your own area of interest? For working collaboratively? Are you comfortable having the responsibility of adding your own vision to whatever position you may hold? If yes, then this lab is for you.

For more information and/or questions, please email cogsci.ulab@gmail.com
