# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# import schedule
import time
#
# def automate(driver, link):
#   driver.get(link)
#   #driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div/span/span/div/div/svg').click()
#   # wait = WebDriverWait(driver, 20)
#   # wait.until(driver.get(link))
#   # element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
#   # element.send_keys("rishi.d.goku")
#   driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys("rs1965@srmist.edu.in")
#   driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
#
# def schedule_time_table(browser):
#     print("CONNECTED")
#     ## MONDAY
#     schedule.every().monday.at("09:00").do(automate, browser,
#                                            "LINK:-https://meet.google.com/lookup/ctv6kwrdcp  Operating Systems. (By- Saurabh Gupta)")
#     schedule.every().monday.at("10:00").do(automate, browser,
#                                            "LINK:-https://meet.google.com/lookup/ceg7iq3out  Probability and Queueing Theory. (By- Tanuj Kumar)")
#     schedule.every().monday.at("11:00").do(automate, browser,
#                                            "LINK:-https://meet.google.com/lookup/ep53rbrwtf  Computer Communications. (By- Amit)")
#     schedule.every().monday.at("13:35").do(automate, browser,
#                                            "LINK:-https://meet.google.com/lookup/ef4rgsip3e  Software Engineer and Project Management(By- Kanika Garg)")
#     schedule.every().monday.at("14:29").do(automate, browser,
#                                            "LINK:-https://meet.google.com/lookup/ep53rbrwtf  (Batch-1)CC LAB(By-Satya Sai/ Abhishek Chauhan )")
#     schedule.every().monday.at("14:30").do(automate, browser,
#                                            "LINK:-https://meet.google.com/lookup/gkmtyn7lwr  (Batch-2)APP LAB(By-Anurag Singh/ Rajiv Ranjan )")
#
#     ## TUESDAY
#     schedule.every().tuesday.at("15:10").do(automate, browser,
#                                             "LINK:-https://meet.google.com/lookup/ceg7iq3out  Probability and Queueing Theory. (By- Tanuj Kumar)")
#     schedule.every().tuesday.at("10:00").do(automate, browser,
#                                             "LINK:-https://meet.google.com/lookup/e6obb4y2fu  Competetive Professional Skills-1(By- Aarti Sharma)")
#     schedule.every().tuesday.at("11:00").do(automate, browser,
#                                             "LINK:-https://meet.google.com/lookup/fw3ddngntg  (Batch-1)Advance Programming Practice(By- Rajiva Ranjan)")
#     schedule.every().tuesday.at("11:00").do(automate, browser,
#                                             "LINK:-https://meet.google.com/lookup/gkmtyn7lwr  (Batch-2)Advance Programming Practice(By- Anurag Singh)")
#     schedule.every().tuesday.at("12:00").do(automate, browser,
#                                             "LINK:-https://meet.google.com/lookup/bokoyk4c4v  Social Engineering(By- Jay Prakash Chaubey)")
#     schedule.every().tuesday.at("13:35").do(automate, browser,
#                                             "LINK:-https://meet.google.com/lookup/ef4rgsip3e  Software Engineer and Project Management(By- Kanika Garg)")
#     schedule.every().tuesday.at("14:25").do(automate, browser,
#                                             "LINK:-https://meet.google.com/lookup/b7oecgbbyn  (Batch-1)DAA LAB(By- Himanshu/ Jeetu)")
#     schedule.every().tuesday.at("14:26").do(automate, browser,
#                                             "LINK:-https://meet.google.com/lookup/ctv6kwrdcp  (Batch-2)OS LAB(By- Saurabh/ Sachi Pandey)")
#
#     ## WEDNESDAY
#     schedule.every().wednesday.at("09:00").do(automate, browser,
#                                               "LINK:-https://meet.google.com/lookup/ctv6kwrdcp  Operating Systems(By- Saurabh Gupta)")
#     schedule.every().wednesday.at("10:00").do(automate, browser,
#                                               "LINK:-https://meet.google.com/lookup/ceg7iq3out  Probability and Queueing Theory(By- Tanuj Kumar)")
#     schedule.every().wednesday.at("11:00").do(automate, browser,
#                                               "LINK:-https://meet.google.com/lookup/gkmtyn7lwr  (Batch-2)Advance Programming Practice(By- Anurag Singh)")
#     schedule.every().wednesday.at("11:00").do(automate, browser,
#                                               "LINK:-https://meet.google.com/lookup/fw3ddngntg  (Batch-1)Advance Programming Practice(By- Rajiva Ranjan)")
#     schedule.every().wednesday.at("12:00").do(automate, browser,
#                                               "LINK:-https://meet.google.com/lookup/b7oecgbbyn  Design and Analysis of Algorithm(By- Himanshu Shekhar)")
#     schedule.every().wednesday.at("13:35").do(automate, browser,
#                                               "LINK:-https://meet.google.com/lookup/ep53rbrwtf  Computer Communication(By- Amit)")
#     schedule.every().wednesday.at("14:25").do(automate, browser,
#                                               "LINK:-https://meet.google.com/lookup/ctv6kwrdcp  (Batch-1)OS LAB(By- Saurabh Gupta/ Kanika Garg)")
#     schedule.every().wednesday.at("14:26").do(automate, browser,
#                                               "LINK:-https://meet.google.com/lookup/ef4rgsip3e  (Batch-2)SEP LAB(By- Kanika Garg/ Ruby Singh)")
#
#     ## THRUSDAY
#     schedule.every().thursday.at("09:00").do(automate, browser,
#                                              "LINK:-https://meet.google.com/lookup/ceg7iq3out Probability and Queueing Theory(By- Tanuj Kumar)")
#     schedule.every().thursday.at("10:00").do(automate, browser,
#                                              "LINK:-https://meet.google.com/lookup/gfzoqdepre  Critical And Creative Thinking Skills(By- Vinay Kumar Sharma)")
#     schedule.every().thursday.at("11:03").do(automate, browser,
#                                              "LINK:-https://meet.google.com/lookup/gkmtyn7lwr  (Batch-2)Advance Programming Practice(By- Anurag Singh)")
#     schedule.every().thursday.at("11:03").do(automate, browser,
#                                              "LINK:-https://meet.google.com/lookup/fw3ddngntg  (Batch-1)Advance Programming Practice(By- Rajiva Ranjan)")
#     schedule.every().thursday.at("12:00").do(automate, browser,
#                                              "LINK:-https://meet.google.com/lookup/b7oecgbbyn  Design and Analysis of Algorithm(By- Himanshu Shekhar)")
#     schedule.every().thursday.at("13:35").do(automate, browser,
#                                              "LINK:-https://meet.google.com/lookup/ctv6kwrdcp  Operating System(By- Saurabh Gupta)")
#     schedule.every().thursday.at("14:25").do(automate, browser,
#                                              "LINK:-https://meet.google.com/lookup/ef4rgsip3e  (Batch-1)SEP LAB(By- Kanika Garg/ Ruby Singh)")
#     schedule.every().thursday.at("14:26").do(automate, browser,
#                                              "LINK:-https://meet.google.com/lookup/b7oecgbbyn   (Batch-2)DAA LAB(By- Himanshu/ Jeetu)")
#
#     ## FRIDAY
#     schedule.every().friday.at("09:00").do(automate, browser,
#                                            "LINK:-https://meet.google.com/lookup/ef4rgsip3e  Software Engineer and Project Management(By- Kanika Garg)")
#     schedule.every().friday.at("10:00").do(automate, browser,
#                                            "LINK:-https://meet.google.com/lookup/ceg7iq3out Probability and Queueing Theory(By- Tanuj Kumar)")
#     schedule.every().friday.at("11:00").do(automate, browser,
#                                            "LINK:-https://meet.google.com/lookup/e6obb4y2fu  Competetive Professional Skills- 1(By- Aarti Sharma)")
#     schedule.every().friday.at("12:00").do(automate, browser,
#                                            "LINK:-https://meet.google.com/lookup/dxynmk724s  Environmental Science(By- Kalpana Patel)")
#     schedule.every().friday.at("13:35").do(automate, browser,
#                                            "LINK:-https://meet.google.com/lookup/b7oecgbbyn  Design and Analaysis of Algorithm(By- Himanshu Shekhar)")
#     schedule.every().friday.at("14:25").do(automate, browser,
#                                            "LINK:-https://meet.google.com/lookup/ep53rbrwtf  (Batch-2)CC LAB(By-Satya Sai/ Abhishek Chauhan )")
#     schedule.every().friday.at("14:26").do(automate, browser,
#                                            "LINK:-https://meet.google.com/lookup/gkmtyn7lwr  (Batch-1)APP LAB(By-Anurag Singh/ Rajiv Ranjan )")
#
#     while True:
#       schedule.run_pending()
#       time.sleep(10)
#
#
# if __name__ == "__main__":
#   browser = webdriver.Chrome('/Users/acephoenix02/Google Drive/Documents/Python/Online-Class-Automation/chromedriver')
#   schedule_time_table(browser)
#   #automate(automate, browser)
#   time.sleep(10)
print(time.time())