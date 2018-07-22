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

research = {
    "aerospace-ulab": {
        "date": "17 Nov, 2017",
        "app-url": "/lab-jobs/aerospace",
        "navbar": "Tiny Home Env. Impact",
        "img": "img/project/mars-spacesuit-design.jpg",
        "title": "Robotics and Aerospace Engineering uLab",
        "team": ["ULAB"],
        "has_mentor": False,
        "mentor": "",
        "content": """To be added. You can learn more about opportunities for students (of all years) <a href=/lab-jobs/aerospace> here </a.  """,
    },
    "physics-ulab": {
        "date": "17 Nov, 2017",
        "app-url": "/lab-jobs/physics",
        "navbar": "Automated Weed Removal",
        "img": "img/project/exoplanet.jpg",
        "title": "Physics and Astrophysics uLab",
        "team": ["ULAB"],
        "has_mentor": False,
        "mentor": "",
        "content": u"""
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
        "team": ["Vera Wang", "Yiming Ding", "Muying Chen", "Bansi Parekh"],
        "has_mentor": False,
        "mentor": "TBD",
        "content": """
                    <h4>Lab Overview</h4>
                    Founded in Fall 2017 by Jenna Martin and Riley McDanal, the CogSci Lab has a vision of offering an experience that benefits all undergraduates in the research community.  Experienced researchers can attain leadership roles in the lab setting while facilitating the training and growth of aspiring researchers so that each group is primed for more advanced research opportunities.

                    <h4>Current Staff</h4>
                    <ul class='bullets'>
                        <li>(Beta) Replicate the Libet Experiment (1983) with fMRI (Lau et al 2004)</li>
                        <li>Replicate the Haggard Experiment (2009) or a related experiment</li>
                        <li>Use an open-source dataset to learn how to visualize fMRI data over multiple time-points and understand standard fMRI visualization techniques.</li>
                        <div style="padding-left:50px">

                            <li>One possible location to find open-source fMRI data-set is <a href="https://openfmri.org/dataset/", target="_blank">here</a>.</li>

                            <li>Be able to justify fMRI results with clinical neuroscience and be able to use segmentation algorithms to track neuronal activation at a macro-structural level in the brain.</li>

                        </div>
                        <li>(Beta) Design a novel research experiment analyzing fMRI data for a patient undergoing a specific task. Submit the raw data for this experiment as a data-set for <a href="https://openfmri.org/contact/" target="_blank">OpenfMRI</a> and write a poster/talk describing the results of this project.</li>
                        <li>(Optional engineering goal) Develop a device which reads input brain data and uses said data to serve as a control of a mechanical or virtual system.</li>
                    </ul>

                    <h4> Want to join us? </h4>

                    We currently have all of our positions filled for this semester, if you would like to be considered for a role in our lab next semester, please fill out this form: <a href="https://goo.gl/forms/AmdIpxRSXQUPdQHv2"> Click here</a>
                """
    },
    "ml-ulab": {
        "date": "17 Nov, 2017",
        "app-url": "/lab-jobs/ml",
        "navbar": "Community Analysis",
        "img": "img/project/human-circuit.jpg",
        "title": "Statistical Modeling and Deep Learning",
        "team": ["Sam Good", "Makena Fetzer"],
        "has_mentor": False,
        "mentor": "TBD",
        "content": "To be added. You can learn more about opportunities for students (of all years) <a href=/lab-jobs/ml> here </a> ",

    },
    "medicine-ulab": {
        "date": "17 Nov, 2017",
        "app-url": "/lab-jobs/medicine",
        "navbar": "Consumable Carcinogen",
        "img": "img/project/bright-chemical-structures.jpg",
        "title": "Medicinal Chemistry and Clinical Research uLab",
        "team": ["Moriel Dror", "Aubrianne Milton"],
        "has_mentor": False,
        "mentor": "Alex Powers",
        "content": "To be added. You can learn more about opportunities for students (of all years) <a href=/lab-jobs/medicine> here </a>  ",

    },
    "genetics-ulab": {
        "date": "17 Nov, 2017",
        "app-url": "/lab-jobs/genetics",
        "navbar": "Public Health Group",
        "img": "img/project/public-health-group.jpg",
        "title": "Genetic Engineering and Molecular Biology uLab",
        "team": ["ULAB"],
        "has_mentor": False,
        "mentor": "",
        "content": """
                    <h4>Motivation</h4>

                    <p>
                        The educational aim of this group is to prepare students to tackle the hardest problems in molecular biology. There are two difficulties in starting research in molecular biology.
                        The primary challenge is access to common laboratory equipment.
                        Without common access to equipment (such as PCR, Gel Electrophoresis, etc.), many students find themselves unable to contribute to any part of lab operations.
                        Some of the students we surveyed cited lack of access to laboratory equipment as a primary reason for why they were unable to train themseleves for wet laboratory positions.
                        This uLab is partnering with several biomedical research facilities on campus and at UCSF to provide access to all common laboratory equipment for students to be trained for all of the common technical procedures done in a molecular biology laboratory.
                        The second difficulty is that "wet labs" by defintion are any research that is not primarily computational. The sheer breadth of research interests and techniques make it difficult for students to articulate how they envision participating in biology research.
                        Through partnerships with many laboratories on campus, and through a cadre of dedicated experienced student researchers, we guide students through a survey of major labs and techniques and help define what "wet laboratory research" they are most passionate about.
                    </p>

                    <br>

                    <p>
                        The research aims of this uLab are in particular focused on synthetic chemistry, genomics (both computational and proteomics), and neurobiology (via medical imaging).
                    </p>

                    <h4>Research Questions</h4>

                    <ul class="bullets">
                        <li> What are novel drug delivery techniques used to deliver novel genetic therapies? </li>
                        <li> How does your genetics play a role in the pathology of neurodegenerative diseases? </li>
                        <li> What are the biological principles behind common blood tests? Can these tests be optimized to provide cheaper alternatives to the larger Berkeley area? </li>
                        <li> What are common synthetic techniques used to construct drugs such as Claratin? </li>

                    </ul>

                    <h4> What do join us? </h4>

                    Want to help construct the first student-run pharmacology group>? Want to contribute to the first student-run genetic engineering laboratory? You can learn more about opportunities for students (of all years) <a href=/lab-jobs/genetics> here </a>.

                    """,
    },
    "ATG-ulab": {
        "date": "12 March, 2018",
        "app-url": "/lab-jobs/atg",
        "navbar": "Community Analysis",
        "img": "img/project/human-circuit.jpg",
        "title": "Advanced Technologies Group",
        # "team": ["Sam Good", "Makena Fetzer"],
        # "has_mentor": False,
        # "mentor": "Amit Akula",
        "content": "To be added. You can learn more about opportunities for students (of all years) <a href=/lab-jobs/atg> here </a> ",
    },
}
foundersOrder = ["Joshua Hug", "Mrinalini Sugosh", "Alex Powers", "Dylan Kato", "Michael Oshiro"]
founders = {
    # "placeholder": {
    #     "title": "placeholder",
    #     "img": "img/team-1.jpg",
    #     "bio": """placeholder""",
    # },
    "Alex Powers": {
        "title": "Cofounder",
        "img": "img/team/alex_power.jpg",
        "personal": "",
        "github": "",
        "linkedin": "",
        "bio": """Alex is currently pursuing a Ph.D. at Stanford University. Alex is extremely passionate about undergraduate research; he worked in Paul Alivisatos's Lab on liquid electron microscopy, the Cohen lab on imaging protein movement, and was also an intern at LBNL. He will continue to advise and work with ULAB.""",
    },
    # "Amit Akula": {
    #     "title": "Cofounder",
    #     "img": "img/team/amit_akula.jpg",
    #     "personal": "",
    #     "github": "",
    #     "linkedin": "",
    #     "bio": """Amit does research at UCSF on algorithms for MRI processing and previously worked in the Goldberg lab on surgical robotics. He has served as an RA, community leadership assistant, and TA. In these pursuits, he has strived to develop new, more effective teaching methods and workshops. His close connections with the Residence Hall programs enabled the partnership between the programs.""",
    # },
    "Mrinalini Sugosh": {
        "title": "Chief Operations Officer",
        "img": "img/team/mrinalini_sugosh.jpg",
        "personal": "",
        "github": "",
        "linkedin": "https://www.linkedin.com/in/mrina24/",
        "bio": """Mrina is currently a member of the CS61A Course Staff, Computer Science Mentors, and Society for Women Engineers. Last year, she researched in Dr. Waqas Khalid's lab at the CITRIS institute on creating a platform that helped visualizea programmable array of nanostructures. She is passionate about promoting diversity in STEM and is excited to lower the barrier for entry into research. """,
    },
    "Dylan Kato": {
        "title": "Lead Mentor",
        "img": "img/team/dylan_kato.jpg",
        "personal": "",
        "github": "",
        "linkedin": "",
        "bio": """Dylan is part of the Cal Seismic team, Cal Environment team, and an officer in TBP. Dylan does research in Professor Goldberg's lab that is looking at treating water using solar energy. He facilitated our pilot program partnership with Berkeley Tiny Home, a renewable housing project with which several of our students are working.""",
    },
    "Michael Oshiro": {
        "title": "Cofounder",
        "img": "img/team/michael_oshiro.jpg",
        "personal": "",
        "github": "",
        "linkedin": "",
        "bio": """Michael works at the LBNL lab with data from the ATLAS experiment, the detector at the Large Hadron Collider. He is interested in making undergraduate research more accessible to freshmen. Michael worked to set up ULAB's framework for workshops and accessible resources across campus.""",
    },
    "Joshua Hug": {
        "title": "Faculty Advisor",
        "img": "img/team/josh_hug.jpg",
        "personal": "",
        "github": "",
        "linkedin": "",
        "bio": """Joshua Hug is a teaching professor at Berkeley and previously a lecturer for Computer Science at Princeton University. His primary research interest is in learning at scale and he has developed large scalable teaching models for CS61B and CS188. His passion for finding new and better ways to educate students led him to advise and support ULAB.""",
    },
}

