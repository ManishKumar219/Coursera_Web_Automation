##########################################
#  Edit Your Personal & Course Details  #
##########################################

course_name = "Introduction to Artificial Intelligence (AI)"

## Enter E-mail Id
E_mail = "***@gmail.com"

## Enter Coursera Password
password = "***"

Wait_time_for_captcha = 30
Wait_Time = 3 #If your Network is Slow Incrase the Wait Time Slightly

Reason_you_applied_for_aid = "I'm a student from India , I figure learning Data Science it will be advantageous for me to practice in a good platform, and I think it will be beneficial for me to get into the firm as an intern. But, I have no job of my own to carry through the expenses to pay for my certificate of this course. Our annual income is quite low with respect to normal national income. I live only for my scholarship. In this circumstance, it is very much difficult for me to gather such amount of money for the certificate. Financial Aid will help me take this course without any inimical impact on my basic monthly needs. We are three sisters and we all are at learning stage and it becomes a lot difficult for the family members to pay the whole amount for all the three of us and if I add up my course it will make even harder for them to pay. So I’m badly in need of this financial aid. Receiving this Financial Aid will open for me a new horizon of the world of Coursera courses, which in turn will help me in future. I also plan to complete all assignments on or before time as I have done in previous Signature Track Courses. Also, I intend to participate in Discussion Forums, which I have found to supplement my learning immensely in the other online courses I have taken on Coursera. I also plan to grade assignments, which are to peer-reviewed, which I believe will an invaluable learning opportunity."


goals = "I want to be an expert in data scientist this course will be my one step towards that, this course will help me to enhance my skills and will be helpful in my job interviews. As this course has been taught by well experienced and top teachers around the world this will a great opportunity for me to learn great things, this course will help me to improve my problem-solving skills. At last I would like to say that this course will help me in numerous ways, to enhance my knowledge, to pass job interviews and to get job in a good company. This course will help me to achieve a bright future in this technical world and will help to go one step ahead in the rush to survive in this world. So, this is the reason why I need this course to achieve my career goals, if you give a positive reply from your side this will be a great help for me."

###_______________________________________________________________________________________________###

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#################################
## log In and Course Selection ##
#################################


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
#Open Coursera Website
driver.get("https://www.coursera.org/")

#Login
login_btn = driver.find_element('class name', 'c-ph-log-in')
login_btn.click()

wait = WebDriverWait(driver, Wait_Time)
wait.until(EC.presence_of_element_located((By.NAME, 'email')))

email = driver.find_element('name', 'email')
email.send_keys(E_mail)
passwd = driver.find_element('name', 'password')
passwd.send_keys(password)
passwd.submit()


time.sleep(Wait_time_for_captcha)

input_course = driver.find_element(By.CSS_SELECTOR, "input[placeholder='What do you want to learn?']")
input_course.send_keys(course_name)
input_course.send_keys(Keys.ENTER)

course = driver.find_element('class name', 'css-1doy6bd')
course.click()

windows = driver.window_handles
driver.switch_to.window(windows[1])
time.sleep(Wait_Time)


#############################################
## First Page of Financial aid Application ##
#############################################

driver.find_element('class name', 'finaid-link').click()
driver.find_element(By.XPATH, "//*[text()='Continue to the application']").click()

time.sleep(Wait_Time)

# Select Education
driver.find_element('id', 'cds-react-aria-2-value').click()
time.sleep(Wait_Time)

edu = driver.find_element(By.XPATH, "//*[text()='College degree']")
if edu.is_enabled():
    driver.find_element('class name', 'css-66nywt').click()
else:
    edu.click()
    
#Set Income Amount
driver.find_element('class name', 'cds-212').clear()
driver.find_element('class name', 'cds-212').send_keys(0)

# Select Employee Status
driver.find_element('id', 'cds-react-aria-7-value').click()
time.sleep(Wait_Time)

emp = driver.find_element(By.XPATH, "//*[text()='Student']")
if emp.is_enabled():
    driver.find_element('class name', 'css-66nywt').click()
else:
    emp.click()

# Reason Why you applied for aid?
reason = driver.find_element('class name', 'cds-210')
text = reason.get_attribute('innerHTML')
if len(text.split()) < 150:
    reason.clear()
    reason.send_keys(Reason_you_applied_for_aid)
    
if not driver.find_element('id', 'cds-react-aria-11').is_selected():
    driver.find_element('id', 'cds-react-aria-11').click()

time.sleep(Wait_Time)
# Continue to the Next part of the Form
driver.find_element(By.XPATH, "//*[text()='Next']").click()
time.sleep(Wait_Time)


###############################################
## Secound Page of Financial aid Application ##
###############################################

inputs = driver.find_elements('class name', 'cds-input-input')

inputs[0].click()
for i in range(5):
    inputs[0].send_keys(Keys.BACKSPACE)
    
# How will your selected course help with your goals?
inputs[1].clear()
inputs[1].send_keys(goals)

# Click on Check Box
chk_box = driver.find_elements('class name', 'cds-255')
for chk in chk_box:
    if not chk.is_selected():
        chk.click()
        
# I agree to the terms above
inputs[3].clear()
inputs[3].send_keys('I agree to the terms above')
