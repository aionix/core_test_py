import allure

import util.custom_logger as cl
import logging

class TestStatus():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASSED")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + resultMessage)
                else:
                    self.resultList.append("FAILED")
                    self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                    #self.screenShot(resultMessage)
                    allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            else:
                self.resultList.append("FAILED")
                self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                #self.screenShot(resultMessage)
                allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            self.resultList.append("FAILED")
            self.log.error("### Exception Occurred !!!")
            #self.screenShot(resultMessage)
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def mark(self, result, resultMessage):
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        self.setResult(result, resultMessage)

        if "FAILED" in self.resultList:
            self.log.error(testName + " ### TEST FAILED")
            self.resultList[:] = []
            assert True == False
        else:
            self.log.info(testName + " ### TEST PASSED")
            self.resultList[:] = []
            assert True == True