advisors = {
    "Joshua Hug": {
        "title": "Faculty Advisor",
        "img": "img/team/josh_hug.jpg",
        "bio": """Joshua Hug is a teaching professor at Berkeley and previously a lecturer for Computer Science at Princeton University. He completed his PhD in EECS at UC Berkeley in 2011. His primary research interest is in learning at scale and he has developed large scalable teaching models for CS61B and CS188. His passion for finding new and better ways to educate students led him to advise and support ULAB.""",
    },
     "Alex Powers": {
         "title": "Cofounder",
         "img": "img/team/alex_power.jpg",
         "bio": """Alex is currently pursuing a Ph.D. at Stanford University. Alex is extremely passionate about undergraduate research; he worked in Paul Alivisatos's Lab on liquid electron microscopy, the Cohen lab on imaging protein movement, and was also an intern at LBNL. He will continue to advise and work with ULAB.""",
     },
    "Sean Burns": {
        "title": "Faculty Advisor",
        "img": "img/team/sean_burns.jpg",
        "bio": """Sean serves as the Director of the Office of Undergraduate Research and Scholarship (OURS) and has been involved with managing and founding organizations and services to assist undergraduate researchers in diverse communities. His own scholarship and teaching focuses on U.S. social movement history and the dynamic intersections of community activism, political education, and the remaking of the social imagination. He is enthusiastic about making ULAB a successful feature in the undergraduate research program ecosystem.""",
    },
}

