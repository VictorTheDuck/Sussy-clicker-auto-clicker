import pyautogui, threading, time
threads = []

time.sleep(3)

def fast_click(click_threads):


    def click():

        for i in range(100):
            pyautogui.click(169, 469) # click among us red crewmate
            pyautogui.click(169, 669)

        for i in range(100):
            pyautogui.click(169, 469)
            for i in range(10):
                pyautogui.click(169, 669)


        for i in range(250):
            pyautogui.click(169, 469)
            for i in range(200):
                pyautogui.click(169, 669)
        
        while True:
            pyautogui.click(169, 469)
            for i in range(1000):
                pyautogui.click(169, 669)
                    

    for i in range(click_threads):
        t = threading.Thread(target=click)
        t.daemon = True
        threads.append(t)
    for i in range(click_threads):
        threads[i].start() 

    for i in range(click_threads):
        threads[i].join()


fast_click(50)
