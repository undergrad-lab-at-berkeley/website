# encoding=utf8
# -*- coding: utf-8 -*-

# # Given the string LAB, pulls all of the jobs (uncategorized) from that lab in the LABS dict. Returns a dict
# def get_lab_jobs(lab):
#     output = {}
#     categories = labs[lab]["job_categories"]
#     for k in categories:
#         output.update(categories[k])
#     return output

import csv


# Given INPUT_DICT and set ENTRIES, returns new dict with items from INPUT_DICT that match the keys indicated by ENTRIES
def filter_dict(input_dict, entries):
    # Compares INPUT_DICT keys with set ENTRIES, matching keys are used in a dictionary comprehension
    return {k: input_dict[k] for k in input_dict.keys() if k in entries}


foundersOrder = ["Riley McDanal", "Jenna Martin", "Arjun Savel", "Yasmeen Musthafa", "Catherine Livelo", "Alan Pham",
                 "Joshua Hug", "Amit Akula", "Mrinalini Sugosh", "Alex Powers", "Dylan Kato", "Michael Oshiro"]
advisorsOrder = ["Joshua Hug", "Arjun Savel", "Riley McDanal", "Sean Burns"]
teamOrder = ['Hareen Seerha', 'Savannah Perez-Piel', 'Catherine Livelo', 'Alan Pham', 'Adam Bittenson']
labOrder = ['cogsci', 'physics', 'bio', 'data', 'compbio']