team = {
    "Arjun Savel": {
        "img": "",
        "position": "Research Director: Physics and Astrophysics",
        "email": "",
        "personal": "",
        "github": "",
        "linkedin": "",
        "bio": """To be added"""
    },

    "Riley McDanal": {
        "img": "img/team/riley_mcdanal.jpg",
        "position": "Research Director: Cognitive Science and Medical Imaging",
        "email": "",
        "personal": "",
        "github": "",
        "linkedin": "",
        "bio": """I like to sing out loud in my apartment despite the never-ending fear of my neighbors judging me. My homemade speciality is carbonara tacos. Also, I love psychology, politics, and really anything that gets me thinking. """
    },
    "Min Young Kim": {
        "img": "img/team/min_young_kim.jpg",
        "position": "Publicity Director",
        "email": "",
        "personal": "",
        "github": "",
        "linkedin": "https://www.linkedin.com/in/min-young-kim-93281211a/",
        "bio": """I love listening to music and spend too much money on different concerts. While I also enjoy watching movies, I usually get too lazy to go to a movie theater to actually watch any of them, so I most likely will not get your movie references."""
    },
    "Yasmeen Musthafa": {
        "img": "",
        "position": "Operations Director",
        "email": "",
        "personal": "",
        "github": "",
        "linkedin": "",
        "bio": """"""
    },
    "Dillon Eskandar": {
        "img": "",
        "position": "Director of Advanced Technologies Group",
        "email": "",
        "personal": "",
        "github": "",
        "linkedin": "",
        "bio": """"""
    },

    # "Amit Akula": {
    #     "img": "img/team/amit_akula.jpg",
    #     "personal": "",
    #     "github": "",
    #     "linkedin": "",
    #     "bio": """I started Berkeley pre-law, pre-med, and engineering because I actually had no idea what I wanted to do. That made Berkeley so much more fun! I worked at the Rent Board. Taught 61B three times. Hiked to abandoned factories across the Golden Gate Bridge. Finally, I found that I was passionate about helping people solve complex problems. Also I'm a better cook than Dylan.""",
    # },

    # "Phat Pham": {
    #     "img": "img/team/phat_pham.jpg",
    #     "personal": "",
    #     "github": "https://github.com/phatlast96",
    #     "linkedin": "https://www.linkedin.com/in/phamphat/",
    #     "bio": """A web and mobile developer with an interest in machine learning. Sometimes, I like to open up a good book while sitting in my hammock and drinking a cup of hot tea. Other times, I like to be wild amongst my group of friends. Not much of a partier, but I'll light up your intellectual mind. Always had a bad habit of signing up for more things than I can handle.""",
    # },
    "Mrinalini Sugosh": {
        "img": "",
        "position": "Director of Finance",
        "email": "",
        "personal": "",
        "github": "",
        "linkedin": "",
        "bio": """Outside of Physics and Math, some of my hobbies include exploring new places, game design, and cooking. I particularly enjoy spicier cuisines like Indian and Thai. """,
    }
}

