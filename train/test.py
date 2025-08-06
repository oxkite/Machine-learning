# import numpy
# import matplotlib.pyplot as plt
# numpy.random.seed(2)

# x = numpy.random.normal(3, 1, 100)
# y = numpy.random.normal(150, 40, 100) / x


# print(x)
# plt.scatter(x, y)
# plt.show()

import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)
r2 = r2_score(train_y, mymodel(train_x))

print(mymodel(myline))

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()



{
  "search_metadata": {
    "id": "search_d97LXP4morupn9X8qk03EOrl",
    "status": "Success",
    "created_at": "2025-08-05T18:10:50Z",
    "request_time_taken": 1.13,
    "parsing_time_taken": 0.19,
    "total_time_taken": 1.32,
    "request_url": "https://www.google.com/search?q=lawyer+&oq=lawyer+&gl=us&hl=en&udm=8&jbr=sep:0",
    "html_url": "https://www.searchapi.io/api/v1/searches/search_d97LXP4morupn9X8qk03EOrl.html",
    "json_url": "https://www.searchapi.io/api/v1/searches/search_d97LXP4morupn9X8qk03EOrl"
  },
  "search_parameters": {
    "engine": "google_jobs",
    "q": "lawyer ",
    "google_domain": "google.com",
    "hl": "en",
    "gl": "us"
  },
  "search_information": {
    "query_displayed": "lawyer",
    "detected_location": "Chicago IL, Illinois",
    "has_no_results_for": false
  },
  "jobs": [
    {
      "position": 1,
      "title": "Legal Counsel - Commercial",
      "company_name": "Medline Industries, LP",
      "location": "Northfield, IL",
      "via": "via LinkedIn",
      "description": "Job Summary\n\nMedline is seeking a Legal Counsel to perform a variety of legal services for clients across Medline’s business. This role will primarily be focused on Commercial counseling.\n\nJob Description\n\nMAJOR RESPONSIBILITIES\n• Provide guidance and counseling to colleagues across the business and functional divisions on commercial matters.\n• Negotiate and draft various contracts, whether for the purchase or sale of goods, services, or technology. Manage a large volume of transactions from start to finish, working closely with commercial colleagues. Work cross-functionally with various control functions to provide seamless support to the business.\n• Counsel the business and functional areas within the company regarding contracts and disputes. Identify and mitigate risks, and advise company leadership on risk mitigation strategies.\n• Support company leadership on various projects, activities, and initiatives.\n\nMinimum Job Requirements\n\nEducation\n• Juris Doctor degree.\n\nCertification / Licensure\n• Member of a state bar in good standing.\n\nWork Experience\n• At least 4 years of post-law school experience at a law firm or in-house at a corporation.\n\nKnowledge / Skills / Abilities\n• Excellent communication and interpersonal skills.\n• Demonstrated ability to independently identify practical legal solutions to complex challenges.\n• Possess the skills to effectively manage legal projects.\n• Knowledge of laws and regulations related to the healthcare industry.\n\nMedline Industries, LP, and its subsidiaries, offer a competitive total rewards package, continuing education & training, and tremendous potential with a growing worldwide organization.\n\nThe Anticipated Salary Range For This Position\n\n$152,880.00 - $229,320.00 Annual\n\nThe actual salary will vary based on applicant’s location, education, experience, skills, and abilities. This role is bonus and/or incentive eligible. Medline will not pay less than the applicable minimum wage or salary threshold.\n\nOur benefit package includes health insurance, life and disability, 401(k) contributions, paid time off, etc., for employees working 30 or more hours per week on average. For a more comprehensive list of our benefits please click here. For roles where employees work less than 30 hours per week, benefits include 401(k) contributions as well as access to the Employee Assistance Program, Employee Resource Groups and the Employee Service Corp.\n\nWe’re dedicated to creating a Medline where everyone feels they belong and can grow their career. We strive to do this by seeking diversity in all forms, acting inclusively, and ensuring that people have tools and resources to perform at their best. Explore our Belonging page here.\n\nMedline Industries, LP is an equal opportunity employer. Medline evaluates qualified individuals without regard to race, color, religion, gender, gender identity or expression, sexual orientation, national origin, age, disability, neurodivergence, protected veteran status, marital or family status, caregiver responsibilities, genetic information, or any other characteristic protected by applicable federal, state, or local laws.",
      "job_highlights": [
        {
          "title": "Qualifications",
          "items": [
            "Juris Doctor degree",
            "Certification / Licensure",
            "Member of a state bar in good standing",
            "At least 4 years of post-law school experience at a law firm or in-house at a corporation",
            "Knowledge / Skills / Abilities",
            "Excellent communication and interpersonal skills",
            "Demonstrated ability to independently identify practical legal solutions to complex challenges",
            "Possess the skills to effectively manage legal projects",
            "Knowledge of laws and regulations related to the healthcare industry"
          ]
        },
        {
          "title": "Benefits",
          "items": [
            "Medline Industries, LP, and its subsidiaries, offer a competitive total rewards package, continuing education & training, and tremendous potential with a growing worldwide organization",
            "The Anticipated Salary Range For This Position",
            "$152,880.00 - $229,320.00 Annual",
            "The actual salary will vary based on applicant’s location, education, experience, skills, and abilities",
            "Our benefit package includes health insurance, life and disability, 401(k) contributions, paid time off, etc., for employees working 30 or more hours per week on average",
            "For roles where employees work less than 30 hours per week, benefits include 401(k) contributions as well as access to the Employee Assistance Program, Employee Resource Groups and the Employee Service Corp"
          ]
        },
        {
          "title": "Responsibilities",
          "items": [
            "This role will primarily be focused on Commercial counseling",
            "Provide guidance and counseling to colleagues across the business and functional divisions on commercial matters",
            "Negotiate and draft various contracts, whether for the purchase or sale of goods, services, or technology",
            "Manage a large volume of transactions from start to finish, working closely with commercial colleagues",
            "Work cross-functionally with various control functions to provide seamless support to the business",
            "Counsel the business and functional areas within the company regarding contracts and disputes",
            "Identify and mitigate risks, and advise company leadership on risk mitigation strategies",
            "Support company leadership on various projects, activities, and initiatives"
          ]
        }
      ],
      "extensions": [
        "18 hours ago",
        "152,880–229,320 a year",
        "Full-time",
        "Paid time off",
        "Dental insurance",
        "Health insurance"
      ],
      "detected_extensions": {
        "posted_at": "18 hours ago",
        "salary": "152,880–229,320 a year",
        "schedule": "Full-time",
        "paid_time_off": true,
        "dental_insurance": true,
        "health_insurance": true
      },
      "apply_link": "https://www.linkedin.com/jobs/view/legal-counsel-commercial-at-medline-industries-lp-4277742690?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
      "apply_links": [
        {
          "link": "https://www.linkedin.com/jobs/view/legal-counsel-commercial-at-medline-industries-lp-4277742690?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "LinkedIn"
        },
        {
          "link": "https://www.indeed.com/viewjob?jk=0ed15571900ac0b5&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Indeed"
        },
        {
          "link": "https://www.ziprecruiter.com/c/Medline/Job/Legal-Counsel-Commercial/-in-Northfield,IL?jid=c9b0ea8392ce574d&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "ZipRecruiter"
        },
        {
          "link": "https://www.glassdoor.com/job-listing/legal-counsel-commercial-medline-industries-JV_IC1158070_KO0,24_KE25,43.htm?jl=1009833947489&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Glassdoor"
        },
        {
          "link": "https://www.monster.com/job-openings/legal-counsel-commercial-northfield-il--65660f14-e1e4-4c09-a7b8-c246b035a5e7?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Monster"
        },
        {
          "link": "https://www.ajiu.live/jobdetail-legal-counsel-commercial-hybrid-job-northfield-il-medline-industries-inc?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Attorney Jobs In USA"
        },
        {
          "link": "https://www.simplyhired.com/job/pBtCOV9e1_Zidsg-nOvxiBXptz-rN7iMDQRjgGRwzb9cOM3sikjn-Q?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "SimplyHired"
        }
      ],
      "sharing_link": "https://www.google.com/search?ibp=htl;jobs&q=lawyer+&htidocid=Ql_gFuy_zo85SuuqAAAAAA%3D%3D&hl=en-US&shndl=37&shmd=H4sIAAAAAAAA_xXHQQrCMBBAUdz2CK5mKVIbFdzo0oVUqniDkqZjEpnOlEwKPYun1W4-7xffVXFo0FuCq0ysSLD7axgwuWiXuUsHija5AMJwE_GE60vIedSzMapUec02R1c5GYwwdjKbj3S6pNVgE45kM7bH036uRvbbzQN7ioxQcz9pThG1hOYFkeEpKYd3ROpLqJsfRSyulZ0AAAA&shmds=v1_AdeF8Kh8iBiyHOGFw7xv-7Ljbwu1HJiOsOq4X-RDOlSfE0o1kA&shem=sdl1pl&source=sh/x/job/li/m1/1#fpstate=tldetail&htivrt=jobs&htiq=lawyer+&htidocid=Ql_gFuy_zo85SuuqAAAAAA%3D%3D",
      "thumbnail": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIADgAOAMBEQACEQEDEQH/xAAbAAACAgMBAAAAAAAAAAAAAAAAAgUGAwQHAf/EADMQAAIBAwIEBAUACwAAAAAAAAECAwAEEQUSBiExURNBgZEVMkJxoQcUFiIjJDNSYYKi/8QAGgEAAgMBAQAAAAAAAAAAAAAAAAECBAUDBv/EACwRAAICAQIEBAUFAAAAAAAAAAABAgMRBDESIUGBE2FxkRQy4fDxBSIzocH/2gAMAwEAAhEDEQA/AKezNuPM9e9e7SPLtnm5u596eAyG5u596MBkNzdz70YDI5SURLKd3hsxVWz1IwSP+h71HKzgeHjIm5u596lgWQ3N3PvRgMg3zH70IGLQIKAMttBLdXEVvboXmlcIiD6mJwBUZyUIuUtkSjFyeEWf9INjHo1xpWjQkMLSyDO4+qR2YsfwPSqH6dY7lO59X/S2LWrh4fDWuiKnWiUwoAZvmP3oH1JKz0mOWQJd3jW7Fd2xbWWR8d8YHL1qtO9rnCOe6R2hSm8SeOxNWmi8LKivearq0qtjDQaeUBz0wTuqrPU6vOIwivWX4O8aKOrfsWLRbjgTQ9Qhnt4dTa9TJjM8LluYIyFwB0z5VTujr74NNrh8mizW9NVJNJ5F1+94I4lumvJn1UXD4TxbeJj0HIYIIoohrtNHhWMebQrXprnxPOSqXej6GzN8N1e8Y5KiObTnzkdRuXz9K0IajUL+SC7SRVlRU/lk/YgbmB7eUxv1HntZc+jAH8VdhNTWUVZRcXhm7ob2MWrRz6mf5aAmUxhSTMyjKp0+o4GTyxmuWoVjr4a93y9PM6UuKnmeyL/dcYaNPJOPiDrJdRQ2090IZA3h4zIVwuQBlgPPc5OMKDWJHQXxS/btlpcu318kaL1Vbe+/IwS8T6TLq8tymqpAkMLfqiqLtoRJjahMZG0bFGeSjJI58jXRaO5VqPBnL5/LnHXn5+onqK3LPF6bmvb6/p3w14X1qZru2t5Iba9u4ZnZ2lI8RxgMVAUBVyc8yTUpaa3xM8HJtNpNdNl/rIq6HD83NLf13Mei8Q6Pothp8Ftc7ngKO58F/wCrI2JZPl+iMFF8zuPKpX6W++cpSW+fZbLu+bFXdXXFJP8AL39iR/abh9Jr57bUAgJdYPEjuELeK3iTSbkXcCSVUdCAn+a4/B6jEeKPrt05Jc/fudPiKstp/b3OcX93LfXctxM8jM7ZHiSNIVHkNzEk4HLma3a61XFRRlzm5yyzC3zH71NEWLQIM450DOlcfX50jhLRuGomxK9vG9yB/ao6er5P+tYX6fV42onqHtl47/Q09VPw6Y1I5rW6ZYUAFADN8x+9CGxaBG7otul3q9lby4ETzoJCegTP7xP2GTXG+bhVKS3wdKo8U0mZ+JtXfXNcu9QfIWV/4an6UHJR7fnNR0tCopjD7ySvs8SxyIurBxCgAoAZgdx5edJDZ5g9qYhkZ0OUJBwRkdiMH8Gk0nuNZQuD2pgGD2oEGD2oAMHtQB//2Q=="
    },
    {
      "position": 2,
      "title": "Community Lawyer",
      "company_name": "Citizen Advocacy Center",
      "location": "Elmhurst, IL",
      "via": "via Indeed",
      "description": "Citizen Advocacy Center is seeking an action-oriented community lawyer, licensed to practice in Illinois, passionate about democracy and uprooting injustice. The ideal candidate has legal advocacy or litigation experience and desires a long-term career in public interest law. Energetic lawyers willing to employ and develop their public speaking, community organizing, advocacy, research, writing, and mentoring skills are also encouraged to apply regardless of experience. Lawyers with social media, marketing, or communications experience should highlight this on their application.\n\nThe Community Lawyer must be willing to work with a diverse group of people in a team environment and have the flexibility to adapt to changing priorities. The Community Lawyer should be comfortable speaking in a public setting and interacting with members of the community on a daily basis.\n\nCOMMUNITY LAWYER RESPONSIBILITIES INCLUDE:\n• Engaging individuals and organizations regarding matters of public concern that fit within our mission and criteria of building democracy for the 21st Century.\n• Conducting legal research and writing.\n• Organizing campaigns and planning strategies that will enable community groups to advance their cause.\n• Giving testimony or public comment at government meetings, and speaking to community groups and professional organizations.\n• Cooperating with policymakers and educators to advance civic engagement policies across a broad spectrum, including statewide civic education.\n• Executing grant-related work as developed in collaboration with the executive director.\n• Planning and executing Democracy Workshops for the public, the press, and public officials about the laws that enable and ensure citizen participation in the governmental decision-making process on matters of public significance.\n• Mentoring student interns and supervising their projects.\n• Educating the public about being active, informed, and effective community leaders through presentations, written materials, one-on-one engagement, and the media.\n• Monitoring local governments for abuses of power and undemocratic practices.\n• Holding government officials and entities accountable for anti-democratic policies that dissuade public participation.\n• Supporting litigation where appropriate or necessary to enforce and strengthen public​ policies that uphold democracy and democratic protocols.\n• Referring community members who have legal issues that are outside the scope of CAC’s service or beyond CAC’s capacity.\n• Collaborating with outside lawyers and legal professionals to ensure effective advocacy.\n\nStart date as soon as possible.\n\nCompensation: $55,000 - $60,000, depending on prior experience, with the potential to increase based on job performance and ability to contribute to the development and growth of the organization. Benefits include health insurance, flexible time off, hybrid work schedule, and participation in a profit-sharing plan when vested.\n\nTo Apply: Applications will be accepted beginning October 24, 2024 and will remain under consideration until the position is filled.\n\nCAC is an Equal Opportunity Employer that values diversity and diverse cultures, perspectives and skills, and experiences. Applicants will not be discriminated against based on race, color, creed, sex, sexual orientation, gender identity or expression, age, religion, national origin, citizenship status, disability, ancestry, marital status, veteran status, medical condition or any protected category prohibited by local, state, or federal laws.\n\nJob Type: Full-time\n\nPay: $55,000.00 - $60,000.00 per year\n\nBenefits:\n• Flexible schedule\n• Health insurance\n• Paid time off\n• Parental leave\n\nWork Location: Hybrid remote in Elmhurst, IL 60126",
      "job_highlights": [
        {
          "title": "Qualifications",
          "items": [
            "The ideal candidate has legal advocacy or litigation experience and desires a long-term career in public interest law",
            "Energetic lawyers willing to employ and develop their public speaking, community organizing, advocacy, research, writing, and mentoring skills are also encouraged to apply regardless of experience",
            "Lawyers with social media, marketing, or communications experience should highlight this on their application",
            "The Community Lawyer must be willing to work with a diverse group of people in a team environment and have the flexibility to adapt to changing priorities",
            "The Community Lawyer should be comfortable speaking in a public setting and interacting with members of the community on a daily basis"
          ]
        },
        {
          "title": "Benefits",
          "items": [
            "Compensation: $55,000 - $60,000, depending on prior experience, with the potential to increase based on job performance and ability to contribute to the development and growth of the organization",
            "Benefits include health insurance, flexible time off, hybrid work schedule, and participation in a profit-sharing plan when vested",
            "Pay: $55,000.00 - $60,000.00 per year",
            "Flexible schedule",
            "Health insurance",
            "Paid time off",
            "Parental leave"
          ]
        },
        {
          "title": "Responsibilities",
          "items": [
            "Engaging individuals and organizations regarding matters of public concern that fit within our mission and criteria of building democracy for the 21st Century",
            "Conducting legal research and writing",
            "Organizing campaigns and planning strategies that will enable community groups to advance their cause",
            "Giving testimony or public comment at government meetings, and speaking to community groups and professional organizations",
            "Cooperating with policymakers and educators to advance civic engagement policies across a broad spectrum, including statewide civic education",
            "Executing grant-related work as developed in collaboration with the executive director",
            "Planning and executing Democracy Workshops for the public, the press, and public officials about the laws that enable and ensure citizen participation in the governmental decision-making process on matters of public significance",
            "Mentoring student interns and supervising their projects",
            "Educating the public about being active, informed, and effective community leaders through presentations, written materials, one-on-one engagement, and the media",
            "Monitoring local governments for abuses of power and undemocratic practices",
            "Holding government officials and entities accountable for anti-democratic policies that dissuade public participation",
            "Supporting litigation where appropriate or necessary to enforce and strengthen public​ policies that uphold democracy and democratic protocols",
            "Referring community members who have legal issues that are outside the scope of CAC’s service or beyond CAC’s capacity",
            "Collaborating with outside lawyers and legal professionals to ensure effective advocacy"
          ]
        }
      ],
      "extensions": [
        "7 days ago",
        "55K–60K a year",
        "Full-time",
        "Dental insurance",
        "Paid time off",
        "Health insurance"
      ],
      "detected_extensions": {
        "posted_at": "7 days ago",
        "salary": "55K–60K a year",
        "schedule": "Full-time",
        "dental_insurance": true,
        "paid_time_off": true,
        "health_insurance": true
      },
      "apply_link": "https://www.indeed.com/viewjob?jk=f4ad43976623ebd5&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
      "apply_links": [
        {
          "link": "https://www.indeed.com/viewjob?jk=f4ad43976623ebd5&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Indeed"
        },
        {
          "link": "https://www.glassdoor.com/job-listing/community-lawyer-citizen-advocacy-center-JV_IC1128830_KO0,16_KE17,40.htm?jl=1009826378128&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Glassdoor"
        },
        {
          "link": "https://www.simplyhired.com/job/vGy7ks5QGy2XawzM4hOs1cArllL6yy5h_qW6e-db3KiEDbLI3b2YdQ?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "SimplyHired"
        }
      ],
      "sharing_link": "https://www.google.com/search?ibp=htl;jobs&q=lawyer+&htidocid=PQqn5iJLB3mdKbhmAAAAAA%3D%3D&hl=en-US&shndl=37&shmd=H4sIAAAAAAAA_xXNsQrCMBAAUFz7CU63FUQbEVx0kiKi9B9KGo8mktyV3FVbf8JfVpe3vuKzKMqaUxop6AyNfc2YYQM37kDQZueBCS7MfcTl0asOcjBGJFa9qNXgKsfJMGHHk3lwJ39a8TbjEK1iu9tvp2qgflXWQcMbCU73JzvrZqiR9JcFgnNMfsyia7g2X4Z-9uOSAAAA&shmds=v1_AdeF8KhlBWrCuKFbqN_0hNy1PqCYtJG7n75jzobgmbzD7nilQg&shem=sdl1pl&source=sh/x/job/li/m1/1#fpstate=tldetail&htivrt=jobs&htiq=lawyer+&htidocid=PQqn5iJLB3mdKbhmAAAAAA%3D%3D"
    },
    {
      "position": 3,
      "title": "Insurance Attorney",
      "company_name": "LHH",
      "location": "Chicago, IL",
      "via": "via LinkedIn",
      "description": "I am currently working with a reputable mid-sized law firm in Chicago, who are actively looking to hire an attorney to join their growing team.\n\nResponsibilities:\n• Handle a caseload of insurance defense matters from inception to resolution.\n• Conduct legal research and analysis on complex insurance issues.\n• Draft pleadings, motions, briefs, and other legal documents.\n• Attend court hearings, depositions, arbitrations, and mediations.\n• Communicate effectively with clients, opposing counsel, and insurance carriers.\n• Provide strategic advice and counsel to clients on legal matters.\n\nQualifications:\n• Juris Doctor (J.D.) degree from an accredited law school.\n• Admission to the Illinois state bar and in good standing.\n• Minimum of 2 years of experience practicing insurance defense law.\n• Strong litigation skills with a proven track record of success.\n• Excellent written and verbal communication skills.\n• Ability to work independently and collaboratively in a fast-paced environment.\n• Prior experience with insurance carriers and familiarity with insurance policies is preferred.\n\nBenefits:\n• Benefit offerings for full-time employment include medical, dental, vision, term life and AD&D insurance, short-term and long-term disability, additional voluntary benefits, commuter benefits, wellness plans, and a 401k plan.\n• Annual discretionary bonus based on company and individual performance.\n• Opportunities for professional development and advancement.\n• Collaborative work environment with a supportive team.\n• Hybrid working patterns.\n• Anticipated Base Pay range (dependent on experience): $150k-220k per annum\n\nEqual Opportunity Employer/Veterans/Disabled\n\nTo read our Candidate Privacy Information Statement, which explains how we will use your information, please navigate to https://www.lhh.com/us/en/candidate-privacy\n\nCandidate Privacy Information Statement - LHH\n\nWe are committed to protecting and respecting your privacy. Learn more about the Candidate Privacy Policy at LHH and how information is handled on our website.\n\nwww.lhh.com\n\nThe Company will consider qualified applicants with arrest and conviction records in accordance with federal, state, and local laws and/or security clearance requirements, including, as applicable:\n\n• The California Fair Chance Act\n\n• Los Angeles City Fair Chance Ordinance\n\n• Los Angeles County Fair Chance Ordinance for Employers\n\n• San Francisco Fair Chance Ordinance\n\nCandidate Privacy | LHH\n\nWe are committed to protecting and respecting your privacy. Learn more about the Candidate Privacy Policy at LHH and how information is handled on our website.",
      "job_highlights": [
        {
          "title": "Qualifications",
          "items": [
            "Juris Doctor (J.D.) degree from an accredited law school",
            "Admission to the Illinois state bar and in good standing",
            "Minimum of 2 years of experience practicing insurance defense law",
            "Strong litigation skills with a proven track record of success",
            "Excellent written and verbal communication skills",
            "Ability to work independently and collaboratively in a fast-paced environment"
          ]
        },
        {
          "title": "Benefits",
          "items": [
            "Benefit offerings for full-time employment include medical, dental, vision, term life and AD&D insurance, short-term and long-term disability, additional voluntary benefits, commuter benefits, wellness plans, and a 401k plan",
            "Annual discretionary bonus based on company and individual performance",
            "Opportunities for professional development and advancement",
            "Collaborative work environment with a supportive team",
            "Hybrid working patterns",
            "Anticipated Base Pay range (dependent on experience): $150k-220k per annum"
          ]
        },
        {
          "title": "Responsibilities",
          "items": [
            "Handle a caseload of insurance defense matters from inception to resolution",
            "Conduct legal research and analysis on complex insurance issues",
            "Draft pleadings, motions, briefs, and other legal documents",
            "Attend court hearings, depositions, arbitrations, and mediations",
            "Communicate effectively with clients, opposing counsel, and insurance carriers",
            "Provide strategic advice and counsel to clients on legal matters"
          ]
        }
      ],
      "extensions": [
        "1 day ago",
        "150K–220K a year",
        "Full-time",
        "Dental insurance",
        "Health insurance"
      ],
      "detected_extensions": {
        "posted_at": "1 day ago",
        "salary": "150K–220K a year",
        "schedule": "Full-time",
        "dental_insurance": true,
        "health_insurance": true
      },
      "apply_link": "https://www.linkedin.com/jobs/view/insurance-attorney-at-lhh-4279258341?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
      "apply_links": [
        {
          "link": "https://www.linkedin.com/jobs/view/insurance-attorney-at-lhh-4279258341?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "LinkedIn"
        },
        {
          "link": "https://us.trabajo.org/job-3035-1c3fdea847001c5d84f7af4bfcab37a5?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Jobs Trabajo.org"
        }
      ],
      "sharing_link": "https://www.google.com/search?ibp=htl;jobs&q=lawyer+&htidocid=gWqhGYm4QkkpHb2ZAAAAAA%3D%3D&hl=en-US&shndl=37&shmd=H4sIAAAAAAAA_xXEsQrCMBAA0L2jo9OtiiYiuOgkDrbSfyiXcCSVeBdyJ1Tw48U3vO7bbQbWd0OOBFczaUwf2MNDAihhixmE4S6SCq0v2azq2XvV4pIa2hxdlJcXpiCLf0rQf5NmbFQLGk3H02FxldN2NfY9zAy3PEdMsoNh_AH1P6dYfgAAAA&shmds=v1_AdeF8Kj7VNIztkpZyLDnemF6TTf4V08toKEsnl5O6cD9ZWsryw&shem=sdl1pl&source=sh/x/job/li/m1/1#fpstate=tldetail&htivrt=jobs&htiq=lawyer+&htidocid=gWqhGYm4QkkpHb2ZAAAAAA%3D%3D",
      "thumbnail": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIADgAOAMBEQACEQEDEQH/xAAZAAEAAwEBAAAAAAAAAAAAAAAAAwUGBwT/xAAqEAABAwMDAgUFAQAAAAAAAAABAgMEAAURBhIhBzETFEGhsjI1cXJ0Uf/EABkBAQADAQEAAAAAAAAAAAAAAAABAgMEBf/EACARAAIDAAIDAQEBAAAAAAAAAAABAgMREjEhIjIEQhP/2gAMAwEAAhEDEQA/AOcV6Z6QoBQCgFAKAUAoBQCgFAKAUAoCeAwJc+LGUopD76GiodxuUBn3qG8WkN4tNL1D0izpCZCYYmOyRJbUsqcSE7cED0/NUqsc0yldjmT9P9FMasi3F5+a9GMQpADaAd2QTzn8VFlrg0sIsscGkVugdOtarvRt78lyMnyynt7aQTkFIxz+1WsnwWlrJ8FqNFF6cxX4Go5JuT4NokPNISG04cCGwsE/5nOKzdzWeOzN3NZ47Kfp5pJnV82ZHfluxhHaS4FNpCs5JHrV7bOC0vbPgjNz44iXCVGSoqDD62go9yEqIz7Vonq00T1aTWP75bf7Gfmmol0yJfLOidevu1o/nd+Saw/N0zD8/TPb0I2+Qvu/6d7WfxtVVf09or+jtFpoCRoJ29lOlIj7U7y6juX4uPDynP1KI77ararePuRYrM9iw04YyYmtTPSVRBdJJfSM5KPCRu7c9s1We+uFZfzhD06f0W9NmDSMV5l8NJ8YueJynPH1k+tTarEvcm1WL6OIXz75c/7HvmquyPyjrj8ohgSBEuEWSpJUGH0OlI7naoHHtUtasJflYdQn9UtPXJaF3HSYlqQCEKkJacKQfQZHFcyokupHOqJLqRXWTqLbLPcby/Fsi2o1wU2Wo7JQgNbUbTwOOTzxVpUyklrJlU2lrM1oHUTWlL0bg/Gckp8spnY2oA5JSc8/rWlkOaw0sjzWGii9RorEDUcY218m7yHnUKDicNBbYQAf9xjPFZul6vPRn/k2156Kfp5q1nSE2ZIfiOyRIaS2EtqCduDnPNXtrc0kXshz8GbnyBLuEqSlJSH31uhJ7jconHvWiWLDRLFhBQCgFAKAUAoBQCgFAKAUAoBQCgP/2Q=="
    },
    {
      "position": 4,
      "title": "Attorney/Lawyer",
      "company_name": "Stange Law Firm",
      "location": "Rolling Meadows, IL",
      "via": "via Monster",
      "description": "Are you a legal professional with a passion for Family Law? Stange Law Firm is accepting resumes only for dynamic, highly motivated attorneys to join the team that provides strategic legal support and guidance for their office in Rolling Meadows, IL, in the Chicago Area in Cook County.\n\nWhether someone is facing a divorce, legal separation, paternity action, estate planning or numerous other issues that affect families, the attorneys at Stange Law Firm, PC are dedicated to achieving the best possible results.\n\nWhy join Stange Law Firm?\n• Competitive Pay! (Salary is BOE: $85,000.00-$115,000.00+)\n• Base Salary & Bonus/Incentive Programs!\n• Signing Bonus\n• Attorney Referral Bonuses\n• Client Referral Bonuses\n• Productivity Bonuses\n• 401 (k)\n• 401 (k) matching\n• Roth IRA\n• 99% Employer Paid Health Insurance for Employees!\n• Dental Insurance\n• Vision Insurance\n• Paid Time Off (Accrued Vacation, 5 Paid Sick Days & 3 Personal Days)\n• 9 Paid Holidays\n• Take Birthday as Paid Leave\n• 36 Work-From-Home Days\n• Company paid laptop and cell phone\n• Fast-growing Family Law Firm - 2nd Largest Family Law Firm in the country!\n• Marketing team works hard for you! Lots of Clients!!\n• Advancement and job growth potential\n• Mentorship program\n• Promotes from within\n• Trial experience, not just paper pushing!\n• Excellent Reputation\n• More!\n\nThis position offers a competitive starting salary, outstanding benefits package, employer-matched 401K after 90 days, potential for incentives/bonus pay on top of base salary based on productivity, malpractice insurance, employer-paid Bar and CLE dues, paid time off, free parking (where applicable), and free company cell phone and laptop. Eligible employees may elect insurance coverage for Accidental, Critical Illness, Short Term Disability, and Term to Age 100 Life.\n• Salary ranges based on experience plus the opportunity for discretionary bonuses and other incentives.*\n\nJob Description\nDuties include but are not limited to the following:\n• Prepares and drafts legal documents for filing with appropriate entities and necessary correspondence\n• Drafts pleadings and motions, including judgments and orders\n• Corresponds with attorneys, court personnel, and clients regarding cases\n• Interviews witnesses for court cases and prepares witnesses to testify\n• Shall ensure the accuracy of all documents prepared\n• Shall promptly appear in court on all cases assigned\n• Shall handle all aspects of cases assigned to them\n• Performs administrative duties as necessary, including filing, mailing, organizing files and pleadings\n• Conducts legal research for particular issues\n\nQualifications\nOur Ideal Candidate will possess the following:\n• J.D\n• Illinois license required\n• Family law experience is preferred but not required\n• Senior Associate positions are available for attorneys with five years or more of litigation experience\n\nCompany Description\n\nStange Law Firm, PC is a multi-state family law firm. LawFirm500 ranks Stange Law Firm as one of the fastest-growing law firms in the country. Attorneys at the firm have received awards from organizations such as Super Lawyers, the National Trial Lawyers, the National Academy of Family Lawyers and many more. Attorneys at the firm also speak at Continuing Legal Education Seminars for organizations such as the Missouri Bar, National Business Institute, MyLawCLE, and many more. This is truly a great opportunity if you want a successful career in family law.\n\nFor more information, please visit www.stangelawfirm.com. E-mail resume and references to the Recruiting Director. Watch the following video to learn more about starting a career with Stange Law Firm: https://www.youtube.com/watch?v=PJMiDiwD-8E\n\nAdditional information\nAll your information will be kept confidential according to EEO guidelines.\n\nThe choice of a lawyer is an important decision that should not be based solely upon advertisements.\n\nAbout the Company:\nStange Law Firm",
      "job_highlights": [
        {
          "title": "Qualifications",
          "items": [
            "Excellent Reputation",
            "Illinois license required",
            "Senior Associate positions are available for attorneys with five years or more of litigation experience"
          ]
        },
        {
          "title": "Benefits",
          "items": [
            "Competitive Pay!",
            "(Salary is BOE: $85,000.00-$115,000.00+)",
            "Base Salary & Bonus/Incentive Programs!",
            "Signing Bonus",
            "Attorney Referral Bonuses",
            "Client Referral Bonuses",
            "Productivity Bonuses",
            "401 (k)",
            "401 (k) matching",
            "Roth IRA",
            "99% Employer Paid Health Insurance for Employees!",
            "Dental Insurance",
            "Vision Insurance",
            "Paid Time Off (Accrued Vacation, 5 Paid Sick Days & 3 Personal Days)",
            "9 Paid Holidays",
            "Take Birthday as Paid Leave",
            "36 Work-From-Home Days",
            "Company paid laptop and cell phone",
            "Lots of Clients!!",
            "Advancement and job growth potential",
            "Mentorship program",
            "Promotes from within",
            "Trial experience, not just paper pushing!",
            "This position offers a competitive starting salary, outstanding benefits package, employer-matched 401K after 90 days, potential for incentives/bonus pay on top of base salary based on productivity, malpractice insurance, employer-paid Bar and CLE dues, paid time off, free parking (where applicable), and free company cell phone and laptop",
            "Eligible employees may elect insurance coverage for Accidental, Critical Illness, Short Term Disability, and Term to Age 100 Life",
            "Salary ranges based on experience plus the opportunity for discretionary bonuses and other incentives.*"
          ]
        },
        {
          "title": "Responsibilities",
          "items": [
            "Prepares and drafts legal documents for filing with appropriate entities and necessary correspondence",
            "Drafts pleadings and motions, including judgments and orders",
            "Corresponds with attorneys, court personnel, and clients regarding cases",
            "Interviews witnesses for court cases and prepares witnesses to testify",
            "Shall ensure the accuracy of all documents prepared",
            "Shall promptly appear in court on all cases assigned",
            "Shall handle all aspects of cases assigned to them",
            "Performs administrative duties as necessary, including filing, mailing, organizing files and pleadings",
            "Conducts legal research for particular issues"
          ]
        }
      ],
      "extensions": [
        "Full-time",
        "Health insurance",
        "Dental insurance",
        "Paid time off"
      ],
      "detected_extensions": {
        "schedule": "Full-time",
        "health_insurance": true,
        "dental_insurance": true,
        "paid_time_off": true
      },
      "apply_link": "https://www.monster.com/job-openings/attorney-lawyer-rolling-meadows-il--c95e2e9b-3887-40dd-a308-90e2d9e4cd31?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
      "apply_links": [
        {
          "link": "https://www.monster.com/job-openings/attorney-lawyer-rolling-meadows-il--c95e2e9b-3887-40dd-a308-90e2d9e4cd31?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Monster"
        },
        {
          "link": "https://www.glassdoor.com/job-listing/attorney-lawyer-stange-law-firm-JV_IC1128962_KO0,15_KE16,31.htm?jl=1009790029338&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Glassdoor"
        },
        {
          "link": "https://www.simplyhired.com/job/Upn9M2P3Np71NFmppeI59yVT-RZ9Z4OKJyZAt60QILm74xxoh9D8gw?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "SimplyHired"
        }
      ],
      "sharing_link": "https://www.google.com/search?ibp=htl;jobs&q=lawyer+&htidocid=ObOGWxpLxTw_xIQMAAAAAA%3D%3D&hl=en-US&shndl=37&shmd=H4sIAAAAAAAA_xXNsQrCQAwAUFz7CU6ZOoj2RHDRyUVR6qIfUNIarifX5LgE2n6E_6wub33FZ1GUJzPJTLOrcZwpwwZu0oIS5q4HYbiI-EjLY2-W9OCcaqy8Glroqk4GJ0ytTO4trf5ptMdMKaJRs9tvpyqxX5VPQ_YEvwLOIQ8QGB4SY2APd8KXjLqGa_0FW3Kp2ZAAAAA&shmds=v1_AdeF8KiIo7OQXMcQW0Mhes4H-2fNDyyNNavsmZdmruMuWsbbuw&shem=sdl1pl&source=sh/x/job/li/m1/1#fpstate=tldetail&htivrt=jobs&htiq=lawyer+&htidocid=ObOGWxpLxTw_xIQMAAAAAA%3D%3D"
    },
    {
      "position": 5,
      "title": "Attorney",
      "company_name": "Avata Partners",
      "location": "Mundelein, IL",
      "via": "via ZipRecruiter",
      "description": "A top law firm in the San Francisco Bay Area seeks an experienced attorney to join its dynamic team. The right candidate will have a strong civil litigation background, a passion for representing individuals, and a desire to take on leadership responsibilities in the future.\n\nResponsibilities:\n• Handle all phases of litigation: discovery, motion practice, depositions, settlement, and trial\n• Appear in court for hearings, case management conferences, and trials\n• Participate in strategy and case planning\n\nQualifications:\n• At least 5 years of experience in plaintiff-side civil litigation and first-chair trial work\n• In Good standing with the CA Bar",
      "job_highlights": [
        {
          "title": "Qualifications",
          "items": [
            "The right candidate will have a strong civil litigation background, a passion for representing individuals, and a desire to take on leadership responsibilities in the future",
            "At least 5 years of experience in plaintiff-side civil litigation and first-chair trial work",
            "In Good standing with the CA Bar"
          ]
        },
        {
          "title": "Responsibilities",
          "items": [
            "Handle all phases of litigation: discovery, motion practice, depositions, settlement, and trial",
            "Appear in court for hearings, case management conferences, and trials",
            "Participate in strategy and case planning"
          ]
        }
      ],
      "extensions": [
        "1 day ago",
        "Full-time"
      ],
      "detected_extensions": {
        "posted_at": "1 day ago",
        "schedule": "Full-time"
      },
      "apply_link": "https://www.ziprecruiter.com/c/Avata-Partners/Job/Attorney/-in-Mundelein,IL?jid=5922333a45afcb1b&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
      "apply_links": [
        {
          "link": "https://www.ziprecruiter.com/c/Avata-Partners/Job/Attorney/-in-Mundelein,IL?jid=5922333a45afcb1b&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "ZipRecruiter"
        },
        {
          "link": "https://www.jobilize.com/amp/job/us-il-mundelein-attorney-jobot-hiring-now-job-immediately-opening?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Jobilize"
        }
      ],
      "sharing_link": "https://www.google.com/search?ibp=htl;jobs&q=lawyer+&htidocid=o0Zgmi6j7U_SrvTKAAAAAA%3D%3D&hl=en-US&shndl=37&shmd=H4sIAAAAAAAA_xXEsQoCMQwA0P0-weUyi7YiuOh0kygK_sGR1tCe1KQ0Uc7JXxff8Lpv1w9m0pg-sIazBFDCFjMIw1EkFVocslnVvfeqxSU1tCm6KE8vTEFm_5Cg_0bN2KgWNBq3u83sKqdlP7zREG7YjKkpTAzXF9-p0MQrOF1-QLFlrIEAAAA&shmds=v1_AdeF8Khql1TISeAi6uFyW54hFSfyf5XwzIWca2hp4D_YHWLzdA&shem=sdl1pl&source=sh/x/job/li/m1/1#fpstate=tldetail&htivrt=jobs&htiq=lawyer+&htidocid=o0Zgmi6j7U_SrvTKAAAAAA%3D%3D",
      "thumbnail": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIADgAOAMBIgACEQEDEQH/xAAZAAEBAQEBAQAAAAAAAAAAAAAABQQGAwH/xAAsEAABBAECBAQGAwAAAAAAAAABAAIDBBEFIQYSMUEyUYHwEyJhcZHBUqGx/8QAGAEBAQEBAQAAAAAAAAAAAAAAAAMCBQH/xAAbEQEBAQEAAwEAAAAAAAAAAAAAARECITFBA//aAAwDAQACEQMRAD8AxIiLrNCItsdQSaa+ww5kY/cDsPe6W4MSIiAiIgIiIN+g6a/VtWr02eF7syHyYNyfx/aoyVm6TxBd0xxDoi4hm+dju0H64OCr3AdWPS9Gua/aaTzMc2MDqWNO+Pu4Y9FxFiWzNaktzB4lfIZHO5cfMTn/AFRnV67s+QfLkBrWXxHoDsfMdl4qvqrW2qkV2MdsO+nsqQq83YCIi9BadNpS6jfgpweOZ4aD5DufQZPosyq8OawzRLzrZqNsSchazmk5eTPU9D9vys9bnj2O44i4jbwuKem6fBHKWQjIeT8jRs3p3OCoF7jy1epzVZ6FYxzMLHYc7O65vVb8uqajPdn2fM7PL/EdAPQYCyqXH4cyTZ5MVdFkbJHNTk8LgSP2ps8ToJnxP6tOF9rzOgmZK3q05x5r0vWRbm+L8MMdjB3zlVyyjOiItAiIgIiICIiAiIg//9k="
    },
    {
      "position": 6,
      "title": "Supply Chain/Transportation Lawyer",
      "company_name": "Axiom",
      "location": "Chicago, IL",
      "via": "via Axiom Law",
      "description": "We are currently seeking Supply Chain/Transportation Lawyers to work full-time with our clients at some of the world’s largest automotive, retail, technology, consumer goods, and professional services companies. Ideal candidates will have a strong background in supply chain and transportation law, with expertise in advising clients on legal matters related to procurement, distribution, transportation, and risk management within the movement of goods and materials.\n\nResponsibilities:\n• Provide legal counsel and support to clients on supply chain and transportation contracts, including drafting and negotiating agreements for procurement, transportation services, logistics, warehousing, and distribution.\n• Advise clients on regulatory compliance matters related to transportation and logistics, including federal transportation regulations, import/export controls, environmental regulations, customs laws, and international trade regulations.\n• Assist clients in mitigating supply chain risks, including supplier disputes, product recalls, supply disruptions, and compliance with ethical sourcing standards.\n\nQualifications:\n• Active bar license in the state in which you reside.\n• Minimum of 3+ years of experience practicing law, with a focus on supply chain, transportation, procurement, or logistics law, preferably in a law firm or corporate legal department setting. Specific experience with electric vehicles is a plus.\n• Strong knowledge of U.S., transportation laws and regulations, and international laws and regulations relevant to supply chain management, including the Uniform Commercial Code (UCC), Incoterms, and the Foreign Corrupt Practices Act (FCPA).\n• Experience drafting, reviewing, and negotiating a wide variety of commercial agreements related to supply chain processes, including vendor, supplier, distribution, and service agreements.\n\nPreferred Qualifications (not required but considered advantageous):\n• Familiarity with emerging trends and technologies in supply chain and transportation, such as blockchain and e-commerce logistics, and specifically within the electric vehicle sector, such as battery technology, charging infrastructure, autonomous driving technology, federal motor vehicle safety standards (FMVSS), emissions regulations, and environmental requirements.\n• Experience advising clients on supply chain optimization strategies, including contract management, supplier relationship management, product liability, warranty claims, regulatory compliance audits, and inventory management.\n• Excellent communication, negotiation, and problem-solving skills, with the ability to effectively advise clients and collaborate with cross-functional teams.\n\nCompensation, Benefits & Location: ​\n\nThis role offers a range of competitive compensation starting at $130,000 and a highly competitive benefits package in the alternative legal services marketplace that includes health benefits, 401K and more.\n\nAxiom is the global leader in high-caliber, on-demand legal talent. Covering North America, the UK, Europe, Australia and APAC, we enable legal departments to drive efficiency and growth and meet the demands of today’s business landscape with best in breed alterative legal services.\n\nAxiom is a leader in diversity, inclusion, and social engagement. Diversity is core to our values and we are proud to be an equal opportunity employer. We are proud to be named a best place to work for LGBTQ+ Equality, earning top marks in the 2021 Corporate Equality Index for the second consecutive year. Axiom’s legal department is Mansfield certified and is committed to considering at least 50% diverse candidates for leadership roles and outside counsel representation.\n\nPursuant to the San Francisco Fair Chance Ordinance, we will consider for employment qualified applicants with arrest and conviction records.\n\nLearn more about working at Axiom.\n\nEqual Opportunity Employer: Axiom ensures equal employment opportunity in recruitment and employment, without discrimination or harassment on the basis of race, color, nationality, national or ethnic origin, religious creed or belief, political opinion, sex, gender reassignment, pregnancy or maternity, age, disability, alienage or citizenship status, marital (or civil or other partnership recognized by law) status, genetic predisposition or carrier status, sexual orientation, military service, or any other characteristic protected by applicable law. Axiom prohibits and will not tolerate any such discrimination or harassment.\n\nAccommodation for Individuals with Disabilities: Upon request and consistent with applicable laws, Axiom will provide reasonable accommodations for individuals with disabilities who require an accommodation to participate in each stage of the recruitment process. To request an accommodation to complete the application form, please contact us at benefits@axiomlaw.com and include “Applicant Accommodation” in the subject line.\n\nAxiom respects your privacy. For an explanation of the kind of information we collect about you and how it is used, our full privacy notice is available at https://www.axiomlaw.com/privacy-notice.\n\nEmployment with Axiom may be contingent upon successful completion of a background check, providing proof of identity, and possessing the necessary legal authorization to work.\n\nBy submitting an application, you acknowledge that all information contained therein, and provided at any part of the application process, is correct and accurate to the best of your knowledge.\n\n#LI-LC3",
      "job_highlights": [
        {
          "title": "Qualifications",
          "items": [
            "Active bar license in the state in which you reside",
            "Minimum of 3+ years of experience practicing law, with a focus on supply chain, transportation, procurement, or logistics law, preferably in a law firm or corporate legal department setting",
            "Strong knowledge of U.S., transportation laws and regulations, and international laws and regulations relevant to supply chain management, including the Uniform Commercial Code (UCC), Incoterms, and the Foreign Corrupt Practices Act (FCPA)",
            "Experience drafting, reviewing, and negotiating a wide variety of commercial agreements related to supply chain processes, including vendor, supplier, distribution, and service agreements",
            "By submitting an application, you acknowledge that all information contained therein, and provided at any part of the application process, is correct and accurate to the best of your knowledge"
          ]
        },
        {
          "title": "Benefits",
          "items": [
            "Compensation, Benefits & Location: ​",
            "This role offers a range of competitive compensation starting at $130,000 and a highly competitive benefits package in the alternative legal services marketplace that includes health benefits, 401K and more"
          ]
        },
        {
          "title": "Responsibilities",
          "items": [
            "Provide legal counsel and support to clients on supply chain and transportation contracts, including drafting and negotiating agreements for procurement, transportation services, logistics, warehousing, and distribution",
            "Advise clients on regulatory compliance matters related to transportation and logistics, including federal transportation regulations, import/export controls, environmental regulations, customs laws, and international trade regulations",
            "Assist clients in mitigating supply chain risks, including supplier disputes, product recalls, supply disruptions, and compliance with ethical sourcing standards"
          ]
        }
      ],
      "extensions": [
        "Full-time",
        "Health insurance"
      ],
      "detected_extensions": {
        "schedule": "Full-time",
        "health_insurance": true
      },
      "apply_link": "https://www.axiomlaw.com/careers/lawyers/available-positions/7895746002?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
      "apply_links": [
        {
          "link": "https://www.axiomlaw.com/careers/lawyers/available-positions/7895746002?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Axiom Law"
        },
        {
          "link": "https://boards.greenhouse.io/embed/job_app?for=axiomtalentplatform&token=7895746002&utm_id=2349686&utm_source=Legal+Services+Jobs&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Greenhouse"
        },
        {
          "link": "https://www.indeed.com/viewjob?jk=731663cef2c2113c&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Indeed"
        },
        {
          "link": "https://www.goinhouse.com/jobs/416835885-supply-chain-transportation-lawyer-at-axiom?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "GoInhouse.com"
        },
        {
          "link": "https://www.glassdoor.com/job-listing/supply-chain-transportation-lawyer-axiom-law-JV_IC1128808_KO0,34_KE35,44.htm?jl=1009768022914&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Glassdoor"
        },
        {
          "link": "https://engage.firmprospects.com/public/jobs/wB8EjR8D/e-discovery-lawyer?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Firm Prospects"
        },
        {
          "link": "https://us.bebee.com/job/c9da6e2fdd30eecbab1b23d6d7c55b69?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "BeBee"
        },
        {
          "link": "https://talents.vaia.com/companies/jobleads-us/lawyer-list-d-10454407/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Talents By Vaia"
        }
      ],
      "sharing_link": "https://www.google.com/search?ibp=htl;jobs&q=lawyer+&htidocid=ekLZzNSFyDRaVqfzAAAAAA%3D%3D&hl=en-US&shndl=37&shmd=H4sIAAAAAAAA_xWNsQrCMBBAce3s5HSzaCKCgzqJgyjddC_XEJJIehdyEdOf8Jttlzc8eLzmt2iOz09KcYSrx0D6lZEkcS5YAhO0-B1thi08uAexmI2HSd-YXbSrsy8lyUlrkaiczI1RhgfNZHuu-s29zOjEY7YpYrHd_rCrKpFbLy818ACBpnMw6HgD9_YPHNVaFZEAAAA&shmds=v1_AdeF8Ki1wP6sfRO8R-pDqMDC529lo4GNJm8sKQNopVq5YK7CJw&shem=sdl1pl&source=sh/x/job/li/m1/1#fpstate=tldetail&htivrt=jobs&htiq=lawyer+&htidocid=ekLZzNSFyDRaVqfzAAAAAA%3D%3D"
    },
    {
      "position": 7,
      "title": "Family Lawyer - Litigation",
      "company_name": "January Family Law, LLC",
      "location": "Chicago, IL",
      "via": "via Indeed",
      "description": "Our growing law firm is looking to hire a family attorney who is fiercely passionate about representing clients facing one of the most challenging times in their lives. Candidates should have courtroom experience. Candidates should be adept at preparing necessary legal documents in connection with prenuptial agreements, initiating and finalizing divorces, maintenance, child support/child custody, and real estate. Experience in handling legal issues such as child abuse, child custody, and domestic violence is also a must. If you have a proven record of success both in and out of court, apply now!\n\nIncentive/bonus plan & great benefits (401k match, medical, dental, vision).\nCompensation:\n\n$120,000+\nResponsibilities:\n• Organize and maintain client files to ensure they are kept current\n• Create legal documents such as pleadings, motions, marital settlement agreements, contracts, judgements and orders for a high volume of cases\n• Help solve legal problems for clients through analyzing the situation, understanding their needs, and creating a strategic plan of action\n• Attend court proceedings as needed to represent clients\n• Manage the division of marital assets, including real estate, during divorce proceedings when needed\n\nManage your caseload from start to finish with dedicated mentorship from experienced attorney\nQualifications:\n• Undergraduate degree with a legal background and Juris Doctor degree required\n• Extra consideration for those with a criminal justice background\n• Candidates should be great negotiators and communicators, specifically in situations when emotions and stress are high\n• Strong knowledge base of representing petitioners and respondents\n• Must have worked on family law issues, with at least 4 years of legal experience\n\nAbout Company\n\nWe are a small family law firm focused on providing excellent services to individuals going through one of the toughest times of their lives. We primarily work remotely but have an upbeat team atmosphere.",
      "job_highlights": [
        {
          "title": "Qualifications",
          "items": [
            "Candidates should have courtroom experience",
            "Candidates should be adept at preparing necessary legal documents in connection with prenuptial agreements, initiating and finalizing divorces, maintenance, child support/child custody, and real estate",
            "Experience in handling legal issues such as child abuse, child custody, and domestic violence is also a must",
            "If you have a proven record of success both in and out of court, apply now!",
            "Undergraduate degree with a legal background and Juris Doctor degree required",
            "Extra consideration for those with a criminal justice background",
            "Candidates should be great negotiators and communicators, specifically in situations when emotions and stress are high",
            "Strong knowledge base of representing petitioners and respondents",
            "Must have worked on family law issues, with at least 4 years of legal experience"
          ]
        },
        {
          "title": "Benefits",
          "items": [
            "Incentive/bonus plan & great benefits (401k match, medical, dental, vision)",
            "$120,000+"
          ]
        },
        {
          "title": "Responsibilities",
          "items": [
            "Organize and maintain client files to ensure they are kept current",
            "Create legal documents such as pleadings, motions, marital settlement agreements, contracts, judgements and orders for a high volume of cases",
            "Help solve legal problems for clients through analyzing the situation, understanding their needs, and creating a strategic plan of action",
            "Attend court proceedings as needed to represent clients",
            "Manage the division of marital assets, including real estate, during divorce proceedings when needed",
            "Manage your caseload from start to finish with dedicated mentorship from experienced attorney"
          ]
        }
      ],
      "extensions": [
        "Full-time",
        "Dental insurance",
        "Health insurance"
      ],
      "detected_extensions": {
        "schedule": "Full-time",
        "dental_insurance": true,
        "health_insurance": true
      },
      "apply_link": "https://www.indeed.com/viewjob?jk=3994b3709fcea915&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
      "apply_links": [
        {
          "link": "https://www.indeed.com/viewjob?jk=3994b3709fcea915&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Indeed"
        },
        {
          "link": "https://www.monster.com/job-openings/family-lawyer-litigation-chicago-il--375662c2-7ab2-4d14-b5f7-558bf0e1afa0?mstr_dist=true&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Monster"
        },
        {
          "link": "https://www.ziprecruiter.com/c/January-Family-Law,-LLC/Job/Family-Lawyer-Litigation/-in-Chicago,IL?jid=76a5a23e85217fd8&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "ZipRecruiter"
        },
        {
          "link": "https://jobs.wizehire.com/job/family-lawyer-litigation-in-chicago-il-us-532136?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Recommended Jobs For You - Wizehire"
        },
        {
          "link": "https://www.linkedin.com/jobs/view/family-lawyer-litigation-at-wizehire-4254632321?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "LinkedIn"
        },
        {
          "link": "https://www.ajiu.live/jobdetail-family-lawyer-litigation-job-chicago-il-january-family-law-llc?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Attorney Jobs In USA"
        },
        {
          "link": "https://www.glassdoor.com/job-listing/family-lawyer-litigation-january-advisors-JV_IC1128808_KO0,24_KE25,41.htm?jl=1009787170262&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Glassdoor"
        },
        {
          "link": "https://www.theladders.com/job/family-lawyer-litigation-january-family-law-llc-chicago-il_82044543?ir=1&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Ladders"
        }
      ],
      "sharing_link": "https://www.google.com/search?ibp=htl;jobs&q=lawyer+&htidocid=MxN5hRMjkOGCGH5tAAAAAA%3D%3D&hl=en-US&shndl=37&shmd=H4sIAAAAAAAA_0WNQQrCMBAA8doneNqTB6mNCl7ssaBY8oeyCSGJpNmQjdj-xOcaT14GBgam-Wya0w1nH1aQ-F5NhgNIX7zF4ilWGUkBG8zaQfU7kQ1m27tSEl-FYA6d5VJj3WmaBUWjaBFPUvzDxA6zSQGLmc6X49KlaPe7EeML8wr_bwtSDuAjDM5rtNTCQ34BzeXIj5sAAAA&shmds=v1_AdeF8KhNVw82VlCvnWAF6W8YDVPZHcNG6rSIDpvYYqDI-1sItQ&shem=sdl1pl&source=sh/x/job/li/m1/1#fpstate=tldetail&htivrt=jobs&htiq=lawyer+&htidocid=MxN5hRMjkOGCGH5tAAAAAA%3D%3D"
    },
    {
      "position": 8,
      "title": "Attorney/Lawyer",
      "company_name": "Robert Half",
      "location": "Chicago, IL",
      "via": "via Robert Half",
      "description": "Robert Half is seeking an Attorney to join a national firm, based in Chicago, Illinois. You will be providing legal expertise particularly in the areas of insurance coverage and insurance defense. You will be handling case management, drafting motions and discovery requests, defending depositions, and participating in court proceedings. You will also play a crucial role in maintaining the firm's relationship with existing clients.Responsibilities:Manage overall case progression, ensuring efficient and effective handling of legal matters.Draft legal documents and motions, ensuring their accuracy and comprehensiveness.Handle discovery requests, meticulously reviewing and responding to each request.Defend depositions, using your legal expertise to protect the interests of the client.Participate in court proceedings, representing the firm and its clients in various legal matters.Maintain strong relationships with the firm's existing client base, ensuring their needs are met and concerns addressed.Conduct thorough and detailed legal research to support case development.Present findings and legal strategies in a clear and concise manner.",
      "job_highlights": [
        {
          "title": "Qualifications",
          "items": [
            "Present findings and legal strategies in a clear and concise manner"
          ]
        },
        {
          "title": "Responsibilities",
          "items": [
            "You will be providing legal expertise particularly in the areas of insurance coverage and insurance defense",
            "You will be handling case management, drafting motions and discovery requests, defending depositions, and participating in court proceedings",
            "You will also play a crucial role in maintaining the firm's relationship with existing clients.Responsibilities:Manage overall case progression, ensuring efficient and effective handling of legal matters",
            "Draft legal documents and motions, ensuring their accuracy and comprehensiveness",
            "Handle discovery requests, meticulously reviewing and responding to each request",
            "Defend depositions, using your legal expertise to protect the interests of the client",
            "Participate in court proceedings, representing the firm and its clients in various legal matters",
            "Maintain strong relationships with the firm's existing client base, ensuring their needs are met and concerns addressed",
            "Conduct thorough and detailed legal research to support case development"
          ]
        }
      ],
      "extensions": [
        "15 days ago",
        "110K–145K a year",
        "Full-time"
      ],
      "detected_extensions": {
        "posted_at": "15 days ago",
        "salary": "110K–145K a year",
        "schedule": "Full-time"
      },
      "apply_link": "https://www.roberthalf.com/us/en/job/chicago-il/attorneylawyer/01300-0013151508-usen?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
      "apply_links": [
        {
          "link": "https://www.roberthalf.com/us/en/job/chicago-il/attorneylawyer/01300-0013151508-usen?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Robert Half"
        },
        {
          "link": "https://www.ziprecruiter.com/c/Robert-Half/Job/Attorney-Lawyer/-in-Chicago,IL?jid=80801743783988fa&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "ZipRecruiter"
        },
        {
          "link": "https://www.linkedin.com/jobs/view/attorney-lawyer-at-robert-half-4275615832?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "LinkedIn"
        },
        {
          "link": "https://jooble.org/jdp/1748354800989436081?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Jooble"
        },
        {
          "link": "https://www.tealhq.com/job/attorney-lawyer_112fb3e3-b26c-4c7d-96b7-4149b5466906?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Teal"
        },
        {
          "link": "https://www.theladders.com/job-listing/2203162327460625965/attorney-lawyer.htm?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Ladders"
        },
        {
          "link": "https://www.jobget.com/jobs/job/8e90afd1-f1e7-46b5-8af7-a9fcf6464ccb?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "JobGet"
        },
        {
          "link": "https://www.career.com/job/robert-half/attorney-lawyer/j202203251229256827526?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Career.com"
        }
      ],
      "sharing_link": "https://www.google.com/search?ibp=htl;jobs&q=lawyer+&htidocid=RiU1HHVlVHmX44YuAAAAAA%3D%3D&hl=en-US&shndl=37&shmd=H4sIAAAAAAAA_xXEOwoCMRAAUGz3CFtNZSGaiGCjlVj4YSsvsEzCmERiJmQG3C29ufiK130X3fKkyq3QbAf8zNRgA3d2IITNR-ACF-aQqT9G1SoHa0WyCaKoyRvPb8uFHE_2xU7-jRKxUc2oNO7228nUElb9gx01hSvmJ6QC55g8Bl7DbfgBB0A9KoQAAAA&shmds=v1_AdeF8KiJ5nuuH6KUEFeTTaEZYtpHOecibvc0LWlAkAUaaKSTFw&shem=sdl1pl&source=sh/x/job/li/m1/1#fpstate=tldetail&htivrt=jobs&htiq=lawyer+&htidocid=RiU1HHVlVHmX44YuAAAAAA%3D%3D"
    },
    {
      "position": 9,
      "title": "Joerika Stitt Esquire, LLC – Associate Attorney (Domestic Relations & Probate)",
      "company_name": "Black Women Lawyers’ Association of Greater Chicago, Inc.",
      "location": "Olympia Fields, IL",
      "via": "via Black Women Lawyers' Association Of Greater Chicago, Inc.",
      "description": "Company Intro\n\nWhere Your Impact Drives Our GrowthAre you a sharp, seasoned litigator who thrives under pressure, consistently delivers exceptional results, and is ready for your performance to be directly tied to significant rewards and a clear path to partnership?\n\nThis isn't just another attorney position; it's an opportunity to join a fast-growing, impact-driven law firm where your expertise in domestic relations (divorce, custody, and orders of protection) and probate law will immediately make a difference. We’re building something special, and we're looking for a driven Associate Attorney to not just manage cases, but to lead, innovate, and grow with us.\n\nIf you pride yourself on courtroom dominance, precision drafting, and a natural ability to generate revenue, you're exactly who we're looking for. We offer the autonomy, authority, and support you need to elevate your career. Our firm is committed to empowering our attorneys to be true leaders, ensuring your expertise is central to our clients' success and our firm's expansion. We understand the demands of high-stakes legal work, which is why we’ve built a benefits package and firm culture that prioritize both professional excellence and personal well-being.\n\nJob Description/Duties\n\nLead, Win, DeliverAt our firm, we empower our attorneys to be true leaders. You won't just be handling cases; you'll be shaping outcomes and driving the firm's success. Your responsibilities will include:\n\nLead a Dynamic Caseload: Take charge of 50–55 active cases, a strategic blend of contested and uncontested divorces, complex custody disputes, orders of protection, and probate matters. We intentionally balance complexity to ensure you're always challenged, engaged, and operating at peak efficiency.\n\nTrue Autonomy & Authority: We trust you to lead client strategy, master court appearances, and dominate mediations and high-stakes negotiations. Your legal acumen will be central to our clients' success.\n\nMasterful Legal Craft: Draft compelling pleadings, motions, settlement agreements, and litigation documents. Your precision and persuasive writing will be critical to our wins.\n\nDirect Impact on Firm Growth: Contribute directly to our firm's expansion by maintaining a minimum of 1,800 billable hours annually through focused, high-quality output.\n\nEmpathetic Advocacy: Communicate with clarity and empathy, consistently delivering tangible results and building lasting client relationships.\n\nLeverage Modern Solutions: Utilize our cutting-edge firm technology and streamlined systems to efficiently manage tasks, track time, and collaborate seamlessly with our supportive team.\n\nJob Criteria\n\nExperience, Excellence, and HustleWe seek attorneys who are ready to make a significant impact from day one. To thrive in this role, you should possess:\n\nJ.D. from an accredited law school and an active Illinois law license in good standing.\n\nA minimum of 3 years of recent, hands-on experience in family law (domestic relations) is mandatory.\n\nExperience in probate litigation is strongly preferred.\n\nA demonstrated ability to independently manage complex, high-volume caseloads from start to finish.\n\nExceptional courtroom presence, persuasive legal writing, and clear, professional client communication skills.\n\nOrganizational mastery, tech fluency, and an outcome-obsessed mindset.\n\nA hunger to contribute meaningfully and grow with a firm that genuinely recognizes and rewards real value.\n\nSalary Range/Hourly Rate\n\n$100,000\n\nOther Benefits and Perks\n\nSupporting Your Success & Well-beingBeyond competitive compensation and generous time off, we invest in our team's continuous growth and personal well-being. Here are some additional ways we support our \"rainmakers\":\n\nContinuous Professional Development: We are committed to your growth. Beyond CLE support, you'll benefit from regular in-house training sessions, a collaborative environment that encourages knowledge sharing, and opportunities to lead internal initiatives that shape firm direction.\n\nModern Work Environment: Our Olympia Fields office is designed for productivity and collaboration, offering a professional and supportive space for your in-person days. We leverage cutting-edge legal technology to streamline workflows, ensuring you have the best tools to manage your caseload efficiently.\n\nTeam & Culture Focus: We believe in working hard and celebrating successes. Expect regular team lunches, social gatherings, and opportunities to connect with colleagues beyond case work. Our collaborative spirit extends to our open-door policy for mentorship and support.\n\nWork-Life Integration Tools: We understand legal work is demanding. Our hybrid model is just one part of our commitment. We provide the secure remote access tools and resources necessary for seamless work from any location on your remote days, ensuring you can manage your work effectively, wherever you are.\n\nConvenient Location & Amenities: Our Olympia Fields office offers ample free parking and is easily accessible, making your commute stress-free. We're situated in a vibrant community with various amenities nearby.",
      "job_highlights": [
        {
          "title": "Qualifications",
          "items": [
            "Masterful Legal Craft: Draft compelling pleadings, motions, settlement agreements, and litigation documents",
            "Experience, Excellence, and HustleWe seek attorneys who are ready to make a significant impact from day one",
            "J.D. from an accredited law school and an active Illinois law license in good standing",
            "A minimum of 3 years of recent, hands-on experience in family law (domestic relations) is mandatory",
            "A demonstrated ability to independently manage complex, high-volume caseloads from start to finish",
            "Exceptional courtroom presence, persuasive legal writing, and clear, professional client communication skills",
            "Organizational mastery, tech fluency, and an outcome-obsessed mindset",
            "A hunger to contribute meaningfully and grow with a firm that genuinely recognizes and rewards real value"
          ]
        },
        {
          "title": "Benefits",
          "items": [
            "Salary Range/Hourly Rate",
            "$100,000",
            "Other Benefits and Perks",
            "Supporting Your Success & Well-beingBeyond competitive compensation and generous time off, we invest in our team's continuous growth and personal well-being"
          ]
        },
        {
          "title": "Responsibilities",
          "items": [
            "You won't just be handling cases; you'll be shaping outcomes and driving the firm's success",
            "Lead a Dynamic Caseload: Take charge of 50–55 active cases, a strategic blend of contested and uncontested divorces, complex custody disputes, orders of protection, and probate matters",
            "We intentionally balance complexity to ensure you're always challenged, engaged, and operating at peak efficiency",
            "True Autonomy & Authority: We trust you to lead client strategy, master court appearances, and dominate mediations and high-stakes negotiations",
            "Your legal acumen will be central to our clients' success",
            "Your precision and persuasive writing will be critical to our wins",
            "Direct Impact on Firm Growth: Contribute directly to our firm's expansion by maintaining a minimum of 1,800 billable hours annually through focused, high-quality output",
            "Expect regular team lunches, social gatherings, and opportunities to connect with colleagues beyond case work"
          ]
        }
      ],
      "extensions": [
        "6 days ago",
        "Full-time"
      ],
      "detected_extensions": {
        "posted_at": "6 days ago",
        "schedule": "Full-time"
      },
      "apply_link": "https://bwla.org/jobs/joerika-stitt-esquire-llc-associate-attorney-domestic-relations-probate/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
      "apply_links": [
        {
          "link": "https://bwla.org/jobs/joerika-stitt-esquire-llc-associate-attorney-domestic-relations-probate/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Black Women Lawyers' Association Of Greater Chicago, Inc."
        }
      ],
      "sharing_link": "https://www.google.com/search?ibp=htl;jobs&q=lawyer+&htidocid=wXIY-yO8sqalgLlxAAAAAA%3D%3D&hl=en-US&shndl=37&shmd=H4sIAAAAAAAA_z2OvU7DQBCERZtHoJoKAQo2QqKBKgkQEVniJwVldL4s9pLzrbldRNzlHah4vbwFHUdDM8VovpkZ_RyMmoVQ4o3D0tgMt_r-wYnGqKoZ9rsvTFTFszPCxExSpAHHN9KRGns8U3DGEhVHeExS59gJzrCQGkou-RYSMRdpAh1et2a9XpWlaigatQz6wktXSqRatuWb1PonK21doj4X0-ri8nxb9LE5fZoG5zd4ycMRlfscKOl-9_3_Ln-AvGKeKGMJs5a9a2SM--gLcMRDGLqeHe6YwlqzX_0CAKjyB_wAAAA&shmds=v1_AdeF8Khd2elKjihiHHhYid_RsulVazGQms2uBJ2MvqWPz3qcpw&shem=sdl1pl&source=sh/x/job/li/m1/1#fpstate=tldetail&htivrt=jobs&htiq=lawyer+&htidocid=wXIY-yO8sqalgLlxAAAAAA%3D%3D"
    },
    {
      "position": 10,
      "title": "Civil Litigation Attorney near Chicago",
      "company_name": "National Client",
      "location": "Chicago, IL",
      "via": "via Republican Jobs",
      "description": "Position summary: Republican Jobs is hiring on behalf of a law firm near Chicago, IL, seeking an experienced Civil Litigation Attorney. /r/n/r/n\nAre you a skilled and driven attorney with a passion for civil litigation? This opportunity offers the chance to advocate for clients and achieve impactful results in a dynamic legal environment. We’re looking for a talented Civil Litigation Attorney to manage diverse caseloads, collaborate with a team of legal professionals, and make a meaningful difference. /r/n/r/n\nAs a Civil Litigation Attorney, you will oversee all aspects of civil cases from inception to resolution. Your work will cover a variety of legal matters, including contract disputes, personal injury claims, property litigation, and other civil issues. This role is ideal for someone who thrives in a fast-paced, collaborative environment while representing clients’ best interests both in and out of the courtroom. /r/n/r/n",
      "job_highlights": [
        {
          "title": "Qualifications",
          "items": [
            "Are you a skilled and driven attorney with a passion for civil litigation?",
            "This role is ideal for someone who thrives in a fast-paced, collaborative environment while representing clients’ best interests both in and out of the courtroom"
          ]
        },
        {
          "title": "Responsibilities",
          "items": [
            "As a Civil Litigation Attorney, you will oversee all aspects of civil cases from inception to resolution",
            "Your work will cover a variety of legal matters, including contract disputes, personal injury claims, property litigation, and other civil issues"
          ]
        }
      ],
      "extensions": [
        "3 days ago",
        "Full-time"
      ],
      "detected_extensions": {
        "posted_at": "3 days ago",
        "schedule": "Full-time"
      },
      "apply_link": "https://www.republicanjobs.law/illinois/chicago/civil-litigation-lawyer.php?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
      "apply_links": [
        {
          "link": "https://www.republicanjobs.law/illinois/chicago/civil-litigation-lawyer.php?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Republican Jobs"
        },
        {
          "link": "https://chicago-il.americanlisted.com/jobs/civil-litigation-attorney-sports-entertainmentrecreation-mostly-remote_8945070970.html?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Chicago, IL - AmericanListed.com"
        },
        {
          "link": "https://us.trabajo.org/job-3035-459bffcb78e311e4b264653975eb568b?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
          "source": "Jobs Trabajo.org"
        }
      ],
      "sharing_link": "https://www.google.com/search?ibp=htl;jobs&q=lawyer+&htidocid=mIzw6eUPtrqnF70EAAAAAA%3D%3D&hl=en-US&shndl=37&shmd=H4sIAAAAAAAA_zWNMQrCQBBFsc0RLGRq0awINoqFpBAleIWwWYbdkXUm7AwS7-JhjYLNKz6P_6r3rDo29KQMLRlFbyQMJzMpjC9g9AWaRMFHgTVcpQedppBgss4iMeP8kMwG3TunmuuoNl2EOsjDCWMvo7tLr190mnzBIXvDbrvbjPXAcbm4_Yo-Q5MJ2YD431vBpf0AkRg2N58AAAA&shmds=v1_AdeF8KgcHtql-edoE5y072AuG83IlSSkTGKC4-kGt4dYYy5_xA&shem=sdl1pl&source=sh/x/job/li/m1/1#fpstate=tldetail&htivrt=jobs&htiq=lawyer+&htidocid=mIzw6eUPtrqnF70EAAAAAA%3D%3D",
      "thumbnail": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADgAAAA4CAMAAACfWMssAAAAulBMVEX///8qL4HkDy0oLYDjABriAADkACgAAHXrcXnjACPkCyseJH32xsnjABRQU5LnQ1IUHHrzrbD87++0tcwKFHgjKX8AD3fT1OEABnbiAAnb3Of4+PrKytoACnYZIHy9vtJIS47mNERtKnCcnb2NjrN1eaf0pKfu7vODhK2qqsVaXZe1m7T4mp35ubo8QIlCRYvqZ3BnGmpnap7/5+ZxV4353N1yYpU0OYaDUIPtQk7pWGLufYPmKzz+19Z38zM1AAAClElEQVRIie2V23LaMBBAd5FAASVEwZK42JYNNjGmAVLSlqZp/v+3KtnOZYIxJC/tdHKGYVhLx7K12gXgk/8Wfxh5XpC910piJoUQkvHF8B1ayozCEsLD+FQ1MMYayggpBSf2F1uc5OWMIDF6mQfDwFsoadcWsX+KZ9fQiQ9B/uVmdQfBWiDyDaxuzypuz2uf03o8zrL5SIqvY9qeriAJEc0WprRbMr6q8XxBkC/tsty+5qzbanXGlxBZU3t37VYJrRMXBlUMaUjcrs7G1DKmA08ikXBWhJS2a8SMIdFZHpL1VqH6dlWygi1Hkwyq8Or7vpgYOyFjXKbBiJv5yw01IappSzcEtT9fp/MJzNPliwhzjrrhHPgM1RaYSVwQvFoRAonl1XrccG6/wtTlRf04f8aX7pZVcLcnegJlkBuUw0kEGmfti4ouIFF9KOOaXXXiJOGEJHq06CuXx4IehTVRG+j2DuTRicNEKGU/RqkZ7VRQ2BESQxlf7IuRQBFFcb/i5/1lxS/gRC1hWgT3qz1xEiKvL6HDIyWSEKwdsDsmvAbR5lkGdQM7gqyp/wTanfG3+OAVaWxirVAkA9rtvKJ97Ru74HBFG8rK1XEYDFq094T1YKOQb6HVKa/UpMO9pUESRvDQpp1eq9frjqeP/obbcvRvaFMh2wKxs/TcH9xcdscXvx/OIbKtkrDgsf3Mda3o72zX4LLqw1m+lrbpMQ8GLxxoef7STeVS7OK1Cl1n5kWKIu9oj8y13UW0NU9cL1ejpctgX0s5OWZmqZFGWVNxwZbFiYi0vdVx0+Yl3ca7TX/hVeclF3ii+fYhRuSD5jD8a6b+uHnCf95bs9ghGb1bLE1WW+rHTCZGzRV9iMz7yHqf/NP8AQbNPO2TEAnSAAAAAElFTkSuQmCC"
    }
  ],
  "pagination": {
    "next_page_token": "eyJmYyI6IkVyY0VDdmNEUVV4cmRGOTJSbVl0VEhWclgwdFJRakUxZGpZMVJWOVFXbDlOY3pGa2RsbEVhMDlYZGxaMk5sQmlVRXhDU2t0dE9XOURaRFpTTm1RellqaEliVmR3ZDJsdFkwTlhNSHB1WDJoQlN6SnNSamMyZUZCU01WZHJNMlIzTlVSdWFFNTBhbk5TUVc0M1pXdGZielpNWVZOWFpVVm5WV3g1UTJRMUxVVkxabHBDZW1KdFpVMHljV3AxV1V0SmVXWnliblowZG1OblVFOTRTVzVDZWtGbGNta3pVMFZqT0c1WFNUSk1kVlZrZFUweE1XTnhNVFpNUlhGUlNrNWFjWEZDT1RSQ2RrUndSVGRRTVd0Q2NWbG1SVEV0TVVkR05sQk5UME5vYldsUWVrRnlSVVp0U0RKRlJUQTNRbFZCY1V0VlZXZEdWbkJyWVhGc1NtUTBaMGhMWnpJd01GWkVSMFZGYXpCSGMyaElUa00xWlc5UE5VcFZUWEJDY1ZsVFh6aERPRmRhWHpsTFVHbHpUbGhCYURSTWRHVk5ZVGxJWlU5ZlZuRkJkVXQ0TmxaQ1pFMU9kbmM1WVVsc1pXbFBZbU00ZWpReFlWTlpYMjFuZVhkWWJtNDBVWGRZUnpOb1ZrZENjM0V3Y3paSVUxQXpaa0pUZFVoSWRWOXBMVFphYjBVd1VGWkdXWGN4TFRaekxVMTRhRXhXYzNWTmFWWnpRWFl0WHpCUGIwdzBTUzE0YkVKeWMwaFFjelJETUdsS1gzVk9jSE5zWDFCUWFXRXRNalpwWjFseVJVRm1Ra3N0YVdKUVlraFdiSEpvUlVVM1kyeEpWbDk2ZVU5bmIyVjJUa1JCZDFKblZqTldaa1phVUhGNGVGOUJTV0k1UVdWZmJEUXRObk1TRjB0cmJWTmhURGRUVG5WdWRIQjBVVkIxTldKUFowRk5HaUpCUmsxQlIwZHZUVjlyTFhkVGMwWkZOa0pzTVZkUWVWQnBPWHBrYW1SdU5GRkIiLCJmY3YiOiIzIiwiZWkiOiJLa21TYUw3U051bnRwdFFQdTViT2dBTSIsImdsIjoidXMiLCJobCI6ImVuIiwidWRtIjo4LCJhc3luYyI6Il9iYXNlanM6JTJGeGpzJTJGXyUyRmpzJTJGayUzRHhqcy5zLmVuLk5YSGNPbm42Q0c0LjIwMTguTyUyRmFtJTNEQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQWdBQUFBQUFBQUFBQUFBQUFBQ0FBaUFBQVFBRUJBQUlBQUFBQUFBQUFJQUNBQUFBQUFBQUFBQUFBQUFBQUFBQUFBRUNBQUFBQUFFZ0FBQUFBQUFBQUFFQUFBQUFBQUFDQUFRSUFBQVFCQ0JRZ0FGQUFBQUFBQUFBQUFBQUFBQUlBQVFBQUFBQUpTQUQ4M3g4TUFBQUFBQUFBQUFBQkFBQUFBQUFBQVlBRUFBQUFBQUFBQUFBQVhBQUFCQlFEZ0VBQ0NBQUFBQUFBQUFBQUFBQkFBQUFBQUFBQUVBQUFBQVFBQUFFQUFBQVVBQUFBQUFBQUFBQUFBQUJBQUFBQUFBQUFBQUFBUUFBQUFPQUFBQUFBQ0FBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFJd0FBQUFBQUFBRWdBb0FDQ0FId0FBQUFBQUFNQUJBQUFJQVFBQUFFY1VEUUFBQUFBQUFBRGtBUEI0QUlmVUZBQUFBQUFBQUFBQUFBQUFBQUFBZ0FBVUJITWdfWUFBQVFBQUFBQUFBQUFBQUFBQUFBQUFBQUNRSW1oaXJRRUFBZyUyRmRnJTNEMCUyRnJzJTNEQUNUOTBvRkFhbDExMU01eVpVaDdOYXh1MlAyb01uOFE3ZyxfYmFzZWNzczolMkZ4anMlMkZfJTJGc3MlMkZrJTNEeGpzLnMuWHREWFQ4N1Yyd0kuTC5XLk8lMkZhbSUzREFDQUVBQkFRQWdBQUFHQUFBQUFBSVFBZ0JVQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBaUFBQUFBQUFnQUFBQUFnQUFBQUFBQUFFQUNBQUFBQUFSQUFBYkZDR0FnQUFBRUR3QWdDQUZDQUFBQUFBZ0E4QUFGY0JFRUFBQUFBSUFBQUFBRWdBQUFBQUFCQWdnQUVBUUFCQUFBQUJpd0lDQUFBQkNCRUFBRUFBQUVCRUFBSUlFZ0FFUkFBZ0VRQUFrQWdBUVFRQUFHQUlHQUFBQUFJQUFBQUFDQUFBOEQ0QWdRVUFRRURBQUNBQUFFQUdRQUFBQUJRRGdBQUNRQUFBQUFBSUFCQUFBQUFBQUFCUUFBQUFFQUFBQUFhQUMwRVlBQUVWQUpZT0RoQUFBQUFBQUFBRUFnQWdJQUFBQUFBQ0FLQUVBT0lCQUFCQUFRQUNNQUR3QkJEd0FBQUFBQkdBQ0FCQUFnQWdBRUFBZ0FBQUVnQW9CQUFCZ0FzQUFRQUFBTUFvQUFBWUFBQVdBRWNVRFFBQUFBQUFBQUNBQUdBQUFBREFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBZ0FJQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFnJTJGcnMlM0RBQ1Q5MG9HQ0VvT0hIWnFRN1pVbXctYmo3czBPdFNTU3F3LF9iYXNlY29tYjolMkZ4anMlMkZfJTJGanMlMkZrJTNEeGpzLnMuZW4uTlhIY09ubjZDRzQuMjAxOC5PJTJGY2slM0R4anMucy5YdERYVDg3VjJ3SS5MLlcuTyUyRmFtJTNEQUNBRUFCQVFBZ0FBQUdBQUFBQUFJUUFnQlVBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFpQUFBQUFBQWdBQUFBQWdBQUFBQUFBQUVBQ0FBaUFBQVJBRUJiRktHQWdBQUFFRHdJZ0NBRkNBQUFBQUFnQThBQUZjQkVFQUFBRUNJQUFBQUFFZ0FBQUFBQUJBZ2dFRUFRQUJBQUFDQml3SUNBQVFCQ0JVZ0FGQUFBRUJFQUFJSUVnQUVSQUlnRVFBQWtBZ0pTUVQ4MzM4TUdBQUFBQUlBQUFBQkNBQUE4RDRBZ1lVRVFFREFBQ0FBQUVBR1hBQUFCQlFEZ0VBQ1NBQUFBQUFJQUJBQUFBQkFBQUJRQUFBQUVBQUFBQWFBQzBFWUFBRVZBSllPRGhBQUFBQUFBQUJFQWdBZ0lBQUFBQUFDUUtBRUFPSUJBQUJBQ1FBQ01BRHdCQkR3QUFBQUFCR0FDQUJBQWdJd0FFQUFnQUFBRWdBb0JDQ0Jud3NBQVFBQUFNQXBBQUFZQVFBV0FFY1VEUUFBQUFBQUFBRGtBUEI0QUlmVUZBQUFBQUFBQUFBQUFBQUFBQUFBZ0FBVUJITWdfWUlBQVFBQUFBQUFBQUFBQUFBQUFBQUFBQUNRSW1oaXJRRUFBZyUyRmQlM0QxJTJGZWQlM0QxJTJGZGclM0QwJTJGdWpnJTNEMSUyRnJzJTNEQUNUOTBvRmhxT0V6UlZLbUgwd3Jsd3h5WTIwZFhwaVFiQSxfZm10OnByb2csX2lkOmZjX0trbVNhTDdTTnVudHB0UVB1NWJPZ0FNXzIifQ=="
  }
}