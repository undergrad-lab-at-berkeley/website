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

foundersOrder = ["Joshua Hug", "Mrinalini Sugosh", "Alex Powers", "Dylan Kato", "Michael Oshiro"]
advisorsOrder = ["Joshua Hug", "Alex Powers", "Sean Burns"]
teamOrder = ['Riley McDanal', 'Arjun Savel', 'Dillon Eskandar', 'Yasmeen Musthafa', 'Min Young Kim', 'Mrinalini Sugosh']
labOrder = ['cogsci','physics','atg','ops','bio','stat','aerospace']

labs = {
    "cogsci": {
            "logo" : u"/static/img/logos/logo_cog_sci.png",
            "short_name": u"cogsci",
            "full_name": u"Cognitive Neuroscience and Medical Imaging",
            "navbar": u"Cog_Sci",
            "status": "Active",
            "members": ["Riley McDanal", "Annelise Meyer", "Hareen Seerha", "Valerie Burleigh", "Stephanie Chang", "Adam Bittenson", "Allie Morehouse"],
            "content": {
                "overview": {
                    "title": "Lab Overview",
                    "text": """
                        Founded in Fall 2017 by Jenna Martin and Riley McDanal, the CogSci Lab has a vision of offering an experience that benefits all undergraduates in the research community.  Experienced researchers can attain leadership roles within this lab setting while facilitating the training and growth of aspiring researchers so that each group is primed for more advanced research opportunities. </br>
                        Last year, our lab worked on projects involving neural atrophication, language processing, consciousness and decision-making, but we are currently developing exciting research projects for the upcoming school year.
                        """
                },
                "join": {
                    "title": "Want to join us?",
                    "text": """
                        We are currently looking to fill mentor and research postions for this semester, so if you would like to be considered for a role in our lab next semester, please fill out the respective form below. If you have any more questions or would like to learn more about our lab, please email <a href="cogsci.ulab@gmail.com">cogsci.ulab@gmail.com</a>. <br/>
                        <a href="https://goo.gl/forms/CP88XEos8anrlNwl2"> Mentor Application</a> <br/>
                        <a href="https://goo.gl/forms/7DAT9Tq1JESJWZG53"> Student Researcher Application</a>
                        """
                }
            }
    },

    "physics": {
            "logo" : u"/static/img/logos/logo_physics.png",
            "short_name": u"physics",
            "full_name": u"Physics and Astrophysics",
            "navbar": u"Physics",
            "status": "Active",
            "members": ["Arjun Savel"],
            "content": {
                "overview": {
                    "title": "Text",
                    "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
                },
                "join": {
                    "title": "Want to join us?",
                    "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
                }
            }
    },

    "atg": {
            "logo" : u"/static/img/logos/logo_atg.png",
	        "short_name" : "ATG",
	        "full_name" : "Advanced Technologies Group",
	        "navbar" : "Advanced Technologies Group",
            "status": "Active",
            "members": ["Dillon Eskandar", "Neil Toledo", "Cibi Pari", "David Liu", "Kavi Vaidya", "Charlie Zhang", "Albert Huang"],
            "content": {
                "overview": {
                    "title": "Page Under Contstruction",
                    "text": "You can learn more about opportunities for students (of all years) <a href=/lab-jobs/atg> here. </a>"
                },
                "join": {
                    "title": "Want to join us?",
                    "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
                }
            },
    },

    "ops": {
            "logo" : u"/static/img/logos/logo_general.png",
            "short_name" : "ops",
	        "full_name" : "Operations and Publicity",
	        "navbar" : "Operations and Publicity",
            "status": "Active",
            "members": ["Yasmeen Musthafa", "Min Young Kim", "Catherine Livelo", "Justin Gerwien"],
            "content": {
                "overview": {
                    "title": "Publicity/Partnership Team",
                    "text": """
                        Our team works to reach out to other campus organizations and resources in order to recruit a more diverse group of students and let students be aware of the opportunities ULAB provides.
                        In partnership, we strive to work together with other research organizations for undergraduate students to create a network of available resources to help students.
                        By publicizing ULAB to incoming freshmen who are looking to develop basic research skills and to other undergraduates with leadership opportunities,
                        we want to allow more students to gain valuable experiences that will help their undergraduate carrier both professionally and personally.
                        """
                },
                "join": {
                    "title": "Want to join us?",
                    "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
                }
            }
    },
    # Coming Soon
    "bio": {
            "logo" : u"/static/img/logos/logo_bio.png",
            "short_name": u"genetics",
            "full_name": u"Genetic Engineering and Molecular Biology",
            "navbar": u"Genetic Engineering and Molecular Biology",
            "status": "Coming Soon",
            "memebers": [],
            "content": {
                "overview": {
                    "title": "This Lab is Under Development",
                    "text": ""
                },
                "join": {
                    "title": "",
                    "text": ""
                }
            }
    },

    # To be Determined
    "stat": {
            "logo" : u"/static/img/logos/logo_stat_ml.png",
            "short_name": "stat",
            "full_name": "Statistical Modeling and Deep Learning",
            "navbar": "Statistical Modeling and Deep Learning",
            "status": "Under Development",
            "members": [],
            "content": {
                "overview": {
                    "title": "This Lab is Under Development",
                    "text": ""
                },
                "join": {
                    "title": "",
                    "text": ""
                }
            }
    },

    "aerospace": {
            "logo" : u"/static/img/logos/logo_robotics_aero.png",
            "short_name": "aerospace",
            "full_name": "Robotics and Aerospace Engineering",
            "navbar": "Robotics and Aerospace Engineering",
            "status": "Under Development",
            "team": [],
            "content": {
                "overview": {
                    "title": "This Lab is Under Development",
                    "text": ""
                },
                "join": {
                    "title": "",
                    "text": ""
                }
            }
    }
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