# corporate = {
#
#     "Research": {
#             "Principal Investigator": {
#                 "description": "We are launching a group this semester in ULAB designated towards working with different projects from labs, campus clubs, and industrial partners. As a member of this team, you'll be working with the best on technologies like drones, web, blockchain, machine learning, and mobile development. As a member of this team, you'll get valuable industrial experience and networking. Anything that our client requests, you'll be working on it.",
#                 "qualifications": "Computational scientists should have at least some coding experience. Recommended coursework includes CS 61A, CS 61B, and Math 54/EE 16A. Data science courses are also useful. Outside experience and internships can replace coursework. We are looking for creative problem solvers with good analytical skills.",
#                 "perks": "Membership perks include working with other developers with experience in all kinds of technologies, working on new technologies, visiting labs, having meeting with clients, & attending fun social events.",
#                 "link": "https://goo.gl/forms/SOmJC45WKGzFtmsJ3",
#                 "deadline": "March 15th",
#             },
#         },
#
#     "Operations": {
#             "Operations Team Member": {
#                 "description": u"As our organization grows, operations have become increasingly complex, making it necessary to devote considerable time to ensuring communication lines and general operations stay functional. An operations team member would be responsible for ensuring that documentation stays updated and that labs are meeting all requirements and making progress with their projects.",
#                 "qualifications": u"Operations background or interest and basic coding experience is preferred. Strong communication and organizational skills.",
#                 "commitment": u"Time commitment is roughly 3-5 hours per week.",
#                 "perks": u"Course credit is available.",
#                 "link": u"https://goo.gl/forms/OcIEQgLkYyxJaZlk1",
#                 "deadline": u"Rolling",
#             },
#             "Operations Analyst": {
#                 "description": """Operations analysts are responsible for helping to manage the growing complexity of ULAB as a organization by ensuring that
#                     the various labs remain in contact with the front office and that all documentation is kept up to date. Additionally, analysts will help
#                     keep communication lines functional and identify possible areas that could run more efficiently. In general, analysts will also keep track
#                     of the projects that labs are working on and whether they are going smoothly.""",
#                 "qualifications": """A background or interest in operations is strongly preferred, as is basic knowledge of coding. Applicants should be
#                     well-organized, able to communicate well, and detail-oreinted.""",
#                 "perks": """Perks: Logistical experience in maintaining a research organization, course credit is available.""",
#                 "link": "https://docs.google.com/forms/d/e/1FAIpQLSdqDBTozuwY5aT8bHKkfPQIjWEh5_6smyl809fDVvSPqd_S4Q/viewform",
#                 "deadline": "Rolling",
#             },
#         },
#
#     "Development": {
#             "Computational Scientist": {
#                 "description": """Nowadays nearly all branches of scientific research make use of computers in some way, and a basic degree of programming
#                     skill has become a necessity. As a computational scientist you will be helping others work with code related to their research projects and
#                     answer their questions about software. You will also work with our software division to acquire and learn to use scientific software. Certain
#                     labs have computational positions specific to them if you have an interest in a particular field of research and want to apply your
#                     computational skills there. To read more information about these lab-specific computational positions, visit their lab positions page.""",
#                 "commitment": """Attendance of weekly lab staff meetings and project meetings with students is required. Computational scientists are expected
#                 to hold office hours for students to ask coding and software questions. Expect to spend 6-8 hours per week.""",
#                 "qualifications": "Computational scientists should have at least some coding experience. Recommended coursework includes CS 61A, CS 61B, and Math 54/EE 16A. Data science courses are also useful. Outside experience and internships can replace coursework. We are looking for creative problem solvers with good analytical skills.",
#                 "perks": "Membership perks include working with other developers with experience in all kinds of technologies, working on new technologies, visiting labs, having meeting with clients, & attending fun social events.",
#                 "link": "https://docs.google.com/forms/d/e/1FAIpQLSdfawgkUoV3cxLPN2rNnYL-skuWhEAFBf6aBKdC4bbyrBuwsA/viewform",
#                 "deadline": "Rolling",
#             },
#             "Graphic Designer/Animator": {
#                 "description": """The Visualization ULAB is looking for people with experience in graphic design and/or animation. As a graphic designer,
#                     you will primarily be tasked with making promotional materials for ULAB such as fliers and images used for presentations. Addtionally,
#                     you may work to refine the design and layout of our website. If you so choose, you may also be using your skills to help the other labs
#                     communicate their work by rendering biological molecules, generating physical simulations, or visualizing their research in some other
#                     way.""",
#                 "qualifications": """Can vary depending on the work you want to do. For general design work, experience in Photoshop or comparable
#                     image editor is necessary. For all cases, previous work/demonstration of your skill set is needed.""",
#                 "commitment": """Time commitment can be variable but expect 3+ hours per week.""",
#                 "perks": """Perks: An opportunity to help research come to life in a visual fashion, possible contacts to outside organizations or animation
#                     studios.""",
#                 "link": "https://docs.google.com/forms/d/e/1FAIpQLScBNQ3hPquCZbPxBgeQF0OKSX6EeQ7-nMftj7IVzd5jVamWOg/viewform",
#                 "deadline": "Rolling",
#             },
#             "Liaison": {
#                 "description": """Many of ULAB's key functions are reliant on partnerships with other laboratories and groups. Without forming relationships
#                     with these outside organizations, we would simply not be able to obtain the equipment or the training needed to conduct research. For this
#                     reason, we are looking for anyone who is interested in helping our researchers reach out to other groups, finding points of contact,
#                     and maintaining friendly relations with other organizations on campus, particularly research labs. You will act as the face of ULAB,
#                     arranging face-to-face meetings, building trust, and keeping track of our interactions with other organizations.""",
#                 "qualifications": """Applicants should be people-oriented, professional and cordial in their interactions with others, and have
#                     excellent communication skills. Ability to work with teams and fulfill their requests is a must.""",
#                 "perks": """Perks: The opporunity to network with professors and graduate students, as well as gain experience in the administrative workings of
#                     research organizations.""",
#                 "link": "https://docs.google.com/forms/d/e/1FAIpQLScHG1LaoHrVrhDNCbikGMBH6upfQW9hwkalfWUsAWHGM-F5yA/viewform",
#                 "deadline": "Rolling",
#             },
#             "Fundraiser": {
#                 "description": """Research is not exactly a cheap endeavor, and as a result ULAB is looking for people who are entrepreneurially-minded and
#                     are willing to come up with ideas for raising the funds necessary for conducting research and the day-to-day operations of the organization.
#                     Additionally, you will likely help with seeking grants and writing proposals to help fund research projects.""",
#                 "qualifications": """Ideally applicants should have previous experience with raising money for student organizations and be comfortable
#                     with reaching out to outside organizations. Knowledge of writing grant proposals is a plus.""",
#                 "perks": """Perks: Administrative experience in a complex organization and experience in obtaining funds for research.""",
#                 "link": "https://docs.google.com/forms/d/e/1FAIpQLSdleSkDzfN8fBRH9em5_Rs9hr_pwVq8ux_RZY5P3EZQgfpAog/viewform",
#                 "deadline": "Rolling",
#             },
#         },
#
#     "Finance": {
#             "Finance Manager": {
#                 "description": u"As our organization grows and finds needs for more funds, we find that that we also require staff to help us effectively manage these funds. The Finance Manager would be responsible for allocating organization funds, managing fund requests, and generally being aware of grant application pipelines.",
#                 "qualifications": u"Accounting background or interested is preferred. Proficiency with Microsoft Excel is required.",
#                 "commitment": u"Time commitment is roughly 3-5 hours per week.",
#                 "perks": u"Perks include gaining experience with fund management for large organizations. Course credit is available.",
#                 "link": u"https://goo.gl/forms/6fqjYf118ntbBL3h1",
#                 "deadline": u"Rolling",
#             },
#         },
# }

