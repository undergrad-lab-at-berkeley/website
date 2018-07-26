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
    "physics-ulab": {
        "date": "17 Nov, 2017",
        "app-url": "/lab-jobs/physics",
        "navbar": "Automated Weed Removal",
        "img": "img/project/exoplanet.jpg",
        "title": "Physics and Astrophysics uLab",
        "team": ["Arjun Savel"],
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
        "mentor": "",
        "staff-info": {
            "Riley McDanal": {
                "title": "Research Director",
                "email": "rileymcdanal@berkeley.edu or cogsci.ulab@berkeley.edu",
                "linkedin": "www.linkedin.com/in/riley-mcdanal",
                "facebook": "www.facebook.com/riley.mcdanal",
                "github": "",
                "personal": "",
                "img": ""
            },
            "Annelise Meyer": {
                "title": "Vice Research Director",
                "email": "annelise.meyer@berkeley.edu",
                "linkedin": "www.linkedin.com/in/annelise-meyer/ ",
                "facebook": "www.facebook.com/anna.meyer.16718 ",
                "github": "",
                "personal": "",
                "img": ""
            },
            "Hareen Seerha": {
                "title": "Lab Manager",
                "email": "hareen_seerha@berkeley.edu",
                "linkedin": "",
                "facebook": "www.facebook.com/hareen.seerha",
                "github": "",
                "personal": "",
                "img": ""
            },
            "Valerie Burleigh": {
                "title": "Operations Director",
                "email": "valerie.burleigh@berkeley.edu",
                "linkedin": "www.linkedin.com/in/valerieannburleigh/",
                "facebook": "www.facebook.com/valerie.burleigh.3",
                "github": "",
                "personal": "",
                "img": ""
            },
            "Stephanie Chang": {
                "title": "Vice Operations Director",
                "email": "stephanieychang@berkeley.edu",
                "linkedin": "www.linkedin.com/in/stephanie-chang-a97457155/",
                "facebook": "",
                "github": "",
                "personal": "",
                "img": ""
            },
            "Adam Bittenson": {
                "title": "Finance Director",
                "email": "abittenson@berkeley.edu",
                "linkedin": "www.linkedin.com/in/adam-bittenson-368507163",
                "facebook": "www.facebook.com/profile.php?id=100000579046414",
                "github": "",
                "personal": "",
                "img": ""
            },
            "Allie Morehouse": {
                "title": "Curriculum and Advising Director",
                "email": "amorehouse@berkeley.edu",
                "linkedin": "www.linkedin.com/in/allison-morehouse-6bb63a139/",
                "facebook": "",
                "github": "",
                "personal": "",
                "img": ""
            },
            "Colin Jindra": {
                "title": "Lead Mentor",
                "email": "cjindra@berkeley.edu",
                "linkedin": "https://www.linkedin.com/in/colin-jindra-17114a142/",
                "facebook": "https://www.facebook.com/colin.jindra",
                "github": "",
                "personal": "",
                "img": ""
            }
        },
        "content": """
                    <h4>Lab Overview</h4>
                    <p>Founded in Fall 2017 by Jenna Martin and Riley McDanal, the CogSci Lab has a vision of offering an experience that benefits all undergraduates in the research community.  Experienced researchers can attain leadership roles within this lab setting while facilitating the training and growth of aspiring researchers so that each group is primed for more advanced research opportunities.
                    </p>
                    <p>Last year, our lab worked on projects involving neural atrophication, language processing, consciousness and decision-making, but we are currently developing exciting research projects for the upcoming school year.
                    </p>

                    <h4>Our Staff</h4>

                    <br />

                    <h4> Want to join us? </h4>

                    We are currently looking to fill mentor and research postions for this semester, so if you would like to be considered for a role in our lab next semester, please fill out the respective form below. If you have any more questions or would like to learn more about our lab, please email <a href="cogsci.ulab@gmail.com">cogsci.ulab@gmail.com</a>.

                    <br />
                    <a href="https://goo.gl/forms/CP88XEos8anrlNwl2"> Mentor Application</a>
                    <br />
                    <a href="https://goo.gl/forms/7DAT9Tq1JESJWZG53"> Student Researcher Application</a>

                """
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
        "staff-info": {
            "Dillion Eskandar": {
                "title": "Director of Advanced Technologies Group",
                "email": "dilloneskandar@berkeley.edu",
                "linkedin": "",
                "facebook": "",
                "github": "",
                "personal": "",
                "img": ""
            },
            "Neil Toledo": {
                "title": "Deputy Director of Advanced Technologies Group",
                "email": "ntoledo@berkeley.edu",
                "linkedin": "",
                "facebook": "",
                "github": "",
                "personal": "",
                "img": ""
            },
            "Cibi Pari": {
                "title": "Deputy Director of Technology",
                "email": "cibi.pari@berkeley.edu",
                "linkedin": "",
                "facebook": "",
                "github": "",
                "personal": "",
                "img": ""
            },
            "David Liu": {
                "title": "Deputy Director of External Affairs",
                "email": "daveliu@berkeley.edu",
                "linkedin": "",
                "facebook": "",
                "github": "",
                "personal": "",
                "img": ""
            },
            "Kavi Vaidya": {
                "title": "Deputy Director of Finance",
                "email": "kavid.vaidya@berkeley.edu",
                "linkedin": "",
                "facebook": "",
                "github": "",
                "personal": "",
                "img": ""
            },
            "Charlie Zhang": {
                "title": "Deputy Director of Design",
                "email": "eucbital@berkeley.edu",
                "linkedin": "",
                "facebook": "",
                "github": "",
                "personal": "",
                "img": ""
            },
            "Albert Huang": {
                "title": "",
                "email": "albert168@berkeley.edu",
                "linkedin": "",
                "facebook": "",
                "github": "",
                "personal": "",
                "img": ""
            }
        },
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
        "staff-info": {
            "Yasmeen Musthafa": {
                "title": "Director of Operations",
                "email": "yasmeenm@berkeley.edu",
                "linkedin": "",
                "facebook": "",
                "github": "",
                "personal": "",
                "img": ""
            },
            "Min Young Kim": {
                "title": "",
                "email": "Minyoung.kim@berkeley.edu",
                "linkedin": "",
                "facebook": "",
                "github": "",
                "personal": "",
                "img": ""
            },
            "Catherine Livelo": {
                "title": "Curriculum Developer/ Biology Lab Leader",
                "email": "catherinelivelo@berkeley.edu",
                "linkedin": "",
                "facebook": "",
                "github": "",
                "personal": "",
                "img": ""
            },
            "Justin Gerwien": {
                "title": "Engineering Task Force",
                "email": "justingerwien@berkeley.edu",
                "linkedin": "linkedin.com/in/justin-gerwien-781b05106",
                "facebook": "",
                "github": "",
                "personal": "",
                "img": ""
            }
        },
        "content": """
                    <h4>Publicity/Partnership Team</h4>

                    <p>
                    Our team works to reach out to other campus organizations and resources in order to recruit a more diverse group of students and let students be aware of the opportunities ULAB provides.
                    In partnership, we strive to work together with other research organizations for undergraduate students to create a network of available resources to help students.
                    By publicizing ULAB to incoming freshmen who are looking to develop basic research skills and to other undergraduates with leadership opportunities,
                    we want to allow more students to gain valuable experiences that will help their undergraduate carrier both professionally and personally.
                    </p>

                    <h4>Current Staff</h4>

                    """,

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

    "stat-ulab": {
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
    }
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
    }
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
    }
}