labs = {
    "cogsci": {
        "logo": u"/static/img/logos/logo_cog_sci.png",
        "short_name": u"cogsci",
        "full_name": u"Psychology and Cognitive Sciences",
        "navbar": u"Cog_Sci",
        "status": "Active",
        "members": ["Jeremy Manwaring", "Nick Zhang", "Tvisha Joshi", "Taylan Dincer", "Eva Reineck", "Armando Lopez",
                     "Teresa Le", "Evan Chau", "Divya Sundar", "Mark D\'Esposito"],
        "content": {
            "overview": {
                "title": u"Lab Overview",
                "slides": ["/static/img/cogsci_slides/cogsci2023.jpg", "/static/img/cogsci_slides/symp_poster.png",
                           "/static/img/cogsci_slides/symp_poster2.png", "/static/img/cogsci_slides/group_far.png",
                            "/static/img/cogsci_slides/symp_poster3.png", "/static/img/cogsci_slides/symp_poster4.png"],
                "text": u"""
                        Founded in Fall 2017 by Jenna Martin and Riley McDanal, the Psych & CogSci Lab has a vision of offering an experience that benefits all undergraduates in the research community while facilitating the training and growth of aspiring researchers.
                        <br><br>
                        We follow a replicate and extend structure. Mentees will be divided into groups of 4-5 and assigned a mentor that will guide them through a year-long project. The first semester will be spent replicating a published study and the second semester will be spent extending the methods based on an original idea. The studies will be provided through a database compiled by the ULab Board of Directors and dedicated graduate students. Each group will have the opportunity to select studies in areas that interest them the most. This will also allow an opportunity for projects to be published!
                        <br><br>
                        Our projects this year involve behavioral psychology, fMRI analyses, visual field cortices, language processing, cognitive neuroscience, and other areas. All projects will be published in a paper and poster series via UC eScholarship Open Access publishing. Posters will be presented to faculty members and peers at UC Berkeley. This will certainly aid in getting on-campus research.
                        <br><br>
                        Currently, Dr. Mark D'Esposito, Professor of Neuroscience and Psychology at UC Berkeley, serves as primary faculty advisor. As the ULab Board of Directors pursues new projects and initiatives, Dr. D'Esposito oversees their work to ensure the advancement of ULab's mission.
                        """
                # Our Sponsors:
                # The <a href="http://www.wheelerlabs.berkeley.edu">Wheeler Labs</a> is a group of scientists dedicatd to developing innovative methods to study brain function, with the goal of translating these methods into clinically useful tools. The Wheeler Lab is sponsoring our lab space as well as our future events.
            },
            "sponsor": {
                "title": u"Want to join us?",
                "text": u"""
                        <b>Applications for 2025-2026 can be found at the following hyperlinks: <a href="https://forms.gle/f7A1LH1AybZggVFJ8">Mentor App</a>, <a href="https://docs.google.com/forms/d/e/1FAIpQLSdzJdpZwrEtupx-Z2P4ZVUdrf4BA_zw57OojJnLb2NDCFIWOQ/viewform">Mentee App</a>.</b> Deadlines and details are provided on the applications. For periodic updates, sign up for our newsletter <a href='http://eepurl.com/gyuGd5'>here</a><br/>  <br/>                      
                        """
                # Applications for mentors and mentees for the 2021-2022 year are closed!
                # However, feel free to reach out to us by <a href = "mailto: cogsci@ulab.berkeley.edu">emailing us </a> or be added to our newsletter by filling out <a href="http://eepurl.com/gyuGd5">this form</a>.
            },
            "join": {
                "title": u"""Check out our publications <a href='https://escholarship.org/uc/ulab_cogscipsych'>here</a>.""",
                "text": u""""""

            },
            # "join": {
            #     "title": """Sign up for our newsletter <a href='http://eepurl.com/gyuGd5'>here</a>.""",
            #     "text": """"""

            # },
            "calendar": {
                "title": u"ULab Division Calendar",
                "text": u"""This calendar has all of the events and deadlines for the year. Exact days and times are subject to change.""",
                "object": u"""<iframe src="https://calendar.google.com/calendar/embed?src=cogsci.ulab%40gmail.com&ctz=America%2FLos_Angeles" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>"""
            },
            "database": {
                "link": u"https://drive.google.com/file/d/1N4Cipbns-FMjD4yefx97KDqVOObv2ulZ/view?usp=sharing"
            },
            "modules": {
                "link": u"https://docs.google.com/document/d/16jjTm23QawiBWiFi368txxgXZ0wVwguHrue-iL7jUck/view?usp=sharing"
            },
            "resources": {
                "link": u"https://drive.google.com/drive/folders/1H7nmUNhrPlhBdOhwsMN9PFK8DOolUcFe?usp=sharing"
            }
        }
    },

    "physics": {
        "logo": u"/static/img/logos/logo_physics.png",
        "short_name": u"physics",
        "full_name": u"Physics and Astronomy",
        "navbar": u"Physics",
        "status": "Active",
        "members": ["Jordan Duan", 'Andrew McHaty', 'Yaamini Jois', 'Brianna Peck', 'Caitlin Begbie', 'Michelle Duan', 'Andrew Wang', 'Sophia Bucker', 'Olivia Wagner'],
        "former": {
            'former_name': [
                'Arjun Savel',
                'Aditya Sengupta',
                # 'Lawrence Edmond, IV',
                'Yi Zhu',
                'Padma Venkatraman',
                'Rav Kaur',
                'Anmol Desai',
                'Dex Bhadra',
                'Saahit Mogan'
            ],
            'former_position': [
                "Director '19, Lab Manager '18",
                "Curriculum Chair '21, Mentor '20",
                # "Mentor '21",
                "Director '21, '22, Lab Manager '20",
                "Curriculum Chair '21",
                "Director '22, '23, Lab Manager '21",
                "Senior Advsior '23, Director '22, Lab Manager '21",
                "Curriculum Manager '23",
                "Director '23, '24, '25"
            ],
            'former_now': [
                'Astro graduate student at UMD',
                'Mathematics masters student at Cambridge',
                # '-',
                'Quantum Science and Engineering graduate student at Harvard University',
                'Post-Baccalaureate Fellow at Kavli Institute for Particle Astrophysics and Cosmology',
                'Astronomy and Astrophysics PhD student at UC Santa Cruz',
                'Post-Baccalaureate Researcher at Goddard Space Flight Center',
                '-',
                'Astrophysics PhD student at UC Berkeley'
            ]
        },
        "content": {
            "overview": {
                "title": u"Lab Overview",
                "slides": ["/static/img/physics_slides/muon.jpg", "/static/img/physics_slides/symposium.jpg",
                           "/static/img/physics_slides/lbl_als_1.jpg", "/static/img/physics_slides/mixing.jpg"],
                "text": u""" 
                        <b style='font-size:150%;'> About Us </b>
                        <br><br>
                        The Undergraduate Lab at Berkeley, Physics &#38; Astronomy Division is a DeCal that aims to make the transition into undergraduate research as seamless as possible. <b>We believe that research should be accessible to all undergrads within the Physics and Astronomy Departments</b> despite significant barriers to entry for students traditionally underrepresented in academia or without a strong research background.
                        <br><br>
                        Under the guidance of experienced undergraduate mentors and graduate/postdoc advisors, groups of mentees complete a year long research project on a topic of their interest. During this process, our staff will help mentees are able to make sense of the current literature, isolate a feasible project, and execute projects on a reasonable timescale. In addition, mentors serve as role-models to help demystify the research process.
                        <br><br>
                        Our program, extends beyond project work. Students attend weekly workshops on essential research skills such as programming, statistics, etc. At the end of our program, students will have gained basic research skills often desired by research labs and will have demonstrated these skills in the process of completing a project of their own from start-to-finish.
                        <br><br>
                        Contact us at <a href="mailto:physics@ulab.berkeley.edu">physics@ulab.berkeley.edu</a> with any questions or concerns!                         
                        <br><br>
                        <a href="https://docs.google.com/document/d/1J_nPg7X1tv7KuOh9MCrAB86AOovm5SFgrrNRBkrfmAI/edit?usp=sharing" target="_blank">ULAB Physics & Astronomy CODE OF CONDUCT</a>
                        """
            },
            "join": {
                "title": u"Join Us!",
                "text": """
                        <b style='font-size:150%;'> Join Us! </b>
                        <br><br>
                        <b>ULAB Physics and Astronomy is a 2-semester DeCal. We meet Mon/Wed 7-8 PM.</b> Mentee/Mentor applications open before the fall semester and close around the second week of the fall semester. Click on the tabs to learn about each position.
                        <br><br>
                        <b>Mentees:</b>
                        The mentee application for Fall 2025-Spring 2026 is now open! 

<a href="https://forms.gle/ypfddqFhPy7Mp3xz6" target="_blank">Apply here.</a>

                        <br><br>
                        <b>Mentors:</b>
                        The mentor application for Fall 2025-Spring 2026 is now open! 

<a href="https://docs.google.com/forms/d/e/1FAIpQLScTVCvQggJnK8nZ2_Ci_DCEBk5ltFmZVytelS58AmOBh78jvg/viewform" target="_blank">Apply here.</a>
 Mentors will be supported by a $600/semester stipend. <b>There are a number of additional staff postions: lab manager and lecturer. Interested candidates may apply at the same link.</b>
                        <br><br>
                        <b>Graduate Students/Postdocs:</b>  Opportunities for graduate students, postdocs, and faculty to get involved are available year-round! Please reach out to us at <a href="mailto:physics@ulab.berkeley.edu">physics@ulab.berkeley.edu</a>
                    """
            },
            "mentees": {
                "title": "Mentees Info",
                "text": u"""
                        <b style='font-size:150%;'> Mentee Information </b>
                        <br><br>
                        ULAB is a 2-semester DeCal sponsored by Prof. Dan Kasen. We meet Mon/Wed 7-8 PM in-person!
                        <br><br>
                        <b>Timeline: </b>Fall semester is dedicated to creating a research proposal. Students are split into groups of 4-6 and assigned a mentor. Together, mentors and groups will explore the required background in their area of interest during weekly group meetings. In the process of learning about the current techniques and experiments in their field, groups will devise a research project they wish to explore. 
                        <br><br>
                        Mentees return in the spring semester to implement their project! ULAB provides funding, space, and graduate/postdoc advisors to assist mentees during this process. The semester culminates in a poster session open to the physics and astronomy departments!
                        <br><br>
                        In addition to weekly groups meetings, ULAB hosts weekly workshops with particular emphasis on Python and other basic research skills. The time commitment is roughly 2-3 hrs of in-person meetings and 2-3 hrs of individual work per week. Please see our <a href="https://docs.google.com/document/d/1cRIS3G5e168pUNx8_B_ZSl9xcOHZb8OaR99JoULMOpk/edit?usp=sharing">syllabus</a> for more detailed information!
                        <br><br><br>
                        <b style='font-size:150%;'> QnA</b>
                        <br><br>
                        <b>Q: What are the prerequisites for ULAB?</b>
                        <br>
                        None! Many students are first and seconds years with no prior research or programming experience. 
                        <br><br>
                        <b>Q: I'm a junior/junior transfer/senior, should I apply?</b>
                        <br>
                        Definitely! Many upperclassmen have found ULAB helpful in obtaining research experience. However, ULAB may not be the right choice if you already feel prepared to join a lab or have very little time left at Berkeley. 
                        <br><br>
                        <b>Q: How competitive is the program?</b>
                        <br>
                        We accept as many students as possible. In the event that space is limited, students that benefit most from our program have priority. 
                        <br><br>
                        <b>Q: How are project topics choosen?</b><br>
                        Available topics are determined by out cohort of mentors and vary year by year. We are able to normally cover the major subfields in physics and astronomy. Mentees have a large say in the mentor/project they work on.<br><br>
                        <b>Q: Can I apply to ULAB in addition to other research programs?</b><br>
                        Yes. Students that join ULAB, but are subsequently accepted into another program (e.g. URAP) may pursue both concurrently or drop ULAB before the drop deadline late September.              
                        <br><br>
                        <b>Q: Do ULAB projects yield results?</b><br>
                        Wrong question. ULAB is a <i>research training</i> organization. Through conducting their projects, mentees learn about the basic knowledge and skills required to conduct research in their field and leave our program a better candidate, and better prepared for research. (...but to answer the question, most projects do yield interesting results; and even when they don't, mentees are able to explain their work and what they've learned).
                        """
            },
            "mentors": {
                "title": "Mentor Info",
                "text": u"""
                        <b style='font-size:150%;'> Mentor Information </b>
                        <br><br>
                        Mentorship can be a very fruitful and rewarding experience for undergraduates with research experience. Mentors' primary job is to meet weekly with their group of 3-5 mentees during the year-long process of conducting an independent research project. Mentors will lead discussions on topics in their field and guide their group through their project.
                        <br><br>
                        Mentorship is a unique <i>learning</i> opportunity. Mentors will expereince the process of leading a scientific project, conduct research in a topic of their interest, and interact with fellow undergraduate and graduate researchers. <b>Mentors are generously supported by the <a href="https://n3as.berkeley.edu/collaboration/students/undergraduates/ulab/">N3AS</a> and will recieve $600/semester stipend*. </b>
                        <br><br>
                        *Stipends are disbursed as a department award and may affect your financial aid. In order to recieve stipends, mentors must fulfill all responsibilities of the position and remain an enrolled Berkeley student.
                        <br><br><br>

                        <b style='font-size:150%;'> QnA</b>
                        <br><br>
                        <b>Q: What is the committment?</b><br>
                        Mentorship is a 2-semester positions. Mentors meet with their groups 1-2 hrs/week and generally spend an additional 1-3 hours outside of in-person meetings. We require that mentors be available Wednesday 7-8 PM and enroll in 2 research units (Astron. 198).<br><br>
                        <b>Q: How much research experience is expected?</b><br>
                        Mentors are not expected to be experts, but should be comfortable exploring their field. They must be prepared to help mentees learn about a new topic, and to learn about a new topic/project themselves. At least 1 semester of research in a group is recommended.
                        <br><br>
                        <b>Q: How are project topics choosen</b>
                        <br>
                        While some mentors have a clear project in mind, most mentors begin an idea of topics they would like to work on. They are paired with mentees with similar interests. Mentors and mentees together determine a suitable project. We are able to reasonably fund physical projects, simulations, etc. 
                    """
            },
            "advisors": {
                "title": "Advisors Info",
                "text": u"""
                        <b style='font-size:150%;'> Advisor Information </b>
                        <br><br>
                        Graduate students and postdocs interested in supporting ULAB's mission are encouraged to become project advisors. Advisors serve to ensure scientific rigor, help determine the practically and scope of a project, and give general guidance on the direction of a project. The advising role is flexible and low-commitment: about 3-5 hours per semester. The format of advising differs by the semester.
                        <br><br>
                        <b>Fall semester</b>: during this time, groups research their areas of interest and devise a question they wish to explore. Advisors spend 1-2 hrs meeting with groups to discuss potential projects. Advisors will spend 1-2 hours reviewing project proposals that students have submitted.
                        <br><br>
                        <b>Spring semester</b>: groups will have finalized their research project and began conducting their experiments. Advisors will check-in periodically with an individual group every 3-4 weeks. 
                        <br><br>
                        Opportunities for advisors are available year-round. Please reach out to us at <a href="mailto:physics@ulab.berkeley.edu">physics@ulab.berkeley.edu</a>
                        <br><br>
                    """
            },
            "projects": {
                "title": "Projects",
                "text": "<b style='font-size:150%;'> Past Projects </b>",
                "years": {
                    '2024-2025': {
                        u'Performance Comparison of new Keck Adaptive Optics System': '/static/doc/posters/2025-1%20(1).pdf',
                        u'CORONA: Classification of R Coronae Objects with Neural Network Automation': '/static/doc/posters/2025-1%20(2).pdf',
                        u'Shedding Light on Obscura - Confirming the Existence of an Exoplanet': '/static/doc/posters/2025-1%20(3).pdf',
                        u'Re-analysis of OB110462 as a Possible Binary Microlensing Event': '/static/doc/posters/2025-1%20(4).pdf',
                        u'Solar Cycle Events and Impacts on Particle Intensity Around the South American Anomaly': '/static/doc/posters/2025-1%20(5).pdf',
                        u'The Dynamics of Rogue Planets in Binary Star Systems': '/static/doc/posters/2025-1%20(6).pdf',
                        u'Increasing Convergence of Three-Channel Scattering Amplitudes': '/static/doc/posters/2025-1%20(7).pdf',
                        u'Simulating Ecosystems with Wild Demographic Fluctuations': '/static/doc/posters/2025-1%20(8).pdf',
                        u'Z-Streak Analysis & Discovery of Near Earth Objects': '/static/doc/posters/2025-1%20(9).pdf',
                    },
                    '2023-2024': {
                        u'Magnetic Energy Transfer in Kerr Black Holes': '/static/doc/posters/s241.pdf',
                        u'Investigating the Effect of Pollution on Muon Flux Using a CosmicWatch Modular Detector': '/static/doc/posters/s242.pdf',
                        u'Probing for Bondi-Hoyle-Lyttleton Accretion in Orion Src I': '/static/doc/posters/s243.pdf',
                        u'Quantum Magnetometry with NV-Centers': '/static/doc/posters/s244.pdf',
                        u'Discovering an Exoplanet': '/static/doc/posters/s245.pdf',
                        u'Machine Learning for Cosmic Structure Simulations': '/static/doc/posters/s246.pdf',
                        u'Cosmic Flux: Geiger Counter': '/static/doc/posters/s247.pdf',
                        u'Classifications of Unknown Transients Using ParSNIP': '/static/doc/posters/s248.pdf',
                        u'Simulating Supernova 1987A Remnants': '/static/doc/posters/s249.pdf',
                        u'Analyzing Variations Within the Delayed-Choice Quantum Eraser Experiment': '/static/doc/posters/s2410.pdf',
                    },

                    '2022-2023': {
                        u'Identifying the Presence of Biosignatures on Exoplanets and Moons in Our Solar System': '/static/doc/posters/s231.pdf',
                        u'Relationship of H-alpha Velocity and H2 Fraction in Galaxies': '/static/doc/posters/s232.pdf',
                        u'Stellar Age Estimation via Machine Learning': '/static/doc/posters/s233.pdf',
                        u'Ray Tracing Schwarzschild and Kerr Black Holes': '/static/doc/posters/s234.pdf',
                        u'Computational Exploration of the BKT Transition in XY-Interaction Systems': '/static/doc/posters/s235.pdf',
                        u'VQE Algorithm for Dihydrogen Ground State Energy': '/static/doc/posters/s236.pdf',
                        u'Electromagnetic Inverse Design of a Compact Wavelength Demultiplexer': '/static/doc/posters/s237.pdf',
                        u'Confirming the Existence of Exoplanet Pluvia': '/static/doc/posters/s238.pdf',
                        u'Feasibility of Muon Tomography to Determine the Electronic Structure of a Thundercloud': '/static/doc/posters/s239.pdf'

                    },
                    '2021-2022': {
                        u'Numerical Spin Analysis of Relativistic Bondi Accretion in M87*': "/static/doc/posters/s221.pdf",
                        u'Analyzing Anomalous Transport in Interplanetary Shocks Using a Mittag-Leffler Function': '/static/doc/posters/s222.pdf',
                        u'Cosmic Ray Predictions With a Homemade Muon Detector': '/static/doc/posters/s223.pdf',
                        u'Observing and Obtaining a Light Curve from a Potential Transiting Exoplanet': '/static/doc/posters/s224.pdf',
                        u'Creating a Pipeline to Generate Radial Velocity Curves from Raw APF Spectral Data': '/static/doc/posters/s225.pdf',
                        u'Simulating Scattering Processes in TGFs Using Monte Carlo Methods': '/static/doc/posters/s226.pdf',
                        u'Determining the Verdet Coefficient of Olive Oil with Faraday Rotation': '/static/doc/posters/s227.pdf',
                        u'Investigating Habitability in the Kepler-47 Binary System': '/static/doc/posters/s228.pdf'

                    },
                    '2020-2021': {
                        u'Measuring Cosmic Distances using Gravitational Waves': "/static/doc/posters/s211.pdf",
                        u'Doppler Imaging of a Simulated Star': '/static/doc/posters/s212.pdf',
                        u'Characterizing Exoplanet Habitability': '/static/doc/posters/s213.pdf',
                        u'Categorizing Solar Flares with Machine Learning': '/static/doc/posters/s214.pdf',
                        u"Determining Hubble's Constant From Time Delays in Lensed Quasars ": '/static/doc/posters/s215.pdf',
                        u'An Exploration into Experimental Particle Physics': '/static/doc/posters/s216.pdf',
                        u'Modeling and Mapping Terrestrial Gamma Ray Flashes': '/static/doc/posters/s217.pdf'
                    },
                    '2019-2020': {
                        u'Computational Analysis of Mixing Layers in the Interstellar Medium': '/static/doc/posters/s201.pdf',
                        u"Investigation on the Potential Origin of 'Oumuamua": '/static/doc/posters/s202.pdf',
                        u'Simulating the Antenna Response of Radio Interferometers': '/static/doc/posters/s203.pdf',
                        u'Accessible Balloon RAdiometer-Detecting the Cosmic Microwave Background': '/static/doc/posters/s204.pdf',
                        u'Period-Luminosity Analysis of Cepheid Variables': '/static/doc/posters/s205.pdf',
                        u'Analyzing the Turnover Point in the Light Curve of the Neutron Star Binary Merger Event GW170817': '/static/doc/posters/s206.pdf',
                        u'Physics of a Tokamak': '/static/doc/posters/s207.pdf',
                        u'Nanoparticle Drug Delivery Methods via DNA Nanotechnology': '/static/doc/posters/s208.pdf',
                        u'Relating Electromagnetic Waves to Light': '/static/doc/posters/s209.pdf'
                    },
                    '2018-2019': {
                        u'Implementation of Partial Quantum Search': '/static/doc/posters/s191.pdf',
                        u'Determining Graphene Stacking via Raman Spectroscopy': '/static/doc/posters/s192.pdf',
                        u'Angular and Altitude Dependence of Cosmic Ray Muons': '/static/doc/posters/s193.pdf',
                        u'Monte Carlo Study of the Ising Model': '/static/doc/posters/s194.pdf',
                        u'Interplanetary Radiation Harnessing Voltaic System': '/static/doc/posters/s195.pdf',
                        u'An Analysis on the Distribution of the Hubble Parameter across the Sky': '/static/doc/posters/s196.pdf',
                        u'Estimating the Mass of the Milky Way Galaxy': '/static/doc/posters/s197.pdf',
                        u'Exoplanet Detections with Machine Learning': '/static/doc/posters/s198.pdf',
                        u'Calibrating the Flux-Weighted Gravity-Luminosity Relation in Blue Supergiant Stars': '/static/doc/posters/s199.pdf',
                    },
                    '2017-2018': {
                        u'Determining the Habitability of Exoplanets': '/static/doc/posters/s181.pdf',
                        u'Measuring the Spin of Rotating Black Holes': '/static/doc/posters/s182.pdf',
                        u'Designing an Electromagnetic Shield to Block Secondary Cosmic Rays': '/static/doc/posters/s183.pdf',
                        u'Study of Isotropic and Anisotropic Electrical Conductivity': '/static/doc/posters/s184.pdf',
                    }
                }
            },
            "calendar": {
                "title": u"Calendar",
                "text": u"""""",
                "object": """<iframe src="https://calendar.google.com/calendar/embed?src=physics.ulab%40gmail.com&ctz=America%2FLos_Angeles" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>"""
            }
        }
    },

    "bio": {
        "logo": u"/static/img/logos/logo_public_health.png",
        "short_name": u"genetics",
        "full_name": u"Health Sciences",
        "navbar": u"Health Sciences",
        "status": "Active",
        "members": ["Aarti Anand", "Christopher Lee", "Heer Nanda", "Tejas Raxwal", "Ariana Chavez", "Antara Majumder",
                    "Fakhrunnesa (Nessa) Samim", "Vivian Lee", "Zarin Mahmud", "Jeffrey Chen",
                    "Kaitlyn Gilbride", "Yihan Xia", "Seo Jin (Ella) Choi"],
        "content": {
            "overview": {
                "title": "Lab Overview Coming Soon!",
                "text": u""" """
            },
            "join": {
                "title": "Want to join us?",
                "text": u"""Applications for Fall 2025 to Spring 2026 year are closed, please check back beginning 
                next Fall 2026!"""
            },
            "calendar": {
                "title": "",
                "text": "",
                "object": ""
            }
        }
    },

    "compbio": {
        "logo": u"/static/img/logos/logo_compbio.png",
        "short_name": u"compbio",
        "full_name": u"Computational Biology",
        "navbar": u"Computational Biology",
        "status": "Active",
        "members": ["Farrah Kaiyom"],
        "content": {
            "overview": {
                "title": "Lab Overview",
                "text": u"""
                Founded in Spring 2021, the Computational Biology Division of the Undergraduate Lab at Berkeley, aims to give interested undergraduates a chance to conduct their own research projects in Computational Biology in small groups under the guidance of experienced undergraduate mentors. Along the way they will gain fundamental research skills, explore relevant background knowledge, and gain experience in the research process. Our goal is to help students feel confident and prepared to seek out on-campus opportunities in the exciting field of computational biology. <br/>
                The lab will meet as a DeCal over the course of two semesters. Students will spend class time learning background information and meeting with their groups to work on their project. Mentors will supervise groups of 4-6 students, and guide them through the process of exploring a research question. The DeCal will conclude with a final project presentation. See the course syllabus <a href="https://docs.google.com/document/d/17VwIgGdOPjNIQTYOh9nihGHIw6HfpLPv4sajlqydwFI">here</a>, and our decal page <a href="https://decal.berkeley.edu/courses/7132">here</a>!<br/>.
                """
            },
            "join": {
                "title": "Join Us!",
                "text": u"""
                    Mentee & Mentor positions are now open for Fall 2023! If you would like to be considered for a role in our lab this semester, please fill out the respective forms below. The application deadline is extended to Saturday, September 16th @ 11:59PM for both mentors and mentees. Both mentors & mentees will hear back from us regarding the decision by Monday, September 18th; the deadline to accept our offer will be Tuesday, September 19th. Although the application deadline is after the course add/drop deadline, all members that hear from us before September 13th will be able to take our Decal for units. Our first class will be held on September 12th in the Social Sciences Building Room 56 from 7-8pm, and we welcome all potential members to attend, even if you are unsure of applying!
                    <br><br>
                    <b>Mentees:</b> Mentees will work in groups of 4-6 students, supervised by a mentor, in developing and working on a research project in their group's area of interest. Along the way they will learn fundamental research skills and background knowledge in Computational Biology. Mentees receive 2 units through BioE 98. The application is due by Monday, January 29th at 11:59PM PT; apply now at the link: <a href='https://tinyurl.com/ulabcompbiomentee23'>tinyurl.com/ulabcompbiomentee23</a>                        <br><br>
                    <b>Mentors:</b> Mentors will guide an undergraduate team of students through the process of designing and working on a research project within their area of interest. Teams will present their projects at an end-of-semester symposium. Mentors receive 2 units through IB 98. The application is due by Monday, September 5th at 11:59PM PT; apply now at the link!: <a href='https://tinyurl.com/ulabcompbiomentor23'>tinyurl.com/ulabcompbiomentor23</a>
                    <br><br>
                    If you are interested in joining and would like to be updated on our program, fill out the interest form: <a href='https://forms.gle/mQaURznvM3xN87ZG8'>tinyurl.com/ulab-compbio</a>
                    <br><br>                    
                """

                # <a href="https://forms.gle/4CUb93ZLr3KVeTcZ6">Apply Now!</a><br/><br/>
                # <b>Mentors:</b> Mentors will guide an undergraduate team of students through the process of designing and working on a research project within their area of interest. Teams will present their projects at an end-of-semester symposium. Mentors receive 2 units through IB 98. The application is due by Wednesday, January 27th at 11:59PM PT; apply now at the link above!.<br/><br/>
                # <b>Mentees:</b> Mentees will work in groups of 4-6 students, supervised by a mentor, in developing and working on a research project in their group's area of interest. Along the way they will learn fundamental research skills and background knowledge in Computational Biology. Mentees receive 2 units through IB 98. The application is due by Friday, January 29th at 11:59PM PT; apply now at the link above!
                # """
            },
            "calendar": {
                "title": "",
                "text": "",
                "object": ""
            }
        },
    },

    "data": {
        "logo": u"/static/img/logos/logo_data.png",
        "short_name": u"data",
        "full_name": u"Data Science",
        "navbar": u"Data Science",
        "status": "Active",
        "members": ["Kashish Kharbanda", "Nandita Radhakrishnan", "Won Shil Park", "Srikanth Nampoothiri", "Ethan Qiu",
                    "Arjun Vats"],
        "content": {
            "overview": {
                "title": "Lab Overview",
                "text": u"""
                        The Data Science Lab, started by Alan Pham in Fall 2018, is a great opportunity for students to conduct data science research by working on an interesting project, with guidance from experienced undergraduate mentors. It might seem difficult, but it's actually very fun and easy, because of our unique way of providing students a gentle introduction to research. For mentors, this is a meaningful opportunity to lead aspiring researchers while getting to know what it might be like to lead a lab. <br/>

                        <br/>

                        Data science is becoming an increasingly important field, and the ability to understand, analyze, and clearly communicate data is valuable in any field, so we encourage everyone to study it. Projects can be about anything you choose, as long as it deals with data. Possible areas of interest could be education, business, technology, health, sports, sociology, government, etc. Basically, anything you learn about or observe in life can be analyzed with data science, so this is a great chance for students of all majors to explore any research topics of their interest. For example, you could investigate factors that increase risk for certain diseases, develop a predictive model for election results, or identify factors that increase school test scores. This is a very beneficial and worthwhile opportunity, and we hope you can join as a researcher or mentor. <br>

                        <br/>

                        Please don't hesitate to contact us if you have any questions."""
            },
            "join": {
                "title": u"Want to join us?",
                "text": u"""
                        Mentee & Mentor positions are now open for Spring 2022! If you would like to be considered for a role in our lab this semester, please fill out the respective forms below. Applications are due Friday, February 4th @ 11:59PM for both mentors and mentees. Both mentors & mentees will hear back from us regarding the decision by Sunday, February 6th; the deadline to accept our offer will be Tuesday, February 8th. 
                        <br><br>
                        If you're interested in getting to know more about ULAB DS and its structure, or if you have any questions you'd like to ask us, attend our info session on Tuesday 2/1 @ 8PM: more details on our Facebook page <a href='https://fb.me/e/22SDc3utS'>here</a>.
                        <br><br> 
                        Mentee Application: <a href='https://docs.google.com/forms/d/e/1FAIpQLSdid-6ZauDfHUX4j4HAGTAhgysko9_se7hfsnyX3uUlwQmNeg/viewform'>tinyurl.com/sp22ulab</a>
                        <br><br>
                        Mentor Application: <a href='https://docs.google.com/forms/d/e/1FAIpQLSfdGP_rMkEOOlOIazpd87fpr7cO2brL5X2VOD3VXdFwEjV6Sg/viewform'>tinyurl.com/sp22dsmentor</a>
                        <br><br>
                        If you have any questions about the application process, please email <a href='mailto:kashishk@berkeley.edu'>kashishk@berkeley.edu</a>!
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

# RESEARCH DICTIONARY IS DEPRECATED
# ONLY HERE FOR REFERENCE DURING WEBSITE REVAMP
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
                <p>The astrophysics branch currently supports two separate projects, the first being on exoplanetary atmospheric analysis. By using open-sourced data from NASA's Kepler mission, the group plans to create an automated method of categorizing various exoplanet's atmospheric compositions and habitability likelihood.</p>
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
        "team": ["Riley McDanal", "Annelise Meyer", "Hareen Seerha", "Valerie Burleigh", "Stephanie Chang",
                 "Adam Bittenson", "Allie Morehouse"],
        "has_mentor": False,
        "mentor": ""
    },

    "ATG-ulab": {
        "date": "12 March, 2018",
        "app-url": "/lab-jobs/atg",
        "navbar": "Community Analysis",
        "img": "img/project/human-circuit.jpg",
        "title": "Advanced Technologies Group",
        "team": ["Dillon Eskandar", "Neil Toledo", "Cibi Pari", "David Liu", "Kavi Vaidya", "Charlie Zhang",
                 "Albert Huang"],
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