# join_infoOrder = ["1st Year", "2nd Year", "Upperclassman", "Graduate Student"]
# join_info = {
#     "1st Year": {
#             "New Student": {
#                 "description": "Undergraduate Labs @ Berkeley's core mission is to train UC Berkeley's newest members so they are prepared to tackle some of the hardest research challenges on campus. To do this, new students (Freshmen and Junior Transfers) work as researchers within our student-run research laboratories. We design all of our research projects based on the interests of new students and to relate to the work being done on campus. That way, working in a uLab as a researcher in your first year allows you to explore what you are passionate about while simultaneously training for a research position at a professional research laboratory on campus.",
#                 "qualifications": "Further, each uLab has dedicated staff composed of 2nd years, upper-division students, and graduate students. These staff members (1) guide students on their research projects, (2) provide advising for their next research opportunity, (3) provide extensive training on fundamental and technical research skills, and (4) arrange for experiential opportunities such as lab tours and coffee chats with graduate students.",
#                 "commitment": "While the projects have already been set up for Spring 2018, we have many openings in our uLabs for students, ranging from studying the habitability of exoplanets to modeling neurodegeneration in multiple sclerosis patients over time. Click on the button below to see our current openings for new students.",
#                 "link": "/new-student",
#                 "linktext": "New Student Positions",
#             },
#         },
#      "2nd Year": {
#             "Mentor": {
#                 "description": "Undergraduate Labs @ Berkeley's core mission is to train UC Berkeley's newest members so they are prepared to tackle some of the hardest research challenges on campus. This is based on a fundamental belief that UC Berkeley undergraduates, graduate students, staff, and faculty have a responsibility to ensure that all new students get the training and support they need to succeed. As a second year student, we believe that our mission extends to you in an incredibly unique way. We ensure that second year students get direct research experience working as assistant mentors. Further, we design all of our opportunities for second years to maximize their interactions with laboratories on campus. For students still looking for research, this unique dual goal allows second year students to quickly find research positions on campus. As assistant mentors, laboratory managers, operations directors, equipment operators, and other core staff, we hope to develop your core research skills while simultaneously enabling you to train the next generation of Berkeley students.",
#                 "qualifications": "If you are already in a research lab, you can apply as a mentor in one of our labs. As a mentor, you gain experience supervising a cadre of new students, network with other student researchers in your field, and develop a variety of technical and core research skills.",
#                 "commitment": "If you want to join a research lab but you haven't already, you have the option of being an assistant mentor; this allows you to gain the experience of working within a lab without adding the pressure of guiding other students through the process as well.",
#                 "perks": "If you want to learn to run large organizations, particularly those with a research focus, apply to one of our management positions. Second years are the core of our lab operations team and many move on to executive management positions within these roles.",
#                 "link": "/ulab-jobs",
#                 "linktext": "Research Jobs",
#                 "link2": "/corporate-jobs",
#                 "linktext2": "Operations and Executive Jobs",
#                 "link3": "/software-jobs",
#                 "linktext3": "Computational Jobs",
#             },
#         },
#     "Upperclassman": {
#             "Mentor": {
#                 "description": "As an upperclassman with research experience, you have the knowledge necessary to guide newer students through the process.",
#                 "qualifications": "Just as we train Berkeley's newest members to contribute to the hardest problems on campus, we provide opportunities for upper-division students to lead research projects, operate research labs, and gain experience in advanced technical skills. As ULAB is run entirely by students, we look to students like you to take on jobs often held by professors, graduate students, and the campus administration.",
#                 "commitment": "If you want to join a research lab but you haven't already, you have the option of being an associate mentor or serve in leadership roles such as operation directors, technical consultants, and more; this allows you to gain the experience of working within a lab without adding the pressure of guiding other students through the process as well.",
#                 "link": "/ulab-jobs",
#                 "linktext": "Research Jobs",
#                 "link2": "/corporate-jobs",
#                 "linktext2": "Operations and Executive Jobs",
#                 "link3": "/software-jobs",
#                 "linktext3": "Computational Jobs",
#             },
#         },
#     "Graduate Student": {
#             "Mentor": {
#                 "description": "As an graduate student with research experience, you have the knowledge necessary to guide newer students through the process.",
#                 "qualifications": "Just as we train Berkeley's newest members to contribute to the hardest problems on campus, we provide opportunities for graduate students to lead research projects, operate research labs, and gain experience in advanced technical skills. As ULAB is run entirely by students, we look to students like you to take on jobs often held by professors and the campus administration.",
#                 "link": "/ulab-jobs",
#                 "linktext": "Research Jobs",
#                 "link2": "/corporate-jobs",
#                 "linktext2": "Operations and Executive Jobs",
#                 "link3": "/software-jobs",
#                 "linktext3": "Computational Jobs",
#             },
#         },
# }

