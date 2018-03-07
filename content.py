# -*- coding: utf-8 -*-

# Given the string LAB, pulls all of the jobs (uncategorized) from that lab in the LABS dict. Returns a dict
def get_lab_jobs(lab):
    output = {}
    categories = labs[lab]["job_categories"]
    for k in categories:
        output.update(categories[k])
    return output

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
        "mentor": "Amit Akula",
        "content": """
                    <h4>Research Questions</h4>
                    <ul class='bullets'>
                        <li>Is there a delay between unconsciously making a decision and consciously making a decision? Can we quantitatively measure this difference?</li>
                        <li>How does region-specific neuronal activation relate to neuronal activity?</li>
                        <li>s free will an illusion? What decisions are made unconsciously?</li>
                    </ul>

                    <h4>Research Goals</h4>
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
        "mentor": "Amit Akula",
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
}
foundersOrder = ["Joshua Hug", "Amit Akula", "MRINALINI SUGOSH", "Alex Powers", "Dylan Kato", "Michael Oshiro"]
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
    "Amit Akula": {
        "title": "Cofounder",
        "img": "img/team/amit_akula.jpg",
        "personal": "",
        "github": "",
        "linkedin": "",
        "bio": """Amit does research at UCSF on algorithms for MRI processing and previously worked in the Goldberg lab on surgical robotics. He has served as an RA, community leadership assistant, and TA. In these pursuits, he has strived to develop new, more effective teaching methods and workshops. His close connections with the Residence Hall programs enabled the partnership between the programs.""",
    },
    "MRINALINI SUGOSH": {
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
    "Karina Yap": {
        "img": "img/team/karina_yap.jpg",
        "personal": "",
        "github": "",
        "linkedin": "",
        "bio": """To be added"""
    },

    "Riley McDanal": {
        "img": "img/team/riley_mcdanal.jpg",
        "personal": "",
        "github": "",
        "linkedin": "",
        "bio": """I like to sing out loud in my apartment despite the never-ending fear of my neighbors judging me. My homemade speciality is carbonara tacos. Also, I love psychology, politics, and really anything that gets me thinking. """
    },
    "Min Young Kim": {
        "img": "img/team/min_young_kim.jpg",
        "personal": "",
        "github": "",
        "linkedin": "https://www.linkedin.com/in/min-young-kim-93281211a/",
        "bio": """I love listening to music and spend too much money on different concerts. While I also enjoy watching movies, I usually get too lazy to go to a movie theater to actually watch any of them, so I most likely will not get your movie references."""
    },
    "May Myat Mon": {
        "img": "img/team/may_myat_mon.jpg",
        "personal": "",
        "github": "",
        "linkedin": "",
        "bio": """Hello! My name is May Myat Mon but you can call me Margaret. I enjoy spending quality time with my family and friends. Aside from academics, I love playing badminton and watching movies! :) """
    },
    "Madeleine Weiser": {
        "img": "img/team/madeleine_weiser.jpg",
        "personal": "",
        "github": "",
        "linkedin": "",
        "bio": """I'm a Minnesotan-turned-Californian girl with many, many interests and I am incredibly indecisive. I am happiest when I am outdoors whether it is walking, swimming, hiking, biking, or just lounging around. I adore nature, animals, and sunshine! My family and friends are super important to me, but I'm also always down to meet new people and try new things."""
    },
    "Amit Akula": {
        "img": "img/team/amit_akula.jpg",
        "personal": "",
        "github": "",
        "linkedin": "",
        "bio": """I started Berkeley pre-law, pre-med, and engineering because I actually had no idea what I wanted to do. That made Berkeley so much more fun! I worked at the Rent Board. Taught 61B three times. Hiked to abandoned factories across the Golden Gate Bridge. Finally, I found that I was passionate about helping people solve complex problems. Also I'm a better cook than Dylan.""",
    },
    "Phat Pham": {
        "img": "img/team/phat_pham.jpg",
        "personal": "",
        "github": "https://github.com/phatlast96",
        "linkedin": "https://www.linkedin.com/in/phamphat/",
        "bio": """A web and mobile developer with an interest in machine learning. Sometimes, I like to open up a good book while sitting in my hammock and drinking a cup of hot tea. Other times, I like to be wild amongst my group of friends. Not much of a partier, but I'll light up your intellectual mind. Always had a bad habit of signing up for more things than I can handle.""",
    },
    "Michael Oshiro": {
        "img": "img/team/michael_oshiro.jpg",
        "personal": "",
        "github": "",
        "linkedin": "",
        "bio": """Outside of Physics and Math, some of my hobbies include exploring new places, game design, and cooking. I particularly enjoy spicier cuisines like Indian and Thai. """,
    },
    "Khang Nguyen": {
        "img": "img/team/khang_nguyen.jpg",
        "personal": "",
        "github": "",
        "linkedin": "",
        "bio": """Born and raised in Houston, Texas! When I'm in Berkeley, it's all studying and hard work but when I'm at home, I indulge myself in some video games and Twitch. Aside from video games, listening to music and finding new music is one of my go-to hobbies for when I have nothing to do. If you're trying to find some relaxing music, try Hammock, Stars of the Lid, or Explosions in the Sky :)""",
    },
}

corporate = {

    "Research": {
            "Principal Investigator": {
                "description": "We are launching a group this semester in ULAB designated towards working with different projects from labs, campus clubs, and industrial partners. As a member of this team, you'll be working with the best on technologies like drones, web, blockchain, machine learning, and mobile development. As a member of this team, you'll get valuable industrial experience and networking. Anything that our client requests, you'll be working on it.",
                "qualifications": "Computational scientists should have at least some coding experience. Recommended coursework includes CS 61A, CS 61B, and Math 54/EE 16A. Data science courses are also useful. Outside experience and internships can replace coursework. We are looking for creative problem solvers with good analytical skills.",
                "perks": "Membership perks include working with other developers with experience in all kinds of technologies, working on new technologies, visiting labs, having meeting with clients, & attending fun social events.",
                "link": "https://goo.gl/forms/SOmJC45WKGzFtmsJ3",
                "deadline": "March 15th",
            },
        },

    "Operations": {
            "Operations Team Member": {
                "description": u"As our organization grows, operations have become increasingly complex, making it necessary to devote considerable time to ensuring communication lines and general operations stay functional. An operations team member would be responsible for ensuring that documentation stays updated and that labs are meeting all requirements and making progress with their projects.",
                "qualifications": u"Operations background or interest and basic coding experience is preferred. Strong communication and organizational skills.",
                "commitment": u"Time commitment is roughly 3-5 hours per week.",
                "perks": u"Course credit is available.",
                "link": u"https://goo.gl/forms/OcIEQgLkYyxJaZlk1",
                "deadline": u"Rolling",
            },
            "Operations Analyst": {
                "description": """Operations analysts are responsible for helping to manage the growing complexity of ULAB as a organization by ensuring that
                    the various labs remain in contact with the front office and that all documentation is kept up to date. Additionally, analysts will help
                    keep communication lines functional and identify possible areas that could run more efficiently. In general, analysts will also keep track
                    of the projects that labs are working on and whether they are going smoothly.""",
                "qualifications": """A background or interest in operations is strongly preferred, as is basic knowledge of coding. Applicants should be
                    well-organized, able to communicate well, and detail-oreinted.""",
                "perks": """Perks: Logistical experience in maintaining a research organization, course credit is available.""",
                "link": "https://docs.google.com/forms/d/e/1FAIpQLSdqDBTozuwY5aT8bHKkfPQIjWEh5_6smyl809fDVvSPqd_S4Q/viewform",
                "deadline": "Rolling",
            },
        },

    "Development": {
            "Computational Scientist": {
                "description": """Nowadays nearly all branches of scientific research make use of computers in some way, and a basic degree of programming
                    skill has become a necessity. As a computational scientist you will be helping others work with code related to their research projects and
                    answer their questions about software. You will also work with our software division to acquire and learn to use scientific software. Certain
                    labs have computational positions specific to them if you have an interest in a particular field of research and want to apply your
                    computational skills there. To read more information about these lab-specific computational positions, visit their lab positions page.""",
                "commitment": """Attendance of weekly lab staff meetings and project meetings with students is required. Computational scientists are expected
                to hold office hours for students to ask coding and software questions. Expect to spend 6-8 hours per week.""",
                "qualifications": "Computational scientists should have at least some coding experience. Recommended coursework includes CS 61A, CS 61B, and Math 54/EE 16A. Data science courses are also useful. Outside experience and internships can replace coursework. We are looking for creative problem solvers with good analytical skills.",
                "perks": "Membership perks include working with other developers with experience in all kinds of technologies, working on new technologies, visiting labs, having meeting with clients, & attending fun social events.",
                "link": "https://docs.google.com/forms/d/e/1FAIpQLSdfawgkUoV3cxLPN2rNnYL-skuWhEAFBf6aBKdC4bbyrBuwsA/viewform",
                "deadline": "Rolling",
            },
            "Graphic Designer/Animator": {
                "description": """The Visualization ULAB is looking for people with experience in graphic design and/or animation. As a graphic designer,
                    you will primarily be tasked with making promotional materials for ULAB such as fliers and images used for presentations. Addtionally,
                    you may work to refine the design and layout of our website. If you so choose, you may also be using your skills to help the other labs
                    communicate their work by rendering biological molecules, generating physical simulations, or visualizing their research in some other
                    way.""",
                "qualifications": """Can vary depending on the work you want to do. For general design work, experience in Photoshop or comparable
                    image editor is necessary. For all cases, previous work/demonstration of your skill set is needed.""",
                "commitment": """Time commitment can be variable but expect 3+ hours per week.""",
                "perks": """Perks: An opportunity to help research come to life in a visual fashion, possible contacts to outside organizations or animation
                    studios.""",
                "link": "https://docs.google.com/forms/d/e/1FAIpQLScBNQ3hPquCZbPxBgeQF0OKSX6EeQ7-nMftj7IVzd5jVamWOg/viewform",
                "deadline": "Rolling",
            },
            "Liaison": {
                "description": """Many of ULAB's key functions are reliant on partnerships with other laboratories and groups. Without forming relationships
                    with these outside organizations, we would simply not be able to obtain the equipment or the training needed to conduct research. For this
                    reason, we are looking for anyone who is interested in helping our researchers reach out to other groups, finding points of contact,
                    and maintaining friendly relations with other organizations on campus, particularly research labs. You will act as the face of ULAB,
                    arranging face-to-face meetings, building trust, and keeping track of our interactions with other organizations.""",
                "qualifications": """Applicants should be people-oriented, professional and cordial in their interactions with others, and have
                    excellent communication skills. Ability to work with teams and fulfill their requests is a must.""",
                "perks": """Perks: The opporunity to network with professors and graduate students, as well as gain experience in the administrative workings of
                    research organizations.""",
                "link": "https://docs.google.com/forms/d/e/1FAIpQLScHG1LaoHrVrhDNCbikGMBH6upfQW9hwkalfWUsAWHGM-F5yA/viewform",
                "deadline": "Rolling",
            },
            "Fundraiser": {
                "description": """Research is not exactly a cheap endeavor, and as a result ULAB is looking for people who are entrepreneurially-minded and
                    are willing to come up with ideas for raising the funds necessary for conducting research and the day-to-day operations of the organization.
                    Additionally, you will likely help with seeking grants and writing proposals to help fund research projects.""",
                "qualifications": """Ideally applicants should have previous experience with raising money for student organizations and be comfortable
                    with reaching out to outside organizations. Knowledge of writing grant proposals is a plus.""",
                "perks": """Perks: Administrative experience in a complex organization and experience in obtaining funds for research.""",
                "link": "https://docs.google.com/forms/d/e/1FAIpQLSdleSkDzfN8fBRH9em5_Rs9hr_pwVq8ux_RZY5P3EZQgfpAog/viewform",
                "deadline": "Rolling",
            },
        },

    "Finance": {
            "Finance Manager": {
                "description": u"As our organization grows and finds needs for more funds, we find that that we also require staff to help us effectively manage these funds. The Finance Manager would be responsible for allocating organization funds, managing fund requests, and generally being aware of grant application pipelines.",
                "qualifications": u"Accounting background or interested is preferred. Proficiency with Microsoft Excel is required.",
                "commitment": u"Time commitment is roughly 3-5 hours per week.",
                "perks": u"Perks include gaining experience with fund management for large organizations. Course credit is available.",
                "link": u"https://goo.gl/forms/6fqjYf118ntbBL3h1",
                "deadline": u"Rolling",
            },
        },
}

