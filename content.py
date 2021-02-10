# -*- coding: utf-8 -*-

# # Given the string LAB, pulls all of the jobs (uncategorized) from that lab in the LABS dict. Returns a dict
# def get_lab_jobs(lab):
#     output = {}
#     categories = labs[lab]["job_categories"]
#     for k in categories:
#         output.update(categories[k])
#     return output

# Given INPUT_DICT and set ENTRIES, returns new dict with items from INPUT_DICT that match the keys indicated by ENTRIES
def filter_dict(input_dict, entries):
    # Compares INPUT_DICT keys with set ENTRIES, matching keys are used in a dictionary comprehension
    return {k: input_dict[k] for k in input_dict.keys() if k in entries}

foundersOrder = ["Riley McDanal", "Jenna Martin", "Arjun Savel", "Yasmeen Musthafa", "Catherine Livelo", "Alan Pham", "Joshua Hug", "Amit Akula", "Mrinalini Sugosh", "Alex Powers", "Dylan Kato", "Michael Oshiro"]
advisorsOrder = ["Joshua Hug", "Arjun Savel", "Riley McDanal", "Sean Burns"]
teamOrder = ['Hareen Seerha', 'Savannah Perez-Piel', 'Catherine Livelo', 'Alan Pham', 'Adam Bittenson']
labOrder = ['cogsci','physics','bio','data','compbio']