labs = {
    "physics": {
            "logo" : u"static/img/logos/logo_physics.png",
            "short_name": u"physics",
            "full_name": u"Physics and Astrophysics",
            "navbar": u"Physics" },

    "cogsci": {
            "logo" : u"static/img/logos/logo_cog_sci.png",
            "short_name": u"cogsci",
            "full_name": u"Cognitive Neuroscience and Medical Imaging",
            "navbar": u"Cog_Sci" },

    "bio": {
            "logo" : u"static/img/logos/logo_bio.png",
            "short_name": u"genetics",
            "full_name": u"Genetic Engineering and Molecular Biology",
            "navbar": u"Genetic Engineering and Molecular Biology" },

    "aerospace": {
            "logo" : u"static/img/logos/logo_robotics_aero.png",
            "short_name": "aerospace",
            "full_name": "Robotics and Aerospace Engineering",
            "navbar": "Robotics and Aerospace Engineering" },

    "cs": {
            "logo" : u"static/img/logos/logo_stat_ml.png",
            "short_name": "cs",
            "full_name": "Statistical Modeling and Deep Learning",
            "navbar": "Statistical Modeling and Deep Learning" },

    "atg" : {
            "logo" : u"static/img/logos/logo_atg.png",
	        "short_name" : "ATG",
	        "full_name" : "Advanced Technologies Group",
	        "navbar" : "Advanced Technologies Group" },

    "ops" : {
            "logo" : "",
            "short_name" : "ops",
	        "full_name" : "Operations and Publicity",
	        "navbar" : "Operations and Publicity" }
    }