join_infoOrder = ["1st Year", "2nd Year", "Upperclassman", "Graduate Student"]
join_info = {
    "1st Year": {
            "New Student": {
                "description": "Undergraduate Labs @ Berkeley's core mission is to train UC Berkeley's newest members so they are prepared to tackle some of the hardest research challenges on campus. To do this, new students (Freshmen and Junior Transfers) work as researchers within our student-run research laboratories. We design all of our research projects based on the interests of new students and to relate to the work being done on campus. That way, working in a uLab as a researcher in your first year allows you to explore what you are passionate about while simultaneously training for a research position at a professional research laboratory on campus.",
                "qualifications": "Further, each uLab has dedicated staff composed of 2nd years, upper-division students, and graduate students. These staff members (1) guide students on their research projects, (2) provide advising for their next research opportunity, (3) provide extensive training on fundamental and technical research skills, and (4) arrange for experiential opportunities such as lab tours and coffee chats with graduate students.",
                "commitment": "While the projects have already been set up for Spring 2018, we have many openings in our uLabs for students, ranging from studying the habitability of exoplanets to modeling neurodegeneration in multiple sclerosis patients over time. Click on the button below to see our current openings for new students.",
                "link": "/new-student",
                "linktext": "New Student Positions",
            },
        },
     "2nd Year": {
            "Mentor": {
                "description": "Undergraduate Labs @ Berkeley's core mission is to train UC Berkeley's newest members so they are prepared to tackle some of the hardest research challenges on campus. This is based on a fundamental belief that UC Berkeley undergraduates, graduate students, staff, and faculty have a responsibility to ensure that all new students get the training and support they need to succeed. As a second year student, we believe that our mission extends to you in an incredibly unique way. We ensure that second year students get direct research experience working as assistant mentors. Further, we design all of our opportunities for second years to maximize their interactions with laboratories on campus. For students still looking for research, this unique dual goal allows second year students to quickly find research positions on campus. As assistant mentors, laboratory managers, operations directors, equipment operators, and other core staff, we hope to develop your core research skills while simultaneously enabling you to train the next generation of Berkeley students.",
                "qualifications": "If you are already in a research lab, you can apply as a mentor in one of our labs. As a mentor, you gain experience supervising a cadre of new students, network with other student researchers in your field, and develop a variety of technical and core research skills.",
                "commitment": "If you want to join a research lab but you haven't already, you have the option of being an assistant mentor; this allows you to gain the experience of working within a lab without adding the pressure of guiding other students through the process as well.",
                "perks": "If you want to learn to run large organizations, particularly those with a research focus, apply to one of our management positions. Second years are the core of our lab operations team and many move on to executive management positions within these roles.",
                "link": "/ulab-jobs",
                "linktext": "Research Jobs",
                "link2": "/corporate-jobs",
                "linktext2": "Operations and Executive Jobs",
                "link3": "/software-jobs",
                "linktext3": "Computational Jobs",
            },
        },
    "Upperclassman": {
            "Mentor": {
                "description": "As an upperclassman with research experience, you have the knowledge necessary to guide newer students through the process.",
                "qualifications": "Just as we train Berkeley's newest members to contribute to the hardest problems on campus, we provide opportunities for upper-division students to lead research projects, operate research labs, and gain experience in advanced technical skills. As ULAB is run entirely by students, we look to students like you to take on jobs often held by professors, graduate students, and the campus administration.",
                "commitment": "If you want to join a research lab but you haven't already, you have the option of being an associate mentor or serve in leadership roles such as operation directors, technical consultants, and more; this allows you to gain the experience of working within a lab without adding the pressure of guiding other students through the process as well.",
                "link": "/ulab-jobs",
                "linktext": "Research Jobs",
                "link2": "/corporate-jobs",
                "linktext2": "Operations and Executive Jobs",
                "link3": "/software-jobs",
                "linktext3": "Computational Jobs",
            },
        },
    "Graduate Student": {
            "Mentor": {
                "description": "As an graduate student with research experience, you have the knowledge necessary to guide newer students through the process.",
                "qualifications": "Just as we train Berkeley's newest members to contribute to the hardest problems on campus, we provide opportunities for graduate students to lead research projects, operate research labs, and gain experience in advanced technical skills. As ULAB is run entirely by students, we look to students like you to take on jobs often held by professors and the campus administration.",
                "link": "/ulab-jobs",
                "linktext": "Research Jobs",
                "link2": "/corporate-jobs",
                "linktext2": "Operations and Executive Jobs",
                "link3": "/software-jobs",
                "linktext3": "Computational Jobs",
            },
        },
}