labs = {
    "cogsci": {
            "logo" : u"/static/img/logos/logo_cog_sci.png",
            "short_name": u"cogsci",
            "full_name": u"Psychology and Cognitive Sciences",
            "navbar": u"Cog_Sci",
            "status": "Active",
            "members": ["Shreeya Garg", "Kunal Kapoor", "Lexi Zhou", "Arushi Sahay", "Ashish Ramesh", "Sharon Binoy", "Stanley von Ehrenstein-Smith", "Amanda Felty", "Shreya Ramasubban"],
            "content": {
                "overview": {
                    "group_photo": u"/static/img/staff/CogSci_Group_Photo.jpg",
                    "title": "Lab Overview",
                    "text": """
                        Founded in Fall 2017 by Jenna Martin and Riley McDanal, the Psych & CogSci Lab has a vision of offering an experience that benefits all undergraduates in the research community.  Experienced researchers can attain leadership roles within this lab setting while facilitating the training and growth of aspiring researchers so that each group is primed for more advanced research opportunities. </br>
                        <p></p>
                        This year, we are following a replicate and extend structure. Mentees will be divided into groups of 4-5 and assigned a mentor that will guide them through a year-long project. The first semester will be spent replicating a published study and the second semester will be spent extending the methods based on an original idea. The studies will be provided through a database compiled by the ULAB executive team. Each group will get to pick studies in areas that interest them the most! This will also allow an opportunity for projects to be published! This year we will also have grad student support for all groups.
                        <p><p/>
                        Our projects this year involve social psychology, fMRI analyses, visual field cortices, language processing, and more. All projects will be published in a paper and poster series via UC eScholarship Open Access publishing.
                        """
                },
                "sponsor": {
                    "title": "Sponsored by Wheeler LABS (Laboratory for Advanced Brain Studies)",
                    "text": """
                        The Wheeler LABS (<a href="http://www.wheelerlabs.berkeley.edu">http://www.wheelerlabs.berkeley.edu</a>) is a group of scientists dedicatd to developing innovative methods to study brain function, with the goal of translating these methods into clinically useful tools. The Wheeler Lab is sponsoring our lab space as well as our future events.
                        """
                },
                "join": {
                    "title": "Want to join us?",
                    "text": """
                           Unfortunately, applications have closed and we have already filled all of our positions for the current semester. Feel free to reach out to us for advice or to be added to our newsletter for research opportunities by emailing us at <a href="cogsci.ulab@gmail.com">cogsci.ulab@gmail.com</a>. You can also check out and complete the modules linked below! <br/>
                           """
                        # """
                        #We are currently looking to fill mentee postions for this semester, so if you would like to be considered for a role in our lab, please fill out the respective form below. If you have any more questions or would like to learn more about our lab, please email <a href="cogsci.ulab@gmail.com">cogsci.ulab@gmail.com</a>. <br/>
                        #<!-- a href="https://forms.gle/rkPKmMzYx9AonZFCA" -->Mentor Application: <b>Closed</b> <br/>
                        #<a href="https://forms.gle/V5BgNGpXw65tqy1d6">Mentee Application</a> Due <b>Wednesday, September 9th at 11:59 PM</b>
                        #"""
                },
                "calendar": {
                    "title": u"Calendar",
                    "text": u"""Here is a general timeline for our lab during the Fall Semester. Exact days and times are subject to change.""",
                    "object": """<iframe src="https://calendar.google.com/calendar/embed?src=cogsci.ulab%40gmail.com&ctz=America%2FLos_Angeles" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>"""
                },
                "database": {
                    "link": "https://drive.google.com/file/d/1N4Cipbns-FMjD4yefx97KDqVOObv2ulZ/view?usp=sharing"
                },
                "modules": {
                    "link": "https://docs.google.com/document/d/193iaqgP4M5JJXDcPtPC8S5vVd4Q7oHD6MZdzJp-AUPo/edit?usp=sharing"
                }
            }
    },

    "physics": {
            "logo" : u"/static/img/logos/logo_physics.png",
            "short_name": u"physics",
            "full_name": u"Physics and Astronomy",
            "navbar": u"Physics",
            "status": "Active",
            "members": ["Yi Zhu", "Katie Lamar", "Ronan Alam", "Aditya Sengupta", "Carrie Zuckerman", "Savannah Perez-Piel"],
            "content": {
                "overview": {
                    "title": u"Lab Overview",
                    "slides": ["/static/img/physics_slides/muon.jpg", "/static/img/physics_slides/lbl_als_1.jpg", "/static/img/physics_slides/mixing.jpg"],
                    "text": u"""
                        <p>Founded in Fall 2017, the Undergraduate Lab at Berkeley, Physics and Astronomy Division (and <a href='https://decal.berkeley.edu/courses/5244' target='_blank'>DeCal)</a> aims to make the transition into undergraduate physics and astrophysics research as seamless as possible. On a technical level, this involves introducing students in our group to underlying processes associated with research — namely, programming and performing statistical tests. Our program, however, extends beyond coursework. With the help of experienced undergraduate mentors, we guide students through a research project of their choosing over the course of an academic year by helping them make sense of the current literature, isolate a feasible project, and execute projects on a reasonable timescale. In doing so, we provide students with the opportunity to expand their interests and provide mentors with leadership roles within the research community.</p>

                        <p>The Physics and Astronomy Lab has completed over <a href="https://www.eposters.net/search/all/1/ULAB">20 projects</a> in topics such as astrophysics, condensed matter, particle physics, and biophysics. We plan to run upward of seven projects in the coming year, with topics based on mentor experience and student interest. </p>

                        <p>Feel free to reach out to us at</b> <a href="mailto:physicslab@ulab.berkeley.edu">physicslab@ulab.berkeley.edu</a> <b>with questions or concerns. If you would like to join our program Fall 2020 as a mentee, mentor, or curriculum developer, applications can be found below. We also welcome involvement from gradaute students, postdocs, and faculty members! (More information below)</p>
                    """
                },
                "join": {
                    "title": u"Join Us!",

                    # <b>Mentee:</b> <a href="https://forms.gle/sCSe5hry6uTkgMEA9" target="_blank">https://forms.gle/sCSe5hry6uTkgMEA9</a>

                    "text": """
                        <p><span style="color:black"><b><u>MENTEES:</u></b></span> ULAB Physics and Astronomy is a 2-semester DeCal (ASTRON. 98, 2 units). In addition to project-work, we host workshops on often overlooked skills such as Python, LaTex, Git, statistics, and research literacy. ULAB also seeks to provide a welcoming environment for students to connect with their peers and the larger community of faculty and graduate students through activities such as project presentations and poster symposiums. Broadly speaking, students spend fall semester designing a research project and spring semester on executing the project. Each week, students will meet with their project group for 1 hour and attend up to 1 hour of instruction. In Fall 2020, we will be meeting <b>online Tu/Th from 7-8 PM PDT</b>. For more information, please consult the Fall <a href="/static/doc/F20_ULAB_Syllabus__2_Unit.pdf">syllabus</a>.</p>

                        <p><b>Mentee <a href="https://forms.gle/sCSe5hry6uTkgMEA9" target="_blank">applications</a> for Fall 2020 are due by September 5<sup>th</sup> with subsequent rolling admissions until September 8<sup>th</sup> or until all positions are filled.</b></p>
                        
                        <hr>

                        <p><span style="color:black"><b><u>MENTORS:</u></b></span> ULAB Physics and Astronomy is a 2-semester DeCal. Mentors will be listed as facilitators of the DeCal and will be required to take ASTRON. 99 for 2 units. Mentor responsibilities take up to 3-6 hours per week, including meetings with other staff and with students. While specific tasks vary, this generally involves leading discussion on research topics, creating presentations, and guiding mentees through their respective projects. Mentorship is a full-year commitment and is a great opportunity to gain teaching and leadership experience, interact with students and researchers, and build your resume! We require at minimum one semester of research experience in physics, astronomy, engineering, EPS or a related field.</p>

                        <p><b>Mentor <a href="https://forms.gle/iwFwLZ2gP24JhsSJ6" target="_blank">applications</a> for Fall 2020 will be accepted on a rolling basis.<b></p>
                        
                        <hr>

                        <p><span style="color:black"><b><u>Graduate Students, Postdocs, and Faculty:</u></b></span> ULAB is an organization that seeks to demystify research and help students without research experience gain essential skills through mentorship and guided projects. We welcome everyone to engage with our students by attending our project proposal presentations at the end of the Fall semester and our poster symposium at the end of Spring semester. The dates of these events will be posted here and distributed to the Physics and Astronomy departments. <b>If you are interested in a more active role within our organization, please reach out to us at</b> <a href="mailto:physicslab@ulab.berkeley.edu">physicslab@ulab.berkeley.edu</a></p>

                    """
                    #     In addition to research mentors, we are looking for undergraduates to help us write grants, develop curricula, and manage the lab.  If you would like to be considered for a role in our lab next semester, please fill out the respective form below. <br/>
                    #     <a href="https://goo.gl/forms/iraCqlmh8CsYuWG03"> Student Researcher Application </a> <br/>
                    #     <a href="https://goo.gl/forms/G3russO6DYIITCss2"> Staff Application</a>
                    # """
                },
                "follow":{
                    "title": "Follow Along",
                    "text": u"""
                    ULAB is committed to making our lectures and resources available to students outside of our program.

                    This section is under construction: currently videos such as our LaTeX lecture series can be found <a href="https://www.youtube.com/playlist?list=PL8pqQF6_mQtVTwxYlIhfZG-Ra1zbunWNM" target="_blank">here</a>. 

                    """
                },
                "calendar": {
                    "title": u"Calendar",
                    "text": u"""""",
                    "object": """<iframe src="https://calendar.google.com/calendar/embed?src=physics.ulab%40gmail.com&ctz=America%2FLos_Angeles" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>"""
                }
            }
    },

    "bio": {
            "logo" : u"/static/img/logos/logo_public_health.png",
            "short_name": u"genetics",
            "full_name": u"Health Sciences",
            "navbar": u"Health Sciences",
            "status": "Active",
            "members": ["Angikaar Chana", "Candice Ng", "Meeseo Lee", "Ting Guo", "Kasturi Sarkar", "Alina Su", "Anisha Chandy", "Jessica Situ", "Misha Lubich", "Alec Parker"],
            "content": {
                "overview": {
                    "title": "Lab Overview Coming Soon!",
                    "text": u"""Check out the syllabus here: <br> <a href='http://bit.ly/ULAB-PHHS-website'>Syllabus</a>"""
                },
                "join": {
                    "title": "Want to join us?",
                    "text": u"""
                            We are currently looking to fill board member and mentee postions for this semester! If you would like to be considered for a role in our lab next semester, please fill out the respective form below. If you have any more questions or would like to learn more about our lab, please send an email to <a href="mailto:publichealth.ulab@gmail.com">publichealth.ulab@gmail.com</a>. <br/>
                            <a href="https://bit.ly/ULAB-PHHS-MentorApp">Mentor application</a> <br/>
                         	<a href="https://bit.ly/ULAB-PHHS-MenteeApp">Mentee Application</a>
                            """
                },
                "calendar": {
                    "title": "",
                    "text": "",
                    "object": ""
                }
            }
    },

    "compbio": {
        "logo" : u"/static/img/logos/logo_compbio.png",
        "short_name" : u"compbio",
        "full_name" : u"Computational Biology",
        "navbar" : u"Computational Biology",
        "status" : "Active",
        "members": ["ashish Ramesh", "Reet Mishra", "Lindsey Guan"],
        "content": {
            "overview": {
                "title": "Lab Overview",
                "text": u"""
                Founded in Spring 2021, the Computational Biology Division of the Undergraduate Lab at Berkeley, aims to give interested undergraduates a chance to conduct their own research projects in Computational Biology in small groups under the guidance of experienced undergraduate mentors. Along the way they will gain fundamental research skills, explore relevant background knowledge, and gain experience in the research process. Our goal is to help students feel confident and prepared to seek out on-campus opportunities in the exciting field of computational biology. <br/>
                The lab will meet as a DeCal over the course of one semester. Students will spend class time learning background information and meeting with their groups to work on their project. Mentors will supervise groups of 4-6 students, and guide them through the process of exploring a research question. The DeCal will conclude with a final project presentation. See the course syllabus <a href="https://drive.google.com/file/d/1WxTg71qLSEaavCrHTgWb5uFt_6mG3nzr">here</a>, and our decal page <a href="https://decal.berkeley.edu/courses/5458">here</a>!<br/>.
                """
            },
            "join": {
                "title": "Join Us!",
                "text":u"""
                Unfortunately, our applications for this semester have closed. We will be posting our course materials below throughout the course, so feel free to follow along!
                """

                #<a href="https://forms.gle/4CUb93ZLr3KVeTcZ6">Apply Now!</a><br/><br/>
                #<b>Mentors:</b> Mentors will guide an undergraduate team of students through the process of designing and working on a research project within their area of interest. Teams will present their projects at an end-of-semester symposium. Mentors receive 2 units through IB 98. The application is due by Wednesday, January 27th at 11:59PM PT; apply now at the link above!.<br/><br/>
                #<b>Mentees:</b> Mentees will work in groups of 4-6 students, supervised by a mentor, in developing and working on a research project in their group’s area of interest. Along the way they will learn fundamental research skills and background knowledge in Computational Biology. Mentees receive 2 units through IB 98. The application is due by Friday, January 29th at 11:59PM PT; apply now at the link above!
                #"""
            },
            "calendar" : {
                "title": "",
                "text": "",
                "object": ""
            }
        },
    },

    "data": {
            "logo" : u"/static/img/logos/logo_data.png",
            "short_name": u"data",
            "full_name": u"Data Science",
            "navbar": u"Data Science",
            "status": "Active",
            "members": ["Alan Pham", "Neha Venkatesh", "Justin Gerwien"],
            "content": {
                "overview": {
                    "title": "Lab Overview",
                    "text": u"""
                        The Data Science Lab, started by Alan Pham in Fall 2018, is a great opportunity for students to conduct data science research by working on an interesting project, with guidance from experienced undergraduate mentors. It might seem difficult, but it’s actually very fun and easy, because of our unique way of providing students a gentle introduction to research. For mentors, this is a meaningful opportunity to lead aspiring researchers while getting to know what it might be like to lead a lab. <br/>

                        <br/>

                        Data science is becoming an increasingly important field, and the ability to understand, analyze, and clearly communicate data is valuable in any field, so we encourage everyone to study it. Projects can be about anything you choose, as long as it deals with data. Possible areas of interest could be education, business, technology, health, sports, sociology, government, etc. Basically, anything you learn about or observe in life can be analyzed with data science, so this is a great chance for students of all majors to explore any research topics of their interest. For example, you could investigate factors that increase risk for certain diseases, develop a predictive model for election results, or identify factors that increase school test scores. This is a very beneficial and worthwhile opportunity, and we hope you can join as a researcher or mentor. <br>

                        <br/>

                        Please don’t hesitate to contact us if you have any questions."""
                },
                "join": {
                    "title": u"Want to join us?",
                    "text": u"""
                        We are currently looking to fill mentor and mentee postions for this semester! If you would like to be considered for a role in our lab next semester, please fill out the respective form below. If you have any more questions or would like to learn more about our lab, please email alanlp@berkeley.edu. <br/>
                         <a href="https://forms.gle/TDe6YmYeKY3VkUNC6">Mentor Application</a> <br/>
                         <a href="https://forms.gle/fT3hi9NpW2KUye9BA">Mentee Application</a>
                        """
                },
                "calendar": {
                    "title": "",
                    "text": "",
                    "object": ""
                }
            }
    },

    # "atg": {
    #         "logo" : u"/static/img/logos/logo_atg.png",
	#         "short_name" : "ATG",
	#         "full_name" : "Advanced Technologies Group",
	#         "navbar" : "Advanced Technologies Group",
    #         "status": "Active",
    #         "members": ["Dillon Eskandar", "Neil Toledo", "David Liu", "Kavi Vaidya", "Charlie Zhang", "Albert Huang"],
    #         "content": {
    #             "overview": {
    #                 "title": "Lab Overview",
    #                 "text": "Founded by Phat Pham in Spring 2018, ULAB's Advanced Technologies Group (ATG) is an elite branch that was formed upon the realization that our labs spend way too much time building the tools they need for their experiments. What if we separate the engineering from the science? ATG is a full-blown organization dedicated to doing just that. More specifically, ATG is an augmented intelligence group that combines human-centered design, data science, and software development to help improve the efficiency of laboratories around the UC Berkeley campus and within ULAB itself. We are currently developing projects and curriculum for the upcoming semester in order to immerse students interested in software development immediately in the quickly-growing field."
    #             },
    #             "join": {
    #                 "title": "Want to join us?",
    #                 "text": """
    #                         Unfortunately, applications have closed and we have already filled all of our positions for the current semester. If you have any more questions or would like to learn more about ATG, please send an email to <a href="dilloneskandar@berkeley.edu">dilloneskandar@berkeley.edu</a>. <br/>
    #                         """
    #
    #                     #     """Fill out our application below and feel free to contact the director at <a href="dilloneskandar@berkeley.edu">dilloneskandar@berkeley.edu</a> if you would like to learn more about the Advanced Technologies Group. <br/>
    #                     # <a href="https://docs.google.com/forms/d/e/1FAIpQLSd22cFsyWXDVcjOFRSTuI0mrbGLfnHFHOmc5TPqLQmaQYGAtQ/viewform"> Software Developer Application</a>
    #                     #     """
    #
    #                     # u"""
    #                     # We are currently looking to fill mentor and mentee postions for this semester! If you would like to be considered for a role in our lab next semester, please fill out the respective form below. If you have any more questions or would like to learn more about our lab, please email alanlp@berkeley.edu. <br/>
    #                     #  <a href="https://forms.gle/TDe6YmYeKY3VkUNC6">Mentor Application</a> <br/>
    #                     #  <a href="https://forms.gle/fT3hi9NpW2KUye9BA">Mentee Application</a>
    #                     # """
    #             },
    #             "calendar": {
    #                 "title": "",
    #                 "text": "",
    #                 "object": ""
    #             }
    #         },
    # },
#
    # "ops": {
    #         "logo" : u"/static/img/logos/logo_general.png",
    #         "short_name" : "ops",
	#         "full_name" : "Operations and Publicity",
	#         "navbar" : "Operations and Publicity",
    #         "status": "Active",
    #         "members": ["Yasmeen Musthafa", "Min Young Kim", "Catherine Livelo", "Neha Venkatesh", "Alan Pham", "Justin Gerwien", "Jesslyn Cabero",
    #                     "Jessica Tin", "Marwat Al-Olefi",  "Sunita Bohara", "Kasey Woo"],
    #         "content": {
    #             "overview": {
    #                 "title": "Publicity/Partnerships Team",
    #                 "text": """
    #                     Our team works to reach out to other campus organizations and resources in order to recruit a more diverse group of students and let students be aware of the opportunities ULAB provides.
    #                     In partnership, we strive to work together with other research organizations for undergraduate students to create a network of available resources to help students.
    #                     By publicizing ULAB to incoming freshmen who are looking to develop basic research skills and to other undergraduates with leadership opportunities,
    #                     we want to allow more students to gain valuable experiences that will help their undergraduate carrier both professionally and personally.
    #                     """
    #             },
    #             "join": {
    #                 "title": "Want to join us?",
    #                 "text": """
    #                         Unfortunately, applications have closed and we have already filled all of our positions for the current semester. If you have any more questions or would like to learn more about our team, please send an email to <a href="yasmeenm@berkeley.edu">yasmeenm@berkeley.edu</a>. <br/>
    #                         """
    #
    #                 # """
    #                 #     If you are interested in joining our Operations and Publicity Team, a list of available positions and their descriptions are available at the link below.  To be considered, please also fill out the following form underneath.  If you have any more questions or would like to learn more about our team, please email <a href="yasmeenm@berkeley.edu">yasmeenm@berkeley.edu</a>. <br/>
    #                 #     <a href="https://docs.google.com/document/d/e/2PACX-1vTwHJF2tisUNZ3yv3bPOyRZqCkhLBXQbsJ9sUvWz22kLq3Y81T0RnaqfN7pCeCeLDaPMtLhwUTu3qvS/pub"> Postitions </a> <br/>
    #                 #     <a href="https://l.facebook.com/l.php?u=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLScuj7uD-TF_2rsHOsHJLUlPOML2Dubbr9TnqGMCGmBcd3zdog%2Fviewform%3Fusp%3Dsf_link&h=AT0y-vYYen3mQcWXNZE6TKhZ8onkgkHxDxshgfkeCGasrrR-jTE6zb3xAIpZOBl18pkmZQDe6M2GapgomjG2Zvo_NDGeAkTQoTfqG16jR4VDmfopa5ab2gtyrwqPrfO8RqudUbdztXPGodqj"> Application </a>
    #                 # """
    #             },
    #             "calendar": {
    #                 "title": "",
    #                 "text": "",
    #                 "object": ""
    #             }
    #         }
    # },
#
    # # To Be Determined
    # "aerospace": {
    #         "logo" : u"/static/img/logos/logo_robotics_aero.png",
    #         "short_name": "aerospace",
    #         "full_name": "Robotics and Aerospace Engineering",
    #         "navbar": "Robotics and Aerospace Engineering",
    #         "status": "Under Development",
    #         "team": [],
    #         "content": {
    #             "overview": {
    #                 "title": "This Lab is Under Development",
    #                 "text": ""
    #             },
    #             "join": {
    #                 "title": "",
    #                 "text": ""
    #             },
    #             "calendar": {
    #                 "title": "",
    #                 "text": "",
    #                 "object": ""
    #             }
    #         }
    # }
}