# software_jobs_order = ["Advanced Technologies Group", "Software Operations", "Visualization", "Statistical Modeling and Deep Learning",
#     "Genetic Engineering and Molecular Biology", "Robotics and Aerospace Engineering", "Medicinal Chemistry and Clinical Research",
#     "Cognitive Neuroscience and Medical Imaging", "Physics and Astrophysics"]
# software_jobs_order.sort()
#
# software_jobs = {
#
#     "Advanced Technologies Group":
#         filter_dict(get_lab_jobs("atg"), {"Software Development Engineer"}),
#

#     "Software Operations":
#         filter_dict(corporate["Development"], {"Computational Scientist"}),
#     "Visualization":
#         filter_dict(corporate["Development"], {"Graphic Designer/Animator"}),

#     "Statistical Modeling and Deep Learning":
#         get_lab_jobs("ml"),
#     "Genetic Engineering and Molecular Biology":
#         filter_dict(get_lab_jobs("genetics"), {"Bioinformatics (Computational) Scientist"}),
#     "Robotics and Aerospace Engineering":
#         filter_dict(get_lab_jobs("aerospace"),
#             {"Controls (Robotics) Engineer", "Controls (Sensory Integration Engineer", "Control Engineer", "Software Engineer"}),
#     "Medicinal Chemistry and Clinical Research":
#         filter_dict(get_lab_jobs("medicine"), {"Bioinformatics (Computational) Scientist"}),
#     "Cognitive Neuroscience and Medical Imaging":
#         filter_dict(get_lab_jobs("cogsci"), {"Lab Tech"}),
#     "Physics and Astrophysics":
#         filter_dict(get_lab_jobs("physics"), {"Computational Scientist"}),
# }

# student = {

#     "Statistical Modeling and Deep Learning":
#         filter_dict(get_lab_jobs("ml"), {"New Student Researcher"}),

#     "Robotics and Aerospace Engineering":
#         labs["aerospace"]["job_categories"]["New Student Positions"],

#     "Development":
#         filter_dict(corporate["Development"], {"Liaison", "Fundraiser"}),

#     "Operations":
#         filter_dict(corporate["Operations"], {"Operations Analyst"}),
# }

# # Add ATG operations director to corporate jobs dict

# corporate["Advanced Technologies Group"] = filter_dict(get_lab_jobs("atg"), {"Operations Director"})