labs = {
    "physics": {
            "img": u"img/labs/phsyicslabcover.jpg",
            "short_name": u"physics",
            "full_name": u"Physics and Astrophysics",
            "navbar": u"Physics",
            "job_categories": {
                "Research Jobs": {
                    "Condensed Matter Mentor": {
                        "description": u"We are looking to hire undergraduates to mentor small groups of students as they perform condensed matter experiments. As a mentor, you will attend weekly meetings with the laboratory staff and students. You will also communicate with the students to answer questions, supervise experiments, and report on progress. As this is a student-run lab, you will be mentoring students on their own independent research projects. Current research interests include superconductivity and graphene deposition.",
                        "qualifications": u"You must have previous research experience, preferably relating to semiconductor physics or solid state physics. However, familiarity with our specific research topics is not required.",
                        "commitment": u"5-6 hours per week",
                        "perks": u"In addition to professional and technical development workshops, you will have the opportunity to network with professors and graduate students on campus. Course credit is available, and you can receive up to four units.",
                        "link": u"https://goo.gl/forms/ViPPKHgrl9VPPdUn2",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner for a better chance."
                    },
                },
                "Lab Management": {
                    "Computational Scientist": {
                        "description": u"We are launching a group this semester in ULAB designated towards working with different projects from labs, campus clubs, and industrial partners. As a member of this team, you'll be working with the best on technologies like drones, web, blockchain, machine learning, and mobile development. As a member of this team, you'll get valuable industrial experience and networking. Anything that our client requests, you'll be working on it.",
                        "qualifications": u"Computational scientists should have at least some coding experience. Recommended coursework includes CS 61A, CS 61B, and Math 54/EE 16A. Data science courses are also useful. Outside experience and internships can replace coursework. We are looking for creative problem solvers with good analytical skills.",
                        "perks": u"Membership perks include working with other developers with experience in all kinds of technologies, working on new technologies, visiting labs, having meeting with clients, & attending fun social events.",
                        "link": u"https://goo.gl/forms/SOmJC45WKGzFtmsJ3",
                        "deadline": u"Rolling",
                    },
                    "Lab Manager": {
                        "description": u"We are looking to hire lab managers for our physics lab. You will be assisting our operations director in the day-to-day running of the lab.  You will also work on building and maintaining partnerships with labs on campus by networking with and pitching to graduate students and professors. You will help maintain equipment, staff, and student rosters. You will also assist with other operations-related ventures such as grant writing, room bookings, and organizing Google Drive files.",
                        "commitment": u"4-6 hrs per week",
                        "perks": u"This is a fantastic opportunity to get involved with scientific research on a more administrative level, while networking with faculty members and learning how to do scientific pitches. You will have access to professional and technical development workshops. Course credit is available, and you can receive up to four units.",
                        "link": u"https://goo.gl/forms/CUbvVJ1RQhCp06us1",
                        "deadline": u"Rolling"
                    },
                },
            },

        },
    "cogsci": {
            "img": u"img/labs/phsyicslabcover.jpg",
            "short_name": u"cogsci",
            "full_name": u"Cognitive Neuroscience and Medical Imaging",
            "navbar": u"Cog_Sci",
            "job_categories": {
                "Research Jobs": {
                    "Mentor (Libet Experiment)": {
                        "description": u"Update lab staff weekly to deliver team progress reports and meet as necessary. Coordinate weekly meetings with student teams in order to provide mentoring and advice towards the development of research projects. Communicate regularly with students in order to determine progress and issues, setting up any formal reporting methods as necessary. Assist in the development of field-specific workshops. In conjunction with other lab staff, assess student curricular development through the evaluation of short turn-ins and assignments. Provide contact info for field experts for consulting and help foster connections with labs.",
                        "qualifications": u"Familiarity with the Libet Exeriment + relevant reserach experience (at least one semester) and coursework in some of the following areas: psychology, cognitive science, and CS 1) Knowledge of EEG theory and operation (preferred) 2) knowledge of general neuroanatomy and neurobio (psych 117, psych c127 are good), Basic CS Skills",
                        "commitment": u"~5 Hours/Week + additional time as needed once projects are underway",
                        "perks": u"Ability to direct a student-run reserach project; Opportunities to meet researchers from other labs on campus through liason meetings; Social events and community of passionate researchers. Course Credit is Available. ",
                        "link": u"https://goo.gl/forms/jCvPLlBLhCFhsuDf1",
                        "deadline": u"Rolling"
                        },
                    "Mentor (Mapping Neural Networks)": {
                        "description": u"Update lab staff weekly to deliver team progress reports and meet as necessary. Coordinate weekly meetings with student teams in order to provide mentoring and advice towards the development of research projects. Communicate regularly with students in order to determine progress and issues, setting up any formal reporting methods as necessary. Assist in the development of field-specific workshops. In conjunction with other lab staff, assess student curricular development through the evaluation of short turn-ins and assignments. Provide contact info for field experts for consulting and help foster connections with labs.",
                        "qualifications": u"Relevant reserach experience (at least one semester) and coursework in some of the following areas: psychology, cognitive science, and CS 1) knowledge of general neuroanatomy and neurobio (psych 117, psych c127 are good options) 2), CS requirements:CS61B, CS188 or equivalent",
                        "commitment": u"~5 Hours/Week + additional time as needed once projects are underway",
                        "perks": u"Ability to direct a student-run reserach project; Opportunities to meet researchers from other labs on campus through liason meetings; Social events and community of passionate researchers. Course Credit is Available. ",
                        "link": u"https://goo.gl/forms/jCvPLlBLhCFhsuDf1",
                        "deadline": u"Rolling"
                        },
                    "Mentor (Mapping Neural Networks)": {
                        "description": u"Update lab staff weekly to deliver team progress reports and meet as necessary. Coordinate weekly meetings with student teams in order to provide mentoring and advice towards the development of research projects. Communicate regularly with students in order to determine progress and issues, setting up any formal reporting methods as necessary. Assist in the development of field-specific workshops. In conjunction with other lab staff, assess student curricular development through the evaluation of short turn-ins and assignments. Provide contact info for field experts for consulting and help foster connections with labs.",
                        "qualifications": u"Relevant reserach experience (at least one semester) and coursework in some of the following areas: psychology, cognitive science, and/or CS",
                        "commitment": u"~5 Hours/Week + additional time as needed once projects are underway",
                        "perks": u"Ability to direct a student-run reserach project; Opportunities to meet researchers from other labs on campus through liason meetings; Social events and community of passionate researchers. Course Credit is Available. ",
                        "link": u"https://goo.gl/forms/jCvPLlBLhCFhsuDf1",
                        "deadline": u"Rolling"
                        },
                    },
                "Lab Management": {
                    "Lab Tech": {
                        "description": u"The lab technician is tasked with working through logistics and running experiments for the lab.",
                        "qualifications": u"Must be able to operate EEG, operate MRI, or be computer science expert (knowledge in statistical modeling and mapping of brain)",
                        "commitment": u"The estimated time commitment is roughly 5 hours per week.",
                        "perks": u"Perks include the ability to help a student-run reserach project; opportunities to meet researchers from other labs on campus through liason meetings; social events and community of passionate researchers. Up to 4 units of course Credit are available. ",
                        "link": u"https://goo.gl/forms/jCvPLlBLhCFhsuDf1",
                        "deadline": u"Rolling"
                        },
                },
            },
        },
     "medicine": {
            "img": u"img/labs/phsyicslabcover.jpg",
            "short_name": u"medicine",
            "full_name": u"Medicinal Chemistry and Clinical Research",
            "navbar": u"Medicinal Chemistry and Clinical Research",
            "job_categories": {
                "Clinical Research": {
                    "Clinical Research Scientist": {
                        "description": u"ULAB is looking for a driven Clinical Research Scientist capable of executing and/or learning procedures relevant to clinical applications. Our main interest is setting up a blood lab that will be used to analyze patient blood samples. We are interested in recruiting clinical research scientists who has Biology/Chemistry lab experience and can teach undergraduates skills that might be conducive to doing clinical research and diagnostics.",
                        "qualifications": u"Qualified applicants will have taken a wet laboratory class on campus (Biology 1AL, 1B, Chemistry 1AL, 3AL, 4A, 4B, etc.), have experience working in a chemical biology/biochemistry/IB/MCB research lab, and using common laboratory equipment. We do a lot of training in house so a willingness to learn new things is the biggest qualification!",
                        "commitment": u"6 - 10 hours a week (heavier at the beginning of the semester, lighter during midterm season)",
                        "perks": u"Practice in clinical design, learning techniques associated with diagnosing blood, potentially formal training from UCSF experts in phlebotomy, experience instructing and undergraduate management, graded course credit (if not already enrolled in lab).",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSdAQ9nLD4iAAJ-0hobLz2unvITRhxNGZbX8nLSDyK5-bo0G5g/viewform",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner for a better chance!"
                    },

                    "Clinical Research Liaison": {
                        "description": u"ULAB is looking for a driven Clinical Research Liaison who is able to communicate effectively in hopes of creating ULAB partnerships with other labs and companies. Must have strong communication to relay message to other team members about lab collaborations and their status/availability. He/she must be willing to create solid relationships that can be built on further down the road. They must also be willing to learn about the possible research methods and relay new methods back to the ULAB teams. Liaisons in our clinical research arm often communicate with hospitals, medical testing labs, and biology research laboratorys.",
                        "qualifications": u"If the applicant is a UC Berkeley undergraduate, be enthusiastic and outgoing as well as being flexible in response to the prospective labs’ available times to meet. Applicant must have experience working with other on a one-on-one setting as well as in a group setting.",
                        "commitment": u"6 - 10 hours a week (heavier at the beginning of the semester, lighter during midterm season)",
                        "perks": u"Involvement in the community of medicine, experience instructing and undergraduate management, graded course credit (if not already enrolled in lab). This individual will build an extensive network of contacts in research laboratories, clinical facilities, and other medical-related groups. Practice in clinical design, learning techniques associated with diagnosing blood, potentially formal training from UCSF experts in phlebotomy, experience instructing and undergraduate management, graded course credit (if not already enrolled in lab).",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSdAQ9nLD4iAAJ-0hobLz2unvITRhxNGZbX8nLSDyK5-bo0G5g/viewform",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner for a better chance!"
                    },

                },

                "Medicinal Chemistry": {
                    "Pharmaceutical Scientist": {
                        "description": u"ULAB is looking for a sophomore/junior “Pharmaceutical Chemist” who would enjoy replicating a known synthetic pathway for a natural product or pharmaceutical product under the mentorship of an experienced undergrad mentor. You can expect to learn synthetic design, reaction setup, water-free techniques, product purification with column chromatography/Prep TLC, and product characterization with H/C13 NMR. The applicant should be interested in medicinal chemistry and have a rough idea of basic organic chemistry techniques, with exposure in at least introductory Organic Chemistry (Chem 3A/B or Chem 12A/B).",
                        "qualifications": u"Applicant needs to have received a B or higher in an introductory Organic Chemistry course (12A, 3A or equivalent) and be enrolled (or have completed) a second semester Organic Chemistry course (12B, 3B or equivalent). Preferred majors: Chemistry, Chemical Biology, Chemical Engineering, Molecular Cell Biology, Bioengineering.",
                        "commitment": u"6 - 8 hours per week",
                        "perks": u"Practice in designing synthetic projects, practice with process chemistry, experience with instructing and undergraduate management, graded course credit (if not already enrolled in lab).",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLScD6jFOYJeUJ_uYZ21PHMtk0Lp7ogN3FR_uNsQj1bi6b4j2rQ/viewform",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner rather than later"
                    },

                    "Medicinal Chemist": {
                        "description": u"ULAB is looking for a research-experienced undergraduate or graduate Medicinal Chemist capable of executing synthetic procedures, and who is interested in learning how to guide less experienced undergraduates through a natural product or pharmaceutical product synthesis pathway. Knowledge of purification techniques (column chromatography, recrystallization, HPLC) is required. Experience with heterocyclic chemical synthesis/being enrolled in Chemistry 114/214 would be highly preferred.",
                        "qualifications": u"If the applicant is a UC Berkeley undergraduate, he/she should have received a B or higher in an introductory Organic Chemistry course (12A, 3A or equivalent) and be enrolled (or have completed) a second semester Organic Chemistry course (12B, 3B or equivalent). Applicant must have research experience performing synthesis either in an academic or professional setting.",
                        "commitment": u"5-6 hours per week",
                        "perks": u"Practice in designing synthetic projects, practice with process chemistry, experience instructing and undergraduate management, course credit, free food, and building relationships with many research laboratories on campus!",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSfo9Q8I7RdJxs5-Q7qEWmD-20n2AnaCjZ5THRZwSCvUFNvtOg/viewform",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner for a better chance."
                    },

                },

                "Computational/Technological": {

                     "Biotechnologist": {
                        "description": u"Biotechnologists/biotechnicians develop and implement new research projects. Set up instruments and laboratory equipment used to conduct and monitor experiments such as centrifuges, flasks and spectrophotometers. Should be able to use spectrophotometers, compound microscopes, and benchtop centrifuges. Be able to use tools to rearrange fragments of DNA and modify genetic material.",
                        "commitment": u"6 - 10 hours a week (heavier at the beginning of the semester, lighter during midterm season)",
                        "qualifications":u"Taken a wet laboratory class on campus (Biology 1AL, 1B, Chemistry 1AL, 3AL, 4A, 4B, etc.), experience working in a research lab preferred, and experience in managing and using laboratory equipment. We do a lot of training in house so a willingness to learn new things is the biggest qualification! Preferable, but not required: Designed and ran a research project.",
                        "perks": u"Perks: Get access to machines such as temperature cyclers, centrifuges, microscopes, and additional machines! working with a group of like-minded researchers, course credit, free food, free swag, and building relationships with many research laboratories on campus.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSefl6cD-_ohvJtMu0aU93OlaUfSPqU16BLb5B8_z1agxj2C_A/viewform",
                        "deadline": u"We'll review applications on a rolling basis until March 15th, or until all our positions have been filled."
                    },

                     "Physical Chemist/Molecular Imaging Specialist": {
                        "description": u"The imaging specialist must possess a passion for imaging, theoretical knowledge of optical microscopy and experimental imaging experience with biological samples.",
                        "commitment": u"5 - 8 hrs per week",
                        "qualifications": u"Must have taken a wet laboratory class on campus (Biology 1AL, 1B, Chemistry 1AL, 3AL, 4A, 4B, etc.), experience working in a research lab is preferred, and experience in managing and using laboratory equipment (ex: imaging live and fixed biological samples such as, various confocal microscopes, multiphoton intravital microscope, slide scanners and live cell imaging microscopes)",
                        "perks": u"Perks: Access to machines such as temperature cyclers, centrifuges, microscopes, and additional machines! working with a group of like-minded researchers, course credit, free food, free swag, and building relationships with many research laboratories on campus.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSfgykXMsOxnU_065CcfezoAd0bDz_qRy2YXq6zWczW-bGltTA/viewform?usp=sf_link",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are hiring people as the applications come in so apply sooner rather than later"
                    },

                     "Bioinformatics (Computational) Scientist": {
                        "description": u"Conduct research using bioinformatics theory and methods in areas such as pharmaceuticals, medical technology, biotechnology, computational biology, proteomics, computer information science, biology and medical informatics. May design databases and develop algorithms for processing and analyzing genomic information, or other biological information.",
                        "commitment": "5 - 8 hrs per week",
                        "qualifications":u"Computational scientists should have at least some coding experience. Recommended coursework includes CS 61A, CS 61B, and Math 54/EE 16A. Data science courses are also useful. Outside experience and internships can replace coursework. We are looking for creative problem solvers with good analytical skills. As this position is focused on biology, talented biology students with experience with BLAST, Genomic Databases, and other computational tools will also be considered and prioritized.",
                        "perks": u"Perks: access to laboratory space and several biomedical research facilities on campus, training in a diverse array of capabilities (from CRIPS-Cas9 to computational genomics), working directly with multiple research laboratories, and working with a networks of researchers spread across many different disciplines in the biological sciences. Course credit is available and the possibility of a stipend for individuals willing to put in significant time in developing the uLab.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSdfawgkUoV3cxLPN2rNnYL-skuWhEAFBf6aBKdC4bbyrBuwsA/viewform",
                        "deadline": u"We'll review applications on a rolling basis until March 15th, or until all our positions have been filled."
                    },

                },

                "Lab Leadership": {

                    "Principal Investigator": {
                        "description": u"Oversees a portfolio of research projects run by undergraduates in a given area of study. Supervise the core leadership (Operation Director, Laboratory Manager, Computational Scientists, etc.) of the uLab and report directly to the ULAB Front Office. While a PI focuses on all aspects of laboratory management, the emphasis is placed on pursuing university level research and cultivating a strong learning environment for all laboratory staff and researchers. This uLab is working on developing cheap blood tests, studying drug delivery problems for CRISPR-Cas9, and using genetics to study autoimmune disorders such as multiple sclerosis. Principal Investigators in this group will be tasked with the largest ever expansion of ULABs' infrastructure, oversee the implementation of industry grade research protocols for all projects, and will drive multiple research projects forward.",
                        "qualifications": u"A PI often has extensive research experience in your field, the ability to manage a large group of people, strong interpersonal skills, teaching experience, and the creativity to solve difficult and novel problems. We really only have one qualification for this position: a passion to and demonstrated experience in solve challenging problems in creative and innovative ways.",
                        "perks": u"Perks: Working with a NASA Astronaut, paid access to Jacobs Hall and several other engineering facilities, direct research experience with two research laboratories, and the ability to work a diverse group of engineers. We also have several contacts at NASA and other Engineering organizations for those seeking opportunities in industry. Course credit is available and the possibility of a stipend for individuals willing to put in significant time in developing the uLab.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSfwvRJ3Zo9tR7zJZy_OI2Gi3fSS8KrzTYNiS9FE-L9WuuZrwA/viewform",
                        "commitment": u"10+ hours a week (a smaller time commitment can be arranged for highly talented candidates with other extensive research obligations).",
                        "deadline": u"This is our newest and fastest growing group. We are looking to place a few select candidates as soon as possible and will keep applications open until the slots are filled.",
                    },

                    "Operations Director": {
                        "description": u"The Operations Director drives the laboratory forward. Managing a large group of individuals in a research setting requires constantly collecting feedback, managing a large program calendar, scheduling the use of complex equipment, certifying and training new members in technical and fundamental research skills, and documenting research results. A typical uLab has several active projects so the operations director is charged with ensuring that the laboratory is running smoothly, developing analytic tools to document and communicate research results at scale, and general operational management. This job is ideal for students wanting management experience and the unique opportunity to run a research laboratory.",
                        "commitment": u"5 - 8 hrs per week",
                        "qualifications":u"While the fundamental operational responsibilities require organizational experience and strong interpersonal skills, we are looking for a candidate that above all else is constantly adapting to new challenges. If you’d like to learn analytical and operational tools to run organizations at scale, this is the job for you.",
                        "perks": u"Perks: access to laboratory space and several biomedical research facilities on campus, training in a diverse array of capabilities (from CRIPS-Cas9 to computational genomics), working directly with multiple research laboratories, and working with a networks of researchers spread across many different disciplines in the biological sciences. Course credit is available and the possibility of a stipend for individuals willing to put in significant time in developing the uLab.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSeqQkt7fcXQ1yl0sv5_R76lejiMtSPbaNroRsQcF9TUOi56UQ/viewform",
                        "deadline": u"We'll review applications on a rolling basis until March 15th, or until all our positions have been filled."
                    },

                     "Lab Manager": {
                        "description": u"Laboratory Managers are responsible for running the uLabs safely and efficiently. The manager, alongside the Principal Investigators, are the primary supervisors for all uLab students. The manager is the principal custodian for all laboratory equipment and oversees the equipment and logistical needs for all laboratory equipment used throughout the uLab. In addition to training students on using equipment, troubleshooting experimental results, and developing trainings for students to safely use equipment, laboratory managers often acquire new equipment and work on operating a variety of sophisticated equipment as part of their research and operational duties. The manager in this uLab will work with several laboratories on campus to operate state-of-the-art genetics and medical testing equipment.",
                        "commitment": "7 - 10 hrs per week",
                        "qualifications":u"As different research projects require a diverse array of new equipment, a willingness to rapidly learn how to maintain and operate equipment is a must. This position is often a great leadership opportunity for students looking to learn how to run a laboratory. Strong organizational skills, fluency in technical analysis, and interpersonal skills often characterize the best laboratory managers. This particular laboratory manager should ideally have experience with common wet laboratory techniques (PCR, Gel Electrophoresis, etc.) and experience managing or working in a molecular biology laboratory.",
                        "perks": u"Perks: access to laboratory space and several biomedical research facilities on campus, training in a diverse array of capabilities (from CRIPS-Cas9 to computational genomics), working directly with multiple research laboratories, and working with a networks of researchers spread across many different disciplines in the biological sciences. Course credit is available and the possibility of a stipend for individuals willing to put in significant time in developing the uLab.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSeyU_l98S5F9wNRrDq6iJMfvfyni64uiAr56ndYefotJ_zdDg/viewform",
                        "deadline": u"We'll review applications on a rolling basis until March 15th, or until all our positions have been filled."
                    },

                },

            },
        },

    "genetics": {
            "short_name": u"genetics",
            "full_name": u"Genetic Engineering and Molecular Biology",
            "navbar": u"Genetic Engineering and Molecular Biology",
            "job_categories": {
                "Genetic Engineering": {

                    "Molecular Biologist (Genetic Engineer)": {
                        "description": u"We are looking for an advanced undergraduate or grad student experienced with with MCB lab equipment and techniques including cell culture, primer design, PCR, cloning, transformation, protein expression, fluorescent microscopy, protein purification, and western blotting.  Capable applicants will have the opportunity to guide the efforts of inexperienced undergraduates looking for lab exposure.  Possible projects include expressing, isolating, and generating a crystal structure for proteins implicated in Multiple Sclerosis.",
                        "qualifications": u"Qualified applicants will have taken a wet laboratory class on campus (Biology 1AL, 1B, Chemistry 1AL, 3AL, 4A, 4B, etc.), have experience working in a chemical biology/biochemistry/IB/MCB research lab, and using common laboratory equipment. We do a lot of training in house so a willingness to learn new things is the biggest qualification!",
                        "commitment": u"6 - 10 hours a week (heavier at the beginning of the semester, lighter during midterm season)",
                        "perks": u"Get access and more experience to machines such as temperature cyclers, centrifuges, and microscopes! Mentor a group of like-minded researchers, course credit, free food, and building relationships with many research laboratories on campus!",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLScsLqQANMG9CoyFaovxPd4Dh_s_x9bfzmwUBNxnKTxGF7e9lA/viewform?usp=sf_link",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner for a better chance."
                    },

                    "Clinical Research Scientist": {
                        "description": u"ULAB is looking for a driven “Clinical Research Scientist” capable of executing and/or learning procedures relevant to clinical applications. Our main interest is setting up a blood lab that will be used to analyze patient blood samples. We are interested in recruiting clinical research scientists who has Biology/Chemistry lab experience and can teach undergraduates skills that might be conducive to doing clinical research and diagnostics.",
                        "qualifications": u"Qualified applicants will have taken a wet laboratory class on campus (Biology 1AL, 1B, Chemistry 1AL, 3AL, 4A, 4B, etc.), have experience working in a chemical biology/biochemistry/IB/MCB research lab, and using common laboratory equipment. We do a lot of training in house so a willingness to learn new things is the biggest qualification!",
                        "commitment": u"6 - 10 hours a week (heavier at the beginning of the semester, lighter during midterm season)",
                        "perks": u"Practice in clinical design, learning techniques associated with diagnosing blood, potentially formal training from UCSF experts in phlebotomy, experience instructing and undergraduate management, graded course credit (if not already enrolled in lab).",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSdAQ9nLD4iAAJ-0hobLz2unvITRhxNGZbX8nLSDyK5-bo0G5g/viewform",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner for a better chance!"
                    },

                },

                "Lab Leadership": {

                    "Principal Investigator": {
                        "description": u"Oversees a portfolio of research projects run by undergraduates in a given area of study. Supervise the core leadership (Operation Director, Laboratory Manager, Computational Scientists, etc.) of the uLab and report directly to the ULAB Front Office. While a PI focuses on all aspects of laboratory management, the emphasis is placed on pursuing university level research and cultivating a strong learning environment for all laboratory staff and researchers. This uLab is working on developing cheap blood tests, studying drug delivery problems for CRISPR-Cas9, and using genetics to study autoimmune disorders such as multiple sclerosis. Principal Investigators in this group will be tasked with the largest ever expansion of ULABs’ infrastructure, oversee the implementation of industry grade research protocols for all projects, and will drive multiple research projects forward.",
                        "qualifications": u"A PI often has extensive research experience in your field, the ability to manage a large group of people, strong interpersonal skills, teaching experience, and the creativity to solve difficult and novel problems. We really only have one qualification for this position: a passion to and demonstrated experience in solve challenging problems in creative and innovative ways.",
                        "perks": u"Perks: Working with a NASA Astronaut, paid access to Jacobs Hall and several other engineering facilities, direct research experience with two research laboratories, and the ability to work a diverse group of engineers. We also have several contacts at NASA and other Engineering organizations for those seeking opportunities in industry. Course credit is available and the possibility of a stipend for individuals willing to put in significant time in developing the uLab.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSfhsAUtqEhPHR231b9ZACkGrKMza3Tbi0hfJRZyhHgTcUoVnQ/viewform?usp=sf_link",
                        "commitment": u"10+ hours a week (a smaller time commitment can be arranged for highly talented candidates with other extensive research obligations).",
                        "deadline": u"This is our newest and fastest growing group. We are looking to place a few select candidates as soon as possible and will keep applications open until the slots are filled.",
                    },

                    "Operations Director": {
                        "description": u"The Operations Director drives the laboratory forward. Managing a large group of individuals in a research setting requires constantly collecting feedback, managing a large program calendar, scheduling the use of complex equipment, certifying and training new members in technical and fundamental research skills, and documenting research results. A typical uLab has several active projects so the operations director is charged with ensuring that the laboratory is running smoothly, developing analytic tools to document and communicate research results at scale, and general operational management. This job is ideal for students wanting management experience and the unique opportunity to run a research laboratory.",
                        "commitment": u"5 - 8 hrs per week",
                        "qualifications": u"While the fundamental operational responsibilities require organizational experience and strong interpersonal skills, we are looking for a candidate that above all else is constantly adapting to new challenges. If you’d like to learn analytical and operational tools to run organizations at scale, this is the job for you.",
                        "perks": u"Perks: access to laboratory space and several biomedical research facilities on campus, training in a diverse array of capabilities (from CRIPS-Cas9 to computational genomics), working directly with multiple research laboratories, and working with a networks of researchers spread across many different disciplines in the biological sciences. Course credit is available and the possibility of a stipend for individuals willing to put in significant time in developing the uLab.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSeqQkt7fcXQ1yl0sv5_R76lejiMtSPbaNroRsQcF9TUOi56UQ/viewform",
                        "deadline": u"We'll review applications on a rolling basis until March 15th, or until all our positions have been filled."
                    },

                     "Lab Manager": {
                        "description": u"Laboratory Managers are responsible for running the uLabs safely and efficiently. The manager, alongside the Principal Investigators, are the primary supervisors for all uLab students. The manager is the principal custodian for all laboratory equipment and oversees the equipment and logistical needs for all laboratory equipment used throughout the uLab. In addition to training students on using equipment, troubleshooting experimental results, and developing trainings for students to safely use equipment, laboratory managers often acquire new equipment and work on operating a variety of sophisticated equipment as part of their research and operational duties. The manager in this uLab will work with several laboratories on campus to operate state-of-the-art genetics and medical testing equipment.",
                        "commitment": u"7 - 10 hrs per week",
                        "qualifications": u"As different research projects require a diverse array of new equipment, a willingness to rapidly learn how to maintain and operate equipment is a must. This position is often a great leadership opportunity for students looking to learn how to run a laboratory. Strong organizational skills, fluency in technical analysis, and interpersonal skills often characterize the best laboratory managers. This particular laboratory manager should ideally have experience with common wet laboratory techniques (PCR, Gel Electrophoresis, etc.) and experience managing or working in a molecular biology laboratory.",
                        "perks": u"Perks: access to laboratory space and several biomedical research facilities on campus, training in a diverse array of capabilities (from CRIPS-Cas9 to computational genomics), working directly with multiple research laboratories, and working with a networks of researchers spread across many different disciplines in the biological sciences. Course credit is available and the possibility of a stipend for individuals willing to put in significant time in developing the uLab.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSeyU_l98S5F9wNRrDq6iJMfvfyni64uiAr56ndYefotJ_zdDg/viewform",
                        "deadline": u"We'll review applications on a rolling basis until March 15th, or until all our positions have been filled."
                    },
                },

                "Computational/Technological": {

                     "Biotechnologist": {
                        "description": u"Biotechnologists/biotechnicians develop and implement new research projects. Set up instruments and laboratory equipment used to conduct and monitor experiments such as centrifuges, flasks and spectrophotometers. Should be able to use spectrophotometers, compound microscopes, and benchtop centrifuges. Be able to use tools to rearrange fragments of DNA and modify genetic material.",
                        "commitment": u"6 - 10 hours a week (heavier at the beginning of the semester, lighter during midterm season)",
                        "qualifications": u"Taken a wet laboratory class on campus (Biology 1AL, 1B, Chemistry 1AL, 3AL, 4A, 4B, etc.), experience working in a research lab preferred, and experience in managing and using laboratory equipment. We do a lot of training in house so a willingness to learn new things is the biggest qualification! Preferable, but not required: Designed and ran a research project.",
                        "perks": u"Perks: Get access to machines such as temperature cyclers, centrifuges, microscopes, and additional machines! working with a group of like-minded researchers, course credit, free food, free swag, and building relationships with many research laboratories on campus. ",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSefl6cD-_ohvJtMu0aU93OlaUfSPqU16BLb5B8_z1agxj2C_A/viewform",
                        "deadline": u"We'll review applications on a rolling basis until March 15th, or until all our positions have been filled."
                    },

                     "Physical Chemist/Molecular Imaging Specialist": {
                        "description": u"The imaging specialist must possess a passion for imaging, theoretical knowledge of optical microscopy and experimental imaging experience with biological samples.",
                        "commitment": u"5 - 8 hrs per week",
                        "qualifications": u"Must have taken a wet laboratory class on campus (Biology 1AL, 1B, Chemistry 1AL, 3AL, 4A, 4B, etc.), experience working in a research lab is preferred, and experience in managing and using laboratory equipment (ex: imaging live and fixed biological samples such as, various confocal microscopes, multiphoton intravital microscope, slide scanners and live cell imaging microscopes)",
                        "perks": u"Perks: Access to machines such as temperature cyclers, centrifuges, microscopes, and additional machines! working with a group of like-minded researchers, course credit, free food, free swag, and building relationships with many research laboratories on campus.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSfgykXMsOxnU_065CcfezoAd0bDz_qRy2YXq6zWczW-bGltTA/viewform?usp=sf_link",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are hiring people as the applications come in so apply sooner rather than later"
                    },

                     "Bioinformatics (Computational) Scientist": {
                        "description": u"Conduct research using bioinformatics theory and methods in areas such as pharmaceuticals, medical technology, biotechnology, computational biology, proteomics, computer information science, biology and medical informatics. May design databases and develop algorithms for processing and analyzing genomic information, or other biological information.",
                        "commitment": u"5 - 8 hrs per week",
                        "qualifications": u"Computational scientists should have at least some coding experience. Recommended coursework includes CS 61A, CS 61B, and Math 54/EE 16A. Data science courses are also useful. Outside experience and internships can replace coursework. We are looking for creative problem solvers with good analytical skills. As this position is focused on biology, talented biology students with experience with BLAST, Genomic Databases, and other computational tools will also be considered and prioritized.",
                        "perks": u"Perks: access to laboratory space and several biomedical research facilities on campus, training in a diverse array of capabilities (from CRIPS-Cas9 to computational genomics), working directly with multiple research laboratories, and working with a networks of researchers spread across many different disciplines in the biological sciences. Course credit is available and the possibility of a stipend for individuals willing to put in significant time in developing the uLab.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSdfawgkUoV3cxLPN2rNnYL-skuWhEAFBf6aBKdC4bbyrBuwsA/viewform",
                        "deadline": u"We'll review applications on a rolling basis until March 15th, or until all our positions have been filled."
                    },
                     "Medicinal Chemist": {
                        "description": u"ULAB is looking for a research-experienced undergraduate or graduate “Medicinal Chemist” capable of executing synthetic procedures, and who is interested in learning how to guide less experienced undergraduates through a natural product or pharmaceutical product synthesis pathway. Knowledge of purification techniques (column chromatography, recrystallization, HPLC) is required. Experience with heterocyclic chemical synthesis/being enrolled in Chemistry 114/214 would be highly preferred.",
                        "commitment": u"Must have at least 8 - 12 hours per week to commit to ULAB.",
                        "qualifications": u"If the applicant is a UC Berkeley undergraduate, he/she should have received a B or higher in an introductory Organic Chemistry course (12A, 3A or equivalent) and be enrolled (or have completed) a second semester Organic Chemistry course (12B, 3B or equivalent). Applicant must have research experience performing synthesis either in an academic or professional setting.",
                        "perks": u"Practice in designing synthetic projects, practice with process chemistry, experience instructing and undergraduate management, course credit, free food, and building relationships with many research laboratories on campus!",
                        "link": u"https://goo.gl/forms/H9C9mzdkL1vTjTk53",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner for a better chance!"
                    },
                },

                "New Students": {},
            },
        },

    "aerospace": {
            "short_name":"aerospace",
            "full_name": "Robotics and Aerospace Engineering",
            "navbar": "Robotics and Aerospace Engineering",
            "job_categories": {
                "Lab Leadership": {
                    "Principal Investigator": {
                        "description": u"Oversees a portfolio of research projects run by undergraduates in a given area of study. Supervise the core leadership (Operation Director, Laboratory Manager, Computational Scientists, etc.) of the uLab and report directly to the ULAB Front Office. While a PI focuses on all aspects of laboratory management, the emphasis is placed on pursuing university level research and cultivating a strong learning environment for all laboratory staff and researchers. The robotics and aerospace uLab principal investigator will oversee two new projects: the development of a spacesuit for Mars exploration and the development of autonomous drone technologies.",
                        "qualifications": u"A PI often has extensive research experience in your field, the ability to manage a large group of people, strong interpersonal skills, teaching experience, and the creativity to solve difficult and novel problems. We really only have one qualification for this position: a passion to and demonstrated experience in solve challenging problems in creative and innovative ways.",
                        "perks": u"Perks: Working with a NASA Astronaut, paid access to Jacobs Hall and several other engineering facilities, direct research experience with two research laboratories, and the ability to work a diverse group of engineers. We also have several contacts at NASA and other Engineering organizations for those seeking opportunities in industry. Course credit is available and the possibility of a stipend for individuals willing to put in significant time in developing the uLab.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSfhsAUtqEhPHR231b9ZACkGrKMza3Tbi0hfJRZyhHgTcUoVnQ/viewform?usp=sf_link",
                        "commitment": u"10 hours per week",
                        "deadline": u"The priority deadline is March 15th, 2018. We place most applicants at the beginning of the semester. We will place applicants for next semester at the end of this semester. Exceptional candidates are always considered.",
                    },

                    "Laboratory Manager": {
                        "description": u" Laboratory Managers are responsible for running the uLabs safely and efficiently. The manager is the principal custodian for all laboratory equipment and oversees the equipment and logistical needs for all laboratory equipment used throughout the uLab. In addition to developing trainings for students to safely use equipment, laboratory managers often acquire new equipment and work on operating a variety of sophisticated equipment as part of their research and operational duties. The manager in this uLab will work with machine shop equipment, state-of-the-art software design tools, and industry standards such as Arduinos.",
                        "qualifications": u"As different research projects require a diverse array of new equipment, a willingness to rapidly learn how to maintain and operate equipment is a must. This position is often a great leadership opportunity for students looking to learn how to run a laboratory. Strong organizational skills, fluency in technical analysis, and interpersonal skills often characterize the best laboratory managers. This particular laboratory manager should ideally have experience with prototyping equipment, MATLAB, CAD, and other core technical design tools.",
                        "perks": u"Perks: Working with a NASA Astronaut, paid access to Jacobs Hall and several other engineering facilities, direct research experience with two research laboratories, and the ability to work a diverse group of engineers. We also have several contacts at NASA and other Engineering organizations for those seeking opportunities in industry. Course credit is available and the possibility of a stipend for individuals willing to put in significant time in developing the uLab.",
                        "link": u"https://goo.gl/forms/yFFnOYrgpp75jU4B2",
                        "commitment": u"10 hours per week",
                        "deadline": u"March 15th, 2018 (or until all positions are filled)",
                    },

                },
                "General Positions": {
                    "Software Engineer": {
                        "description": u"Aerospace Engineering and Robotics are both rich fields that use their own set of software tools. Further, common engineering projects require specialized technical design tools such as CAD. Software Engineerings in the Robotics and Aerospace Lab develop custom capabilities, and work with industry standards, to analyze and implement real engineering systems. Current projects invovle the design of a Martian Spacesuit Glove, Autonomous Drone Navigation, and novel control systems for quadcopters.",
                        "qualifications": u"Knowledge of the material covered in EE 16A and CS 61A is preferred. We general take students that have a demonstrated interest in software engineering, in particular when their interest is related to robotics or aerospace engineering.",
                        "commitment": u"6 hours per week minimum, including 1 weekly meeting with students and 1 weekly meeting with PIs",
                        "perks": u"Perks: Working with a NASA Astronaut, paid access to Jacobs Hall and several other engineering facilities, direct research experience with two research laboratories, and the ability to work a diverse group of engineers. We also have several contacts at NASA and other Engineering organizations for those seeking opportunities in industry. Course credit is available and the possibility of a stipend for individuals willing to put in significant time in developing the uLab.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSfv1MDryeN4VnsYgQwNNEbVyKIhvrXor9RjsWIgYjp6-iUH_Q/viewform",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner rather than later."
                    },
                    "Product Design Engineer": {
                        "description": u"Product Design Engineers will work on all ULAB Projects to implement real engineering systems. From designing the glove controllor to building aerodynamic systems, designers will work in industry standards (AutoCAD, SolidWorks, etc.) to deisgn, prototype, and build products. Engineers often get experience with various sensors, 3D printers, controllers, and other core mechanical and electrical tools",
                        "qualifications": u"Having machine shop training, knowledge of AutoCAD, Solidworks, and MATLAB are all prefereable. Knowledge of finite element analysis is highly desired.",
                        "commitment": u"6 hours per week minimum, including 1 weekly meeting with students and 1 weekly meeting with PIs",
                        "perks": u"Perks: Working with a NASA Astronaut, paid access to Jacobs Hall and several other engineering facilities, direct research experience with two research laboratories, and the ability to work a diverse group of engineers. We also have several contacts at NASA and other Engineering organizations for those seeking opportunities in industry. Course credit is available and the possibility of a stipend for individuals willing to put in significant time in developing the uLab.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSdmg7BntRkyqAVgQw7qvwFkLnbXVBenEh_mh9_slYg_BoRydQ/viewform",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner rather than later."
                    },
                    "Control Engineer": {
                        "description": u"The Control Engineer is responsible for the design and ultimate performance of electrical and electronic controls of highly complex system. For our glove controlled quadcopter project, Calibrate different type of sensors and collect data to our 'hand motion library.' They will also apply basic control to those electronic devices such as TV, lights, drones, VR headsets and instruments.",
                        "qualifications": u"Taken (or taking) at least one control classes: ME 132, ME C134(EE C106A), ME 131, and ME 135, or EE 128. Strong fundamental knowledge of MATLAB or LABVIEW. Other desired qualifications include: took 102A or know basic knowledge about sensors, some experience with micro controller or motion controller card, and haven taken at least one project class or having experience in research lab",
                        "commitment": u"6 hours per week minimum, including 1 weekly meeting with students and 1 weekly meeting with PIs",
                        "perks": u"Perks: Working with a NASA Astronaut, paid access to Jacobs Hall and several other engineering facilities, direct research experience with two research laboratories, and the ability to work a diverse group of engineers. We also have several contacts at NASA and other Engineering organizations for those seeking opportunities in industry. Course credit is available and the possibility of a stipend for individuals willing to put in significant time in developing the uLab.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSdmg7BntRkyqAVgQw7qvwFkLnbXVBenEh_mh9_slYg_BoRydQ/viewform",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner rather than later."
                    },
                },
                "Mars Spacesuit": {
                    "Controls (Robotics) Engineer": {
                        "description": u"ULAB is looking for an undergraduate who would enjoy designing a robotic operating system for aiding astronauts and working on the implementation of the system in a humanoid suit (the spacesuit). This device will play an integral part of future astronauts being able to do work in a low pressure, vacuum like environment. The overall mechanics will be able to sense muscle movement in the finger, and relay a feedback to the robotic assist device. Thus, you will be working with Stanley Chang to research, test, and analyze the design use in relation to the function of the elements in the system.",
                        "qualifications": u"Qualified applicants must have a basic knowledge of MATLAB, ROS, and Arduino. Applicants must have also taken a few controls classes, and while not necessarily required, it is recommended that they have also taken EE C106A. Additionally, EECS and Mechanical Engineering students are highly encouraged to apply. The best applicant is one who is willing to learn.",
                        "perks": u"Membership perks include working with other developers with experience in all kinds of technologies, working on new technologies, visiting labs, having meeting with clients, & attending fun social events.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLScsw1tE6PYN3oLJ18rDtwdzqpY8emmDULTnErsZVOzP_tPv9A/viewform",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner rather than later.",
                    },

                    "Design Engineer": {
                        "description": u"ULAB is looking for an undergraduate who would enjoy conceptualizing solutions for design problems associated with the construction of a spacesuit, such as 3D mockups for gloves or integrating features into the suit. Before the preliminary design, designers would research and do some analysis about the stimulatory environment and air-tightness mechanism. Additionally, you will make brief sketches fitting the design requirements and technical range, and you will create the 3D model by Creo or Solidworks and manufacture it by 3D printing or other methods. Thus, you will be working with Yutin Zhan to create a fully immersive environment within the suit, especially making gloves that feel like they do not exist.",
                        "qualifications": u"Qualified applicants must have experience with Solidworks, Autodesk Fusion 360, and 3DS (render animations), along with the ability to think outside the box with a high degree of creativity. E 128 is strongly recommended for this position. Applicants should also have an understanding of basic solid mechanics, a how stress works, and user research or human-centered design. Lastly, quiet sketch and 3D modeling skills would be very helpful.",
                        "perks": u"Perks: Working with a NASA Astronaut, paid access to Jacobs Hall and several other engineering facilities, direct research experience with two research laboratories, and the ability to work a diverse group of engineers. We also have several contacts at NASA and other Engineering organizations for those seeking opportunities in industry. Course credit is available.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSeS4MKnxArOMYIx1Nw3x0zSvOYdBzP5UWk5fGBaUtyisVhMew/viewform",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner rather than later.",
                    },

                    "Controls (Sensory Integration) Engineer": {
                        "description": u"ULAB is looking for an undergraduate who would enjoy designing a controller for force-enhancing space gloves and integrating other necessary sensors for an astronaut suit. The sensor system will be primarily used to collect data on the astronaut’s physiology, keeping him/her in an ideal state, while monitoring the outside conditions. This system will be the astronaut’s “Sixth Sense,” so to speak, when they are out working on the martian environment. Thus, you will be prototyping with 3D-printed parts and working with Minglong Li and Stanley Chang to research, test, and analyze the design use in relation to the function of the elements in the system.",
                        "qualifications": u"Qualified applicants must have some experience with microcontrollers and control algorithms. Applicants must have also taken a few controls classes, and while not necessarily required, it is recommended that they have also taken ME 102A or ME 107. Additionally, EECS and Mechanical Engineering students are highly encouraged to apply.",
                        "perks": u"Perks: Working with a NASA Astronaut, paid access to Jacobs Hall and several other engineering facilities, direct research experience with two research laboratories, and the ability to work a diverse group of engineers. We also have several contacts at NASA and other Engineering organizations for those seeking opportunities in industry. Course credit is available.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSc-s6QSK-7AGqDv3DWwXntq23faybT9DLLPlUtOjmvKxeTxiQ/viewform",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner rather than later.",
                    },

                    "Materials and Thermal Specialist": {
                        "description": u"We are launching a group this semester in ULAB designated towards working with different projects from labs, campus clubs, and industrial partners. As a member of this team, you'll be working with the best on technologies like drones, web, blockchain, machine learning, and mobile development. As a member of this team, you'll get valuable industrial experience and networking. Anything that our client requests, you'll be working on it.",
                        "qualifications": u"Qualified applicants must have some experience with mechanical and thermal properties of materials. Applicants must have also taken a few material properties classes, and while not necessarily required, it is recommended that they have also taken ME 108 or CE 60. Additionally, Material Science students and Mechanical Engineering are highly encouraged to apply.",
                        "perks": u"Perks: Working with a NASA Astronaut, paid access to Jacobs Hall and several other engineering facilities, direct research experience with two research laboratories, and the ability to work a diverse group of engineers. We also have several contacts at NASA and other Engineering organizations for those seeking opportunities in industry. Course credit is available.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSeyRnYobvwxiogaSu4OujPMvCnlmmRJ2h0cDFxb0_wpV4AhVg/viewform",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner rather than later.",
                    },

                },

                "New Student Positions": {
                    "Design Engineer": {
                        "description": u"ULAB is looking for an undergraduate who would enjoy conceptualizing solutions for design problems associated with the construction of a spacesuit, such as 3D mockups for gloves or integrating features into the suit. Before the preliminary design, designers would research and do some analysis about the stimulatory environment and air-tightness mechanism. Additionally, you will make brief sketches fitting the design requirements and technical range, and you will create the 3D model by Creo or Solidworks and manufacture it by 3D printing or other methods. Thus, you will be working with Yutin Zhan to create a fully immersive environment within the suit, especially making gloves that feel like they do not exist.",
                        "qualifications": u"Qualified applicants must have experience with Solidworks, Autodesk Fusion 360, and 3DS (render animations), along with the ability to think outside the box with a high degree of creativity. E 128 is strongly recommended for this position. Applicants should also have an understanding of basic solid mechanics, a how stress works, and user research or human-centered design. Lastly, quiet sketch and 3D modeling skills would be very helpful.",
                        "perks": u"Perks: Working with a NASA Astronaut, paid access to Jacobs Hall and several other engineering facilities, direct research experience with two research laboratories, and the ability to work a diverse group of engineers. We also have several contacts at NASA and other Engineering organizations for those seeking opportunities in industry. Course credit is available.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSeS4MKnxArOMYIx1Nw3x0zSvOYdBzP5UWk5fGBaUtyisVhMew/viewform",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner rather than later.",
                    },

                    "Controls (Sensory Integration) Engineer": {
                        "description": u"ULAB is looking for an undergraduate who would enjoy designing a controller for force-enhancing space gloves and integrating other necessary sensors for an astronaut suit. The sensor system will be primarily used to collect data on the astronaut’s physiology, keeping him/her in an ideal state, while monitoring the outside conditions. This system will be the astronaut’s “Sixth Sense,” so to speak, when they are out working on the martian environment. Thus, you will be prototyping with 3D-printed parts and working with Minglong Li and Stanley Chang to research, test, and analyze the design use in relation to the function of the elements in the system.",
                        "qualifications": u"Qualified applicants must have some experience with microcontrollers and control algorithms. Applicants must have also taken a few controls classes, and while not necessarily required, it is recommended that they have also taken ME 102A or ME 107. Additionally, EECS and Mechanical Engineering students are highly encouraged to apply.",
                        "perks": u"Perks: Working with a NASA Astronaut, paid access to Jacobs Hall and several other engineering facilities, direct research experience with two research laboratories, and the ability to work a diverse group of engineers. We also have several contacts at NASA and other Engineering organizations for those seeking opportunities in industry. Course credit is available.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSc-s6QSK-7AGqDv3DWwXntq23faybT9DLLPlUtOjmvKxeTxiQ/viewform",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner rather than later.",
                    },

                    "Materials and Thermal Specialist": {
                        "description": u"We are launching a group this semester in ULAB designated towards working with different projects from labs, campus clubs, and industrial partners. As a member of this team, you'll be working with the best on technologies like drones, web, blockchain, machine learning, and mobile development. As a member of this team, you'll get valuable industrial experience and networking. Anything that our client requests, you'll be working on it.",
                        "qualifications": u"Qualified applicants must have some experience with mechanical and thermal properties of materials. Applicants must have also taken a few material properties classes, and while not necessarily required, it is recommended that they have also taken ME 108 or CE 60. Additionally, Material Science students and Mechanical Engineering are highly encouraged to apply.",
                        "perks": u"Perks: Working with a NASA Astronaut, paid access to Jacobs Hall and several other engineering facilities, direct research experience with two research laboratories, and the ability to work a diverse group of engineers. We also have several contacts at NASA and other Engineering organizations for those seeking opportunities in industry. Course credit is available.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSeyRnYobvwxiogaSu4OujPMvCnlmmRJ2h0cDFxb0_wpV4AhVg/viewform",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner rather than later.",
                    },

                },

                "Autonomous Drones": {
                    "Software Engineer": {
                        "description": u"Aerospace Engineering and Robotics are both rich fields that use their own set of software tools. Further, common engineering projects require specialized technical design tools such as CAD. Software Engineerings in the Robotics and Aerospace Lab develop custom capabilities, and work with industry standards, to analyze and implement real engineering systems. Current projects invovle the design of a Martian Spacesuit Glove, Autonomous Drone Navigation, and novel control systems for quadcopters.",
                        "qualifications": u"Knowledge of the material covered in EE 16A and CS 61A is preferred. We general take students that have a demonstrated interest in software engineering, in particular when their interest is related to robotics or aerospace engineering.",
                        "commitment": u"6 hours per week minimum, including 1 weekly meeting with students and 1 weekly meeting with PIs",
                        "perks": u"Perks: Working with a NASA Astronaut, paid access to Jacobs Hall and several other engineering facilities, direct research experience with two research laboratories, and the ability to work a diverse group of engineers. We also have several contacts at NASA and other Engineering organizations for those seeking opportunities in industry. Course credit is available and the possibility of a stipend for individuals willing to put in significant time in developing the uLab.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSfv1MDryeN4VnsYgQwNNEbVyKIhvrXor9RjsWIgYjp6-iUH_Q/viewform",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner rather than later."
                    },
                    "Product Design Engineer": {
                        "description": u"Product Design Engineers will work on all ULAB Projects to implement real engineering systems. From designing the glove controllor to building aerodynamic systems, designers will work in industry standards (AutoCAD, SolidWorks, etc.) to deisgn, prototype, and build products. Engineers often get experience with various sensors, 3D printers, controllers, and other core mechanical and electrical tools",
                        "qualifications": u"Having machine shop training, knowledge of AutoCAD, Solidworks, and MATLAB are all prefereable. Knowledge of finite element analysis is highly desired.",
                        "commitment": u"6 hours per week minimum, including 1 weekly meeting with students and 1 weekly meeting with PIs",
                        "perks": u"Perks: Working with a NASA Astronaut, paid access to Jacobs Hall and several other engineering facilities, direct research experience with two research laboratories, and the ability to work a diverse group of engineers. We also have several contacts at NASA and other Engineering organizations for those seeking opportunities in industry. Course credit is available and the possibility of a stipend for individuals willing to put in significant time in developing the uLab.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSdmg7BntRkyqAVgQw7qvwFkLnbXVBenEh_mh9_slYg_BoRydQ/viewform",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner rather than later."
                    },
                    "Control Engineer": {
                        "description": u"The Control Engineer is responsible for the design and ultimate performance of electrical and electronic controls of highly complex system. For our glove controlled quadcopter project, Calibrate different type of sensors and collect data to our 'hand motion library.' They will also apply basic control to those electronic devices such as TV, lights, drones, VR headsets and instruments.",
                        "qualifications": u"Taken (or taking) at least one control classes: ME 132, ME C134(EE C106A), ME 131, and ME 135, or EE 128. Strong fundamental knowledge of MATLAB or LABVIEW. Other desired qualifications include: took 102A or know basic knowledge about sensors, some experience with micro controller or motion controller card, and haven taken at least one project class or having experience in research lab",
                        "commitment": u"6 hours per week minimum, including 1 weekly meeting with students and 1 weekly meeting with PIs",
                        "perks": u"Perks: Working with a NASA Astronaut, paid access to Jacobs Hall and several other engineering facilities, direct research experience with two research laboratories, and the ability to work a diverse group of engineers. We also have several contacts at NASA and other Engineering organizations for those seeking opportunities in industry. Course credit is available and the possibility of a stipend for individuals willing to put in significant time in developing the uLab.",
                        "link": u"https://docs.google.com/forms/d/e/1FAIpQLSdmg7BntRkyqAVgQw7qvwFkLnbXVBenEh_mh9_slYg_BoRydQ/viewform",
                        "deadline": u"Rolling. While the priority application deadline is March 15th, we are recruiting people as the applications come in so apply sooner rather than later."
                    },
                },
            },
        },

    "ml": {
            "short_name":"ml",
            "full_name": "Statistical Modeling and Deep Learning",
            "navbar": "Statistical Modeling and Deep Learning",
            "job_categories": {

                "Research Jobs": {
                    "Data Science Staff Scientist and Mentor": {
                        "description": "Identifying nuclei allows researchers to identify individual cells in a sample and easily underlying biological processes at work. Automating this process can shorten the 10 years it takes for each new drug to come to market. This project will walk students through the deep learning stack and apply machine learning techniques to medical imaging. Students will be utilizing computer vision techniques and data science tools to identify nuclei in a given dataset. Mentor responsibilities include working with PIs to design tutorials for projects, working with PIs to ensure success and development of research projects, holding tutorials for students, and working with student teams to provide mentoring and advice towards the development of research projects.",
                        "qualifications": "Must be highly responsive and able to pick up new tools quickly. Must have familiarity with Python, Linear algebra, and Deep Learning. Additional qualifications include experience with Python numerical tools (Numpy) and Data Science tools (Matplotlib, Jupyter Notebook). Preferable qualifications include experience with Deep Learning tools (Keras or Tensorflow or Pytorch).",
                        "commitment": "6 hours per week minimum, including 1 weekly meeting with students and 1 weekly meeting with PIs",
                        "perks": "Perks include involvement with research projects and leadership experience. Course Credit is Available. ",
                        "link": "https://goo.gl/forms/r9u4BYopImEkV3Yw1",
                        "deadline": "We will review applications on a rolling basis until March 15th or until all our positions have been filled."
                                 },
                    "Computer Vision Staff Scientist and Mentor": {
                        "description": "Artistic style for all of history has been inseparable from the content of the artist's creation. Now, with the magic of deep learning, we can separate and recombine the image content and style, reproduce famous painting styles on natural images. This project will walk students through the deep learning stack, reproducing the state-of-the-art style transfer results and exploring research directions. See: https://www.youtube.com/watch?v=xVJwwWQlQ1o. Mentor responsibilities will include working with PIs to design tutorials for projects, working with PIs to ensure success and development of research projects, holding tutorials for students, and working with student teams to provide mentoring and advice towards the development of research projects.",
                        "qualifications": "Must be highly responsive and able to pick up new tools quickly. Must have familiarity with Python, linear algebra, and deep learning. Additional qualifications include experience with Python numerical tools (Numpy) and Data science tools (Matplotlib, Jupyter Notebook). Preferable qualifications include experience with Deep Learning tools (Keras or Tensorflow or Pytorch).",
                        "commitment": "6 hours per week minimum, including 1 weekly meeting with students and 1 weekly meeting with PIs",
                        "perks": "Perks include involvement with research projects and leadership experience. Course credit is available.",
                        "link": "https://goo.gl/forms/r9u4BYopImEkV3Yw1",
                        "deadline": "We will review applications on a rolling basis until March 15th or until all our positions have been filled."
                                },
                    "Natural Language Processing Staff Scientist and Mentor": {
                        "description": "Analysis of language-based data requires a deep understanding of natural language text and semantics, which is generally difficult tasks for computers. However, a number of statistical approaches have been shown to work well for sentiment analysis of text data. This project will involve automating the process of analyzing the helpfulness of Amazon reviews with the recent advances in deep learning models for NLP. Mentor responsibilities include working with PIs to design tutorials for projects, working with PIs to ensure success and development of research projects, holding tutorials for students, and working with student teams to provide mentoring and advice towards the development of research projects.",
                        "qualifications": "Must be highly responsive and able to pick up new tools quickly. Must have familiarity with Python, Linear algebra, and Deep Learning. Additional qualifications include experience with Python numerical tools (Numpy), Data Science tools (Matplotlib, Jupyter Notebook), and Scikit Learn. Preferable qualifications include experience with Deep Learning tools (Keras or Tensorflow or Pytorch).",
                        "commitment": "6 hours per week minimum, including 1 weekly meeting with students and 1 weekly meeting with PIs",
                        "perks": "Perks include involvement with research projects and leadership experience. Course Credit is Available. ",
                        "link": "https://goo.gl/forms/r9u4BYopImEkV3Yw1",
                        "deadline": "We will review applications on a rolling basis until March 15th or until all our positions have been filled."
                                  },
                },

                "Student Positions": {
                    "New Student Researcher": {
                        "description": "New Students (Freshman or Junior Transfers) are the on-the-ground researchers. We we will train you in contemporary machine learning techniques and motivated students who complete the initial training will be given a university-level research project. We work with several labs on campus so we try to place motivated students in research positions on campus for their Sophomore (or Senior) year.",
                        "commitment": "Time commitment includes 9-12 hours a week developing with one's designated team.",
                        "link": "https://docs.google.com/forms/d/e/1FAIpQLSelh2HtqamgGb37HGAALDEGi7v2OdOZnCsNNoV-rUk9TCQL2w/viewform?usp=sf_link",
                        "deadline": "We will review applications on a rolling basis until March 15th, or until all our positions have been filled. After filling out an application, you will be contacted to set up an interview within a few days.",
                    },
                },

                "Lab Management": {
                    "Laboratory Manager": {
                        "description": "The CS ULAB will be aided by lab managers who handle administrative logistics. Lab managers are responsible for coordinating with the mentors and other ULAB teams to ensure these projects run smoothly. In addition, lab managers will build and maintain partnerships with on campus labs to access instruments and equipment, in addition to overseeing training for all projects. Lab managers will also handle organizing research meetings and scheduling technical workshops, while also gathering student and staff feedback to improve the experience of ULAB.",
                        "qualifications": "Must be highly responsive. General interest in statistical modeling and deep learning is optional.",
                        "commitment": "Must be able to commit 4+ hours per week",
                        "perks": "Perks include involvement with cutting-edge ML research projects and leadership experience. Course Credit is Available. ",
                        "link": "https://goo.gl/forms/l6nDfZtIU8Bth3uh1",
                        "deadline": "We will review applications on a rolling basis until March 15th or until all our positions have been filled."
                    },
                },
            },
        },

}