#RESEARCH DICTIONARY IS DEPRECATED
#ONLY HERE FOR REFERENCE DURING WEBSITE REVAMP
research = {
    "physics-ulab": {
        "date": "17 Nov, 2017",
        "app-url": "/lab-jobs/physics",
        "navbar": "Automated Weed Removal",
        "img": "img/project/exoplanet.jpg",
        "title": "Physics and Astrophysics uLab",
        "has_mentor": False,
        "mentor": "",
        "staff-info": {
            "Arjun Savel": {
                "title": "Research Director",
                "email": "asavel@berkeley.edu",
                "linkedin": "https://www.linkedin.com/in/arjun-s-234859b4/",
                "facebook": "",
                "github": "",
                "personal": "",
                "img": ""
            }
        },
        "content": """
            <h4>Astrophysics</h4>
                <p>The Astrophysics branch of uLab provides an academic outlet for first-year students with an interest in space physics, exoplanets, cosmology, and much more, regardless of their intended majors. While Astrophysics uLab functions as a gateway to classes and research opportunities for those who decide to pursue astrophysics research in the future, those who do not will leave the program with the benefits of a broad range of academic skills, research experience, and an heightened understanding of basic astrophysics.</p>
                <p>In this sense, uLab welcomes passionate students more than anything else. From those determining their interest in a major to those to those already sure, uLab Astrophysics is a great place to improve research paper literacy, experimental design and computer programming skills, in addition to participating in the epicenter of important interdisciplinary discoveries.</p>
                <p>The astrophysics branch currently supports two separate projects, the first being on exoplanetary atmospheric analysis. By using open-sourced data from NASA’s Kepler mission, the group plans to create an automated method of categorizing various exoplanet’s atmospheric compositions and habitability likelihood.</p>
                <p>The second of the astrophysics projects focuses on black holes. By comparing the results of an existing research paper making use of RELXILL with those calculated from the new FENRIR model, students will examine black hole spins and hone computational skills.</p>
            <h4>Condensed Matter</h4>
                <p>The Condensed Matter branch of uLab allows students with an interest in atomic and molecular physics to investigate the mechanical, electrical, magnetic, and optical properties of nanomaterials and nanostructures. Students who join the condensed matter team will learn about the various techniques and methods that are prevalent throughout the field. We work closely with research groups in the physics department. Current areas of research at Berkeley are quantum information, physics of nanomaterials, magnetism, quantum materials, optical properties, photoemission, superconductivity, and new materials. Our undergraduate mentors are involved in various condensed matter research groups, and can share their experience in the field as they guide students in their projects.</p>
                <p>Given the interdisciplinary nature of the field of condensed matter, students from various majors, such as physics, chemistry, biology, materials science and engineering are welcome to join. Students interested in developing applicable research skills, such as learning how to write research papers, being introduced to working in a laboratory environment, and professional development are invited to pursue independent research with our undergraduate mentors.</p>
                <p>The condensed matter branch of uLab is currently running projects in graphene deposition and high-temperature superconductors. In the graphene project, we compare two chemical vapor deposition techniques. Between both growth methods, we will compare the prevalence of surface defects and deformations in graphene, and the yield and quality of growth.
            <h4>Particle Physics</h4>
                <p>The uLab Particle Physics Group allows first-year students interested in particle, nuclear, and high-energy physics to learn about the research community at Berkeley while performing new research in fundamental physics. This semester, the particle physics group is investigating the possibility of active cosmic ray shielding using magnetic fields in order to reduce the noise in precision particle physics experiments. The group will be constructing a particle detector and measuring the reduction in particle intensity when different shielding designs are used. In the process, students will also learn about statistics and data analysis as well as software commonly used in the particle physics. An effective shield will allow the group to pursue other precision experiments without the interference of cosmic rays.</p>
            """,
},
    "cogsci-ulab": {
        "date": "17 Nov, 2017",
        "app-url": "/lab-jobs/cogsci",
        "navbar": "Cognitive Neuroscience and Medical Imaging uLab",
        "img": "img/project/mind-reading.png",
        "title": "Cognitive Neuroscience and Medical Imaging uLab",
        "team": ["Riley McDanal", "Annelise Meyer", "Hareen Seerha", "Valerie Burleigh", "Stephanie Chang", "Adam Bittenson", "Allie Morehouse"],
        "has_mentor": False,
        "mentor": ""
    },

    "ATG-ulab": {
        "date": "12 March, 2018",
        "app-url": "/lab-jobs/atg",
        "navbar": "Community Analysis",
        "img": "img/project/human-circuit.jpg",
        "title": "Advanced Technologies Group",
        "team": ["Dillon Eskandar", "Neil Toledo", "Cibi Pari", "David Liu", "Kavi Vaidya", "Charlie Zhang", "Albert Huang"],
        "has_mentor": False,
        "mentor": "",
        "content": "To be added. You can learn more about opportunities for students (of all years) <a href=/lab-jobs/atg> here </a> ",
    },

    "ops-ulab": {
        "date": "",
        "app-url": "/lab-jobs/ops",
        "navbar": "Operations Lab",
        "img": "",
        "title": "Operations and Publicity",
        "team": ["Yasmeen Musthafa", "Min Young Kim", "Catherine Livelo", "Justin Gerwien"],
        "has_mentor": False,
        "mentor": "",
    },

    "genetics-ulab": {
        "date": "17 Nov, 2017",
        "app-url": "/lab-jobs/genetics",
        "navbar": "Public Health Group",
        "img": "img/project/public-health-group.jpg",
        "title": "Genetic Engineering and Molecular Biology uLab",
        "team": ["ULAB"],
        "has_mentor": False,
        "mentor": ""
    },

    "stat-ulab": {
        "date": "17 Nov, 2017",
        "app-url": "/lab-jobs/ml",
        "navbar": "Community Analysis",
        "img": "img/project/human-circuit.jpg",
        "title": "Statistical Modeling and Deep Learning",
        "team": ["Sam Good", "Makena Fetzer"],
        "has_mentor": False,
        "mentor": "TBD"
    },

    "aerospace-ulab": {
        "date": "17 Nov, 2017",
        "app-url": "/lab-jobs/aerospace",
        "navbar": "Tiny Home Env. Impact",
        "img": "img/project/mars-spacesuit-design.jpg",
        "title": "Robotics and Aerospace Engineering uLab",
        "team": ["ULAB"],
        "has_mentor": False,
        "mentor": "",
    }
}
