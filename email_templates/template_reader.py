class TemplateReader:
    def __init__(self):
        pass

    def read_course_template(self,course_name):
        try:
            email_message = None
            if (course_name=='data science masters'):
                email_file = open("email_templates/DSM_Template.html", "r")
                email_message = email_file.read()
            elif (course_name=='machine learning masters'):
                email_file = open("email_templates/MLM_Template.html", "r")
                email_message = email_file.read()
            elif (course_name == 'deep learning masters'):
                email_file = open("email_templates/DLM_Template.html", "r")
                email_message = email_file.read()
            elif (course_name == 'NLP masters'):
                email_file = open("email_templates/NLPM_Template.html", "r")
                email_message = email_file.read()
            elif (course_name == 'DataScienceForManagers'):
                email_file = open("email_templates/DSFM_Template.html", "r")
                email_message = email_file.read()
            elif (course_name == 'Vision'):
                email_file = open("email_templates/Vision_Template.html", "r")
                email_message = email_file.read()
            return email_message
        except Exception as e:
            print('The exception from read_course_template is '+str(e) + course_name)