software_jobs_order = ["Advanced Technologies Group", "Software Operations", "Visualization", "Statistical Modeling and Deep Learning",
    "Genetic Engineering and Molecular Biology", "Robotics and Aerospace Engineering", "Medicinal Chemistry and Clinical Research",
    "Cognitive Neuroscience and Medical Imaging", "Physics and Astrophysics"]
software_jobs_order.sort()

software_jobs = {

    "Advanced Technologies Group": {
        "Software Development Engineer": {
            "description": "The Advanced Technologies Group is a branch of ULAB \
            that was launched upon the realization that our labs \
            spent way too much time on building the tools they need for their \
            experiments. What if we separate the engineering from the science? \
            ATG is dedicated to doing just that. They design custom computational \
            capabilities to tackle complex research problems for labs on the UC Berkeley campus. \
            The group supports various research groups on campus as well as ULAB's \
            student-run research laboratories. Students will have the unique \
            opportunity to solve computational problems in other fields such as \
            astrophysics or cognitive neuroscience. Developers work on small teams \
            on custom software capabilities. Projects typically last a few weeks so \
            developers usually get the opportunity to work on multiple projects \
            throughout the uLab and other organizations on campus. \
            Past projects include automating access to uLab \
            infrastructure using the Google Drive API and writing an analytical \
            engine to process logistical requests. Future projects include \
            visualization of exoplanets, simulating control systems for a glove \
            to work on a Martian spacesuit, entrepreneurial projects and more. \
            \n This group is designed for students who are interested in becoming \
            software engineers or who are interested in learning practical \
            programming skills. Teams often build web tools, mobile applications, \
            and work on projects directly related to work done in industry.",

            "qualifications": "Qualifications: Proficiency in at least one programming language",

            "commitment": "Time commitment includes 90 minutes a week of mandatory \
             meeting with the rest of the ATG group in addition to 6-9 hours a week \
             developing with one's designated pod.",

            "perks": "Membership perks include working with other developers with \
            experience in all kinds of technologies, training with the smartest \
            people on campus, attending private workshops, working on new technologies, \
            visiting labs, having meeting with clients, & attending fun social events.",

            "link": "https://goo.gl/forms/kiQXLwG1JOrZkWHR2",

            "deadline": "Applicants will be reviewed and admitted in weekly batches for this semester only. \
            ULAB ATG will get more exclusive from next semester onwards due to limited resources.",
        },

        "Operations Director": {
            "description": u"""The ATG Operations Director drives the sub-organization forward. Managing a large
                group of individuals in a research setting requires constantly collecting feedback, managing a
                large program calendar, scheduling the use of complex equipment, certifying and training new members
                in technical and fundamental research skills, and documenting research results. With ULAB Advanced
                Technologies Group  having several active projects, the operations director is charged with ensuring
                that ATG operations  are running smoothly, developing analytic tools to document and communicate
                research results at scale, and general operational management. This job is ideal for students wanting
                management experience and the unique opportunity to run a research and development group. While the
                branch has emphasis is on software development, the Operations Director will be responsible for expanding
                the scope of existing programs to fit the needs of the client.""",

            "qualifications": u"""Qualifications: While the fundamental operational responsibilities require organizational
                experience and strong interpersonal skills, we are looking for a candidate that above all else is constantly
                adapting to new challenges. If you’d like to learn analytical and operational tools to run organizations at
                scale, this is the job for you.""",

            "commitment": u"""Expect to commit 5-10 hours/week. As an Operations Director of the ATG branch of ULAB, your
                responsibilities for maintaining software that could be used by the other uLabs and outside clients include:
                (1) Reporting, as an ATG Operations Director, directly to your executive director regarding anything related to ATG.
                (2) Working with several ATG executives on maintaining the sub-organization’s culture.
                (3) Hiring students with relevant skills and delegating tasks to them. As an ATG Operations Director, you are not
                expected to write the code yourself.
                (4) Coming to the meetings that are not necessarily at a fixed time (we need you to have a semi-flexible schedule).""",

            "perks": u"""In addition to being in the ULab organization (with perks including socials and research
                experience), as a member of the ATG department, you will be given additional workshops, career-building
                activities and leadership experience. Since the ATG collaborates with many other departments and plans to
                expand and collaborate with other clubs, there will also be many networking opportunities.""",

            "link": u"https://docs.google.com/forms/d/e/1FAIpQLSeqQkt7fcXQ1yl0sv5_R76lejiMtSPbaNroRsQcF9TUOi56UQ/viewform",

            "deadline": u"Rolling"
        },
    },

    "Software Operations":
        filter_dict(corporate["Development"], {"Computational Scientist"}),
    "Visualization":
        filter_dict(corporate["Development"], {"Graphic Designer/Animator"}),

    "Statistical Modeling and Deep Learning":
        get_lab_jobs("ml"),
    "Genetic Engineering and Molecular Biology":
        filter_dict(get_lab_jobs("genetics"), {"Bioinformatics (Computational) Scientist"}),
    "Robotics and Aerospace Engineering":
        filter_dict(get_lab_jobs("aerospace"),
            {"Controls (Robotics) Engineer", "Controls (Sensory Integration Engineer", "Control Engineer", "Software Engineer"}),
    "Medicinal Chemistry and Clinical Research":
        filter_dict(get_lab_jobs("medicine"), {"Bioinformatics (Computational) Scientist"}),
    "Cognitive Neuroscience and Medical Imaging":
        filter_dict(get_lab_jobs("cogsci"), {"Lab Tech"}),
    "Physics and Astrophysics":
        filter_dict(get_lab_jobs("physics"), {"Computational Scientist"}),
}

student = {

    "Statistical Modeling and Deep Learning":
        filter_dict(get_lab_jobs("ml"), {"New Student Researcher"}),

    "Robotics and Aerospace Engineering":
        labs["aerospace"]["job_categories"]["New Student Positions"],

    "Development":
        filter_dict(corporate["Development"], {"Liaison", "Fundraiser"}),

    "Operations":
        filter_dict(corporate["Operations"], {"Operations Analyst"}),
}

# Add ATG operations director to corporate jobs dict

corporate["Advanced Technologies Group"] = filter_dict(software_jobs["Advanced Technologies Group"], {"Operations Officer"})