team = {
    "Riley McDanal": {
            "img": "img/team/riley_mcdanal.jpg",
            "position": "Research Director: Cognitive Science and Medical Imaging",
            "email": "",
            "personal": "",
            "github": "",
            "linkedin": "",
            "bio": """I like to sing out loud in my apartment despite the never-ending fear of my neighbors judging me. My homemade speciality is carbonara tacos. Also, I love psychology, politics, and really anything that gets me thinking. """
    },

    "Arjun Savel": {
        "img": "",
        "position": "Research Director: Physics and Astrophysics",
        "email": "",
        "personal": "",
        "github": "",
        "linkedin": "",
        "bio": """To be added"""
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

    "Yasmeen Musthafa": {
        "img": "",
        "position": "Operations Director",
        "email": "",
        "personal": "",
        "github": "",
        "linkedin": "",
        "bio": """"""
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

lab_ordering = ['cogsci','physics','atg','ops','bio','stat','aerospace']

labs = {
    "cogsci": {
            "logo" : u"/static/img/logos/logo_cog_sci.png",
            "short_name": u"cogsci",
            "full_name": u"Cognitive Neuroscience and Medical Imaging",
            "navbar": u"Cog_Sci",
            "status": "Active",
            "content": """
                        <h4>Lab Overview</h4>
                        <p>Founded in Fall 2017 by Jenna Martin and Riley McDanal, the CogSci Lab has a vision of offering an experience that benefits all undergraduates in the research community.  Experienced researchers can attain leadership roles within this lab setting while facilitating the training and growth of aspiring researchers so that each group is primed for more advanced research opportunities.
                        </p>
                        <p>Last year, our lab worked on projects involving neural atrophication, language processing, consciousness and decision-making, but we are currently developing exciting research projects for the upcoming school year.
                        </p>
    
                        <h4>Our Staff</h4>
    
                        <br />
    
                        <h4> Want to join us? </h4>
    
                        We are currently looking to fill mentor and research postions for this semester, so if you would like to be considered for a role in our lab next semester, please fill out the respective form below. If you have any more questions or would like to learn more about our lab, please email <a href="cogsci.ulab@gmail.com">cogsci.ulab@gmail.com</a>.
    
                        <br />
                        <a href="https://goo.gl/forms/CP88XEos8anrlNwl2"> Mentor Application</a>
                        <br />
                        <a href="https://goo.gl/forms/7DAT9Tq1JESJWZG53"> Student Researcher Application</a>
    
                    """
    },

    "physics": {
            "logo" : u"/static/img/logos/logo_physics.png",
            "short_name": u"physics",
            "full_name": u"Physics and Astrophysics",
            "navbar": u"Physics",
            "status": "Active",
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

    "atg": {
            "logo" : u"/static/img/logos/logo_atg.png",
	        "short_name" : "ATG",
	        "full_name" : "Advanced Technologies Group",
	        "navbar" : "Advanced Technologies Group",
            "status": "Active",
            "content": "Page under construction. You can learn more about opportunities for students (of all years) <a href=/lab-jobs/atg> here </a> "
    },

    "ops": {
            "logo" : u"/static/img/logos/logo_general.png",
            "short_name" : "ops",
	        "full_name" : "Operations and Publicity",
	        "navbar" : "Operations and Publicity",
            "status": "Active",
            "content": """
                        <h4>Publicity/Partnership Team</h4>
    
                        <p>
                        Our team works to reach out to other campus organizations and resources in order to recruit a more diverse group of students and let students be aware of the opportunities ULAB provides.
                        In partnership, we strive to work together with other research organizations for undergraduate students to create a network of available resources to help students.
                        By publicizing ULAB to incoming freshmen who are looking to develop basic research skills and to other undergraduates with leadership opportunities,
                        we want to allow more students to gain valuable experiences that will help their undergraduate carrier both professionally and personally.
                        </p>
    
                        <h4>Current Staff</h4>
    
                        """,
    },
    # Coming Soon
    "bio": {
            "logo" : u"static/img/logos/logo_bio.png",
            "short_name": u"genetics",
            "full_name": u"Genetic Engineering and Molecular Biology",
            "navbar": u"Genetic Engineering and Molecular Biology",
            "status": "Coming Soon",
            "content":
                    """
                    <h4> Coming Soon! </h4>
                    """
    },

    # To be Determined
    "stat": {
            "logo" : u"/static/img/logos/logo_stat_ml.png",
            "short_name": "stat",
            "full_name": "Statistical Modeling and Deep Learning",
            "navbar": "Statistical Modeling and Deep Learning",
            "status": "Under Development",
            "content":
                    """
                    <h4> Under Development </h4>
                    """
    },

    "aerospace": {
            "logo" : u"/static/img/logos/logo_robotics_aero.png",
            "short_name": "aerospace",
            "full_name": "Robotics and Aerospace Engineering",
            "navbar": "Robotics and Aerospace Engineering",
            "status": "Under Development",
            "content":
                    """
                    <h4> Under Development </h4>
                    """
    }
}
